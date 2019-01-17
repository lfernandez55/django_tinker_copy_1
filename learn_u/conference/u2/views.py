from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewPresentationForm
from .models import Presentation

def home(request):
    return HttpResponse('Hello, World!')

def apply(request):
    # presentation = get_object_or_404(Presentation, pk=pk)
    presentation = get_object_or_404(Presentation, pk=1)

    if request.method == 'POST':
        description = request.POST['description']
        presentation = Presentation.objects.create(description=description)
         #If the request is a post process the submitted form data using the class NewTopicForm in forms.py
         #then redirect to the topics list for that board
        # form = NewPresentationForm(request.POST)
        # if form.is_valid():
        #     topic = form.save(commit=False)
        #     topic.board = board
        #     topic.starter = user
        #     topic.save()
        #     post = Post.objects.create(
        #         message=form.cleaned_data.get('message'),
        #         topic=topic,
        #         created_by=user
        #     )
            # return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
            # return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
        return render(request, 'created.html')
    else:

        form = NewPresentationForm()

    return render(request, 'apply.html', {'presentation': presentation, 'form': form})
    # return render(request, 'apply.html')

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

# return HttpResponse('Apply')
# try:
#         #the below is outputted to the console
#         print ('debug', foo_id)
#         foo = Foo.objects.get(pk=foo_id)
# except Foo.DoesNotExist:
#         raise Http404("Foo does not exist")
# return render(request, 'apply.html', {'foo': foo})
