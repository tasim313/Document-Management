from rest_framework import serializers

class DocumentConversionSerializer(serializers.Serializer):
    docx_file = serializers.FileField()

    def validate_docx_file(self, value):
        valid_extensions = ['docx']
        file_extension = value.name.split('.')[-1].lower()

        if file_extension not in valid_extensions:
            raise serializers.ValidationError("Invalid file format. Only .docx files are supported.")
        
        return value