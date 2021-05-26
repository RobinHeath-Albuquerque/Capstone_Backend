from django.db import models

class Market(models.Model):
    name = models.CharField(max_length=50)
    time = models.TimeField(default=None)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fName


class Grower(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fName


class Buyer(models.Model):
    objects = None
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fName
