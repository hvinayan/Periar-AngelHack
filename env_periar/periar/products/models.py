from django.contrib.auth.models import Permission, User
from django.db import models

class Category(models.Model):
    cname = models.CharField(max_length=100)
    cdisc = models.CharField(max_length=300)

    def __str__(self):
        return self.cname + ' - ' + self.cdisc

class Product(models.Model):
    seller = models.ForeignKey(User, default=1)
    category = models.ForeignKey(Category, default=1)
    pname = models.CharField(max_length=100)
    prating = models.IntegerField(default=0)
    nrating = models.IntegerField(default=0)
    pdisc = models.CharField(max_length=300)
    image = models.CharField(max_length=500)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.pname + ' : ' + self.pdisc

class Cart(models.Model):
    uid = models.ForeignKey(User, default=1)
    pid = models.ForeignKey(Product)
    qty = models.IntegerField(default=1)

    #def __str__(self):
     #   return +  str(self.qty)

class Comment(models.Model):
    uid = models.ForeignKey(User, default=1)
    pid = models.ForeignKey(Product)
    comment = models.CharField(max_length=500)


class Feedback(models.Model):
    uid = models.ForeignKey(User, default=1)
    feedback = models.CharField(max_length=500)
