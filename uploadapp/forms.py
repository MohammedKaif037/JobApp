from . models import Uploads, UploadsFile
from  django import forms

class UploadFileForm(forms.ModelForm):
    class  Meta:
        model=Uploads
        fields='__all__'

class UploadActualFileForm(forms.ModelForm):
    class  Meta:
        model=UploadsFile
        fields='__all__'