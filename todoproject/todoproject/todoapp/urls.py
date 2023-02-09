from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('',views.index,name='index'),
   # path('details/',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update')
]
