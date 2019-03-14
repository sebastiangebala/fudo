from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.decorators.cache import cache_page

from dummy_images.views import ImageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^images/([0-9]{1,4})x([0-9]{1,4})/$', cache_page(60 * 60)(ImageView.as_view()), name='image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

