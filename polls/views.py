from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from polls.models import Question, Choice

from utils.debug import pprint_data

def index(request):
    latest_polls = Question.objects.order_by("-date_published")[:5]
        
    context = {
        "latest_polls": latest_polls
    }

    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, "polls/results.html", 
        {"question": question}
    )

def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        choice = question.choices.get(id=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice."
        })
    else:
        choice.votes += 1
        choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))