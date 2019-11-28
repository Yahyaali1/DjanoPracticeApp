from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import View, generic
from .models import Question, Choice
from .forms import Feedback
from django.shortcuts import render, get_object_or_404


# Create your views here.

class IndexView(generic.ListView):
    template_name = "electionsapp/index.html"
    context_object_name = "index_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class PollDetail(generic.DetailView):
    model = Question
    template_name = "electionsapp/detail.html"
    context_object_name = "question_detail"
# def welcome_message(request):
#     """
#     welcome message
#     :param request:
#     :return: Response object with html to render
#     """
#     questions = Question.objects.all()
#     context = {
#         'index_list': questions,
#     }
#     return render(request, 'electionsapp/index.html', context)
#
#


def election_index(request):
    return HttpResponse()


# def poll_detail(request, question_id):
#     """
#     We need to manage exceptions
#     We can use shortcuts if we are expecting errors and use method such as get_object_or_error
#     :param request:
#     :param question_id:
#     :return:
#     """
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404(" No such poll exist")
#
#     question = get_object_or_404(Question.objects, pk=question_id)
#
#     return render(request, 'electionsapp/detail.html', context={'question_detail': question})


def poll_results(request, question_id):
    question = get_object_or_404(Question.objects, pk=question_id)

    return render(request, 'electionsapp/results.html', context={"results": question.choice_set.all().order_by("-votes")
                                                                 })


def vote(request, question_id):
    question = get_object_or_404(Question.objects, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'electionsapp/detail.html', context={'question_detail': question, 'error_msg':
                                                                    "No Choice Selected"})
    else:
        # TODO learn F() to prevent race condition
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('elect:results', args=(question_id,)))
