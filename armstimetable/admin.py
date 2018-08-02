from django.contrib import admin
from .models import Lecturer, Event, Comment, Student, Specialty, allowedCourse, Responses, Signup, References


# Register your models here.


class StepInline2(admin.StackedInline):
    model = Specialty


class UserInline2(admin.ModelAdmin):
    inlines = [StepInline2, ]


class StepInline4(admin.StackedInline):
    model = References


class UserInline4(admin.ModelAdmin):
    inlines = [StepInline4, ]


class StepInline3(admin.StackedInline):
    model = Responses


class UserInline3(admin.ModelAdmin):
    inlines = [StepInline3, ]


admin.site.register(Event,UserInline4)
admin.site.register(Signup)
admin.site.register(Comment, UserInline3)
admin.site.register(Student)
admin.site.register(allowedCourse)
# admin.site.register(Responses)
admin.site.register(Lecturer, UserInline2)
