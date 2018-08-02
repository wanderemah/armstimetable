from . import views
from django.conf.urls import url

app_name = 'timetable'

urlpatterns = [
    url(r'^activities/', views.docket, name='docket'),
    url(r'^signup/', views.Sign_up.as_view(), name='signup'),
    url(r'^add_activity/', views.Action.as_view(), name='addactivity'),
    url(r'^tutor/(?P<tutor>[A-Za-z]+)$', views.tutor_detail, name='tutordetails'),
    url(r'^query/', views.Question.as_view(), name='query'),
    url(r'^response/', views.Respond.as_view(), name='repond'),
    url(r'^topic/(?P<topic>[A-Za-z]+)$', views.topic_detail, name='topicdetails'),
    url(r'^edit_activity/(?P<pk>[A-Za-z]+)$', views.Update.as_view(), name='editactivity'),
    url(r'^delete_activity/(?P<pk>[A-Za-z]+)$', views.delete, name='deleteactivity'),
    # url(r'^description',views.description, name='description'),
]
