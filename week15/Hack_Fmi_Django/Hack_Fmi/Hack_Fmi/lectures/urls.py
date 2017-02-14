from django.conf.urls import url
from Hack_Fmi.lectures import views


urlpatterns = [
    url(r'^new/$', views.create_lecture,
        name='create_lecture'),
    url(r'^(?P<lecture>[A-Za-z0-9]+)/$', views.detail_lecture,
        name="detail_lecture")
]
