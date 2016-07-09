from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX =re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]*$')
NAME = re.compile(r'[0,1,2,3,4,5,6,7,8,9]')

class UserManager(models.Manager):
	def login(self, email, password):
		activeU = self.filter(email__iexact = email)
		#  gets return a list
		if activeU and bcrypt.hashpw(password.encode("utf-8") , activeU[0].password.encode("utf-8")) == activeU[0].password:
		#should be classified as a succesful login
			return (True, activeU[0])
		else:
			return(False, {"login" : "login failed, please try again"})

	def register(self, name, alias, email, password, confirm_password, dob):
		errors = {}
		if len(name) <1:
			errors['name'] = "Name cannot be left blank"
		elif NAME.match(name):
			errors['name1'] = "Name cannot contain number(s)"
		elif len(alias) <1:
			errors['alias'] = "Alias Name cannot be left blank"
		elif len(email) < 1:
			errors['email'] = "Email cannot be left blank"
		elif len(password) < 1:
			errors['password'] = "Password cannot be left blank"
		elif len(dob) < 1:
			errors['password'] = "Date of Birth cannot be left blank"
		elif len(password) < 8:
			errors['password'] = "Password is too short"
		elif password != confirm_password:
			errors['confirm_password'] = "Passwords must match"
		elif not EMAIL_REGEX.match(email):
			errors['email'] = "Please enter a valid email"
		elif self.filter(email__iexact = email):
			errors['invalid'] = "Invalid registration"	

		if errors:
			return (False, errors)
		else:
		#register this person!
			hash_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
			self.create(name = name, alias = alias, email = email, password = hash_password, date_of_birth=dob)
			return (True, self.filter(email = email)[0])


	def add(self, user1_id, user2_id):
		user1 = User.objects.filter(id=user1_id)
		user2 = User.objects.filter(id=user2_id)
		Friend.objects.create(user1=user1[0], user2=user2[0])
		Friend.objects.create(user1=user2[0], user2=user1[0])
		return(True)


class User(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
    objects = models.Manager()


class Friend(models.Model):
    user1 = models.ForeignKey(User, related_name="f1")
    user2 = models.ForeignKey(User, related_name="f2")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    userManager = UserManager()
    objects = models.Manager()

