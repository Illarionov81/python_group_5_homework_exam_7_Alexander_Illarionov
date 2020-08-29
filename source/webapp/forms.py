from django import forms
from webapp.models import Poll, Choice, Answer
from django.forms import widgets


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_answer']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['choice']
        widgets = {'choice': forms.widgets.Select}
