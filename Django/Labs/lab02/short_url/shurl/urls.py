from django.urls import path 
from . import views 

app_name = 'shurl'

urlpatterns = [
    path('', views.index, name='index'),
    path('shurl/<str:short_url>/', views.redirect, name='redirect'),
    # path('redirect/', views.redirect, name='redirect')
]