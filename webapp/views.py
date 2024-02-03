from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello, Django!")
  return render(request,'webapps/index.html')


def base(request):
    return render(request,'webapps/base.html')



