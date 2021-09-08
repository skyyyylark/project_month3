from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from allauth.account.views import LoginView

# Create your views here.
from .models import BlogUser


def register_view(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            return HttpResponse("Passwords does not match!")

        user = BlogUser.objects.create_user(username=email, first_name=first_name,
                                            last_name=last_name, email=email, age=age, password=password)

        return HttpResponse("Registered successfully!")


def logout_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)
        return HttpResponseRedirect('/users/login/')
    if request.method == 'GET':
        return render(request, 'layout.html')


class Gog_log(generic.TemplateView):
    template_name = 'login.html'

    def login_view(self, request):
        if self.request.method == 'GET':
            return render(self.request, 'login.html')
        if self.request.method == 'POST':
            email = self.request.POST['email']
            password = self.request.POST['password']
            user = authenticate(self.request, email=email, password=password)
            if user is not None:
                login(self.request, user)
                return HttpResponseRedirect('/blog/')

            return render(self.request, 'login.html', context={"message": "Nepravilnyi login ili parol"})


class MyLoginView(LoginView):
    template_name = 'login.html'

