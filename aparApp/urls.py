from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardHome.as_view(), name='DashboardHome'),
    path('create/', views.CreateApar.as_view(), name='createapar'),
    path('update/<int:pk>', views.UpdateApar.as_view(), name='updateapar'),
    path('scan/', views.ScanMenu.as_view(), name='scanmenu'),
    path('scan/<slug:slug>', views.ScanMenu.as_view(), name='scanmenu'),
    path('cek/', views.CekApar.as_view(), name='cekapar'),
    path('cek/<slug:slug>', views.CekAparById.as_view(), name='cekapar'),
    path('history/', views.CekAparList.as_view(), name='cekhistory'),
    path('detail/', views.DetailApar.as_view(), name='detailapar'),
    path('detail/<slug:slug>', views.DetailApar.as_view(), name='detailapar'),
    #path('scan/', views.ScanMenu.as_view(), name='scanmenu'),
]