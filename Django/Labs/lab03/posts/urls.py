from django.urls import path 
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.ListChirps.as_view(), name='home'),
    path('posts/create/', views.CreateChirp.as_view(), name='create'),
    path('posts/<int:pk>/', views.DetailChirp.as_view(), name='detail'),
    path('posts/<int:pk>/delete/', views.DeleteChirp.as_view(), name='delete'),
]