from django.urls import include, path

urlpatterns = [ 
    path("login/", include("core.rest.urls.Login")),
    path("register/", include("core.rest.urls.Register")),
    path('document/', include("core.rest.urls.document")),
    path('share/', include("core.rest.urls.share")),
]