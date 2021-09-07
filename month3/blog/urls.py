from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view()),
    path('<int:pk>/', views.BlogDetailView.as_view()),
    path('now/', views.date_view),
    path('rand_num/', views.view_random),
    path('image/', views.image_view),
    path('students/', views.view_students),
    path('create-post/', views.create_post),
    path('data/', views.BlogListApiView.as_view())
]