from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^application/', views.application, name='application'),
    url(r'^route/', views.route, name='route'),
    url(r'^details/', views.details, name='details'),
    url(r'^participants/', views.participants, name='participants'),
    url(r'^thanks/', views.thanks, name='thanks'),
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^sponsors/', views.sponsors, name='sponsors')
]

urlpatterns += staticfiles_urlpatterns()