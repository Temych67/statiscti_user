from django.db import models
from usersApp.models import User
from django.urls import reverse


class Statics(models.Model):
	date 					= models.DateField()
	page_views 				= models.IntegerField(null=True)
	clicks 					= models.IntegerField(null=True)
	user_id					= models.ForeignKey(User, on_delete=models.CASCADE)
	
	def get_absolute_url(self):
		return reverse("statistic:user_static", kwargs={"id": self.user_id})

	def __int__(self):
		return self.date