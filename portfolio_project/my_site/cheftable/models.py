from unicodedata import name
from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    menu_category_name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.menu_category_name
    
class Menus(models.Model):
    menu_item=models.CharField(max_length=200)
    price=models.IntegerField(null=False)
    category_id=models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")
    
    def __str(self):
        return self.menu_item
    
class Customer(models.Model):
    name=models.CharField(max_length=100)
    reservation_day=models.CharField(max_length=50)
    seats=models.IntegerField()
    
    def __str__(self):
        return self.name
    
# modelform

class Logger(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    time_log=models.TimeField(help_text='Enter the exact time')
    
    
    def __str__(self):
        return self.first_name
    

    
    
    
