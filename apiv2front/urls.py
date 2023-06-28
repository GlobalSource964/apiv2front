from api_app import views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from api_app.views import index, amp
from apiv2front import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('amp', amp),
    path('robots.txt', serve, {'document_root': settings.BASE_DIR, 'path': 'robots.txt'}),
    path('sitemap.xml', views.sitemap),
    path('yandex_304bf76ccfb461c4.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_304bf76ccfb461c4.html'}),
    path('yandex_f4c50a18f25e6b20.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_f4c50a18f25e6b20.html'}),
    path('yandex_8a3df29fdd1bab74.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_8a3df29fdd1bab74.html'}),
    path('yandex_859b7bab1ec98146.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_859b7bab1ec98146.html'}),
    path('yandex_ab7df91959b748f2.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_ab7df91959b748f2.html'}),
    path('yandex_8dda85408d17aed4.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_8dda85408d17aed4.html'}),
    path('yandex_cda50f9470014ae7.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_cda50f9470014ae7.html'}),
    path('yandex_0524d52a5837a669.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_0524d52a5837a669.html'}),
    path('yandex_02a4a80fa09cc827.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_02a4a80fa09cc827.html'}),
    path('yandex_cd8686ddfa65d4b0.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_cd8686ddfa65d4b0.html'}),
    path('yandex_eb730c5531324e5d.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_eb730c5531324e5d.html'}),
    path('yandex_41197f8f09d6c967.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_41197f8f09d6c967.html'}),
    path('yandex_28bd4520e8cf4383.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_28bd4520e8cf4383.html'}),
    path('yandex_ea9851d31a2d4bc0.html', serve, {'document_root': settings.BASE_DIR, 'path': 'yandex_ea9851d31a2d4bc0.html'}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
