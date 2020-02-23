from django.db import models

class Search(models.Model):
    description = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.description

class Result(models.Model):
    title = models.TextField()
    summary = models.TextField()
    location = models.TextField()
    company = models.TextField()
    url = models.URLField()
    listing_id = models.TextField()

    def __str__(self):
        return self.title
