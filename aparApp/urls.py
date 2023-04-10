from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardHome.as_view(), name='DashboardHome'),
    path('create/', views.CreateApar.as_view(), name='createapar'),
    path('update/<int:pk>', views.UpdateApar.as_view(), name='updateapar'),
    path('scan/<int:pk>', views.ScanMenu.as_view(), name='scanmenu'),
    path('cek', views.CekApar.as_view(), name='cekapar'),
    #path('scan/', views.ScanMenu.as_view(), name='scanmenu'),
]