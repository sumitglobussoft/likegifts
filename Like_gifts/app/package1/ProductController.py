# -*- coding: utf-8 -*-

"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpRequest, HttpResponse
from django.template import loader,RequestContext
from django.shortcuts import render_to_response
from datetime import datetime
from django import *
from app.forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from app.models import *
import json
from django.core import serializers
from django.core.mail import send_mail


def setsession(request):
    if request.method == 'POST':
        data=request.POST.get("data","")
        key=request.POST.get("key","")
        try:
            del request.session[key]
        except :
            x=1
        request.session[key] = data
        resp = {'success': 'success'}
        return HttpResponse(json.dumps(resp), content_type="application/json")


def gifts(request):
    products = Products.objects.raw('SELECT * FROM products')
    template=loader.get_template("app/browse.html")
    rc=RequestContext(request,{'products':products})
    return HttpResponse(template.render(rc))

def testchk(request):
    template=loader.get_template("admin/test.html")
    rc=RequestContext(request,{'products':'hii'})
    return HttpResponse(template.render(rc))

def filter(request):
    if request.method == 'POST':
        fiteroption=request.POST.get("filterdata","")
        sortdata=request.POST.get("sortdata","")
        locationdata=request.POST.get("locationdata","")
        pricedata=request.POST.get("pricedata","")

        if '(0' in fiteroption:
            fiteroption='(0,1,2,3,4,5,6,7,8,9,10,11,12)'
        else :
            x=1
        query='SELECT * FROM products WHERE ProductCategoryId in '+fiteroption
        if locationdata=='("")':
            x=2
        else :
            query = query+'and ProductLocation in '+locationdata
        #filterarray = fiteroption.split(',')
        query=query+' and ProductPrice between '+pricedata
        if sortdata=='Sort result by ...':
            x=1
        if sortdata=='Price H-L':
            query=query+' ORDER BY ProductPrice DESC'
        if sortdata=='Price L-H':
            query=query+' ORDER BY ProductPrice'
        if sortdata=='Popular':
            x=2
        if sortdata=='New':
            xquery=query+' ORDER BY ProductUpdateDate'
        #print query
        #for cat in filterarray:
        #    query = query,cat
        products = Products.objects.raw(query)#SELECT * FROM products WHERE ProductCategoryId in (4,5) and ProductLocation in ("Moscow") ProductPrice between 10 and 200 ORDER BY ProductPrice 
        products = serializers.serialize("json",products)
        data = {'products': products}
        return HttpResponse(json.dumps(data), content_type="application/json")

def catgift(request, cat):
    #print ('hiiii')
    #print (cat)
    products = Products.objects.raw('SELECT * FROM products WHERE ProductCategoryId ='+ cat)
    template=loader.get_template("app/browse.html")
    rc=RequestContext(request,{'products':products})
    return HttpResponse(template.render(rc))

def bestfor(request, cat):
    #print ('hiiii')
    #print (cat)
    products = Products.objects.raw('SELECT * FROM products WHERE ProductBestFor ='+ cat)
    template=loader.get_template("app/browse.html")
    rc=RequestContext(request,{'products':products})
    return HttpResponse(template.render(rc))

@csrf_protect
def  saveorderdetails(request):

     if request.method == 'POST':
        form = request.POST
        user_id = request.session['user']
        ordersession=json.loads(request.session['order'])
        qty=ordersession['Qty']
        productid=ordersession['Productid']
        color=ordersession['Color']
        size=ordersession['Size']
        tokentrack=token(int(str(productid)),50000)
        lastconnection = datetime.strptime(form['r_start'], "%d.%m.%Y").strftime('%Y-%m-%d')
        order = Orders(orderuserid=user_id, orderamount='100', ordershipname = form['r_fname'], ordercity=form['r_city'],
                       orderstate=form['r_State'], orderzip=form['r_zip'],orderphone=form['r_phone'],orderdesc = str(ordersession),
                       orderemail=form['r_email'],orderdate=lastconnection,
                       ordershipaddress = form['r_info'],ordertrackingnumber=tokentrack,)
        order.save()
        oid=order.orderid
        
        product = Products.objects.raw('SELECT * FROM products WHERE ProductId ='+ str(productid))[0]
        ammountperpice=product.productprice
        paymentmoney=int(str(qty)) * ammountperpice
        productdesc=str(ordersession)
        Qty=str(qty)

        sendmail(str(form['r_email']),str(tokentrack),'Gift recive code')
        #orderdet = Orderdetails(detailname = form['fname'])
        #orderdet.save()
        template = loader.get_template("app/payment.html")
        rc = RequestContext(request,{'orderid': oid,'paymentmoney': paymentmoney,'productdesc': productdesc,'Qty': Qty})
        return HttpResponse(template.render(rc))

def sendgift(request):
    #print ('hiiii')
    try:
       user_id = request.session['user']
       user = Users.objects.raw('SELECT * FROM users WHERE UserID ='+user_id)
       template = loader.get_template("app/send_gift.html")
       rc = RequestContext(request,{'user':user})
       return HttpResponse(template.render(rc))
    except :
       currenturl='/sendgift'
       request.session['preurl'] = currenturl
       template = loader.get_template("app/page_login.html")
       rc = RequestContext(request,{'message':'Login first'})
       return HttpResponse(template.render(rc))


def search(request, keyword):
    #print (keyword)
    #keyword=keyword.replace('%20',' ')
    querey = 'SELECT * FROM products WHERE ProductName LIKE \'%%'+keyword+'%%\''
    products = Products.objects.raw(querey)
    template = loader.get_template("app/browse.html")
    rc = RequestContext(request,{'products':products})
    return HttpResponse(template.render(rc))

def selgift(request, id):
    #print ('hiiii')
    #print (id)
    product = Products.objects.raw('SELECT * FROM products WHERE ProductId ='+ id)[0]
    try:
        stock=product.productstock+1
    except :
        stock=1
    try:
        size=product.productsize
        sizearry=size.split(',');
    except :
        sizearry=[]
    try:
        color=product.productcolor
        colorarry=color.split(',');
    except :
        colorarry=[]
    template=loader.get_template("app/product.html")
    rc=RequestContext(request,{'product':product,'stock':stock,'range':range(stock),'size':sizearry,'color':colorarry})
    return HttpResponse(template.render(rc))

def ordergift(request, id):
    #print ('hiiii')
    #print (id)
    products = Products.objects.raw('SELECT * FROM products WHERE ProductId ='+ id)[0]
    try:
      user_id = request.session['user']
      ordersession=json.loads(request.session['order'])
      qty=ordersession['Qty']
      productid=ordersession['Productid']
      color=ordersession['Color']
      size=ordersession['Size']
      ammountperpice=products.productprice
      ammount=int(str(qty)) * ammountperpice
      user = Users.objects.raw('SELECT * FROM users WHERE UserID =1')[0]
      template = loader.get_template("app/send_gift.html")
      rc = RequestContext(request,{'user':user,'products':products,'ammount':ammount})
      return HttpResponse(template.render(rc))
    except :
      currenturl='/ordergift/'+id
      request.session['preurl'] = currenturl
      template = loader.get_template("app/page_login.html")
      rc = RequestContext(request,{'message':'Login first'})
      return HttpResponse(template.render(rc))

def sendmail(To, Messege, subject):
    from django.core.mail import EmailMessage
    email = EmailMessage(Messege, subject, to=[To])
    email.send()
    send_mail(subject, Messege, 'nitindwivedi@globussoft.com',[To], fail_silently=False)
    return

def sendsms(request):
    from sendsms.message import SmsMessage
    message = SmsMessage(body='lolcats make me hungry', from_phone='+919713872684', to=['+918792414595'])
    message.send()
    return HttpResponseRedirect('/gifts')

import random

def token(a,b):
    n = random.randint(a,b)
    return n


def receivegift(request):
    #print ('hiiii')
    if (request.is_ajax()):
        trackcode = request.GET['trackcode']
        user_id = request.session['user']
        user = Users.objects.get(userid = user_id)
        user_email = user.useremail
        order = Orders.objects.get(ordertrackingnumber = trackcode)
        order_email = order.orderemail

        if (user_email == order_email) :
            orderuserid = order.orderuserid
            ordercost = order.orderamount
            orderdesc = order.orderdesc
            sent_user = Users.objects.get(userid = orderuserid)
            sendername = sent_user.userfirstname +' '+ sent_user.userlastname
            result = 'success'

            data = {'sendername':sendername, 'ordercost':ordercost, 'orderdesc':orderdesc, 'result':result}
            return HttpResponse(json.dumps(data), content_type="application/json")
            
        else:
            #print('not authorized')
            result = 'NOT AUTHORIZED'
            data = {'result':result}
            return HttpResponse(json.dumps(data), content_type="application/json")

def getcategories(request):
    if (request.is_ajax()):
        categories = Productcategories.objects.raw('SELECT * FROM Productcategories')
        category = serializers.serialize("json",categories)
        data = {'category': category}
    return HttpResponse(json.dumps(data), content_type="application/json")