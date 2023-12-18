from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class customuser(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/products')
    availability = models.CharField(max_length=100)
    
    
    
    def __str__(self):
        return self.product_name
    
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/products')
    
    
    def __str__(self):
        return f"Image for {self.product.product_name}"




        
        
    
    

class Category(models.Model):
    category =models.ForeignKey(Product,on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='products/image1')
    image2 = models.ImageField(upload_to='products/image2')
    image3 = models.ImageField(upload_to='products/image3')
    
    def __str__(self):
        return self.category_name
    
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
   
 
    phone_number = PhoneNumberField()
    message = models.CharField(max_length=200)
    
    
    
    def __str__(self):
        return self.first_name
    
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
    
    
    
    
    





    
    
    
    
    
    

    




    
    





    
    
    
    
