from django import forms

from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

def check_comma(value):
    if ',' in value:
        raise forms.ValidationError('Invalid name Recheck')
    return value

# class SubscribeForm(forms.Form):
#     first_name=forms.CharField(max_length=100,label='Enter First Name',help_text='Enter Only Characters')
#     last_name=forms.CharField(max_length=100,disabled=False,validators=[check_comma],label='Enter Last Name',help_text='Enter Only Characters')
#     email=forms.EmailField(max_length=100,validators=[check_comma],label='Enter Email')
#     def clean_first_name(self):
#         data=self.cleaned_data['first_name']
#         if ',' in data:
#             raise forms.ValidationError("Invalid first name")
#         return data
class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        labels={'first_name':_('Enter First Name'), 'last_name':_('Enter Last Name'),'email':_('Enter Email')}
        error_messages={'first_name':{'required':_('Enter First Name cannot be empty')}}
        # help_texts={'first_name':_('Enter Characters Only')}