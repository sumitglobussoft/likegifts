"""
Definition of urls for Like_gifts.
"""

from datetime import datetime
from django.conf.urls import patterns, include, url
from app.forms import BootstrapAuthenticationForm

from app.views import *
from app.package1.HomeController import *
from app.package1.ProductController import *
from app.package1.importer import *
from app.package1.Admin import *

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', contact, name='contact'),
    url(r'^aboutus$', aboutus, name='aboutus'),
    url(r'^blog$', blog, name='blog'),
    url(r'^faq$', faq, name='faq'),
    url(r'^privacy$', privacy, name='privacy'),
    url(r'^terms$', terms, name='terms'),



    url(r'^sendgift', sendgift, name='sendgift'),
    url(r'^userlogin', userlogin, name='userlogin'),
    url(r'^userlogout', userlogout, name='userlogout'),
    url(r'^usersignup', usersignup, name='usersignup'),
    url(r'^howitworks', howitworks, name='howitworks'),
    url(r'^gifts', gifts, name='gifts'),
    url(r'^filter', filter, name='filter'),
    url(r'^catgift/(?P<cat>\w{0,2})/$', catgift, name='catgift'),
    url(r'^bestfor/(?P<cat>\w{0,5})/$', bestfor, name='bestfor'),
    url(r'^ordergift/(?P<id>\w{0,2})/$', ordergift, name='ordergift'),
    url(r'^selgift/(?P<id>\w{0,2})/$', selgift, name='selgift'),
    url(r'^saveorderdetails', saveorderdetails, name='saveorderdetails'),
    url(r'^search/(?P<keyword>[\w|\W]+)/$', search, name='search'),
    url(r'^sendmail', sendmail, name='sendmail'),
    url(r'^setsession', setsession, name='setsession'),
    url(r'^sendsms', sendsms, name='sendsms'),
    url(r'^sendsms', sendsms, name='sendsms'),
    url(r'^testchk', testchk, name='testchk'),
    url(r'^receivegift', receivegift, name='receivegift'),
    url(r'^getcategories', getcategories, name='getcategories'),


     # Admin Controllers

    url(r'^admin', admin, name='admin'),
    url(r'^loginadmin', loginadmin, name='loginadmin'),
    url(r'^logoutadmin', logoutadmin, name='logoutadmin'),
    url(r'^myusers', myusers, name='myusers'),
    url(r'^oneuser', oneuser, name='oneuser'),#/(?P<userid>\w{0,2})$
    url(r'^updateuser', updateuser, name='updateuser'),
    url(r'^deleteuser/(?P<uid>\w{0,2})$', deleteuser, name='deleteuser'),
    url(r'^uploadimage', uploadimage, name='uploadimage'),
    url(r'^saveproductimage', saveproductimage, name='saveproductimage'),
    #url(r'^myproducts/(?P<cat>\w{0,2})/$', myproducts, name='myproducts'),
    url(r'^allproducts', allproducts, name='allproducts'),
    url(r'^uploadproducts', uploadproducts, name='uploadproducts'),
    url(r'^uploadproductsfile', uploadproductsfile, name='uploadproductsfile'),
    url(r'^oneproduct', oneproduct, name='oneproduct'),
    url(r'^updateproduct', updateproduct, name='updateproduct'),
    url(r'^delproduct/(?P<pid>\w{0,2})$', delproduct, name='delproduct'),
    url(r'^allorders', allorders, name='allorders'),
    url(r'^oneorder', oneorder, name='oneorder'),
    url(r'^updateorder', updateorder, name='updateorder'),
    url(r'^delorder/(?P<oid>\w{0,2})$', delorder, name='delorder'),



    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
