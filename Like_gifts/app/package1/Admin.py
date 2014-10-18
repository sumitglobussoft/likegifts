# -*- coding: utf-8 -*-
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

def admin(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'admin/page_login.html',
        
        {
            'title':'About',
            'message':'Your application description page.',
        }
    )

@csrf_protect
def loginadmin(request):
    """Renders the about page."""
    if request.method == 'POST':
        form = request.POST
        username = form['username']
        password = form['password']
        if(username == 'admin'):
           if( password == 'admin123'):
            return render(request,'admin/index.html',        
            {
            'title':'About',
            'message':'Your application description page.',
            })
           else:
            return render(request,'admin/page_login.html',
            {
            'title':'About',
            'message':'Your application description page.',
            })
        else:
            return render(request,'admin/page_login.html',
            {
            'title':'About',
            'message':'Your application description page.',
            })

def logoutadmin(request):
    """Renders the about page."""
    del request.session
    return render(
        request,
        'admin/page_login.html',
        
        {
            'title':'About',
            'message':'Your application description page.',
        }
    )

def myusers(request):
    #print ('hiiii')
    users = Users.objects.raw('SELECT * FROM users')
    template=loader.get_template("admin/userlist.html")
    rc=RequestContext(request,{'users':users})
    return HttpResponse(template.render(rc))

def oneuser(request):
    #print ('hiiii')
    if (request.is_ajax()):
        userid = request.GET['userid']
        thisuser = Users.objects.raw('SELECT * FROM users WHERE userid = '+userid)
        onlyuser = serializers.serialize("json",thisuser)
        data = {'onlyuser': onlyuser}
    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_protect
def updateuser(request):
    #print ('hiiii')
    if request.method == 'POST':
        form = request.POST
        user = Users(userid= form['newid'], useremail = form['newemail'], userpassword= form['newpass'], userfirstname = form['newfname'], 
                     userlastname= form['newlname'], usercity = form['newcity'], userstate= form['newstate'], userzip = form['newzip'], 
                     useremailverified= form['newemailver'], userregistrationdate = form['newdate'], userverificationcode= form['newcode'], 
                     userip = form['newip'], userphone= form['newphone'], userfax = form['newfax'], usercountry= form['newcountry'], 
                     useraddress = form['newadd'], useraddress2 = form['newadd2'])
        user.save()
        return HttpResponseRedirect('/myusers')

def deleteuser(request, uid):
    #print ('hiiii'+uid)
    Users.objects.filter(userid=uid).delete()
    return HttpResponseRedirect('/myusers')

def myproducts(request, cat):
    #print ('hiiii')
    #print (cat)
    products = Products.objects.raw('SELECT * FROM products WHERE ProductCategoryId ='+ cat)
    template=loader.get_template("admin/tables_datatables.html")
    rc=RequestContext(request,{'products':products})
    return HttpResponse(template.render(rc))

def allproducts(request):
    #print ('hiiii')
    products = Products.objects.raw('SELECT * FROM products')
    template=loader.get_template("admin/tables_datatables.html")
    rc=RequestContext(request,{'products':products})
    return HttpResponse(template.render(rc))

def oneproduct(request):
    #print ('hiiii')
    if (request.is_ajax()):
        productid = request.GET['productid']
        thisproduct = Products.objects.raw('SELECT * FROM products WHERE productid = '+productid)
        onlyproduct = serializers.serialize("json",thisproduct)
        data = {'onlyproduct': onlyproduct}
    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_protect
def updateproduct(request):
    #print ('hiiii')
    if request.method == 'POST':
        form = request.POST
        price = float(form['newprice'])
        weight = float(form['newweight'])
        product = Products(productid= form['newid'], productsku = form['newsku'], productname= form['newname'], productprice = price, 
                     productweight= weight, productbestfor = form['newbest'], productcartdesc= form['newcdesc'], productlocation = form['newloc'],
                     productshortdesc = form['newsdesc'], productlongdesc= form['newldesc'], productthumb = form['newtumb'], 
                     productimage= form['newimg'], productcategoryid = form['newcatid'], productupdatedate= form['newdate'], 
                     productstock = form['newstock'], productlive= form['newlive'], productunlimited = form['newunlimit'],
                     productsize = form['newsize'], productcolor = form['newcolor'], productrating = form['newrating'],
                     productimage2 = form['newimg2'], productimage3 = form['newimg3'])
        product.save()
        return HttpResponseRedirect('/allproducts')

def delproduct(request, pid):
    #print ('hiiii'+pid)
    Products.objects.filter(productid=pid).delete()
    return HttpResponseRedirect('/allproducts')

def allorders(request):
    #print ('hiiii')
    orders = Orders.objects.raw('SELECT * FROM orders')
    template=loader.get_template("admin/orderlist.html")
    rc=RequestContext(request,{'orders':orders})
    return HttpResponse(template.render(rc))

def oneorder(request):
    #print ('hiiii')
    if (request.is_ajax()):
        orderid = request.GET['orderid']
        thisorder = Orders.objects.raw('SELECT * FROM orders WHERE orderid = '+orderid)
        onlyorder = serializers.serialize("json",thisorder)
        data = {'onlyorder': onlyorder}
    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_protect
def updateorder(request):
    #print ('hiiii')
    if request.method == 'POST':
        form = request.POST
        amount = float(form['amount'])
        shipping = float(form['shipping'])
        tax = float(form['tax'])
        order = Orders(orderid= form['oid'], orderuserid = form['ouid'], orderamount= amount, ordershipname = form['shipname'],
                     ordershipaddress= form['shipadd'], ordershipaddress2 = form['shipadd2'], ordercity= form['city'],
                     orderstate = form['state'], orderzip= form['zip'], ordercountry = form['country'], orderphone= form['phone'], 
                     orderdesc = form['desc'], ordershipping= shipping, ordertax = tax, orderemail= form['email'], 
                     orderdate = form['date'], ordershipped = form['shipped'], ordertrackingnumber = form['otnum'])
        order.save()
        return HttpResponseRedirect('/allorders')

def delorder(request, oid):
    #print ('hiiii'+oid)
    Orders.objects.filter(orderid=oid).delete()
    return HttpResponseRedirect('/allorders')

def uploadimage(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'admin/image_uploader.html',
        
        {
            'title':'About',
            'message':'Your application description page.',
        }
    )


def saveproductimage(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for oneimage in request.FILES.getlist('image_files'):
                layout = Layout(image=oneimage)
                layout.save()
            return HttpResponse('image upload success')
    return HttpResponse('allowed only via POST')


def uploadproducts(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'admin/upload_product.html',
        
        {
            'title':'About',
            'message':'Your application description page.',
        }
    )

@csrf_protect
def uploadproductsfile(request):
    print('uploading file')
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for onefile in request.FILES.getlist('product_files'):
                prolayout = Prolayout(productfile=onefile)
                prolayout.save()
                Project_Root = path.dirname(path.abspath(path.dirname(__file__)))
                Media_Root = path.join(Project_Root, 'static/assets/img/main').replace('\\', '/')
                csv_filepathname = Media_Root+'/products_Upload.csv'

                import csv
                with open(csv_filepathname, 'r') as csvfile:
                    dataReader = csv.reader(csvfile, delimiter=',', quotechar='"')

                    for row in dataReader:
                        if row[0] != 'ProductID': # Ignore the header row, import everything else
                            products = Products()
                            products.productsku = row[0]
                            products.productname = row[1]
                            products.productprice = row[2]
                            products.productweight = row[3]
                            products.productbestfor = row[4]
                            products.productcartdesc = row[5]
                            products.productshortdesc = row[6]
                            products.productlongdesc = row[7]
                            products.productsize = row[8]
                            products.productcolor = row[9]
                            products.productrating = row[10]
                            products.productthumb = 'assets/img/main/'+row[11]
                            products.productimage = 'assets/img/main/'+row[12]
                            products.productimage2 = 'assets/img/main/'+row[13]
                            products.productimage3 = 'assets/img/main/'+row[14]
                            products.productcategoryid = row[15]
                            products.productupdatedate = row[16]
                            products.productstock = row[17]
                            products.productlive = row[18]
                            products.productunlimited = row[19]
                            products.productlocation = row[20]
                            products.save()
                    products = Products.objects.raw('SELECT * FROM products')
                    template=loader.get_template("admin/tables_datatables.html")
                    rc=RequestContext(request,{'products':products})
                os.remove(csv_filepathname)
                return HttpResponse(template.render(rc))
    return HttpResponse('allowed only via POST')