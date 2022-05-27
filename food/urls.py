from django.contrib import admin
from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('food/', views.index, name='index'),
    path('food/<int:item_id>/', views.detail, name='detail'),
    path('add', views.create_item, name='create_item'),       #add
    path('update/<int:id>/', views.update_item, name= 'update_item'),  #update
    path('delete/<int:id>/', views.delete_item, name= 'delete_item'),  #delete
]
