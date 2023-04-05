from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardHome.as_view(), name='DashboardHome'),
    path('update/<int:pk>', views.UpdateApar.as_view(), name='updateapar'),
    path('scan/<int:pk>', views.ScanMenu.as_view(), name='scanmenu'),
    #path('scan/', views.ScanMenu.as_view(), name='scanmenu'),
]
