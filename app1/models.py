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


class ModelwithTupleTuple(models.Model):
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


class ModelTestRandomField(models.Model):
    name = models.CharField(max_length=100,null= True)
    age = models.IntegerField()
    email = models.EmailField()

class MyCustomField(models.CharField):
    def from_db_value(self, value, expression, connection):
        print("from_db_value",value)
        if value is None:
            return value
        return value.upper()  # Convert the value to uppercase during deserialization

    def get_prep_value(self, value):
        print("get_prep_value", value)
        if value is None:
            return value
        return value.capitalize()  # Capitalize the value for database storage

class MyModel(models.Model):
   my_field = MyCustomField(max_length=100, null=True)

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    major = models.ForeignKey('Subject', on_delete=models.CASCADE)
    minor = models.ForeignKey('Subject', related_name='minor_students', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name