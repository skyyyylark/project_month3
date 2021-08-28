from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_view),
    path('now/', views.date_view),
    path('rand_num/', views.view_random),
    path('image/', views.image_view),
    path('students/', views.view_students),
    path('create-post/', views.create_post),
]