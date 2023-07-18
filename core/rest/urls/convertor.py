from django.urls import path

from ..views import pdfConvertor


urlpatterns = [
    path('',
         pdfConvertor.DocumentConversionView.as_view(),
         name="convert_document"),
]