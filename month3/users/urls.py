from django.urls import path, include

from . import views

urlpatterns = [
    path('registration/', views.register_view),
    path('login/', views.Gog_log.as_view()),
    path('logout/', views.logout_view),
    path('accounts/', include('allauth.urls')),
]