from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^registration$', views.registration_process),
    url(r'^books$', views.books),
    url(r'^login$', views.login_process),
]