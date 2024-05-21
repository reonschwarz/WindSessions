"""
URL configuration for WindSessions project.

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
from django.urls import path, include
from sessionData import views as session_views
from sessionData import auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('upload/', session_views.upload_session_data, name='session_upload'),
    path('upload/success/', session_views.upload_success, name='session_upload_success'),
    path('accounts/login/', auth_views.login_view, name='login'),
    path('accounts/logout/', auth_views.logout_view, name='logout'),
    path('accounts/register/', auth_views.register_view, name='register'),
    path('session/results/<int:session_id>/', session_views.session_results, name='session_results'),
]

# only in development
if True:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)