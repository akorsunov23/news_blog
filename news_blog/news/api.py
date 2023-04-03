from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import \
    ListModelMixin, \
    CreateModelMixin, \
    RetrieveModelMixin, \
    UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.authentication import SessionAuthentication

from news.models import News, Comment
from news.pagination import StandardResultsSetPagination
from news.serializers import \
    NewsListSerializer, \
    NewsCreateSerializer, \
    CommentReadSerializer, \
    CommentCreateSerializer
from news.authentication import CustomAuth
from news.permissions import CheckingPermissions


class NewsListViewSet(ListModelMixin, GenericAPIView):
    """API для показа списка всех новостей с пагинацией."""
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
    pagination_class = StandardResultsSetPagination

    def get(self, request: Request):
        return self.list(request)

class NewsCreateViewSet(CreateModelMixin, GenericAPIView):
    """API для добавления новости"""
    serializer_class = NewsCreateSerializer
    authentication_classes = CustomAuth, SessionAuthentication

    def post(self, request: Request):
        return self.create(request)

class NewsUpdateOrDeleteViewSet(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    """
    API для редактирования или удаления новости, с проверкой авторизации.
    """
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
    lookup_field = 'id'
    authentication_classes = (CustomAuth, )
    permission_classes = (CheckingPermissions, )

    def get(self, request: Request, *args, **kwargs):
        """Метод API позволяющий просмотреть информацию о конкретной новости по первичному ключу."""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        """Метод API позволяющий редактировать информацию о конкретной новости по первичному ключу."""
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        """Метод API позволяющий удалять новость."""
        return self.destroy(request, *args, **kwargs)

class CommentViewSet(ListModelMixin,  GenericAPIView):
    """API, позволяющий выводить список комментариев к новости."""

    serializer_class = CommentReadSerializer
    lookup_field = 'news_id'
    pagination_class = StandardResultsSetPagination
    authentication_classes = (CustomAuth,)

    def get_queryset(self):
        query = Comment.objects.all()
        news_id = self.kwargs.get('news_id')
        return query.filter(news=news_id)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class CommentCreateViewSet(CreateModelMixin, GenericAPIView):
    """API, позволяющий добавлять комментарий к новости по pk."""

    serializer_class = CommentCreateSerializer
    lookup_field = 'news_id'
    authentication_classes = (CustomAuth, )

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CommentDeleteViewSet(RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """API для удаления комментария по его pk"""

    serializer_class = CommentCreateSerializer
    authentication_classes = (CustomAuth, )
    permission_classes = (CheckingPermissions, )
    lookup_field = 'id'

    def get_queryset(self):
        query = Comment.objects.all()
        news_id = self.kwargs.get('news_id')
        return query.filter(news=news_id)

    def get(self, request: Request, *args, **kwargs):
        """Метод API позволяющий показывающий новость по pk."""
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        """Метод API позволяющий удалять новость."""
        return self.destroy(request, *args, **kwargs)

class LikePostAPIView(APIView):
    """Лайки новостей."""
    authentication_classes = (CustomAuth, )

    @staticmethod
    def get(request, pk):
        user = request.user
        post = get_object_or_404(News, pk=pk)

        if user in post.likes.all():
            post.likes.remove(user)

        else:
            post.likes.add(user)

        return Response(status=status.HTTP_200_OK)
