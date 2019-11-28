from django.contrib import admin

from .models import Question, Choice
# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = Choice
    readonly_fields = ['votes']
    can_delete = False
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'question_text')
    fieldsets = [(None,               {'fields': ['question_text']}),
                 ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
                 ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

