from django.contrib import admin
from django.urls import path

from myapp import views


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'notes/',
        views.notes,
        name='notes'
    ),

    path(
        'addnote/',
        views.addnote,
        name='addnote'
    ),

    path(
        'viewnote/<int:id>/',
        views.viewnote,
        name='viewnote'
    ),

    path(
        'editnote/<int:id>/',
        views.editnote,
        name='editnote'
    ),

    path(
        'deletenote/<int:id>/',
        views.deletenote,
        name='deletenote'
    ),
]