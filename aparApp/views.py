from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DetailView, CreateView, TemplateView
from .models import *
from .forms import *
import qrcode
from pathlib import os
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

class AparLoginView(LoginView):
    template_name = 'login.html'

redirect_authenticated_user = True

class AparLogoutView(LogoutView):
    def logout_view(selfrequest):
        logout(request)
    template_name = 'login.html'
    next_page = 'scanner'

class DashboardHome(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Apar
    template_name = 'dashboard.html'
    ordering = ['nomor']

class Scanner(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'scan.html'

class CreateApar(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Apar
    template_name = 'apar_createview.html'
    form_class = FormCreateApar

class UpdateApar(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Apar
    #fields = '__all__'
    template_name = 'apar_updateview.html'
    form_class = FormUpdateApar

    def form_valid(self, form):
        qrcode = "fln-apar-" + str(form.cleaned_data['nomor'])
        self.valid_submission_callback(qrcode)
        return super(UpdateApar, self).form_valid(form)

    def valid_submission_callback(self, data):
        input_data = data
        qr = qrcode.QRCode(
            version=1,
            box_size=5,
            border=2)
        qr.add_data(input_data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        imgfile = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/images/qrcodes/' + data + '.png')
        img.save((imgfile))

    #def form_valid(self, form):
        # Get the current value of the 'name' field
        #current_name = self.object.name
        
        # Do something with the current name value...
        
        #return super().form_valid(form)

class DetailApar(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Apar
    template_name = 'apar_detailview.html'
    #form_class = FormDetailApar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        apar = self.get_object()
        pemeriksaan_list = Pemeriksaan.objects.filter(apar=apar).order_by('-tanggal')
        context['pemeriksaan_list'] = pemeriksaan_list
        return context
    
class ScanMenu(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Apar
    template_name = 'menu_scan.html'
        
class CekApar(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Pemeriksaan
    template_name = 'pemeriksaan_createview.html'
    form_class = FormPemeriksaan

class CekAparList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Pemeriksaan
    template_name = 'pemeriksaan_listview.html'
    
class CekAparById(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Pemeriksaan
    template_name = 'pemeriksaanbyid_createview.html'
    form_class = FormPemeriksaanById
    #success_url = reverse_lazy('scanmenu', kwargs={'slug':self.slug})
    #extra_context = {'url':apar}

    def get_absolute_url(self):
        return reverse_lazy('scanmenu', kwargs={'slug':self.slug})

    def get_initial(self): #digunakan untuk memberikan nilai default di form    
        apar = get_object_or_404(Apar, slug=self.kwargs.get('slug'))
        return {
            'apar':apar,
        }
    
    def get_context_data(self, **kwargs): #digunakan untuk mengambil url dan mengirimkan nilainya ke template
        context = super().get_context_data(**kwargs)
        context['current_path'] = os.path.basename(self.request.get_full_path()) #digabung dengan fungsi os untuk mengambil url bagian terakhir saja
        context['path_without_query_string'] = self.request.path
        return context

    
    #def get_object(self, queryset=None):
    #    return queryset.get(slug=self.slug)
    
    #def form_valid(self, form):
    #    current_path = self.request.get_full_path()
    #    path_without_query_string = self.request.path

    #    context = {
    #    'current_path': current_path,
    #    'path_without_query_string': path_without_query_string,
    #}

    #    return context
    
    #def get(self, request, *args, **kwargs):
    #    current_path = request.get_full_path()
    #    return Httpcurrent_path
    
    #def get_current_path(self):
    #    return {
    #    'current_path': self.get_full_path(),
    #    'babi': 'babi',
    #    }

    
    #def form_valid(self, form):
        #form.instance.apar = self.kwargs['apar']
        #return super(CekAparById, self).form_valid(form)
