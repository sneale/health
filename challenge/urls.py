from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

app_name = 'challenge'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customer/(?P<customer_id>[0-9]+)/$', views.customer, name='customer'),
    url(r'^team/(?P<team_id>[0-9]+)/$', views.team, name='team'),
    url(r'^customers/$', views.CustomerList.as_view()),
    url(r'^customers/(?P<customer_id>\d+)/teams/$', views.TeamList.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)