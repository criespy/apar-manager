from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DetailView
from .models import Apar

class DashboardHome(ListView):
    model = Apar
    template_name = 'dashboard.html'
    ordering = ['nomor']

class UpdateApar(UpdateView):
    model = Apar

class ScanMenu(DetailView):
    model = Apar
    template_name = 'menu_scan.html'
    


