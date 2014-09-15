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
    )

def sendgift(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/send_gift.html',
        
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

