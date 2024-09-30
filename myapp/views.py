from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import TodoForm,RegistrationForm,LoginForm

from django.contrib.auth import authenticate,login,logout

from myapp.models import Todo

from django.contrib import messages

from myapp.decorators import signin_required

from django.utils.decorators import method_decorator



# Create your views here.
@method_decorator(signin_required,name="dispatch")
class TodoCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=TodoForm(user=request.user)

        return render(request,"todo_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=TodoForm(request.POST,user=request.user)

        if form_instance.is_valid():

            # form_instance.save()
            data=form_instance.cleaned_data

            Todo.objects.create(**data,owner=request.user)

            return redirect("todo-list")
        
        else:

            return render(request,"todo_add.html",{"form":form_instance})
        

class TodoListView(View):

    def get(self,request,*args,**kwargs):

        qs=Todo.objects.filter(owner=request.user)

        return render(request,"todo_list.html",{"qs":qs})
        



        

class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=RegistrationForm()

        return render(request,"register.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=RegistrationForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            print("register successfully...")

            messages.success(request,'account created successfuly')

            return redirect("signin")

        else:

            print("registration failed")

            messages.success(request,'account creation failed')

            return render(request,"register.html",{"form":form_instance})
        
class SignInView(View):

    def get(self,request,*args,**kwargs):

        form_instance=LoginForm()

        return render(request,"login.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=LoginForm(request.POST)

        if form_instance.is_valid():
             
             data=form_instance.cleaned_data

             user_obj=authenticate(request,**form_instance.cleaned_data)
     
             if user_obj:
     
                 login(request,user_obj)

                 print("successfully...")

                #  messages.success(request,'Login Successfully..!')
     
                 return redirect("todo-dis")
             
        print("login failed")

        messages.success(request,'Login failed..!')
            
        return render(request,"login.html",{"form":form_instance})
    
@method_decorator(signin_required,name="dispatch")
class TodoUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        todo_obj=Todo.objects.get(id=id)

        form_instance=TodoForm(instance=todo_obj,user=request.user)

        return render(request,"todo_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        todo_obj=Todo.objects.get(id=id)

        form_instance=TodoForm(request.POST,instance=todo_obj,user=request.user)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("todo-list")
        
        else:

            return render(request,"todo_edit.html",{"form":form_instance})
        
@method_decorator(signin_required,name="dispatch")       
class TodoDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Todo.objects.get(id=id).delete()

        return redirect("todo-list")
    
class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")
    
class TodoDiscriptionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"todo_discription.html")
    
    def post(self,request,*args,**kwargs):

        return redirect('todo-add')





    


             

            




            



    




