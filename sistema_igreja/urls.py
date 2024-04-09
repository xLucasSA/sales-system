from barraquinhas.admin import custom_admin_site
from django.urls import path, include
from barraquinhas.views import index


urlpatterns = [
    path('', index, name='index'),
    path('admin/',custom_admin_site.urls, name='customadmin'),
    path('barraquinhas/', include('barraquinhas.urls')),
]
