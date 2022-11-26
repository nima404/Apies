from rest_framework import serializers
from .models import Article, Tags, Comments
from django.contrib.auth import get_user_model
from rest_framework_recursive.fields import RecursiveField

User = get_user_model()


class SubCommentsSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author_id.full_name', read_only=True)

    class Meta:
        model = Comments
        fields = [
            'id',
            'content',
            'author',
            'article_id',
            'like',
            'dislike',
        ]
        extra_kwargs = {
            'article_id': {
                'write_only': True,
            },
            'like': {
                'read_only': True,
            },
            'dislike': {
                'read_only': True
            }
        }


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author_id.full_name', read_only=True)
    subs = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = [
            'id',
            'content',
            'author',
            'article_id',
            'like',
            'sub_comment_id',
            'dislike',
            'subs',
        ]
        extra_kwargs = {
            'article_id': {
                'write_only': True,
            },
            'like': {
                'read_only': True,
            },
            'dislike': {
                'read_only': True
            }
        }

    def get_subs(self, obj):
        subs = []
        for sub in Comments.objects.filter(sub_comment_id=obj, is_sub=True):
            subs.append(super(CommentsSerializer, self).to_representation(sub))
        return subs

    def create(self, validated_data):
        validated_data['author_id'] = self.context.get('request').user
        return super().create(validated_data)


class ArticleSerializers(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True, source='article_comments')
    writer = serializers.CharField(source='writer.full_name')
    tags = serializers.ListSerializer(child=serializers.CharField())

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'image',
            'body',
            'tags',
            'writer',
            'created_at',
            'updated_at',
            'comments'
        ]


class ArticleListSerializer(serializers.ModelSerializer):
    writer = serializers.CharField(source='writer.full_name')
    url = serializers.CharField(source='get_absolute_url')

    class Meta:
        model = Article
        fields = [
            "title",
            "image",
            "writer",
            "header",
            "created_at",
            "url"
        ]
