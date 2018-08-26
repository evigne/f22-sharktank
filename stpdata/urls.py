from django.conf.urls import url
from django.views.generic import ListView,DetailView
from stpdata.models import Product
from . import views

urlpatterns=[

    url(r'',views.products,name='products'),
    url(r'^(?P<pk>\d+)$',views.detail,name='details_product'),
    #url(r'products/(?P<pk>\d+)',DetailView.as_view(model=Product,template_name="stpdata/product_display.html")),
]
