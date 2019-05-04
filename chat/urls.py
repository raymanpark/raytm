from django.urls import path, re_path
from .views import index, about, gmlogin, createchat, joinchat, events, todo, add, details, mydetails, getgroupname, joinsubchat, deleteconfirmation, destroy

urlpatterns = [
    path('', gmlogin, name='gmlogin'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    re_path(r'^join/(?P<group_name>[^/]+)', joinchat, name='joinchat'),
    re_path(r'^subjoin/(?P<id>[^/]+)/(?P<group_name>\w{0,50})/', joinsubchat, name='joinchat'),
    re_path(r'^category/(?P<group_name>[^/]+)', events, name='events'),
    # This is the url re for making any chat
    re_path(r'^makechat/(?P<group_name>[^/]+)', createchat, name='createchat'),

    path('todo/', todo, name='todo'),
    re_path(r'^add/(?P<group_name>[^/]+)', add, name='add'),
    re_path(r'^details/(?P<group_name>[^/]+)/(?P<id>\w{0,50})/$', details, name='details'),
    re_path(r'^getgroupname/$', getgroupname, name='getgroupname'),
    re_path(r'^deleteconfirmation/(?P<id>[^/]+)/(?P<group_name>\w{0,50})/', deleteconfirmation, name='deleteconfirmation'),
    re_path(r'^destroy/(?P<id>[^/]+)/(?P<group_name>\w{0,50})/', destroy, name='destroy'),
]
