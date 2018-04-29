# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.db import models
from django.utils.encoding import  python_2_unicode_compatible
from  django.utils import timezone
import datetime


@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField('问题',max_length=200)
    pub_date = models.DateTimeField('发布日期',)

    def __str__(self):
        return  self.question_text
    #def was_published_recently(self):
    #   return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name='问题'
        verbose_name_plural='问题'
        ordering=['pub_date',]


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选择内容',max_length=200)
    votes = models.IntegerField('票数',default=0)

    def __str__(self):
        return self.choice_text
    class Meta:
        verbose_name='选择'
        verbose_name_plural='选择'
        ordering=['votes',]