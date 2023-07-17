from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.urls import path

urlpatterns = i18n_patterns(
    path(_("admin/"), admin.site.urls),
)