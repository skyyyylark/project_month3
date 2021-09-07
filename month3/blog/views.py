import random

from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
import random
from .models import *
from django.shortcuts import redirect
from django.views import generic
from rest_framework.generics import ListAPIView
from .forms import *



class BlogView(generic.ListView):
    template_name = "index.html"
    queryset = Blog.objects.all()
    context_object_name = "posts"

class BlogDetailView(generic.DetailView, generic.CreateView):
    template_name = "detail-post.html"
    queryset = Blog.objects.all()
    context_object_name = "post"
    extra_context = {"comments": Comment.objects.all()}
    
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        blog_id = self.kwargs['pk']
        comments = Comment.objects.filter(blog_id=blog_id)
        context['comments'] = comments
        return context


    def post(self, request, **kwargs):
        if request.method == "POST":
            # context = super(BlogDetailView, self).get_context_data(**kwargs)
            form = self.request.POST
            comment = form['comments']
            Comment.objects.create(text=comment, blog_id=self.kwargs['pk'])
            return HttpResponseRedirect('/blog/')





# def hello_view(request):
#     blog = Blog.objects.all()
#     context = {'posts': blog}
#     return render(request, 'index.html', context)


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


class BlogListApiView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
