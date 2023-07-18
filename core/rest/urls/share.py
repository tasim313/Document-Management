from django.urls import path, include
from core.rest.views import share

from rest_framework.routers import DefaultRouter

from rest_framework import routers

router = DefaultRouter()

router.register(r'share', share.ShareDocumentView, basename='share-file')

urlpatterns = [
    path('create/', 
         share.ShareDocumentListCreate.as_view(),
         name='share-file-create'),
    path('', include(router.urls)),
    path("me/share/document", share.ShareDocumentViewerAPIView.as_view(),
         name='document-share-with-me'),
]