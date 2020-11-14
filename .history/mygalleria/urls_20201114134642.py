
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views


urlpatterns=[
   url('^$',views.index,name = 'index'),
    url(r'^category/(\d+)',views.category,name ='category'),
    url(r'^admin/', views.admin_dashboard,name = "admin_dashboard"),
   url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_photos, name = 'pastPhotos'),
   url(r'^search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)