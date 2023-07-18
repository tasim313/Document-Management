from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from ...models import Document
from ..serializers import document
from ..permission import base



class DocumentList(generics.ListAPIView):
    """authorize and unauthorize user can see document meta data"""
    
    queryset = Document.objects.filter(status="Active")
    serializer_class = document.DocumentSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['title',
                      'description',
                      'file',
                      'created_date',
                      'updated_date',
                    ]
    


class DocumentCreate(generics.ListCreateAPIView):
    
    """authorize  user can create and see his document meta data. also search document by title,description,file,created_date, """

    permission_classes = [IsAuthenticated, base.IsOwnerOrAdminOrReadOnly]
    queryset = Document.objects.filter(
        status="Active")
    serializer_class =  document.DocumentSerializer


    def get_queryset(self):
        user = self.request.user
        return Document.objects.filter(user_created=user)
    

    def post(self, request, format=None, **kwargs):
        serializer = document.DocumentCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    

class DocumentRetrieveUpdate(generics.RetrieveUpdateAPIView):
     
    """authorize  user can update their document meta data. by uid """

    permission_classes = [IsAuthenticated, base.IsOwnerOrAdminOrReadOnly]
    queryset = Document.objects.all()
    serializer_class = document.DocumentUpdateSerializer
    lookup_field = 'uid'


class DocumentShareOrDownloadList(generics.ListAPIView):
    """authorize  user can share and download document meta data. by url path """
    permission_classes = [IsAuthenticated, base.IsOwnerOrAdminOrReadOnly]
    queryset = Document.objects.filter(status="Active")
    serializer_class = document.FileShareOrDownloadSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['title',
                      'description',
                      'file',
                      'created_date',
                      'updated_date',
                    ]
    
    def get_queryset(self):
        user = self.request.user
        return Document.objects.filter(user_created=user)
