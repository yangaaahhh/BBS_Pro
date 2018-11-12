from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'bbs'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<bbs_id>[0-9]+)/$', views.bbs_detail, name='bbs_detail'),
    url(r'^sub_comment/$', views.sub_comment, name='sub_comment'),
    url(r'^bbs_pub/$', views.bbs_pub, name='bbs_pub'),
    url(r'^bbs_sub/$', views.bbs_sub, name='bbs_sub'),
    url(r'^account/login/$', login, {'template_name': 'login.html'}),
    url(r'^login/$', views.bbs_login, name='bbs_login'),
    url(r'^acc_login/$', views.acc_login, name='acc_login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.bbs_category, name='bbs_category'),
]
