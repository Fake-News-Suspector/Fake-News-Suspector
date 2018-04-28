from django.conf.urls import url,include
from django.contrib.auth  import views as auth_views
from . import views
urlpatterns=[
	url(r'^login/$',auth_views.login,{'template_name':'accounts/login_user.html'}),
    url(r'^logout/$',auth_views.logout,{'next_page':'/'}),
    url(r'^register/$',views.register,name='register'),
]