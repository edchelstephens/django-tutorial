from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from polls.models.question import Question
from polls.models.choice import Choice

from utils.debug import debug_exception, pprint_data

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_polls"

    def get_queryset(self):
        """Get the top 5 latest polls.*
        
        *Not including questions that are set to be
        published in the future.
        """
        return Question.objects.filter(
            date_published__lte=timezone.now()
        ).order_by("-date_published")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """Only show questions that are already published.*
        
        *Hide futue questions, i.e futures with date_published > timezone.now()
        """
        return Question.objects.filter(date_published__lte=timezone.now())


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


class APIView(generic.View):
    """Sample API View to handle request passed arguments from another view."""
    def post(self, request, from_api=False, data=None, *args, **kwargs):
        try:
            response = {
                "data": data
            }

            if from_api:
                return response
            else:
                return HttpResponse(response)

        except Exception as exc:
            debug_exception(exc)
            raise exc

class VoteView(generic.View):
    """Class based view for voting"""
    
    def post(self, request, question_id, *args, **kwargs):
        try:

            data = {"question_id": question_id}

            api_view = APIView.as_view()
            response = api_view(request, from_api=True, data=data)


            return HttpResponse(response, content_type="application/json")
        except Exception as exc:
            debug_exception(exc)
            return HttpResponse("Error")

def vote_new(request, question_id):
    """function based voting view"""
    try:

        data = {
            "question_id": question_id
        }

        api_view = APIView.as_view()
        response = api_view(request)

        return HttpResponse(response, content_type="application/json")


    except Exception as exc:
        debug_exception(exc)
        return HttpResponse("Error", status=400)
