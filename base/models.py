from django.db import models

from django.db import models


class ToDo(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']
    
    def __str__(self):
        return self.name

# Create your models here.

