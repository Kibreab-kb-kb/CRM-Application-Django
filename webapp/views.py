from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, Django!")
  return render(request,'webapps/index.html')



 



