from django.shortcuts import render
from .models import *


# Create your views here.

def home_page(request):
    content = Posts.objects.all()
    return render(request, 'home.html', {"BlogPosts": content})

