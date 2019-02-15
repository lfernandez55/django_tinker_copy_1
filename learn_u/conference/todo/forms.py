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

    def clean_label(self):
        label = self.cleaned_data['label']
        # if User.objects.filter(email=email).exists():
        if self.cleaned_data['label'] == 'xxxx':
            raise ValidationError("You may not call your todo 'xxxx'")
        return label
