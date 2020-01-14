from django import forms
from usersApp.models import User

class CreateUses(forms.ModelForm):
	class Meta:	
		model = User
		fields = '__all__'