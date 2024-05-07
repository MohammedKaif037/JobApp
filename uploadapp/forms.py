from . models import Uploads
from  django import forms

class UploadFileForm(forms.ModelForm):
    class  Meta:
        model=Uploads
        fields='__all__'