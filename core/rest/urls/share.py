from django.urls import path, include
from core.rest.views import share

urlpatterns = [
    path('create/', 
         share.ShareDocumentListCreate.as_view(),
         name='share-file-create'),
    path('', share.ShareDocumentView.as_view(),name='share-file'),
    path("me/share/document", share.ShareDocumentViewerAPIView.as_view(),
         name='document-share-with-me'),
]