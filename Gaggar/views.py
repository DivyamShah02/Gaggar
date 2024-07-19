from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from logs.lg_logger import log_access, log_error, log_info

def home(request):
    log_access(request)
    return render(template_name="index.html", request=request)

def about(request):
    log_access(request)
    return render(template_name="about.html", request=request)

def contact(request):
    log_access(request)
    return render(template_name="contact.html", request=request)

def products(request):
    log_access(request)
    return render(template_name="products.html", request=request)
