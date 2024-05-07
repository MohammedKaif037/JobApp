from django.shortcuts import render

from uploadapp.forms import UploadFileForm

# Create your views here.
def upload_image(request):
    if request.method=='POST':
        form=UploadFileForm(request.POST,request.FILES)#accept form with post data and files
        if form.is_valid():
            form.save()
    else:
        uploadform=UploadFileForm()
    return render(request,'uploadapp/addimage.html',context={'form':uploadform})