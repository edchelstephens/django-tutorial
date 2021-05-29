from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from polls.models import Question

def index(request):
    latest_polls = Question.objects.order_by("-date_published")[:5]
        
    context = {
        "latest_polls": latest_polls
    }

    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)