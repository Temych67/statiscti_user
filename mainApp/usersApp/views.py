from django.shortcuts import render
from usersApp.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from datetime import datetime
from statistic.models import Statics

BLOG_POSTS_PER_PAGE = 50

def users_page_view(request):
	users_list = User.objects.all()

	# Pagination
	page = request.GET.get('page', 1)
	paginator = Paginator(users_list, BLOG_POSTS_PER_PAGE)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		users = paginator.page(user_paginator.num_pages)
	statistic_user={"object":users}
	return render(request, 'users_page/first.html', statistic_user)

def is_valid_queryparam(param):
	return param != '' and param is not None

def user_detail_view(request, id):
	qs_count = Statics.objects.filter(user_id=id)
	default_date = []
	clicks = []
	page_views = []
	total_page_views= 0
	total_clicks = 0



	if request.GET:
		# Sorting by for(date_min) to(date_max)
		date_min = request.GET.get('date_min')
		if is_valid_queryparam(date_min):
			qs_count = qs_count.filter(date__gte=date_min)

		date_max = request.GET.get('date_max')
		if is_valid_queryparam(date_max):
			qs_count = qs_count.filter(date__lt=date_max)
		
		if  date_min == '' and date_max == '':
			qs_count = qs_count.filter(date__gte=datetime(2019,10,24))
			
		default_date		= qs_count.values_list('date', flat=True)
		clicks 				= qs_count.values_list('clicks', flat=True)
		page_views 			= qs_count.values_list('page_views', flat=True)
		
		for temp in clicks:
			total_clicks += temp
		for temp in page_views:
			total_page_views += temp
	
	 #Defualt date 
	else:
		default_date 	= qs_count.values_list('date',flat=True).filter(date__gte=datetime(2019,10,24))
		clicks 			= qs_count.values_list('clicks',flat=True).filter(date__gte=datetime(2019,10,24))
		page_views 		= qs_count.values_list('page_views',flat=True).filter(date__gte=datetime(2019,10,24))
		
		for temp in clicks:
			total_clicks += temp
		for temp in page_views:
			total_page_views += temp

	context = {
		"total_page_views":total_page_views,
		"total_clicks":total_clicks,
		"default_date":default_date,
		"clicks":clicks,
		"page_views":page_views,
	}
	return render(request, "users_page/user_detail.html", context)
