from django.shortcuts import render

from uploadapp.forms import UploadActualFileForm, UploadFileForm

# Create your views here.
def upload_image(request):
    if request.method=='POST':
        form=UploadFileForm(request.POST,request.FILES)#accept form with post data and files
        if form.is_valid():
            form.save()
            saved_object=form.instance
            return render(request,'uploadapp/addimage.html',{'form':form, 'saved_object':saved_object})
    else:
        form=UploadFileForm()
    return render(request,'uploadapp/addimage.html',context={'form':form})

def upload_file(request):
    if request.method=='POST':
        form=UploadActualFileForm(request.POST,request.FILES)#accept form with post data and files
        if form.is_valid():
            form.save()
            saved_object=form.instance
            return render(request,'uploadapp/addfile.html',{'form':form, 'saved_object':saved_object})
    else:
        form= UploadActualFileForm()
    return render(request,'uploadapp/addfile.html',context={'form':form})