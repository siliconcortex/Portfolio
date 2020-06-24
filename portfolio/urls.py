"""portfolio URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import include, path
from main_app import views
from django.conf.urls.static import static

"""edit this to match projectname"""
from . import settings



""""the paths for the login and logout are done using the built-in django features"""


urlpatterns = [
    path('admin/', admin.site.urls, name='admin-login'),
    path('', views.post_list, name='post_list'),
    path('post/<pk>', views.post_detail, name = 'post_detail'),
    path('page/<pk>', views.page_detail, name = 'page_detail'),
    path('contact/',include('contact.urls', namespace='contact')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
