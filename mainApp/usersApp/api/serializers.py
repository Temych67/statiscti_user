from rest_framework import serializers

from usersApp.models import User

class UserSerializer(serializers.ModelSerializer):

	id = serializers.SerializerMethodField('get_email_from_user')
	
	class Meta:
		model = User
		fields = ['id', 'first_name', 'last_name', 'email','gender','ip_address']

	def get_email_from_user(self, user):
		id = user.id
		return id
