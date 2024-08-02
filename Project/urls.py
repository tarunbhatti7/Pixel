"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('upload.urls')),
    path('',include('User_profile.urls')),
    path('',include('Friend.urls')),
    path('',include('chat.urls')),
    path('',include('noto_stuff.urls'))
]
admin.site.site_header = "Noto Admin"
admin.site.site_title = "Noto Admin Portal"
admin.site.index_title = "Noto admin Portal"

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static (settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)