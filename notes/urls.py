from django.urls import path

from notes import views

urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('notes/<int:id>/', views.getNote),
    path('notes/create/', views.createNote),
    path('notes/edit/<int:id>/', views.updateNote),
    path('notes/delete/<int:id>/', views.deleteNote),
]