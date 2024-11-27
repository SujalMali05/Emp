from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('emp/',views.emp,name='emp'),
    path('record/',views.emp_record,name='emp_record'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.Delete,name='Delete'),
]