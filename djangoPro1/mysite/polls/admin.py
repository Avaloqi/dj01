from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_data', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_data'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'myPub_data', 'was_published_recently')
    list_filter = ['pub_data']
    search_fields = ['question_text']


# Register your models here.
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
