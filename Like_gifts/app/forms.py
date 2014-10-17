# -*- coding: utf-8 -*-
"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from app.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image_files = forms.ImageField()

class FileUploadForm(forms.Form):
    """Image upload form."""
    product_files = forms.FileField()

#right now not using
class UserForm(ModelForm):

    class Meta:
        model = Users

        fields=['userid','useremail','userpassword','userfirstname','userlastname','usercity','userstate','userzip','useremailverified','userregistrationdate','userverificationcode','userip','userphone','userfax','usercountry','useraddress','useraddress2']