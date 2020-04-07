from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='add'),
    path('<int:id>/', views.employee_form, name='update'),
    path('list/', views.employee_list, name='list'),
    path('delete/<int:id>', views.employee_delete, name='delete'),
]
