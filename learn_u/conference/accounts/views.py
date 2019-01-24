from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('debugHERE valid form')
            user = form.save()
            auth_login(request, user)
            return redirect('homeward')
        else:
            print('debugHERE INVALID form')
    else:

        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
