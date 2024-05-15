"""This module contains the admin interface for the onlinecourse app."""
from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class LessonInline(admin.StackedInline):
    """This class represents the Lesson model inline in the Course model."""
    model = Lesson
    extra = 5

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    """This class represents the Course model in the admin interface."""
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    """This class represents the Lesson model in the admin interface."""
    list_display = ['title']


# <HINT> Register Question and Choice models here
class ChoiceInline(admin.StackedInline):
    """This class represents the Choice model inline in the Question model."""
    model = Choice
    extra = 2
class QuestionInline(admin.StackedInline):
    """This class represents the Question model inline in the Course model."""
    model = Question
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    """This class represents the Question model in the admin interface."""
    inlines = [ChoiceInline]
    list_display = ['content']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
