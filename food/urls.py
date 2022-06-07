from django.contrib import admin
from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('food/', views.IndexClassView.as_view(), name='index'),
    path('food/<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('add', views.CreateItem.as_view(), name='create_item'),       #add
    path('update/<int:id>/', views.update_item, name= 'update_item'),  #update
    path('delete/<int:id>/', views.delete_item, name= 'delete_item'),  #delete
]
