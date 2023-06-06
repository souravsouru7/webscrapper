from django.db import models

# Create your models here.

class Links(models.Model):
    def __str__(self):
        return self.name


    adress=models.CharField(max_length=1000,null=True,blank=True)
    name=models.CharField(max_length=1000,null=True,blank=True)


