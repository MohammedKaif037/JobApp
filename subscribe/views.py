from django.shortcuts import redirect, render
from django.urls import reverse

from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

# Create your views here.
# def subscribe(request):
#     error_message=''
#     if not request.POST['fname']:
#         error_message+='You must enter a name'
#     if not request.POST['email']:
#         error_message+='You must enter email'


#     context={error_message:error_message}
#     return render(request,'subscribe/subscribe.html',context=context)

def subscribe(request):
    subscribe_form=SubscribeForm()  
    if request.POST:
        subscribe_form=SubscribeForm(request.POST) # binding data to form creating instance with data coming from the form
        if subscribe_form.is_valid():
            '''print('Valid form')
            print(subscribe_form.cleaned_data)
            first_name=subscribe_form.cleaned_data['first_name']
            last_name=subscribe_form.cleaned_data['last_name']
            email=subscribe_form.cleaned_data['email']
            subscribe=Subscribe(email=email, first_name=first_name, last_name=last_name,)
            subscribe.save()'''
            subscribe_form.save() # this happened because we now used model forms
            return redirect(reverse('thank_you'))
        # subscribe=Subscribe(last_name=lname,email=email,first_name=fname, )
        
    context={'form':subscribe_form}

    return render(request,'subscribe/subscribe.html',context= context)


def thank_you(request):
    return render(request,'subscribe/thank_you.html')