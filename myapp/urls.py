from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('load_form/', views.load_form, name='load_form'),
    path('add', views.add, name='add'),
    path('show/', views.show, name='show'),
    path('edit/<int:id>/', views.edit),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete),
    path('search', views.search)
]


