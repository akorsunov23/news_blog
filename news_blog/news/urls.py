from django.urls import path
from news.api import \
	NewsListViewSet, \
	NewsCreateViewSet, \
	NewsUpdateOrDeleteViewSet, \
	CommentViewSet, \
	CommentCreateViewSet, \
	CommentDeleteViewSet, \
	LikePostAPIView

app_name = 'news'

urlpatterns = [
	path('', NewsListViewSet.as_view(), name='news_list'),
	path('create/', NewsCreateViewSet.as_view(), name='news_create'),
	path('<id>/', NewsUpdateOrDeleteViewSet.as_view(), name='news_update'),
	path('<news_id>/comments/', CommentViewSet.as_view(), name='news_comment'),
	path('comment/create/', CommentCreateViewSet.as_view(), name='news_comment_create'),
	path('<news_id>/comments/<id>/', CommentDeleteViewSet.as_view(), name='news_comment_delete'),
	path('<int:pk>/like/', LikePostAPIView.as_view(), name='news_like')
]