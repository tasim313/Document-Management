from rest_framework import serializers

from ...models import DocumentShare
from ...choice import UserStatus


class ShareDocumentSerializer(serializers.Serializer):
    share_person = serializers.ListField(child=serializers.IntegerField())
    document = serializers.ListField(child=serializers.UUIDField(format='hex_verbose'))

    class Meta:
        fields = ('share_person', 'document')
    
    def create(self, validated_data):
        share_persons = validated_data['share_person']
        documents = validated_data['document']
        request = self.context['request']
        user = request.user
        
        for document in documents:
            for share_person in share_persons:
                document_file = DocumentShare.objects.create(
                    document=document,
                    share_person=share_person,
                    # user_created=user,
                    status=UserStatus.Active   
                )
        return document_file
    
class ShareDocumentListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = DocumentShare
        fields = ["uid", 'document', 'share_person', 'user_created']