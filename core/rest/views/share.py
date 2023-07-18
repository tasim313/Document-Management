from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from ..serializers import share
from ...models import DocumentShare
from ..permission import base

    

class ShareDocumentView(viewsets.ModelViewSet):
    "Here user can see how many people and which user share his document"
    permission_classes = [IsAuthenticated, base.IsOwnerOrAdminOrReadOnly]
    queryset = DocumentShare.objects.all()
    serializer_class = share.ShareDocumentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_date']


class ShareDocumentListCreate(generics.CreateAPIView):
    "User can share his document with other user as he can."
    permission_classes = [IsAuthenticated, base.IsOwnerOrAdminOrReadOnly]
    queryset = DocumentShare.objects.all()
    serializer_class = share.ShareDocumentListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_date']


class ShareDocumentViewerAPIView(generics.ListAPIView):

    " Request User can see share document if anyone share his document with him"

    permission_classes = [IsAuthenticated, base.IsOwnerOrAdminOrReadOnly]
    serializer_class = share.ShareDocumentSerializer

    def get_queryset(self):
        user = self.request.user
        return DocumentShare.objects.filter(share_person=user)