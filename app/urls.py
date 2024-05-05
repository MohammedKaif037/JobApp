from django.urls import path

from app.views import alljobs, hello,jobdetail


urlpatterns = [
    # path("",hello),
    # path("/job/1",jobdetail) would not work
    # path("job/1",jobdetail)  # would work too 
    path("job/<int:id>",jobdetail,name='jobdetail'), #  would work
    path("",alljobs,name='alljobs'),
    path("hello",hello)
]
