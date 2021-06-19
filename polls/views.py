from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
    

class VoteView(generic.View):
    """Sample API View to handle request passed arguments from another view."""
    def post(self, request, from_api=False, data=None, *args, **kwargs):
        try:

            question_id = data.get("question_id")
            choice_id = data.get("choice_id")

            question = Question.objects.get(id=question_id)
            choice = question.choices.get(id=choice_id)

            choice.votes = F("votes") + 1
            choice.save()
            
            choice.refresh_from_db()
            message = "Poll updated!"
            response = {
                "message": message,
                "question": question.name,
                "choice": choice.name,
                "votes": choice.votes,
                "success": True
            }

            if from_api:
                return response
            else:
                return HttpResponse(message)

        except Question.DoesNotExist:
            return HttpResponse("Question does not exists!", status=404)

        except Choice.DoesNotExist:
            return HttpResponse("Choice does not exists!", status=404)

        except Exception as exc:
            debug_exception(exc)
            raise exc

class Votes(generic.View):
    """Class based view for voting"""
    redirect = True

    def post(self, request, question_id, *args, **kwargs):
        try:

            form_data = request.POST.copy()
            
            data = {
                "question_id": question_id,
                "choice_id": form_data.get("choice_id")
            }

            api_view = VoteView.as_view()
            results = api_view(request, from_api=True, data=data)
            
            if self.redirect:
                response = HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
            else: 
                response = JsonResponse(data=results)

            return response
        except Exception as exc:
            debug_exception(exc)
            return HttpResponse("Error")
