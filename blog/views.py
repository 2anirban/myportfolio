from django.shortcuts import render
from .models import *

def allBlogs(request):
    blogs=Blog.objects
    return render(request,"blog/allblogs.html",{"blog4":blogs})
