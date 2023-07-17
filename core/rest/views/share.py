from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import share
from ...models import DocumentShare


class ShareDocumentView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = DocumentShare.objects.filter(
        status="Active")
    serializer_class = share.ShareDocumentListSerializer

    def post(self, request, format=None, **kwargs):
        serializer = share.ShareDocumentSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)