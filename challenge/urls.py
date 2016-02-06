from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customer/(?P<customer_id>[0-9]+)/$', views.customer, name='customer'),
    url(r'^team/(?P<team_id>[0-9]+)/$', views.team, name='team'),
]