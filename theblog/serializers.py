from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'image',
            'title_tag',
            'author',
            'body',
            'create_date',
            'category',
            'likes',
            'ingredients'
        ]


"""
class PostSerializer(serializers.Serializer):
    all the field with certain attributes like
    title = serializers.CharField(max_lenght=100)
    title = serializers.CharField(max_lenght=100)
    body = serializers.Textarea()...

    
    def create(self, validated_data):
        return Post.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.email = validated_data.get('email', instance.email)
        instance.body = validated_date.get('body', instance.body)
"""

"""
in DB shell from console
    from app.models import Post
    from app.serializers import PostSerializer
    from rest_framework.renderers import JSONRenderer
    from rest_framework.parsers import JSONParser

    post = Post(title='example', body='example'...)
    serialized_post = PostSerializer(post)
    content = JSONRenderer().render(serialized_post.data)
    print(content) -> if you would like to see the output
    
    # Basic Concepts for an object serialization.
    # Normally follow the examples below.
    serializer = PostSerializer(Post.object.all(), many=True)
"""
