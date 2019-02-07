from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="board_homepage"),
    path('add/', views.add_note, name="add_note"),
    path('delete/<note_id>', views.delete_note, name="delete_note"),
    path('api/all', views.NotesList.as_view())
]
