from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse

def index(request):
    blog=Blog.objects.all()
    return render(request,'blogapp/index.html',{'blog_title':blog})

def details(request,id):
    blog=Blog.objects.get(id=id)
    return render(request,'blogapp/details.html',{'details':blog})