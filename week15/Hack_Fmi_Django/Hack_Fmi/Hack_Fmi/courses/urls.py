from django.conf.urls import url
from Hack_Fmi.courses import views


urlpatterns = [
    url(r'^new/$', views.create_course, name='create_course'),
    url(r'^edit/(?P<course>[A-Za-z0-9]+)/$',
        views.edit_course, name="edit_course"),
    url(r'^(?P<course>[A-Za-z]+)/$', views.detail_course, name="detail_course")
]
