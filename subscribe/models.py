from django.db import models


NEWSLETTER_OPTIONS=[
    ('W','weekly'),
    ('M','monthly'),
]
# Create your models here.
class Subscribe(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    option=models.CharField(max_length=2,choices=NEWSLETTER_OPTIONS)


