from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice

from utils.debug import pprint_data

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_polls"

    def get_queryset(self):
        """Get the top 5 latest polls."""
        return Question.objects.order_by("-date_published")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    


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