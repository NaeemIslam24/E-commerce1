from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.


class Customer(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)


class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField()
    product_image = models.ImageField(null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

# if u dont upload a image, then u dont hava to face error this code help u
    @property
    def imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ''
        return url


class Order(models.Model):

    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_Item_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

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


class OrderItem(models.Model):

    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


# to find total price

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):

    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    zip_code = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
