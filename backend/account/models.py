from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from club.models import Status

class User(AbstractUser):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255, unique=True)
	username = models.CharField(max_length=255)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', ]

	# def save(self, **kwargs):
	# 	password = make_password(self.password)
	# 	return password

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=datetime.now)
	phone = models.CharField(max_length=32)
	email = models.EmailField(max_length=128)
	full_name = models.CharField(max_length=255, blank=True, null=True)
	status = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return self.user.email