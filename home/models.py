from django.db import models



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