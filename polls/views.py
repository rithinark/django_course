from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
# Create your views here.
def owner(request):
    return HttpResponse("Hello, world. 690db34e is the polls index.")
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
        
def results(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")
def vote(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")