from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from api_app.views import index
from apiv2front import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
