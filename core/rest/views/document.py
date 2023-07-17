from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from ...models import Document
from ..serializers import document



class DocumentList(generics.ListAPIView):
    
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

    permission_classes = [IsAuthenticated]
    queryset = Document.objects.filter(
        status="Active")
    serializer_class =  document.DocumentSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['title',
                      'description',
                      'file',
                      'created_date',
                      'updated_date',
        ]

    def post(self, request, format=None, **kwargs):
        serializer = document.DocumentCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class DocumentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = document.DocumentUpdateSerializer
    lookup_field = 'uid'


class DocumentShareOrDownloadList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.filter(status="Active")
    serializer_class = document.FileShareOrDownloadSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['title',
                      'description',
                      'file',
                      'created_date',
                      'updated_date',
                    ]
