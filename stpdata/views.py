from django.shortcuts import render

from stpdata.models import Product


def products(request):
    params = request.GET
    amount = params.get('amount')
    investors = params.get('investors')
    filter_params = {}
    for k, v in params.items():
        if not v or k in ('amount', 'investors'):
            continue
        filter_params.update({k:v})
    if investors:
        investors_list = investors.split('-')
        for inv in investors_list:
            if not inv:
                continue
            filter_params.update({inv: True})

    products = Product.objects.all().filter(**filter_params)
    if amount:
        start_amount, end_amount = tuple(amount.split('-'))
        print(end_amount)
        if start_amount:
            products = products.filter(amount__gte=int(start_amount))
        if end_amount:
            products = products.filter(amount__lte=int(end_amount))




    context = {'products': products}
    # print(context)
    return render(request, 'stpdata/stpdata.html', context)

# def detail(request, pk=None):
#     product=Product.objects.all().filter(id=pk)
#     context={'product':product}
#     return render(request, 'stpdata/product_display.html',context)




