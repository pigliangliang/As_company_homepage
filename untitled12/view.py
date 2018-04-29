#-*-coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render,loader
from polls.forms import Addform
from  blogs.views import IndexView
from django.conf    import settings
from blogs.models import  Article,Carousel,Nav
from django.views.generic import ListView,TemplateView,DetailView
from comments.models import Comment
from systems.models import  Link




def hello(request):
    #return HttpResponse("Hello world ! ")
    if request.method =='POST':
        form = Addform(request.POST)
        if form.is_valid():
            a = form.cleaned_data['h']

            b = form.cleaned_data['s']
            return render(request,'calc_result.html',{'result':str(int(a)+int(b))})
    else:
        form = Addform()
   # return render(request,'index.html',{'form':form,'ip':request.META['REMOTE_ADDR']})

    return  HttpResponseRedirect('http:/c/180.76.246.28/blogs/')