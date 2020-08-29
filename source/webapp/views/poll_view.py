from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SimpleSearchForm, PollForm
from webapp.models import Poll


class PollView(ListView):
    template_name = 'poll/polls_view.html'
    context_object_name = 'poll_list'
    model = Poll
    form = SimpleSearchForm
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        data = self.model.objects.all()
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(question__icontains=search)
        return data.order_by('-created_at')


class OnePollView(DetailView):
    template_name = 'poll/poll_detail_view.html'
    model = Poll
    paginate_comments_by = 5
    paginate_comments_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answers, page, is_paginated = self.paginate_comments(self.object)
        context['answers'] = answers
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        return context

    def paginate_comments(self, poll):
        answers = poll.choice.all()
        if answers.count() > 0:
            paginator = Paginator(answers, self.paginate_comments_by, orphans=self.paginate_comments_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1
            return page.object_list, page, is_paginated
        else:
            return answers, None, False


class PollCreateView(CreateView):
    model = Poll
    template_name = 'poll/poll_create.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/poll_update.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'poll/poll_delete.html'
    success_url = reverse_lazy('polls')




