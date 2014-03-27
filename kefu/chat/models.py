from django.db import models
from django.contrib.auth.models import User 


# Create your models here.



class Contact(models.Model):
	client_id=models.IntegerField(unique=True)
	client_name=models.CharField(max_length=50)
	content=models.TextField(null=True,blank=True,default='hello!')
	contact_time=models.DateTimeField()
	#user=models.ManyToManyField(user)
	def __unicode__(self):
		return self.client_name
'''
class Contact2(models.Model):
	client_id = models.IntegerField(unique=True)
	client_name=models.CharField(max_length=50)
	contact_time=models.DateTimeField()
	content=models.TextField(null=True,blank=True,default='hello!')
'''
class chat_user(models.Model):
	user=models.ForeignKey(User,null=True)
	user_status=models.CharField(max_length=5,null=True, blank=True)
	def __unicode__(self):
		return '%s' % self.user

