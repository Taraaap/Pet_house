from django.db import models
from django.contrib.auth.models import User

# makemigratins - create changes and store in a file
# migrate - apply change in database

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=13)
    message=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
    

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products')


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    size = models.CharField(max_length=10, default="M")

    def get_total(self):
        return self.product.price * self.quantity
    
    
class Order(models.Model):

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('DELIVERED', 'Delivered'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    size = models.CharField(max_length=10)
    quantity = models.IntegerField(default=1)

    fullname = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    payment_method = models.CharField(max_length=50)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.product.name}"

