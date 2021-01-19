from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=False, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='undefined')
    likes = models.ManyToManyField(User, related_name='blog_post')
    ingredients = models.ManyToManyField(Ingredient, related_name='blog_post')

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.title + ' | ' + str(self.author) + " cat: " + self.category

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
        # return reverse('home')

