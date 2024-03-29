from django.urls import path
from . import views

urlpatterns = [
    path('list', views.DashboardHome.as_view(), name='DashboardHome'),
    path('create/', views.CreateApar.as_view(), name='createapar'),
    path('update/<int:pk>', views.UpdateApar.as_view(), name='updateapar'),
    path('scan/', views.ScanMenu.as_view(), name='scanmenu'),
    path('scan/<slug:slug>', views.ScanMenu.as_view(), name='scanmenu'),
    path('cek/', views.CekApar.as_view(), name='cekapar'),
    path('cek/<slug:slug>', views.CekAparById.as_view(), name='cekapar'),
    path('history/', views.CekAparList.as_view(), name='cekhistory'),
    path('detail/', views.DetailApar.as_view(), name='detailapar'),
    path('detail/<slug:slug>', views.DetailApar.as_view(), name='detailapar'),
    path('', views.Scanner.as_view(), name='scanner'),
    #path('scan/', views.ScanMenu.as_view(), name='scanmenu'),
    path('login/', views.AparLoginView.as_view(), name='login'),
    path('logout/', views.AparLogoutView.as_view(), name='logout'),
]