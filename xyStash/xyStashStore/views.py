# import email
from operator import sub
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from numpy import product

from .models import *
from .forms import *
from django.core import serializers
import json

def index(request):
    return render(request, 'pages/index.html')

def shop(request):
    product = Product.objects.all() #allows access to all products
    return render(request, 'pages/shop.html', {'products' : product})

def categories(request):
    return {
        'categories' : Category.objects.all()
    }

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'pages/product.html', {'product' : product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'pages/category.html', {'category': category, 'products' : products })

# def cart(request):
#     return render(request, 'pages/index.html')

def contact(request):
    if request.method == 'POST':
        contact_form = contactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['fullname']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']

            contact_data = fromContactForm(name = name, email = email, message = message)
            contact_data.save()
            form = contactForm()
            msg_confirmed = "Message sent! Thank you for reaching out."
            return render(request, 'pages/contact.html', {'ContactForm': form, 'message': msg_confirmed })
    
    else:
        form = contactForm()
        return render(request, 'pages/contact.html', {'ContactForm' : form})

def profile(request):
    if request.session.has_key('username'):
        return render(request, 'pages/profile.html', {'username' : request.session['username'] })

    else:
        request.session['error'] = "You need to log in first to go to profile!"
        return redirect('login')

def login(request):
    if request.method == 'POST':
        submitted_form = loginForm(request.POST)
        if submitted_form.is_valid():
            username = submitted_form.cleaned_data['username']
            password = submitted_form.cleaned_data['password']

            member = user.objects.filter(db_username = username, db_password = password)
            if member:
                member = serializers.serialize('json', member)
                userinfo = json.loads(member)
                # request.session['fname'] = userinfo[0]['fields']['db_fname']
                # request.session['lname'] = userinfo[0]['fields']['db_lname']
                # request.session['email'] = userinfo[0]['fields']['email']
                request.session['username'] = userinfo[0]['fields']['db_username']
                return redirect('profile')
                
            else:
                error = "Username or password is wrong."
                form = loginForm()
                return render(request, 'pages/login.html', {'LoginForm': form, 'error' : error})
    else:
        if request.session.has_key('error'):
            error = request.session['error']
        else:
            error = " "

        form = loginForm()
        return render(request, 'pages/login.html', {'error' : error, 'LoginForm' : form})

def signup(request):
    if request.method == 'POST':
        submitted_form = signUpForm(request.POST)
        if submitted_form.is_valid():
            fname = submitted_form.cleaned_data['firstName']
            lname = submitted_form.cleaned_data['lastName']
            userEmail = submitted_form.cleaned_data['email']
            username = submitted_form.cleaned_data['username']
            userPassword = submitted_form.cleaned_data['password']

            if user.objects.filter(db_username = username):
                error = 'Username already exists.'
                form = signUpForm()
                return render(request, 'pages/signup.html', {'signUpForm': form, 'error' : error})
            else:
                user_data = user(db_fname = fname, db_lname = lname, db_email = userEmail, db_username = username, db_password = userPassword)
                user_data.save()

            request.session['firstName'] = fname
            request.session['lastName'] = lname
            request.session['username'] = username
           
        return redirect('profile')
            
    else: 
        form = signUpForm()
        return render(request, 'pages/signup.html', { 'signUpForm' : form })

def logoutUser(request):
    del request.session['username']    
    if request.session.has_key('error'):
        del request.session['error']
    
    return redirect('login')

# def newsletter(request):
#     subscribe = subscribersForm()
#     return { 'sub_email' : subscribe }

