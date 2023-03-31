from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardHome.as_view(), name='DashboardHome'),
    path('scan/<int:pk>', views.ScanMenu.as_view(), name='scanmenu'),
]
