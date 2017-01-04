from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'travels$', (views.index)),
    url(r'logout$', (views.logout)),
    url(r'add_page$', (views.add_page)),
    url(r'add$', (views.add)),
    url(r'trip/(?P<id>\d*)$', views.trip),
    url(r'join/(?P<id>\d*)$', views.join)
]
