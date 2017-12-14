from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout  # 利用內建的view funciton

#from django.conf import settings
urlpatterns = [
    url(r'^accounts/login/$', views.user_login, name='login'),
    url(r'^index/', views.index, name="index"),
    url(r'^accounts/logout/$', views.logout, name="logout"),
    url(r'^addschoolclass/$', views.addschoolclass, name="addschoolclass"),
    url(r'^deleteschoolclass/(?P<id>\d+)/$',
        views.deleteschoolclass, name="deleteschoolclass"),
    url(r'^classparent/(?P<id>\d+)/',
        views.classparent, name="classparent"),
    url(r'^addclassparent/$', views.addclassparent, name="addclassparent"),
    url(r'deleteclasstu/(?P<id>\d+)/(?P<vpk>\d+)/$',
        views.deleteclasstu, name="deleteclasstu"),
    url(r'^ebook/', views.ebook, name='ebook'),
    url(r'^addebook/$', views.addebook, name="addebook"),
    url(r'^deletebook/(?P<id>\d+)/$',
        views.deletebook, name="deletebook"),
    url(r'^addebookdetail/(?P<id>\d+)/$',
        views.addebookimage, name="addebookdetail"),
    url(r'^contactindex/', views.contactindex, name="contactindex"),
    url(r'^addcontact/(?P<id>\d+)/$', views.addcontact, name="contactindex"),
    url(r'deletecontact/(?P<id>\d+)/(?P<vpk>\d+)/$',
        views.deletecontact, name="deletecontact"),
    url(r'^adddailyrecord/$', views.adddailyrecord, name="adddailyrecord"),
    url(r'^deletedailyrecord/(?P<id>\d+)/$', views.deletedailyrecord, name="deletedailyrecord"),
    url(r'^addannounce/', views.addannounce, name="addannounce"),
    url(r'^deleteannounce/(?P<id>\d+)/$', views.deleteannounce, name="deleteannounce"),


    
    
]
