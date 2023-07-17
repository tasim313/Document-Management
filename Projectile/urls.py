from django.conf.urls.static import static
from django.conf import settings

from .ProjectileURLs.admin import urlpatterns as admin
from .ProjectileURLs.debug_toolbar import urlpatterns as debug
from .ProjectileURLs.health import urlpatterns as health
from .ProjectileURLs.swagger import urlpatterns as swagger
from .ProjectileURLs.core import urlpatterns as core


urlpatterns = admin+debug+health+swagger+core + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
    ) + static(
        settings.MEDIA_URL_2,
        document_root=settings.MEDIA_ROOT)