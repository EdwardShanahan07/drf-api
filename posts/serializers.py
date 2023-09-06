from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.username')
    profile_image = serializers.ReadOnlyField(source='owner.image')

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'content', 'image', 'is_owner', 'profile_id', 'image_filter', 'profile_image'
        ]
        
    def validate_image(self, value):
        if value.size > 1024 * 1024 *2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
        )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
        )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
        )
        return value

        
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

