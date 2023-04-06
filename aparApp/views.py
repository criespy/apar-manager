from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DetailView
from .models import Apar
from .forms import *

class DashboardHome(ListView):
    model = Apar
    template_name = 'dashboard.html'
    ordering = ['nomor']

class UpdateApar(UpdateView):
    model = Apar
    #fields = '__all__'
    template_name = 'apar_updateview.html'
    form_class = FormUpdateApar

    #def form_valid(self, form):
        # Get the current value of the 'name' field
        #current_name = self.object.name
        
        # Do something with the current name value...
        
        #return super().form_valid(form)
    
class ScanMenu(DetailView):
    model = Apar
    template_name = 'menu_scan.html'
        


