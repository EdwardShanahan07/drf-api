from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(souce='owner.username')
    profile_image = serializers.ReadOnlyField(source='owner.image')

    class Meta:
        model = Ppst
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 'content', 'image', 'is_owner'
        ]
        
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

