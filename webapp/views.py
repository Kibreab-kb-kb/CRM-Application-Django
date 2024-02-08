from django.shortcuts import render,redirect
from .forms  import CreateUserForm,LoginForm



#Homepage

def home(request):
    # return HttpResponse("Hello, Django!")
  return render(request,'webapps/index.html')


#register

def register(request):
    form = CreateUserForm()
    if request.method=='POST':
       form=CreateUserForm(request.POST)

       if form.is_valid():
          form.save()
          # return redirect('')
    

    context={'form':form}
       


   
 







 



