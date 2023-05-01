from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("Log in")

def signup(request):
    return HttpResponse("Sign up")
