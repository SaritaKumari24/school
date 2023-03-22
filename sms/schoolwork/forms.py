from django.forms import ModelForm ,Form,CharField,PasswordInput
from .models import Student,Classes



class StudentForm(ModelForm):
    class Meta:
        model =Student
        fields="__all__"
        exclude =("isApproved","rf_code")

class EditStudentForm(ModelForm):
    class Meta:
        model=Student
        exclude=("isApproved",)        

# class LoginForm(Form):
#     username =  CharField(max_length=200)
#     password =CharField(max_length=200,widget=PasswordInput())  
class ClassForm(ModelForm):
    class Meta:
        model = Classes
        fields ="__all__"      
    