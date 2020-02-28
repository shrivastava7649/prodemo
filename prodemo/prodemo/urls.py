"""prodemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from prodemoapp.views import CustomAuthToken
from prodemoapp import views
from prodemoapp.views import *
from prodemo import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(openapi.Info(title="API CA Firm Arpit",default_version='v1',description="Test description Of CA Firm",terms_of_service="https://www.google.com/policies/terms/",contact=openapi.Contact(email="arpit.s@flitwebs.com"),license=openapi.License(name="BSD License"),),public=True,permission_classes=(permissions.AllowAny,),)

urlpatterns = [
    path('app/', include('prodemoapp.urls')),
    path('admin/', admin.site.urls),
    path('userauth', CustomAuthToken.as_view()),





    #path(r'setpassword_forgot_org', setpassword_forgotviewset_for_org),
    path('xyz',views.xyz),

    path('verify-account/<str:hash>/', views.SendConfirmUserMail.as_view()),
    path('swagger-ui/', TemplateView.as_view(template_name='swagger-ui.html',extra_context={'schema_url':'openapi-schema'}), name='swagger-ui'),
    path('snippets', views.SnippetList.as_view()),
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),






]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Arpit Admin "
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to Flit Webs CA  Portal"