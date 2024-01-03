from django.db import models
from users.models import CustomUser


class Food(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    discounted_price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.FileField(upload_to="food_images", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Proteins(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    discounted_price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.FileField(upload_to="proteins_images", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Pastries(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price= models.CharField(max_length=225, null=True, blank=True)
    discounted_price= models.CharField(max_length=225, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.FileField(upload_to="pastries_images", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Drinks(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.CharField(max_length=225, null=True, blank=True)
    discounted_price = models.CharField(max_length=225, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.FileField(upload_to="drinks_images", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Morsels(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    discounted_price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.FileField(upload_to="morsels_images", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Cart(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    no_of_orders = models.IntegerField(default=1, null=True, blank=True)
    total_amount = models.CharField(max_length=225, null=True, blank=True)
    category = models.CharField(max_length=225, null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SoldFoodItems(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    no_of_orders = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=225, null=True, blank=True)
    total_amount = models.CharField(max_length=225, null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class CustomerReceipts(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    receipt = models.FileField(upload_to="customers_receipts", blank=True, null=True)
    invoice_number = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

