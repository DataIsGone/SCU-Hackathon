from django.db import models

class Search(models.Model):
    description = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length=2)

class Result(models.Model):
    title = models.TextField()
    summary = models.TextField()
    location = models.TextField()
    company = models.TextField()
    url = models.URLField()
    listing_id = models.TextField()
