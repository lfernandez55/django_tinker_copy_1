from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewPresentationForm
from .models import Presentation
from django.template.response import TemplateResponse
from django.views import generic


def home(request):
    return render(request, 'home.html');
    # return HttpResponse('Hello, World!')

def apply(request):
    presentation = get_object_or_404(Presentation, pk=1)
    error=""
    if request.method == 'POST':
        description = request.POST['description']

        print ('number of words:', len(description.split()))
        if len(description.split()) > 15:
           # print('Submission is more than 500 words')
           error = 'Submission is more than 15 words'
        elif len(description.split()) < 10:
           # print('Submission is less than 10 words')
           error = 'Submission is less than 10 words'
        else:
           presentation = Presentation.objects.create(description=description)
           return render(request, 'created.html')
        form = NewPresentationForm()
        return render(request, 'apply.html', {'presentation': presentation, 'form': form,'error': error})
    else:
        form = NewPresentationForm()
    return render(request, 'apply.html', {'presentation': presentation, 'form': form, 'error': error })


def presentations(request):
    presentation_list = Presentation.objects.all()
    return render(request, 'presentations.html', {'presentation_list': presentation_list})

class presentations_list_view(generic.ListView):
    model = Presentation
    slug_field = 'product_slug'
    #template inferred (presentation_list.html)

class presentation_detail_view(generic.DetailView):
    model = Presentation
    #template inferred  (presentation_detail.html) (you can override it)

def foo(request):
    myString="foo"
    print('dddddddddddddddddddddebug')
    return TemplateResponse(request, 'foo.html', { 'myString': myString })


def presentation(request,presentation_id):
    presentation = Presentation.objects.get(pk=presentation_id)
    return render(request, 'presentation.html', {'presentation': presentation})
