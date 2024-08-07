from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from logs.lg_logger import log_access, log_error, log_info

def home(request):
    log_access(request)
    data = {
        'page_name':'home',
    }
    return render(request, "index.html", data)

def about(request):
    log_access(request)
    data = {
        'page_name':'about',
    }
    return render(request, "about.html", data)

def contact(request):
    log_access(request)
    data = {
        'page_name':'contact',
    }
    return render(request, "contact.html", data)

def products(request):
    log_access(request)
    data = {
        'page_name':'products',
    }
    return render(request, "products.html", data)

def rpet(request):
    log_access(request)
    data = {
        'page_name':'rpet',
    }
    return render(request, "rpet.html", data)

def terms_conds(request):
    log_access(request)
    return render(request, "terms_conds.html")

def privacy_policy(request):
    log_access(request)
    return render(request, "privacy_policy.html")

def cookies_policy(request):
    log_access(request)
    return render(request, "cookies_policy.html")
