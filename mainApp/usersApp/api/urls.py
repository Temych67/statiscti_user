from django.urls import path

from usersApp.api.views import(
	api_detail_user_view,
)

app_name = 'usersApp'

urlpatterns = [
	path('<int:id>/', api_detail_user_view, name="detail"),
	]