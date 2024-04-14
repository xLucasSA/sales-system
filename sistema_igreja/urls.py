from django.contrib import admin
from django.urls import path, include
from barraquinhas.views import index


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('barraquinhas/', include('barraquinhas.urls')),
]
