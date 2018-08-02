from django import forms
from django.contrib.auth.models import User
from armstimetable.models import Event, Comment, Responses, Signup


class Add(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['tutor','date', 'topic', 'description','venue']


class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class SignForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = Signup
        fields = ['picture']


class Queries(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['student', 'topic', 'query']


class Response(forms.ModelForm):
    class Meta:
        model = Responses
        fields = ['query', 'tutor', 'answer']
