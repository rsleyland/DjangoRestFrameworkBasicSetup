
from django.contrib import admin
from django.urls import path, include
from api_basic import urls as api_basic_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('articles/', include(api_basic_urls))
]
