from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
            many=True,
            read_only=True,
            view_name='comment-detail'
        )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('slug',)


class CommentSerializer(serializers.ModelSerializer):
    children = serializers.HyperlinkedRelatedField(
            many=True,
            read_only=True,
            view_name='comment-detail'
        )

    class Meta:
        model = Comment
        fields = '__all__'
