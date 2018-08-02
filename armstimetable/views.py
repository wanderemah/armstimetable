from django.shortcuts import render, redirect
from .models import Lecturer, Event, Comment, Responses, Signup
from final.forms import Userform, Add, Queries, Response, SignForm
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
import time
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required


#
#
# # Create your views here.
#
#

@login_required
def docket(request):
    events = Event.objects.order_by('date')
    query = Comment.objects.all()
    return render(request, 'armstimetable/timetable.html',
                  {'events': events, 'queries': query})


# def action(request):
#     if request.method == 'POST':
#         form = Add(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('timetable:docket')
#     else:
#         form = Add()
#     return render(request, 'itinerary/activity.html', {'form': form})


# class Action(View):
#     form_class = Add
#     template_name = 'itinerary/activity.html'
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'aform': form})
#
#     def post(self, request):
#         form = self.form_class(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('timetable:docket'))
#
#         return render(request, self.template_name, {'aform': form})


#
#
#
#
def topic_detail(request, topic):
    subject = Event.objects.get(pk=topic)
    return render(request, 'itinerary/topic.html', {'topic': subject})


def tutor_detail(request, tutor):
    person = Lecturer.objects.get(name=tutor)
    return render(request, 'itinerary/tutor.html', {'person': person})


class Update(UpdateView):
    model = Event
    fields = ['topic', 'description', 'date', 'tutor', 'venue']

class Action(CreateView):
    model = Event
    fields = ['topic', 'description', 'date', 'tutor', 'venue']


class Sign_up(View):
    user_form_class = Userform
    profile_form_class = SignForm
    template_name = 'signup.html'

    def get(self, request):
        user_form = self.user_form_class(None)
        profile_form = self.profile_form_class(None)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        user_form = self.user_form_class(data=request.POST)
        profile_form = self.profile_form_class(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            if user is not None:
                login(request, user)
                return redirect('timetable:docket')

        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})




class Question(View):
    form_class = Queries
    template_name = 'itinerary/query.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'yform': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.save()
            return redirect('timetable:docket')

        return render(request, self.template_name, {'yform': form})


class Respond(View):
    form_class = Response
    template_name = 'itinerary/response.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'myform': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.save()
            return redirect('timetable:docket')

        return render(request, self.template_name, {'myform': form})


def delete(request, pk):
    item = Event.objects.get(pk=pk)
    item.delete()
    return redirect('timetable:docket')
