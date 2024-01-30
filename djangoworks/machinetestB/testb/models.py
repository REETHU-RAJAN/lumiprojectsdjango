from django.db import models

class Category(models.Model):

    category_name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    product_name=models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    
    price=models.PositiveIntegerField()
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    
   
        
    def __str__(self):
        return self.name
