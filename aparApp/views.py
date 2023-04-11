from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DetailView, CreateView
from .models import *
from .forms import *
import qrcode
from pathlib import os
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

class DashboardHome(ListView):
    model = Apar
    template_name = 'dashboard.html'
    ordering = ['nomor']

class CreateApar(CreateView):
    model = Apar
    template_name = 'apar_createview.html'
    form_class = FormCreateApar

class UpdateApar(UpdateView):
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
    
class ScanMenu(DetailView):
    model = Apar
    template_name = 'menu_scan.html'
        
class CekApar(CreateView):
    model = Pemeriksaan
    template_name = 'pemeriksaan_createview.html'
    form_class = FormPemeriksaan

class CekAparById(CreateView):
    model = Pemeriksaan
    template_name = 'pemeriksaanbyid_createview.html'
    form_class = FormPemeriksaanById
    success_url = reverse_lazy('post_list')
    #extra_context = {'url':request.get_full_path()}

    def get_initial(self): #digunakan untuk memberikan nilai default di form    
        apar = get_object_or_404(Apar, slug=self.kwargs.get('slug'))
        babi = 'babi'
        return {
            'apar':apar,
            'keterangan':apar,
        }
    
    def get_object(self, queryset=None):
        return queryset.get(slug=self.slug)
    
    def get_current_path(self):
        return {
        'current_path': self.get_full_path(),
        'babi': 'babi',
        }

    
    #def form_valid(self, form):
        #form.instance.apar = self.kwargs['apar']
        #return super(CekAparById, self).form_valid(form)
