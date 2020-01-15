from django.urls import path

from usersApp.views import(

user_detail_view,

)
app_name = 'usersApp'

urlpatterns = [

	path('<int:id>/',user_detail_view, name='user_info'),
]