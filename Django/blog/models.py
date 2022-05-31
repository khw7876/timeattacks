from unicodedata import category
from django.db import models


# Create your models here.




class Category(models.Model):
    class Meta:
        db_table = "Category"

    title = models.CharField(max_length=256)
    content =  models.CharField(max_length=256)

class Article(models.Model):
    class Meta:
        db_table = "Article"

    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content =  models.CharField(max_length=256)