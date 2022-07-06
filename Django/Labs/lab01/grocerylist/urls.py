from django.urls import path
from . import views

app_name = 'grocerylist'

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:grocery_item_id>/', views.complete, name='complete'),
    path('delete/<int:grocery_item_id>/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    # path('<int:grocery_item_id>/update', views.update, name='update'),
]
