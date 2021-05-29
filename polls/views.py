from django.shortcuts import render
from django.http import HttpResponse, response

def index(request):
    return HttpResponse("Hi! Welcome to ed's pollsite! This is the site index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question {}".format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)