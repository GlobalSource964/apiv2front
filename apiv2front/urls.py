from api_app import views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from api_app.views import index, redirect_to_amp, amp
from apiv2front import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('amp', amp),
    path('robots.txt', serve, {'document_root': settings.BASE_DIR, 'path': 'robots.txt'}),
    path('sitemap.xml', views.sitemap),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
