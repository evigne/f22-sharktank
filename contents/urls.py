from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^abtsharks/',views.abtsharks,name='abtsharks'),
    url(r'^kevinOleary/',views.kevinOleary,name='KevinOleary'),
    url(r'^daymondjohn/',views.daymondjohn,name='diamondjohn'),
]