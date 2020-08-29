from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.models import Poll, Choice
from webapp.forms import ChoiceForm


class AnswerCreateView(CreateView):
    model = Choice
    template_name = 'choice/choice_create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        answer = form.save(commit=False)
        answer.poll = poll
        answer.save()
        return redirect('poll_view', pk=poll.pk)


class AnswerUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/choice_update.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})
