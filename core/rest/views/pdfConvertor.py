from rest_framework import generics, serializers
from rest_framework.response import Response
from ...utils import convert_docx_to_pdf
from ...models import DocumentConvertor
from ..serializers import convertor

        
class DocumentConversionView(generics.ListCreateAPIView):
    queryset = DocumentConvertor.objects.all()
    serializer_class = convertor.DocumentConversionSerializer

    def perform_create(self, serializer):
        docx_file = serializer.validated_data['docx_file']

        try:
            pdf_bytes = convert_docx_to_pdf(docx_file)
            
            DocumentConvertor.objects.create(docx_file=docx_file, pdf_file=pdf_bytes)

        except Exception as e:
            raise serializers.ValidationError(str(e))

        return Response({'message': 'Document converted successfully.'}, status=201)