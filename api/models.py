from django.db import models
from django.utils.text import slugify
import os


class Origin(models.Model):
    """This class represents the origin model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    """This class represents the character model."""

    def upload_to(self, filename):
        filename, file_extension = os.path.splitext(filename)
        return'characters/%s%s' % (slugify(self.name), file_extension)

    name = models.CharField(max_length=255, blank=False, unique=True)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    image = models.ImageField(editable=True, upload_to=upload_to)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
