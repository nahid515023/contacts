from django.db import models

class Contact(models.Model):
    full_name=models.CharField(max_length=80)
    relationship=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField(max_length=254)
    address=models.TextField()

    def __str__(self):
        return self.full_name
