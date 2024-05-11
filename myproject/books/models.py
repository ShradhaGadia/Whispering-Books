# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    c = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(Books, models.DO_NOTHING, blank=True, null=True)
    quantity_ordered = models.IntegerField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Sales(models.Model):
    sale_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Books, models.DO_NOTHING, blank=True, null=True)
    quantity_sold = models.IntegerField(blank=True, null=True)
    sold = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'

