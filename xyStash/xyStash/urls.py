"""xyStash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from xyStashStore import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('shop', views.shop, name="shop"),
    path('item/<slug:slug>/', views.product_detail, name="product_detail"),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    # path('cart', views.cart, name="cart"),
    path('contact', views.contact, name="contact"),
    path('profile', views.profile, name="profile"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logoutUser, name="logout"),
    # path('newsletter', views.newsletter, name="newsletter"),
]

#Will allow access to local storage. settings.DEBUG should not be used in production mode. (check bottom code for settings.py)
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
