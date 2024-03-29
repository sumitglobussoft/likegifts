# -*- coding: utf-8 -*-
"""
Definition of views.
"""
from BeautifulSoup import BeautifulSoup
import HTMLParser
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

class LoginForm(forms.Form):
    username=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

def home(request):     
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
       {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    #    htmlpages = Htmlpages.objects.raw('SELECT * FROM htmlpages WHERE slno = 3')[0]    
    #value= htmlpages.htmlcode
    #htmlml = str(value)
    #template = loader.get_template("app/contact.html")
    #rc = RequestContext(request,{'bshtml':htmlml,'title':'Contact'})
    #return HttpResponse(template.render(rc)
    )

def aboutus(request):
    """Renders the about page."""
    aboutcontent = AboutUs.objects.raw('SELECT * FROM aboutus WHERE slno = 1')[0]
    template = loader.get_template("app/about_us.html")
    rc = RequestContext(request,{'aboutcontent':aboutcontent,'title':'About Us'})
    return HttpResponse(template.render(rc)
    )

def blog(request):
    """Renders the about page."""
    allblogs = Blogs.objects.raw('SELECT * FROM blogs ORDER BY Blogs.PublishedDate DESC')
    recentblogs = Blogs.objects.raw('SELECT * FROM blogs ORDER BY Blogs.PublishedDate DESC LIMIT 2')
    template = loader.get_template("app/blog.html")
    rc = RequestContext(request,{'allblogs':allblogs,'recentblogs':recentblogs,'title':'Blogs'})
    return HttpResponse(template.render(rc)
    )


def faq(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/faq.html',
        
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )




def privacy(request):
    """Renders the about page."""
   
    htmlpages = Htmlpages.objects.raw('SELECT * FROM htmlpages WHERE slno = 2')[0]    
    value= htmlpages.htmlcode
    htmlml = str(value)
    #h = HTMLParser.HTMLParser()
    #html= h.unescape(htmlml)
    #bsvalue = BeautifulSoup((value),convertEntities=BeautifulSoup.HTML_ENTITIES)
    template = loader.get_template("app/privacy.html")
    rc = RequestContext(request,{'bshtml':htmlml,'title':'Privacy'})
    return HttpResponse(template.render(rc)
    )


def terms(request):
    """Renders the about page."""
    htmlpages = Htmlpages.objects.raw('SELECT * FROM htmlpages WHERE slno = 1')[0]    
    value= htmlpages.htmlcode
    htmlml = str(value)
    template = loader.get_template("app/terms.html")
    rc = RequestContext(request,{'bshtml':htmlml,'title':'Terms'})
    return HttpResponse(template.render(rc)
    )


def userlogin(request):
    """Renders the login page."""
    if request.method=="POST":
         #form=LoginForm()
         form=(request.POST)
         if 1==1:
             new_user = authenticate(username = form['username'],
                                password = form['password'])
              
             if new_user is not None:
                if new_user.is_active:
                    login(request, new_user)
                    request.session['user'] = new_user.id
                    if 'preurl' in request.session:
                       preurl=request.session['preurl']
                       del request.session['preurl']
                       return HttpResponseRedirect(preurl)
                    else:
                       return HttpResponseRedirect('/gifts')
                else:
                    template=loader.get_template("app/page_login.html")
                    rc=RequestContext(request,{'message':'Your account has been disabled!'})
                    return HttpResponse(template.render(rc))
                    
             else:
                template=loader.get_template("app/page_login.html")
                rc=RequestContext(request,{'message':'Please do sigh up first'})
                return HttpResponse(template.render(rc))
         else:
           template=loader.get_template("app/page_login.html")
           rc=RequestContext(request,{'message':'Email or password not validate'})
           return HttpResponse(template.render(rc))
    else:
        template=loader.get_template("app/page_login.html")
        rc=RequestContext(request,{'message':''})
        return HttpResponse(template.render(rc))


@csrf_protect
def usersignup(request):
    request.session['err_data'] = ''
    if request.method == 'POST':
        form = request.POST
        user = User.objects.create_user(username = form['username'],
            password = form['password1'],
            email = form['email'])
        new_user = authenticate(username = form['username'],
                                password = form['password1'])

        users = Users(userfirstname = form['username'],
              useremail = form['email'],
              userpassword = form['password1'])
        users.save()

        if new_user is not None:
            if new_user.is_active:
                login(request, new_user)
                request.session['user'] = new_user.id
                return HttpResponseRedirect('/sendgift')
            else:
                request.session['err_data'] = "Your account has been disabled!"
                return HttpResponseRedirect('/usersignup')
        else:
            request.session['err_data'] = "The credentials you provided are not correct!"
            return HttpResponseRedirect('/usersignup')
    else:
     template = loader.get_template("app/page_registration.html")
     rc = RequestContext(request,{'message':''})
     return HttpResponse(template.render(rc))


@login_required
def userlogout(request):
    del request.session["user"]
    logout(request)
    return HttpResponseRedirect('/')

