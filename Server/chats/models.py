from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User , related_name='person')
    GENDER = (
        (Male , 'male'),
        (Female , 'female'),
    )
    gender = models.CharField(choices=GENDER , max_length=5)
