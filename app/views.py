from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from app.models import JobPost
# Create your views here.
def hello(request):
    tempobj=TempClass()
    some_list=["abc", "def", "efd"]
    return render(request, 'app/index.html',context={"name":"kaif","description":some_list,"classvalue":tempobj,"age":23,"colors":["red","green","yellow","blue"]})
# def jobdetail(request,id):
#     return HttpResponse(f"<h2>Job Detail Page for job {id}<h2>")

# def jobdetail(request,id):
#     if id==0:
#         return redirect(reverse('alljobs'))
#     return_html=f"<h2>Job Title {job_title[id]}</h2><h3> Job Description {job_description[id]}</h3>"
#     return HttpResponse( return_html)

def jobdetail(request,id):
    if id==0:
        return redirect(reverse('alljobs'))
    # return_html=f"<h2>Job Title {job_title[id]}</h2><h3> Job Description {job_description[id]}</h3>"
    # data={"jobtitle":job_title[id],"jobdescription":job_description[id]}
    data=JobPost.objects.get(id=id)
    context={'data':data}
    return render(request,'app/jobdetail.html',context=context)

# def alljobs(request):
#     res='<ul>'
#     for i in job_title:
#         job_id=job_title.index(i)
#         # print(reverse('jobdetail',args=(job_id,)))
#         resulting_url=reverse('jobdetail',args=(job_id,))
#         # res+=f"<li><a href='job/{job_id}'>{i}</li>"
#         res+=f"<li><a href='{resulting_url}'>{i}</li>"

#     res+='</ul>'
#     return HttpResponse(res)
def alljobs(request):
    jobs=JobPost.objects.all()
    context={'jobs':jobs}
    return render(request, 'app/index.html',context=context)