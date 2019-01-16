from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from django.db import models
from .models import Presentation

def home(request):
    return HttpResponse('Hello, World!')

def apply(request):
    # return HttpResponse('Apply')
    # try:
    #         #the below is outputted to the console
    #         print ('debug', foo_id)
    #         foo = Foo.objects.get(pk=foo_id)
    # except Foo.DoesNotExist:
    #         raise Http404("Foo does not exist")
    # return render(request, 'apply.html', {'foo': foo})
    return render(request, 'apply.html')

def presentations(request):
    # return HttpResponse('Apply')
    presentation_list = Presentation.objects.all()
    # try:
    #         #the below is outputted to the console
    #         print ('debug')
    #         presentations = Presentations.objects.all()
    # except Presentations.DoesNotExist:
    #         raise Http404("Presentations does not exist ZZZZZZZZZZZZZZ")
    return render(request, 'presentations.html', {'presentation_list': presentation_list})
    # return render(request, 'presentations.html')
