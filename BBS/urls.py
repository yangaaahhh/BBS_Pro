from django.conf.urls import url
from . import views

app_name = 'bbs'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<bbs_id>[0-9]+)/$', views.bbs_detail, name='bbs_detail'),
    url(r'^sub_comment/$', views.bbs_detail, name='bbs_detail')
]
