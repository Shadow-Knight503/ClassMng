from cloudinary.forms import CloudinaryFileField
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from Home.models import UserProf, Code


class CreateUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username']
        help_texts = {
            'username': 'This is your identification value so it must be unique'
        }

    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'


class UserProfPage(forms.ModelForm):
    class Meta:
        model = UserProf
        fields = ['Name', 'Profile_pic', 'RollNo']
        help_texts = {
            'Name': 'This will act as your display name',
        }

    def __init__(self, *args, **kwargs):
        super(UserProfPage, self).__init__(*args, **kwargs)

        self.fields['Name'].widget.attrs['class'] = 'form-control'
        self.fields['Profile_pic'].widget.attrs['class'] = 'form-control'
        self.fields['RollNo'].widget.attrs['class'] = 'form-control'

    Profile_pic = CloudinaryFileField(
        options={
            'folder': 'Profile/',
            'overwrite': True,
            'resource_type': 'image',
            'invalidate': True,
        })


class LoginUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']

    def __init__(self, *args, **kwargs):
        super(LoginUser, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'

        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None


class CodeSubForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['Author', 'Problem', 'ScrSht']

    def __init__(self, *args, **kwargs):
        super(CodeSubForm, self).__init__(*args, **kwargs)

        self.fields['Author'].widget.attrs['class'] = 'form-control'
        self.fields['Problem'].widget.attrs['class'] = 'form-control'
        self.fields['ScrSht'].widget.attrs['class'] = 'form-controlx'

    ScrSht = CloudinaryFileField(
        options={
            'folder': 'ScreenShots/',
            'overwrite': True,
            'resource_type': 'image',
            'invalidate': True,
        })
