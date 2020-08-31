"""dbproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('',include('evmanage.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#password reset urls
#url(r'^password-reset/$',auth_views.password_reset,name='password_reset'),
#url(r'^password-reset/done/$',auth_views.password_reset_done,name='password_reset_done'),
#url(r'^password-reset/confirm/(?P<uidb64>[\w-]+)$'/(?P<token>[\w-]+)$', auth_views.password_reset_confirm,name='password_reset_confirm')
