from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name="add"),
    # path('', views.view, name="view"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('adminlogin/',views.login,name="adminlogin"),
    path('',views.register,name='register'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('home/',views.home,name='home'),

]
