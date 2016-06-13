from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s, %s" %(self.last_name, self.first_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    description = models.TextField()
    publiched_date = models.DateField(default= timezone.now())
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField(default=0)
    cover_image = models.ImageField(upload_to='books/', default='books/slider3')


class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    publshed_date = models.DateField(default=timezone.now())
    text = models.TextField()
