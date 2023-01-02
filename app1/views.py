from django.shortcuts import render

# Create your views here.

def operations(request):
    d={'name':'ram','L':[10,20,30]}


    return render(request,'operations.html',d)