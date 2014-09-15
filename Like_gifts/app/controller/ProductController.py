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


def gifts(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/browse.html',
        
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )