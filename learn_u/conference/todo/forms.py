from django import forms
from .models import Todo
from django.core.exceptions import ValidationError

class NewTodoForm(forms.ModelForm):

    label = forms.CharField(
        widget=forms.TextInput(
        attrs={'placeholder': 'Write your todo label here'}
        ),
        max_length=300,
        help_text='The max length of the text is 300.'
    )
    class Meta:
        model = Todo
        fields = ['label' ]
