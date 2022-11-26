from rest_framework import views, mixins, viewsets, permissions, generics, status, pagination
from .serializers import ArticleSerializers, CommentsSerializer, ArticleListSerializer
from .models import Article, Comments
from django.utils.text import slugify
from rest_framework.views import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view


class ArticleView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class = ArticleSerializers
    queryset = Article.objects.filter()
    pagination_class = pagination.PageNumberPagination

    def list(self, request, *args, **kwargs):
        ser = ArticleListSerializer(instance=self.queryset, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class CommentView(generics.CreateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    permission_classes = [
        permissions.IsAuthenticated  # TODO: uncomment Is Authenticated
    ]


@api_view(['POST'])
def like_comment_view(request, pk):
    obj = get_object_or_404(Comments, pk=pk)
    obj.like += 1
    obj.save(update_fields=['like'])
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def dislike_comment_view(request, pk):
    obj = get_object_or_404(Comments, pk=pk)
    obj.dislike += 1
    obj.save(update_fields=['dislike'])
    return Response(status=status.HTTP_200_OK)
