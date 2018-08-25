from django.conf.urls import url
from django.views.generic import ListView,DetailView
from stpdata.models import Product

urlpatterns=[
    url(r'^$',ListView.as_view(queryset=Product.objects.all()[:25],template_name="stpdata/stpdata.html"))
]
