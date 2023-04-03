from rest_framework import serializers

from news.models import News, Comment

class NewsListSerializer(serializers.ModelSerializer):
    """Сериализатор, для вывода списка новостей."""
    author = serializers.CharField(source='author.username', read_only=True)
    comments = serializers.SerializerMethodField()
    likes = serializers.IntegerField(source='likes.count')

    @staticmethod
    def get_comments(obj):
        return Comment.objects.filter(news=obj.id).values('comment')[:10]

    class Meta:
        model = News
        fields = 'id', 'title', 'body', 'author', 'comments', 'likes', 'created_at', 'update_at'

class NewsCreateSerializer(serializers.ModelSerializer):
    """Сериализатор, для добавления новости"""
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = News
        fields = '__all__'
    @staticmethod
    def get_likes(obj):
        likes = list(like.username for like in obj.likes.get_queryset().only('username'))
        return likes

class CommentReadSerializer(serializers.ModelSerializer):
    """Сериализатор, для просмотра комментариев"""
    author = serializers.CharField(source='author.username', read_only=True)
    news = serializers.CharField(source='news.title', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    """Сериализатор, для просмотра редактирования комментариев"""
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = 'comment', 'author', 'news'
