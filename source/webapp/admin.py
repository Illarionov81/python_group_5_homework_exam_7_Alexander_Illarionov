from django.contrib import admin

from webapp.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    # filter_horizontal = ('tags',)
    list_filter = ('question',)
    list_display = ('pk', 'question', 'created_at')
    list_display_links = ('pk', 'question',)


class ChoiceAdmin(admin.ModelAdmin):
    list_filter = ('choice_answer',)
    list_display = ('pk', 'choice_answer',)
    list_display_links = ('pk', 'choice_answer',)


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)

