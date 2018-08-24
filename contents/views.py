from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'contents/home.html')
def abtsharks(request):
    print ("Hello")
    # return HttpResponse("<h1>Hello</h1>")
    return render(request,'contents/abtsharks.html')

def kevinOleary(request):
    return render(request,'contents/kevinOleary.html')
def daymondjohn(request):
    return render(request,'contents/daymondjohn.html')



