from django.urls import path
from . import views

app_name = 'mysiteinfo'

urlpatterns = [
    path('api/', views.SiteDetailList.as_view(), name='site_info'),
]
