from django.db import models

# Models to create tables: Products and User

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)


# We don't put any property because by default the table will create an "id" property.
class User(models.Model):
    pass