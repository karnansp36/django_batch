from django import forms
from .models import User_db, image_storage

class UserForm(forms.ModelForm):
    class Meta:
        model = User_db
        exclude = ['created_at', 'updated_at']
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control username', "id":'username'}),
        }
class ImageForm(forms.ModelForm):
    class Meta:
        model = image_storage
        fields = ['image', 'description', 'files']
       
