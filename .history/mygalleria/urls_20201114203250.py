# from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('archives/(\d{4}-\d{2}-\d{2})/', views.past_days_photos, name = 'pastPhotos'),    
    path('search/', views.search_results, name='search_results'),
    path('category/(\d+)',views.category,name ='category')
]