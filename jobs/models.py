from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    body = models.TextField(max_length=255)



