from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'catagories'
    
class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=25)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    caragory = models.ForeignKey(Category , on_delete=models.CASCADE , default=1)
    description = models.CharField(max_length=250, default='', blank= True, null= True)
    image = models.ImageField(upload_to= "uploads/product/")
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2 , default=0)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    quantity = models.IntegerField(default= 1)
    address = models.CharField(max_length= 100 , default= '' , blank= True)
    phone = models.CharField(max_length=20, default='', blank= True)
    data = models.DateField(default= datetime.datetime.today)
    status = models.BooleanField(default= False)
    
    def __str__(self):
        return self.product