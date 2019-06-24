from django import forms
from .models import Profile,Image,Comments

class NewImageForm(forms.ModelForm):
  class Meta:
    model=Image
    exclude = ['user','likes','comments']

class NewProfileForm(forms.ModelForm):
  class Meta:
    model=Profile
    exclude = ['user']

class NewCommentForm(forms.ModelForm):
  class Meta:
    model=Comments
    exclude = ['user','image']