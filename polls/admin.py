#-*-coding:utf-8 -*-
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question,Choice
'''
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
'''
admin.site.site_header = "系统管理"



class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text','pub_date')
    '''
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]'''
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question','choice_text','votes')
    #fields = ('question','choice_text')


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)