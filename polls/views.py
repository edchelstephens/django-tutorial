from pprint import pprint
from django.http import HttpResponse, HttpResponseRedirect, response
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from polls.models.question import Question
from polls.models.choice import Choice

from utils.debug import debug_exception, pprint_data

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


class APIView(generic.View):
    """Sample API View to handle request passed arguments from another view."""
    def post(self, request, from_api=False, data=None, *args, **kwargs):
        try:
            pprint_data(request, "in APIView request", bg="blue")
            pprint_data(from_api, "from api", bg="blue")
            pprint_data(data, "passed data", bg="blue")
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

            pprint_data(request, "In VoteView class based view")
            data = {"question_id": question_id}

            api_view = APIView.as_view()
            response = api_view(request, from_api=True, data=data)

            pprint_data(response, "response from APIView.as_view() then passed with request and other arguments")

            return HttpResponse(response, content_type="application/json")
        except Exception as exc:
            debug_exception(exc)
            return HttpResponse("Error")

def vote_new(request, question_id):
    """function based voting view"""
    try:
        pprint_data(request, "In vote_new function based view")

        data = {
            "question_id": question_id
        }

        api_view = APIView.as_view()
        response = api_view(request)
        pprint_data(response, "Response from api_view")

        return HttpResponse(response, content_type="application/json")


    except Exception as exc:
        debug_exception(exc)
        return HttpResponse("Error", status=400)
