"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import PollView, OnePollView, PollCreateView, PollUpdateView, PollDeleteView, AnswerCreateView, \
    AnswerUpdateView, AnswerDeleteView
from webapp.views.answer import CollectAnswerCreateView, AnswerSaveView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollView.as_view(), name='polls'),
    path('poll/<int:pk>/', OnePollView.as_view(), name='poll_view'),
    path('poll/add/', PollCreateView.as_view(), name='poll_create_view'),
    path('poll/<int:pk>/update/', PollUpdateView.as_view(), name='poll_update_view'),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),

    path('poll/<int:pk>/answer/add/', AnswerCreateView.as_view(), name='poll_answer_add'),
    path('answer/<int:pk>/update/', AnswerUpdateView.as_view(), name='answer_update'),
    path('poll/<int:pk>/answer/delete/', AnswerDeleteView.as_view(), name='answer_delete_view'),

    path('collect_answer/<int:pk>/', CollectAnswerCreateView.as_view(), name='collect_answer_view'),
    path('save_answer/<int:pk>/', AnswerSaveView.as_view(), name='save_answer_view'),

]
