"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
#import django.contrib.auth.views
from django.contrib.auth import views
from django.contrib import admin


from myblog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name="dg_logout", kwargs={'next_page': '/'}),

    # url(r'^register/$', RegisterFormView.as_view(), name='register'),
    # url(r'^login/$', LoginFormView.as_view(), name='login'),
    # url(r'^$', LogoutView.as_view(), name='logout'),
    url(r'^$', post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)$', post_detail, name='post_detail' ),
    url(r'^post/new/$', post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),
    url(r'^drafts/$', post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', post_remove, name='post_remove' ),


]
