"""CRM_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from Organization.views import OrganizationViewSetAPI
from .views import homepage

router = DefaultRouter()
router.register('organization', OrganizationViewSetAPI)

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    # path('login/', loginpage, name="login"),
    # path('admin/logout', admin.site.urls, name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='login_page.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('', homepage, name="homepage"),
    path('Organization/', include('Organization.urls')),
    path('Product/', include('Product.urls')),
    path('Quote/', include('Quote.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
