from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^abtsharks/',views.abtsharks,name='abtsharks'),
    url(r'^shark_six/',views.shark_six,name='SharkSix'),
    url(r'^guests/',views.guests,name='guests'),
]