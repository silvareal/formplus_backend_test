from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=50)
    created = models.DateTimeField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

