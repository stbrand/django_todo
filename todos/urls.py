from django.conf.urls import url

from . import views
#from .views import (TodoItemCreateView,TodoItemDeleteView,TodoItemDetailView,
#TodoItemListView,TodoItemUpdateView)


urlpatterns = [

    url(r'^$', views.item_list, name='item_list'),
    url(r'^add/$', views.add, name='add'),
    url(r'^imp$', views.imp, name='imp'),
    #url(r'^edit/{?P<id>\w{0,50}}$', views.add, name='add'),

    #url(r'^$', views.item_list, name='item_list'),
    #url(r'^$', views.item_list, name='item_list'),
    #url(r'^$', views.item_list, name='item_list'),
    #url(r'^$', views.item_list, name='item_list'),

    #url(r'^$', TodoItemListView.as_view(), name='list'),
    #url(r'^add/$', TodoItemCreateView.as_view(),name='create'),
	#url(r'^(?P<pk>\d+)/$', TodoItemDetailView.as_view(),name='detail'),
	#url(r'^(?P<pk>\d+)/update/$',TodoItemUpdateView.as_view(), name='update'),
	#url(r'^(?P<pk>\d+)/delete/$',TodoItemDeleteView.as_view(), name='delete'),

]
