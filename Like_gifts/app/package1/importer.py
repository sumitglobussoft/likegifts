from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpRequest, HttpResponse
from datetime import datetime
from django import *
from app.models import Products
from app.forms import *
from django.template import loader,RequestContext
from django.shortcuts import render_to_response

def  uploadproducts(request):

    if request.method == 'POST':
        form = request.POST
    # Full path and name to your csv file
    csv_filepathname=form['mycsvfile']#"D:/likestore/likestore/sample_products.csv"
    # Full path to your django project directory
    your_djangoproject_home="D:/likestore/likestore/likestore"

    import sys,os
    sys.path.append(your_djangoproject_home)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'likestore.settings'

    import csv
    dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

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
            products.productthumb = row[11]
            products.productimage = row[12]
            products.productimage2 = row[13]
            products.productimage3 = row[14]
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
    return HttpResponse(template.render(rc))