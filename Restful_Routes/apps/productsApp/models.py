from __future__ import unicode_literals
from django.db import models

class ProdManager(models.Manager):
	def create(self, name, description, price):
		errors = {}
		#validations
		if len(name)<1: 
			errors['name'] = 'Name is too short'
		elif len(description)<1: 
			errors['description'] = 'Description is too short'
		elif len(price)<1:
			errors['price'] = 'Price is too short' 

		product_exists = self.filter(name=name)
		if errors:
			return(False,errors)
		else:
			if product_exists:
				return(False,{"duplicate":"Product already exists"})
			else:
				Product.objects.create(name=name, description=description, price=price)
				return(True,{"success": "Product created"})

	def edit(self, id, name, description, price):
		errors = {}
		#validations
		if len(name)<1: 
			errors['name'] = 'Name is too short'
		elif len(description)<1: 
			errors['description'] = 'Description is too short'
		elif len(price)<1:
			errors['price'] = 'Price is too short'

		if errors:
			return(False,errors)
		else:
			Product.objects.filter(id=id).update(name=name, description=description, price=price)
			return(True,{"success", "Product updated"})


	def show(self,id):
		product = self.get(id=id)
		return(True, product)


# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=40)
	description = models.CharField(max_length=255)
	price = models.FloatField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	prodManager = ProdManager()
	objects = models.Manager()

