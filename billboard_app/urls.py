from django.conf.urls import url
from . import views


app_name = 'billboard_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.billboard, name='billboard'),
]
