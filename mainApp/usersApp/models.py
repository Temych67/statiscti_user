from django.db import models
from django.urls import reverse

class User(models.Model):
	
	SEX_CHOICES = (
		('Male',u"Male"),
		('Female',u"Female"),
	)

	id 						= models.IntegerField(primary_key=True)
	first_name				= models.CharField(max_length=20)
	last_name				= models.CharField(max_length=30)
	email					= models.EmailField(max_length=70, unique=True)
	gender					= models.CharField(max_length=6,verbose_name=u"Gender",choices=SEX_CHOICES)
	ip_address				= models.GenericIPAddressField()
	total_clicks			= models.IntegerField(null=True)
	total_page_views		= models.IntegerField(null=True)
	
	
	def get_absolute_url(self):
		return reverse("usersApp:user_info", kwargs={"id": self.id})

	def __int__(self):
		return self.id




