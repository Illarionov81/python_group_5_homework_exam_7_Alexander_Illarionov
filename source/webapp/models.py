from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return "{}. {}".format(self.pk, self.question)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    choice_answer = models.TextField(max_length=5000, null=False, blank=False, verbose_name='Вариант_ответа')
    poll = models.ForeignKey('webapp.Poll', related_name='choice', on_delete=models.CASCADE, verbose_name='Опрос')

    def __str__(self):
        return "{}. {}".format(self.pk, self.choice_answer)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Answer(models.Model):
    choice = models.ForeignKey('webapp.Choice', related_name='answer', on_delete=models.CASCADE, verbose_name='Ответ')
    poll = models.ForeignKey('webapp.Poll', related_name='answer', on_delete=models.CASCADE, verbose_name='Вопрос')
    add_at = models.DateTimeField(auto_now_add=True, verbose_name='Время заполнения')
    
    def __str__(self):
        return "{}".format(self.pk)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
