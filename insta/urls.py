from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url(r'^$',views.home,name='home'),
  url(r'^accounts/',include('registration.backends.simple.urls')),
  url(r'^user/',views.user_profile,name='userProfile'),
  url(r'^new/post$',views.new_post,name='newPost'),
  url(r'^profile/',views.profile,name='profile'),
  url(r'^feed/',views.feeds,name='feed'),
  url(r'^comment/',views.comments,name='comment'),
  url(r'^search/',views.search,name='search')
]
if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)