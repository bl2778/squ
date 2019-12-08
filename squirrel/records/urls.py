from django.urls import path

from . import views

app_name='records'

urlpatterns = [
   # path('',views.index,name='index'),
    path('list/', views.all_squirrels,name='list'),
    path('map/',views.map),
    path('add/', views.add_squirrel),
    path('stats/',views.stats),
    path('<int:squirrel_id>/', views.edit_squirrel),
]

