from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi! Welcome to ed's pollsite! This is the site index.")