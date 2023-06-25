from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=250)
    likes = models.ManyToManyField(
        User, related_name='like', default=None, blank=True)

    def get_absolute_url(self):
        return reverse('app1:post_single', args=[self.slug])

    def __str__(self):
        return self.title


class MyModel(models.Model):
    MY_CHOICES = (
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    )

    my_field = models.CharField(
        max_length=20,
        choices=MY_CHOICES,
        default='option1'
    )
