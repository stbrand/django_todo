from django.conf.urls import url

from . import views
#from .views import (TodoItemCreateView,TodoItemDeleteView,TodoItemDetailView,
#TodoItemListView,TodoItemUpdateView)


urlpatterns = [

    url(r'^$', views.item_list, name='item_list'),
    url(r'^add/$', views.add, name='add'),
    url(r'^imp$', views.imp, name='imp'),
    url(r'^edit/(?P<pk>\d+)$', views.edit, name='edit'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'),
    url(r'^details/(?P<pk>\d+)$', views.details, name='details'),

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
