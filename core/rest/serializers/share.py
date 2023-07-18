from rest_framework import serializers

from ...models import DocumentShare
from ...choice import UserStatus
from ..serializers import User, document


    
class ShareDocumentListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = DocumentShare
        fields = ["uid", 'document', 'share_person', 'user_created']




class ShareDocumentSerializer(serializers.ModelSerializer):
    document = document.DocumentSerializer(many=True, read_only=True)
    share_person = User.UserSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = DocumentShare
        fields = ("uid", "slug",'document', 'share_person', 'user_created',)
        extra_kwargs = {
            'document': {'required': False},
            'share_person': {
                'required': False
            }
                        }