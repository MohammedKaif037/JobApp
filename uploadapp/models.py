from django.db import models

# Create your models here.
class  Uploads(models.Model):
    image=models.ImageField(upload_to='images')#  images are uploaded on server rather than on the database
    description=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.description

class UploadsFile(models.Model):
    file=models.FileField(upload_to='files')
    description=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.description