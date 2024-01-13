from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='add'),
    path('food/', views.food, name='food'),
    path('order/', views.order, name='order'),
]
