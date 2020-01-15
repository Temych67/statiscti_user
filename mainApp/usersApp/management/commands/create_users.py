from usersApp.models import User
from statistic.models import Statics
from django.core.management.base import BaseCommand
import json
import os


class Command(BaseCommand):
	help = u'Создание случайного пользователя'

	def add_arguments(self, parser):
		parser.add_argument('total', type=int, help=u'Количество создаваемых пользователей')

	def handle(self, *args, **kwargs):
		total = kwargs['total']

		module_dir = os.path.dirname(__file__)  # get current directory
		file_path = os.path.join(module_dir, 'users_statistic.json')
		
		with open(file_path) as f:
			templates = json.load(f)   
		
		for temp in range(len(templates)):
			statictics = Statics(None,templates[temp]['date'],templates[temp]['page_views'],templates[temp]['clicks'],templates[temp]['user_id'])
			statictics.save()
		    # user =User(id=1, first_name='Christie', last_name='Gann',email='cgann0@hostgator.com', gender='m',ip_address='57.14.195.231')