from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from webapp.models import Poll, Choice, Answer


class CollectAnswerCreateView(View):

    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        answers = poll.choice.all()
        context = {'poll': poll, 'answers': answers}
        return render(request, 'answer/answer.html', context)


class AnswerSaveView(View):

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if request.POST.get('id'):
                answer = Answer()
                poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
                answer.choice_id = request.POST.get('id')
                answer.poll_id = poll.pk
                answer.save()
        return redirect('polls')
