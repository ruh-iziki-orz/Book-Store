from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models.deletion import CASCADE
STATE_CHOICES=(
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Haryana','Haryana'),
    ('Gujrat','Gujrat'),
    ('Bihar','Bihar'),
    ('Assam','Assam'),
    ('Jharkhand','Jharkhand'),
    ('New Delhi','New Delhi'),
)

class Customer (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    locality = models.CharField(max_length = 200)
    city = models.CharField(max_length = 50)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES,max_length = 50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
    ('MO','Motivational'),
    ('RL','Light Romantic'),
    ('RD','Dark Romantic'),
    ('H','Pure Horror'),
    ('HC','Horror+Comedy'),
    ('N','Manga'),
)

class Product(models.Model):
    title = models.CharField(max_length = 200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length = 200)
    category = models.CharField(choices = CATEGORY_CHOICES,max_length = 2)
    product_image = models.ImageField(upload_to ='productimg')

    def __str__(self):
        return str(self.id)






   




class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price



STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    ordered_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 50,choices = STATUS_CHOICES,default = 'Pending')


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.title, self.name)