from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import shop.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop.views.index),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns