from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'contents/home.html')

def abtsharks(request):
    #print ("Hello")
    # return HttpResponse("<h1>Hello</h1>")
    return render(request,'contents/abtsharks.html')

def shark_six(request):
    return render(request,'contents/shark_six.html')

def guests(request):
    return render(request,'contents/guests.html')
def contact(request):
    return render(request, 'contents/basic.html',{'content':['If you would like to contact me, please email me.','vigneshwaranethirajan@gmail.com']})



