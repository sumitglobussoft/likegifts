"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import *

# Create your models here.



class Optiongroups(models.Model):
    optiongroupid = models.IntegerField(db_column='OptionGroupID', primary_key=True)  # Field name made lowercase.
    optiongroupname = models.CharField(db_column='OptionGroupName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'optiongroups'


class Options(models.Model):
    optionid = models.IntegerField(db_column='OptionID', primary_key=True)  # Field name made lowercase.
    optiongroupid = models.IntegerField(db_column='OptionGroupID', blank=True, null=True)  # Field name made lowercase.
    optionname = models.CharField(db_column='OptionName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'options'


class Orderdetails(models.Model):
    detailid = models.IntegerField(db_column='DetailID', primary_key=True)  # Field name made lowercase.
    detailorderid = models.IntegerField(db_column='DetailOrderID')  # Field name made lowercase.
    detailproductid = models.IntegerField(db_column='DetailProductID')  # Fieldname made lowercase.
    detailname = models.CharField(db_column='DetailName', max_length=250)  # Field name made lowercase.
    detailprice = models.FloatField(db_column='DetailPrice')  # Field name madelowercase.
    detailsku = models.CharField(db_column='DetailSKU', max_length=50)  # Fieldname made lowercase.
    detailquantity = models.IntegerField(db_column='DetailQuantity')  # Field name made lowercase.

    class Meta:
        db_table = 'orderdetails'


class Orders(models.Model):
    orderid = models.IntegerField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    orderuserid = models.IntegerField(db_column='OrderUserID')  # Field name made lowercase.
    orderamount = models.FloatField(db_column='OrderAmount')  # Field name madelowercase.
    ordershipname = models.CharField(db_column='OrderShipName', max_length=100) # Field name made lowercase.
    ordershipaddress = models.CharField(db_column='OrderShipAddress', max_length=100)  # Field name made lowercase.
    ordershipaddress2 = models.CharField(db_column='OrderShipAddress2', max_length=100)  # Field name made lowercase.
    ordercity = models.CharField(db_column='OrderCity', max_length=50)  # Fieldname made lowercase.
    orderstate = models.CharField(db_column='OrderState', max_length=50)  # Field name made lowercase.
    orderzip = models.CharField(db_column='OrderZip', max_length=20)  # Field name made lowercase.
    ordercountry = models.CharField(db_column='OrderCountry', max_length=50)  #Field name made lowercase.
    orderphone = models.CharField(db_column='OrderPhone', max_length=20)  # Field name made lowercase.
    orderdesc = models.CharField(db_column='OrderDesc', max_length=100)  # Field name made lowercase.
    ordershipping = models.FloatField(db_column='OrderShipping')  # Field name made lowercase.
    ordertax = models.FloatField(db_column='OrderTax')  # Field name made lowercase.
    orderemail = models.CharField(db_column='OrderEmail', max_length=100)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate')  # Field name made lowercase.
    ordershipped = models.IntegerField(db_column='OrderShipped')  # Field name made lowercase.
    ordertrackingnumber = models.CharField(db_column='OrderTrackingNumber', max_length=80, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'orders'


class Payments(models.Model):
    paymentid = models.IntegerField(db_column='PaymentID', primary_key=True)  #Field name made lowercase.
    orderid = models.CharField(db_column='OrderId', max_length=50, blank=True)# Field name made lowercase.
    paymentmethod = models.CharField(db_column='PaymentMethod', max_length=30, blank=True)  # Field name made lowercase.
    paymentammount = models.IntegerField(db_column='PaymentAmmount', blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.IntegerField(db_column='PaymentStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'payments'


class Productcategories(models.Model):
    categoryid = models.IntegerField(db_column='CategoryID', primary_key=True)# Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=50)  #Field name made lowercase.

    class Meta:
        db_table = 'productcategories'


class Productoptions(models.Model):
    productoptionid = models.IntegerField(db_column='ProductOptionID', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID')  # Field name made lowercase.
    optionid = models.IntegerField(db_column='OptionID')  # Field name made lowercase.
    optionpriceincrement = models.FloatField(db_column='OptionPriceIncrement', blank=True, null=True)  # Field name made lowercase.
    optiongroupid = models.IntegerField(db_column='OptionGroupID')  # Field name made lowercase.

    class Meta:
        db_table = 'productoptions'


class Products(models.Model):
    productid = models.IntegerField(db_column='ProductID', primary_key=True)  #Field name made lowercase.
    productsku = models.CharField(db_column='ProductSKU', max_length=50)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=100)  # Field name made lowercase.
    productprice = models.FloatField(db_column='ProductPrice')  # Field name made lowercase.
    productweight = models.FloatField(db_column='ProductWeight')  # Field name made lowercase.
    productbestfor = models.CharField(db_column='ProductBestFor', max_length=15, blank=True)  # Field name made lowercase.
    productcartdesc = models.CharField(db_column='ProductCartDesc', max_length=250)  # Field name made lowercase.
    productshortdesc = models.CharField(db_column='ProductShortDesc', max_length=1000)  # Field name made lowercase.
    productlongdesc = models.TextField(db_column='ProductLongDesc')  # Field name made lowercase.
    productsize = models.CharField(db_column='ProductSize', max_length=100)  # Field name made lowercase.
    productcolor = models.CharField(db_column='ProductColor', max_length=100)  # Field name made lowercase.
    productrating = models.IntegerField(db_column='ProductRating', blank=True, null=True)  # Field name made lowercase.
    productthumb = models.CharField(db_column='ProductThumb', max_length=100)  # Field name made lowercase.
    productimage = models.CharField(db_column='ProductImage', max_length=100)  # Field name made lowercase.
    productimage2 = models.CharField(db_column='ProductImage2', max_length=100)  # Field name made lowercase.
    productimage3 = models.CharField(db_column='ProductImage3', max_length=100)  # Field name made lowercase.
    productcategoryid = models.IntegerField(db_column='ProductCategoryID', blank=True, null=True)  # Field name made lowercase.
    productupdatedate = models.DateTimeField(db_column='ProductUpdateDate')  # Field name made lowercase.
    productstock = models.IntegerField(db_column='ProductStock', blank=True, null=True)  # Field name made lowercase.
    productlive = models.IntegerField(db_column='ProductLive', blank=True, null=True)  # Field name made lowercase.
    productunlimited = models.IntegerField(db_column='ProductUnlimited', blank=True, null=True)  # Field name made lowercase.
    productlocation = models.CharField(db_column='ProductLocation', max_length=250, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'products'


class Users(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    useremail = models.CharField(db_column='UserEmail', max_length=500, blank=True)  # Field name made lowercase.
    userpassword = models.CharField(db_column='UserPassword', max_length=500, blank=True)  # Field name made lowercase.
    userfirstname = models.CharField(db_column='UserFirstName', max_length=50, blank=True)  # Field name made lowercase.
    userlastname = models.CharField(db_column='UserLastName', max_length=50, blank=True)  # Field name made lowercase.
    usercity = models.CharField(db_column='UserCity', max_length=90, blank=True)  # Field name made lowercase.
    userstate = models.CharField(db_column='UserState', max_length=20, blank=True)  # Field name made lowercase.
    userzip = models.CharField(db_column='UserZip', max_length=12, blank=True)# Field name made lowercase.
    useremailverified = models.IntegerField(db_column='UserEmailVerified', blank=True, null=True)  # Field name made lowercase.
    userregistrationdate = models.DateTimeField(db_column='UserRegistrationDate', blank=True, null=True)  # Field name made lowercase.
    userverificationcode = models.CharField(db_column='UserVerificationCode', max_length=20, blank=True)  # Field name made lowercase.
    userip = models.CharField(db_column='UserIP', max_length=50, blank=True)  #Field name made lowercase.
    userphone = models.CharField(db_column='UserPhone', max_length=20, blank=True)  # Field name made lowercase.
    userfax = models.CharField(db_column='UserFax', max_length=20, blank=True)# Field name made lowercase.
    usercountry = models.CharField(db_column='UserCountry', max_length=20, blank=True)  # Field name made lowercase.
    useraddress = models.CharField(db_column='UserAddress', max_length=100, blank=True)  # Field name made lowercase.
    useraddress2 = models.CharField(db_column='UserAddress2', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'users'


class Layout(models.Model):
    image = models.FileField(upload_to='')

    class Meta:
        db_table = 'layout'

class Prolayout(models.Model):
    productfile = models.FileField(upload_to='')

    class Meta:
        db_table = 'prolayout'