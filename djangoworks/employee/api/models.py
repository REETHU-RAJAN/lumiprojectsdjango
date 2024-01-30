from django.db import models

# Create your models here.
class employee(models.Model):

    name=models.CharField(max_length=100,unique=True)
    age=models.PositiveIntegerField()
    salary=models.PositiveIntegerField()
    department=models.CharField(max_length=150)
    email=models.EmailField()

    def __str__(self):
        return self.name