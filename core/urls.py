from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('add/product/', views.add_product, name='add_product'),
    path('delete/product/<int:id>/', views.delete_product, name='delete_product')
]