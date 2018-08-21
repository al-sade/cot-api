from django.db import models


class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    properties = models.ManyToManyField('Property', blank=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    TYPE = [('JSON', 'Json'), ('PLAINTEXT', 'Plaintext'), ('BINARY', 'Binary')]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(choices=TYPE, max_length=15)

    def __str__(self):
        return self.name

