from django import forms

from myapp.models import Todo

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class TodoForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):

        self.user=kwargs.pop("user")  #to remove user from that dictionary

        return super().__init__(*args,**kwargs)


    class Meta:

        model=Todo

        fields=["title","status"]

        widgets={
            
            "title":forms.TextInput(attrs={"class":"form-control"}),

           
        }

class RegistrationForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))


    class Meta:

        model=User

        fields=["username","email","password1","password2"]

        widgets={

            "username":forms.TextInput(attrs={"class":"form-control mb-3"}),

            "email":forms.EmailInput(attrs={"class":"form-control mb-3"}),

        }

class LoginForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2"}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-2"}))





