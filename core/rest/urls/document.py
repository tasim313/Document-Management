from django.urls import path
from core.rest.views import document

urlpatterns = [
    path('', 
         document.DocumentCreate.as_view(),
         name='document-list-create'),
    path('<uuid:uid>/',
         document.DocumentRetrieveUpdate.as_view(),
         name='document-update'),
    path('list/', 
         document.DocumentList.as_view(),
         name='document-list'),
    path('share/', 
         document.DocumentShareOrDownloadList.as_view(),
         name='document-share'),
]