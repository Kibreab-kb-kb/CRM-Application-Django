from django.shortcuts import render,redirect
from .forms  import CreateUserForm,LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User




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
    return render(request,'webapps/register.html',context=context)





#login

def login(request):
   form=LoginForm()
   if request.method=='POST':
      form=LoginForm(request,data=request.POST)

      if form.is_valid():
         username=form.cleaned_data['username']
         password=form.cleaned_data['password']

         user=authenticate(request,username=username,password=password)
      
         if user is not None:
          auth.login(request,user)
          # redirect('')

   context={'form':form}

   return render(request,'webapps/login.html', context=context)






       


   
 







 



