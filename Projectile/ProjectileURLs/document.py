from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
        path("api/document/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "docs/",
            SpectacularSwaggerView.as_view(
                template_name="swagger-ui.html", url_name="schema"
            ),
            name="swagger-ui",
        ),
  

]