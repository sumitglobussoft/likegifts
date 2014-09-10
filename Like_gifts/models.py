# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Optiongroups(models.Model):
    optiongroupid = models.IntegerField(db_column='OptionGroupID', primary_key=True)  # Field name made lowercase.
    optiongroupname = models.CharField(db_column='OptionGroupName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'optiongroups'


class Options(models.Model):
    optionid = models.IntegerField(db_column='OptionID', primary_key=True)  # Field name made lowercase.
    optiongroupid = models.IntegerField(db_column='OptionGroupID', blank=True, null=True)  # Field name made lowercase.
    optionname = models.CharField(db_column='OptionName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'options'


class Orderdetails(models.Model):
    detailid = models.IntegerField(db_column='DetailID', primary_key=True)  # Field name made lowercase.
    detailorderid = models.IntegerField(db_column='DetailOrderID')  # Field name made lowercase.
    detailproductid = models.IntegerField(db_column='DetailProductID')  # Field name made lowercase.
    detailname = models.CharField(db_column='DetailName', max_length=250)  # Field name made lowercase.
    detailprice = models.FloatField(db_column='DetailPrice')  # Field name made lowercase.
    detailsku = models.CharField(db_column='DetailSKU', max_length=50)  # Field name made lowercase.
    detailquantity = models.IntegerField(db_column='DetailQuantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderdetails'


class Orders(models.Model):
    orderid = models.IntegerField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    orderuserid = models.IntegerField(db_column='OrderUserID')  # Field name made lowercase.
    orderamount = models.FloatField(db_column='OrderAmount')  # Field name made lowercase.
    ordershipname = models.CharField(db_column='OrderShipName', max_length=100)  # Field name made lowercase.
    ordershipaddress = models.CharField(db_column='OrderShipAddress', max_length=100)  # Field name made lowercase.
    ordershipaddress2 = models.CharField(db_column='OrderShipAddress2', max_length=100)  # Field name made lowercase.
    ordercity = models.CharField(db_column='OrderCity', max_length=50)  # Field name made lowercase.
    orderstate = models.CharField(db_column='OrderState', max_length=50)  # Field name made lowercase.
    orderzip = models.CharField(db_column='OrderZip', max_length=20)  # Field name made lowercase.
    ordercountry = models.CharField(db_column='OrderCountry', max_length=50)  # Field name made lowercase.
    orderphone = models.CharField(db_column='OrderPhone', max_length=20)  # Field name made lowercase.
    orderfax = models.CharField(db_column='OrderFax', max_length=20)  # Field name made lowercase.
    ordershipping = models.FloatField(db_column='OrderShipping')  # Field name made lowercase.
    ordertax = models.FloatField(db_column='OrderTax')  # Field name made lowercase.
    orderemail = models.CharField(db_column='OrderEmail', max_length=100)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate')  # Field name made lowercase.
    ordershipped = models.IntegerField(db_column='OrderShipped')  # Field name made lowercase.
    ordertrackingnumber = models.CharField(db_column='OrderTrackingNumber', max_length=80, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Payments(models.Model):
    paymentid = models.IntegerField(db_column='PaymentID', primary_key=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderId', max_length=50, blank=True)  # Field name made lowercase.
    paymentmethod = models.CharField(db_column='PaymentMethod', max_length=30, blank=True)  # Field name made lowercase.
    paymentammount = models.IntegerField(db_column='PaymentAmmount', blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.IntegerField(db_column='PaymentStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payments'


class Productcategories(models.Model):
    categoryid = models.IntegerField(db_column='CategoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productcategories'


class Productoptions(models.Model):
    productoptionid = models.IntegerField(db_column='ProductOptionID', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID')  # Field name made lowercase.
    optionid = models.IntegerField(db_column='OptionID')  # Field name made lowercase.
    optionpriceincrement = models.FloatField(db_column='OptionPriceIncrement', blank=True, null=True)  # Field name made lowercase.
    optiongroupid = models.IntegerField(db_column='OptionGroupID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productoptions'


class Products(models.Model):
    productid = models.IntegerField(db_column='ProductID', primary_key=True)  # Field name made lowercase.
    productsku = models.CharField(db_column='ProductSKU', max_length=50)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=100)  # Field name made lowercase.
    productprice = models.FloatField(db_column='ProductPrice')  # Field name made lowercase.
    productweight = models.FloatField(db_column='ProductWeight')  # Field name made lowercase.
    productbestfor = models.CharField(db_column='ProductBestFor', max_length=15, blank=True)  # Field name made lowercase.
    productcartdesc = models.CharField(db_column='ProductCartDesc', max_length=250)  # Field name made lowercase.
    productshortdesc = models.CharField(db_column='ProductShortDesc', max_length=1000)  # Field name made lowercase.
    productlongdesc = models.TextField(db_column='ProductLongDesc')  # Field name made lowercase.
    productthumb = models.CharField(db_column='ProductThumb', max_length=100)  # Field name made lowercase.
    productimage = models.CharField(db_column='ProductImage', max_length=100)  # Field name made lowercase.
    productcategoryid = models.IntegerField(db_column='ProductCategoryID', blank=True, null=True)  # Field name made lowercase.
    productupdatedate = models.DateTimeField(db_column='ProductUpdateDate')  # Field name made lowercase.
    productstock = models.FloatField(db_column='ProductStock', blank=True, null=True)  # Field name made lowercase.
    productlive = models.IntegerField(db_column='ProductLive', blank=True, null=True)  # Field name made lowercase.
    productunlimited = models.IntegerField(db_column='ProductUnlimited', blank=True, null=True)  # Field name made lowercase.
    productlocation = models.CharField(db_column='ProductLocation', max_length=250, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'products'


class Users(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    useremail = models.CharField(db_column='UserEmail', max_length=500, blank=True)  # Field name made lowercase.
    userpassword = models.CharField(db_column='UserPassword', max_length=500, blank=True)  # Field name made lowercase.
    userfirstname = models.CharField(db_column='UserFirstName', max_length=50, blank=True)  # Field name made lowercase.
    userlastname = models.CharField(db_column='UserLastName', max_length=50, blank=True)  # Field name made lowercase.
    usercity = models.CharField(db_column='UserCity', max_length=90, blank=True)  # Field name made lowercase.
    userstate = models.CharField(db_column='UserState', max_length=20, blank=True)  # Field name made lowercase.
    userzip = models.CharField(db_column='UserZip', max_length=12, blank=True)  # Field name made lowercase.
    useremailverified = models.IntegerField(db_column='UserEmailVerified', blank=True, null=True)  # Field name made lowercase.
    userregistrationdate = models.DateTimeField(db_column='UserRegistrationDate', blank=True, null=True)  # Field name made lowercase.
    userverificationcode = models.CharField(db_column='UserVerificationCode', max_length=20, blank=True)  # Field name made lowercase.
    userip = models.CharField(db_column='UserIP', max_length=50, blank=True)  # Field name made lowercase.
    userphone = models.CharField(db_column='UserPhone', max_length=20, blank=True)  # Field name made lowercase.
    userfax = models.CharField(db_column='UserFax', max_length=20, blank=True)  # Field name made lowercase.
    usercountry = models.CharField(db_column='UserCountry', max_length=20, blank=True)  # Field name made lowercase.
    useraddress = models.CharField(db_column='UserAddress', max_length=100, blank=True)  # Field name made lowercase.
    useraddress2 = models.CharField(db_column='UserAddress2', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
