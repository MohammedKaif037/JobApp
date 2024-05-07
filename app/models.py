from django.db import models
from django.utils.text import slugify


class skills(models.Model):
    name=models.CharField(max_length=100)

class author(models.Model):
    name=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)

class location(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    zip=models.CharField(max_length=100)
# Create your models here.
class JobPost(models.Model):
    JOB_TYPE_CHOICES=[
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
        ('Contract','Contract'),
        ('Internship','Internship'),
        ('Freelance','Freelance'),
    ]
    title=models.CharField(max_length=50)
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    expiry=models.DateField(null=True)
    salary=models.IntegerField() 
    slug =models.SlugField(null=True,max_length=40,unique=True)
    location=models.OneToOneField(location,on_delete=models.CASCADE, null=True)
    author=models.ForeignKey(author,null=True,on_delete=models.CASCADE)
    skills=models.ManyToManyField(skills,)
    job_type=models.CharField(max_length=200,null=False,choices=JOB_TYPE_CHOICES)

    def save(self,*args,**kwargs):
        if not self.id:
             self.slug=slugify(self.title) # to prevent updation of slug since it is part of url
        return super(JobPost,self).save(*args,**kwargs)        
    # def __str__(self):
    #     return self.title

    def __str__(self):
        return f"{self.title} with salary {self.salary}"


 