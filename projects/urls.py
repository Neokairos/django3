from . import views
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [path('home/', views.home, name ="home" ),
            path('num/<int:number>/', views.num, name="num"),
            path('imgpage', views.imgpage, name='imgpage'),
            path('signup/', views.signupView, name='signup'),
            path('login/', views.loginView, name='login'),
            path('logout/', views.logoutView, name='logout'),
            path('create/', views.create_note, name='create_note'),
            path('notes', views.notes_page, name='notes'),
            path('delete/<int:note_id>/', views.delete_note, name='delete_note')
            ]