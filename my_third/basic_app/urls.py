from django.urls import path, re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    re_path(r'^relative/$',views.relative_url, name='relative'),
    re_path(r'^other/$', views.other, name='other'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.user_login, name='user_login')
]
