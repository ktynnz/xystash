from distutils.command.upload import upload
from tabnanny import verbose
from time import timezone
from unicodedata import category
from django.db import models
from django.urls import reverse
from django.utils import timezone

# from xyStash import xyStashStore
# from django.contrib.auth.models import User #default table django creates for users


class user(models.Model):
    db_fname = models.CharField(max_length=50)
    db_lname = models.CharField(max_length=50)
    db_email = models.CharField(max_length=100)
    db_username = models.CharField(max_length=100)
    db_password = models.CharField(max_length=100)

    def __str__(self):
        return self.db_fname + " " + self.db_lname + " - " + self.db_username

class fromContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    created = models.DateTimeField(default=timezone.now) #The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.

    class Meta: 
        verbose_name_plural = 'Contact Form'
        ordering = ('-created', )

    def __str__(self):
        return self.email


# class subscriber(models.Model):
#     sub_email = models.CharField(max_length=100)
#     created = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.sub_email


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    #appears after / in every page 
    #unique=True means in the database there should only be one slug
    slug = models.SlugField(max_length=100, unique=True)

    class Meta: 
        verbose_name_plural = 'Categories' #override Categorys (appears by default) to categories

    def get_absolute_url(self):
        return reverse('category_list', args=[self.slug])
        
    def __str__(self):
        return self.name


class Product(models.Model):
    #link to reference Category table
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='img/')
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        # verbose_name_plural = 'Products'
        ordering = ('-created', ) #-created - last item that is added to the database will be shown first (ascending order) where as created shows the items in a descending order meaning the item that was added firt will be the item that will show first

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])
    
    def __str__ (self):
        return self.title

    