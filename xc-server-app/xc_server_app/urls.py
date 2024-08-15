"""
URL configuration for xc_server_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('users.urls')),
    path('api/login/', include('login.urls')),
    path('api/app/', include('dashboard.urls')),
    path('api/customer/', include('customers.urls')),
    path('api/lead/', include('leads.urls')),
    path('api/sale/', include('sales.urls')),
    path('api/marketing/', include('marketing.urls')),
    path('api/report/', include('reports.urls')),
    path('api/settings/', include('accountsettings.urls')),
    path('api/disconnect/', include('users.urls')),
]
