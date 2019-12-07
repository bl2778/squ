from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.all_squirrels),
    path('add/', views.add_squirrel),
    path('<int:squirrel_id>/', views.squirrel_details),
    path('<int:squirrel_id>/edit/', views.edit_squirrel),
]

