from django.shortcuts import render

from stpdata.models import Product


def products(request):
    detail(request,1)
    print("inside products")
    season = request.GET.get('season')
    deal = request.GET.get('deal')
    gender=request.GET.get('gender')
    products = Product.objects.all().filter(season=season,entrepreneur_gender=gender, deal=deal)
    context = {'products': products}
    return render(request, 'stpdata/stpdata.html', context)

def detail(request, pk=None):
    product=Product.objects.all().filter(id=pk)
    context={'product':product}
    return render(request, 'stpdata/product_display.html',context)




