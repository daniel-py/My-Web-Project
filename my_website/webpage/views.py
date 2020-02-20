from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.

def index(request):
    return render(request, "index.html", {})

def achievement(request):
	posts = Post.objects.all()
	return render(request, "achievement.html", {'posts':posts})

def contact_us(request):
	return render(request, "contact_us.html", {})

def about(request):
	return render(request, "about.html", {})
