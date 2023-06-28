from django.contrib import admin
from . import models

admin.site.register(models.Post)
admin.site.register(models.ModelwithTupleTuple)
admin.site.register(models.ModelTestRandomField)

