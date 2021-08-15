from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.


class Customer1(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Product1(models.Model):

    name = models.CharField(max_length=200)
    price = models.FloatField()
    added_date = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField()
    digital = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):

        try:
            url = self.product_image.url
        except:
            url = ''

        return url


class Order1(models.Model):

    customer = models.ForeignKey(
        Customer1,  on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=30,  null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    # this is to generate transaction id with random module
    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []
        for i in range(10):
            num = random.choice(number_list)
            code_items.append(num)
        code_string = "".join(str(item) for item in code_items)
        self.transaction_id = code_string
        super().save(*args, **kwargs)


class OrderItem1(models.Model):

    product = models.ForeignKey(
        Product1,  on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order1,  on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)

    @property
    def get_total(self):

        all = self.quantity * self.product.price

        return all
