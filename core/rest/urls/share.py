from django.urls import path
from core.rest.views import share

urlpatterns = [
    path('', 
         share.ShareDocumentView.as_view(),
         name='share-file'),
]