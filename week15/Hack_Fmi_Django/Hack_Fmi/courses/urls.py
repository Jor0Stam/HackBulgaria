from django.conf.urls import url
from courses import views


urlpatterns = [
    url(r'^new/$', views.create_course, name='create_course'),
    url(r'^(?P<course>[A-Za-z]+)/$', views.detail_course, name="detail_course")
    # url(r'^edit/(?P<course>[A-Za-z]+)/$', views.edit_course, name="edit_course"),
]
