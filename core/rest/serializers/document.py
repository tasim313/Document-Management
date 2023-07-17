from rest_framework import serializers 

from ...models import Document
from ...choice import UserStatus
from ...helpers import (
    validate_file_size,
    validate_file_format,
)

import logging

logger = logging.getLogger(__name__)


class DocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Document
        fields = (
            'uid',
            'title',
            'description',
            'file',
            'created_date',
            'updated_date',
            'status',
            'user_created',
            'user_updated',
            )
    
    
    
    



class DocumentCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=300,
        trim_whitespace=True)
    description = serializers.CharField(max_length=None,
                                        trim_whitespace=True)
    file = serializers.FileField(max_length=None,
                                allow_empty_file=False,
                                validators=[validate_file_size, validate_file_format],
                                required=False)
   
    class Meta:
        model = Document
        fields = ('uid','title', 'description', 'file')


    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        title = validated_data['title']
        description = validated_data['description']
        file = validated_data['file']
        document = Document.objects.create(
                    title=title,
                    description=description,
                    file=file,
                    user_created=user,
                    status=UserStatus.Active
                    ) 
        return document
    
    


class DocumentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
                'uid',
                'title',
                'description',
                'file',
                'status',
                'updated_date',
                'user_updated'
            )
        
        
class FileShareOrDownloadSerializer(serializers.ModelSerializer):
     download_url = serializers.SerializerMethodField()
     share_url = serializers.SerializerMethodField()

     class Meta:
        model = Document
        fields = (
            'download_url',
            'share_url',
        )

     def get_download_url(self, obj):
        request = self.context.get('request')
        document_id = obj.uid
        download_url = None
        
        if request and document_id:
            user = request.user
            document = Document.objects.filter(uid=document_id).first()

            if document and (document.user_created == user or user.is_superuser): 
                download_url = request.build_absolute_uri(f'/media/{document.file}')
        
        return download_url
     
     def get_share_url(self, obj):
        request = self.context.get('request')
        share_id = obj.uid
        share_url = None
        
        if request and share_id:
            user = request.user
            document = Document.objects.filter(uid=share_id).first()

            if document and (document.user_created == user or user.is_superuser): 
                share_url = request.build_absolute_uri(f'/media/{document.file}')
        
        return share_url