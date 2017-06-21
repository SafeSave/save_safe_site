# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from customer.models import Customer
from customer.views import customer
from core.forms import SearchForm

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        # render a user specified web page
        # assign administrator as super user
        # assign translator as staff
        if request.user.is_superuser:
            return None

        else:
            return customer(request, request.user)
    else:
        return render(request, 'index.html', {
            'form': SearchForm()
        })