from django.shortcuts import render,get_object_or_404,render_to_response

# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from  models import  Question,Choice
from django.template import loader
from django.core.urlresolvers import reverse
#from django.core.urlresolvers import
from .forms import Addform





def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:10]
    #template = loader.get_template('index.html')
    #output= ','.join([q.question_text for q in latest_question_list])
    content = {
                'latest_question_list':latest_question_list
    }
    return render(request, 'polls/index.html', content)


def detail(request, question_id):
    '''
    try:
        question =Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('question doesnot exist...')
    return render(request,'polls/detail.html',{'question':question})
        '''
    question = get_object_or_404(Question,pk=question_id)
    return  render(request,'polls/detail.html',{'question':question})

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question,pk=question_id)
    return  render(request,'polls/results.html',{'question':question})

def vote(request, question_id):
    p = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form.
         return render(request, 'polls/detail.html', {
        'question': p,
        'error_message': "You didn't select a choice.",
         })

    else:
        selected_choice.votes += 1
        selected_choice.save()
# Always return an HttpResponseRedirect after successfully dealing
# with POST data. This prevents data from being posted twice if a
# user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
   # return HttpResponse("You're voting on question %s." % question_id)