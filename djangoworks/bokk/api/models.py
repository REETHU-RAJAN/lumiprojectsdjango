from django.db import models

# Create your models here.
class bokks(models.Model):
    # name,age,salary,department,email
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    category=models.CharField(max_length=20)
    price=models.PositiveIntegerField()
    

    def __str__(self) -> str:
        return self.name