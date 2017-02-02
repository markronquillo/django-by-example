from django.conf.urls import url
from django.contrib.auth import views as authviews

from . import views


urlpatterns = [
	# url(r'^login/$', views.user_login, name='login'),

	url(r'^register/$', views.register, name='register'),

	url(r'^login/$', authviews.login, name='login'),
	url(r'^logout/$', authviews.logout, name='logout'),
	url(r'^logout-then-login/$', authviews.logout_then_login, name='logout_then_login'),
	url(r'^$', views.dashboard, name="dashboard"),

	url(r'^password-change/$', authviews.password_change,
		name='password_change'),
	url(r'^password-change/done/$', authviews.password_change_done,
		name="password_change_done"),

	url(r'^password-reset/$', 
		authviews.password_reset, name='password_reset'),
	url(r'^password-reset/done/$', 
		authviews.password_reset_done, name='password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 
		authviews.password_reset_confirm, name='password_reset_confirm'),
	url(r'^password-reset/complete/$', 
		authviews.password_reset_complete, name='password_reset_complete'),

	url(r'^edit/$', views.edit, name='edit')
]


