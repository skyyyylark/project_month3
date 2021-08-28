import random

from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse, FileResponse
import random
from .models import Student, Blog
from django.shortcuts import redirect



def hello_view(request):
    blog = Blog.objects.all()
    context = {'posts': blog}
    return render(request, 'index.html', context)


def date_view(request):
    today = datetime.now()
    return HttpResponse(str(today))


def view_random(request):
    num = random.randint(1, 100)
    context = {'num': num}
    return render(request, 'random.html', context)

def image_view(request):
    path = settings.BASE_DIR / 'static' / '123.jpg'
    file = open(path, 'rb')
    return FileResponse(file)

def view_students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students.html', context)



def create_post(request):
    if request.method == "POST":
        form = request.POST
        title = form['title']
        description = form['description']
        hashtags = form['hashtags']
        image = request.FILES['image']
        Blog.objects.create(title=title, description=description, hashtags=hashtags, image=image)
        return redirect('/blog/')
    if request.method == "GET":
        return render(request, 'create.html')
