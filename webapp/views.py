from django.shortcuts import render,redirect
from .forms  import CreateUserForm,LoginForm,CreateRecordForm,UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Record


#Home page

def home(request):
    # return HttpResponse("Hello, Django!")
  return render(request,'webapps/index.html')


#register page

def register(request):
    form = CreateUserForm()
    if request.method=='POST':
       form=CreateUserForm(request.POST)

       if form.is_valid():
          form.save()
          return redirect('login')
    

    context={'form':form}
    return render(request,'webapps/register.html',context=context)





#login page

def login(request):
   form=LoginForm()
   if request.method=='POST':
      form=LoginForm(request,data=request.POST)

      if form.is_valid():
         username=form.cleaned_data['username']
         password=form.cleaned_data['password']

         user=authenticate(request,username=username,password=password)
      
         if user is not None:
          auth_login(request,user)
          return redirect('dashboard')
      

   context={'form':form}

   return render(request,'webapps/login.html', context=context)





#logout page

def logout(request):
   auth_logout(request)
   return redirect('login')



#dashboard page
  
@login_required(login_url='login')
def dashboard(request):
   records=Record.objects.all()
   context={'records':records}
   
   return render(request,'webapps/dashboard.html',context=context)




#Create a record

@login_required(login_url='login')
def create_record(request):
   form=CreateRecordForm()
   if request.method=='POST':
      form=CreateRecordForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('dashboard')
   context={'form':form}
   return render(request,'webapps/create_record.html',context=context)



#Update a record

@login_required(login_url='login')
def update_record(request,pk):
   record=Record.objects.get(id=pk)
   form=UpdateRecordForm(instance=record)
   if request.method=='POST':
      form=UpdateRecordForm(request.POST,instance=record)
      if form.is_valid():
         form.save()
         return redirect('dashboard')
   context={'form':form}
   return render(request,'webapps/update_record.html',context=context)

   


