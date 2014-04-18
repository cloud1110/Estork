# -*- coding: utf-8 -*-
from django.db import models

class Product (models.Model):
	productID = models.CharField(,max_length = 200)
	en_name = models.CharField(max_length = 800)
	ch_name = models.CharField(max_length = 800)
	comment = models.CharField(max_length = 500)
	ori_price = models.DecimalField(max_digits = 7, decimal_places = 2)
	retail_price = models.DecimalField(max_digits = 7, decimal_places = 2)
	category = models.CharField(max_length = 200)
	attribute = models.CharField(max_length = 500)
	#TODO: use PIL
	image = models.ImageField()

class Event (models.Model):
	#FIXME: dim event type
	event_type = models.IntegerField()
	create_date = models.DateTimeField(auto_now_add = True)
	update_date = models.DateTimeField(auto_now = True)
	product = models.ForeignKey(Product)
	number = models.IntegerField()

	comment = models.CharField(max_length = 500)

class Procure (models.Model):
	#TODO: models.ForeignKey(Supplier)
	supplier = models.CharField(max_length = 200)
	#TODO: models.ForeignKey(Staff)
	staff = models.CharField(max_length = 200)
	create_date = models.DateTimeField(auto_now_add = True)
	update_date = models.DateTimeField(auto_now = True)
	#FIXME: dim Procure type
	procure_type = models.IntegerField()
	anticipate_date = models.DateTimeField()

class Order (models.Model):
