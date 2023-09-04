from django.db import models

class Address(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField(max_length=50)

    def __str__(self):
        return self.name