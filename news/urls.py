from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^list/$', views.list, name="news_list"),
    url(r'^entry/(?P<slug>[\w-]+)/$', views.entry, name="news_entry"),
)