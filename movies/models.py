from django.db import models
from uuid import uuid4

# Create your models here.
class Movies(models.Model):
    id_movies = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    director  = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    release_year = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)