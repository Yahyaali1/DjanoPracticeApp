import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=255, verbose_name="Election Type")
    pub_date = models.DateTimeField(verbose_name="Date of Election")

    def __str__(self):
        return self.question_text

    def was_recent_pub(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.choice_text} and vote count {self.votes}'


