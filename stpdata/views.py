from django.shortcuts import render

from stpdata.models import Product


def products(request):
    params = request.GET
    filter_params = {}
    for k, v in params.items():
        if not v:
            continue
        filter_params.update({k:v})
    products = Product.objects.all().filter(**filter_params)

    context = {'products': products}
    return render(request, 'stpdata/stpdata.html', context)

def detail(request, pk=None):
    product=Product.objects.all().filter(id=pk)
    context={'product':product}
    return render(request, 'stpdata/product_display.html',context)




