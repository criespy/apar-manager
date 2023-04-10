from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DetailView
from .models import Apar
from .forms import *
import qrcode
from pathlib import os

class DashboardHome(ListView):
    model = Apar
    template_name = 'dashboard.html'
    ordering = ['nomor']

class UpdateApar(UpdateView):
    model = Apar
    #fields = '__all__'
    template_name = 'apar_updateview.html'
    form_class = FormUpdateApar

    def form_valid(self, form):
        qrcode = "FLN_APAR_" + str(form.cleaned_data['nomor'])
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
        


