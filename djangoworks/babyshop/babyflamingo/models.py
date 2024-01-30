from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from datetime import date



class User(AbstractUser):

    phone=models.CharField(max_length=100,unique=True)
    address=models.CharField(max_length=200)


class Category(models.Model):

    name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Toys(models.Model):
    name=models.CharField(max_length=200)


    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    options=(
        ('electric-toy','electric-toy'),
        ('battery-toy','battery-toy'),
        ('plastic-toy','palstic-toy')
       
    )
    mode=models.CharField(max_length=200,choices=options,default="plastic-toy")

    image=models.ImageField(upload_to="images")
    @property
    def varients(self):
       
        qs=self.toyvarients_set.all()
        
        return qs
    @property
    def reviews(self):
        qs=self.reviewstoy_set.all()
        return qs
    @property
    def avg_rating(self):
        ratings=self.reviewstoy_set.all().values_list("rating",flat=True)
        return sum(ratings)/len(ratings) if ratings else 0
   

 

    def __str__(self):
        return self.name

class ToyVarients(models.Model):
    price=models.PositiveIntegerField()
    
    options=(
        ('extrasmall','extrasmall'),
        ('small','small'),
        ('medium','medium'),
        ('large','large'),
        ('extralarge','extralarge')
        
       
    )

    size=models.CharField(max_length=200,choices=options,default="small")
    
    toy=models.ForeignKey(Toys,on_delete=models.CASCADE)
    @property
    def offerstoy(self):
        current_date=date.today()
        qs=self.offerstoy_set.all()
        qs=qs.filter(due_date__gte=current_date)
        return qs

    def __str__(self):
        return self.toy.name


class Offerstoy(models.Model):
    toyvarient=models.ForeignKey(ToyVarients,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    start_date=models.DateTimeField()
    due_date=models.DateTimeField()


class Cartstoy(models.Model):
    toyvarient=models.ForeignKey(ToyVarients,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    date=models.DateTimeField(auto_now_add=True)

    


class Orderstoy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    toyvarient=models.ForeignKey(ToyVarients,on_delete=models.CASCADE)
    options=(
      
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatced","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    orderd_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateField(null=True)
    address=models.CharField(max_length=200)

from django.core.validators import MinValueValidator,MaxValueValidator

class Reviewstoy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    toy=models.ForeignKey(Toys,null=True,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=300)




class Dress(models.Model):
    name=models.CharField(max_length=200)


    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    options=(
       ('boy','boy'),
       ('girl','girl'),
       ('infant','infant')
       
    )
    mode=models.CharField(max_length=200,choices=options,default="boy")

    image=models.ImageField(upload_to="images")
    @property
    def varients(self):
       
        qs=self.dressvarients_set.all()
        
        return qs
    @property
    def reviews(self):
        qs=self.reviewsdress_set.all()
        return qs
    @property
    def avg_rating(self):
        ratings=self.reviewsdress_set.all().values_list("rating",flat=True)
        return sum(ratings)/len(ratings) if ratings else 0
   

 

    def __str__(self):
        return self.name

class DressVarients(models.Model):
    price=models.PositiveIntegerField()
    
    options=(
        ('extrasmall','extrasmall'),
        ('small','small'),
      ('medium','medium'),
        ('large','large'),
        ('extralarge','extralarge')
        
       
    )

    size=models.CharField(max_length=200,choices=options,default="small")
    
    dress=models.ForeignKey(Dress,on_delete=models.CASCADE)
    @property
    def offersdress(self):
        current_date=date.today()
        qs=self.offersdress_set.all()
        qs=qs.filter(due_date__gte=current_date)
        return qs

    def __str__(self):
        return self.dress.name


class Offersdress(models.Model):
    dressvarient=models.ForeignKey(DressVarients,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    start_date=models.DateTimeField()
    due_date=models.DateTimeField()


class Cartsdress(models.Model):
    dressvarient=models.ForeignKey(DressVarients,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    date=models.DateTimeField(auto_now_add=True)

    


class Ordersdress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dressvarient=models.ForeignKey(DressVarients,on_delete=models.CASCADE)
    options=(
      
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatced","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    orderd_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateField(null=True)
    address=models.CharField(max_length=200)

from django.core.validators import MinValueValidator,MaxValueValidator

class Reviewsdress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dress=models.ForeignKey(Dress,null=True,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=300)



class Stationary(models.Model):
    name=models.CharField(max_length=200)


    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    options=(
        ('powder','powder'),
        ('kajol','kajol'),
        ('shamboo','shamboo'),
        ('bottle','bottle'),
        ('brush','brush'),
        ('pambers','pambers'),
        ('wipes','wipes'),
        ('bag','bag'),
        ('baby-bed','baby-bed')
       
    )
    mode=models.CharField(max_length=200,choices=options,default="powder")

    image=models.ImageField(upload_to="images")
    @property
    def varients(self):
       
        qs=self.stationaryvarients_set.all()
        
        return qs
    @property
    def reviews(self):
        qs=self.reviewsstationary_set.all()
        return qs
    @property
    def avg_rating(self):
        ratings=self.reviewsstationary_set.all().values_list("rating",flat=True)
        return sum(ratings)/len(ratings) if ratings else 0
   

 

    def __str__(self):
        return self.name

class StationaryVarients(models.Model):
    price=models.PositiveIntegerField()
    
    options=(
        ('extrasmall','extrasmall'),
        ('small','small'),
        ('medium','medium'),
        ('large','large'),
        ('extralarge','extralarge')
        
       
    )

    size=models.CharField(max_length=200,choices=options,default="small")
    
    stationary=models.ForeignKey(Stationary,on_delete=models.CASCADE)
    @property
    def offersstationary(self):
        current_date=date.today()
        qs=self.offersstationary_set.all()
        qs=qs.filter(due_date__gte=current_date)
        return qs

    def __str__(self):
        return self.stationary.name


class Offersstationary(models.Model):
    stationaryvarient=models.ForeignKey(StationaryVarients,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    start_date=models.DateTimeField()
    due_date=models.DateTimeField()


class Cartsstationary(models.Model):
    stationaryvarient=models.ForeignKey(StationaryVarients,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    date=models.DateTimeField(auto_now_add=True)

    


class Ordersstationary(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stationaryvarient=models.ForeignKey(StationaryVarients,on_delete=models.CASCADE)
    options=(
      
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatced","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    orderd_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateField(null=True)
    address=models.CharField(max_length=200)

from django.core.validators import MinValueValidator,MaxValueValidator

class Reviewsstationary(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stationary=models.ForeignKey(Stationary,null=True,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=300)





    


    






