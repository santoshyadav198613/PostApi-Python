from rest_framework import serializers

from post.models import Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'title', 'body')
        extra_kwargs = {
            'url': {
                'view_name': 'posts:post-detail',
            }
        }
