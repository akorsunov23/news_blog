from django.db import models
from users.models import CustomUser


class News(models.Model):
	title = models.CharField(max_length=200, null=False, blank=False, verbose_name='заголовок')
	body = models.TextField(null=False, blank=False, verbose_name='текст новости')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
	update_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
	author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='автор', related_name='author_news')
	likes = models.ManyToManyField(CustomUser, blank=True, verbose_name='лайки', related_name='likes')

	class Meta:
		ordering = ('-created_at', )
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'

	def __str__(self):
		return f'{self.title} опубликована {self.author.username}'


class Comment(models.Model):
	news = models.ForeignKey(News, on_delete=models.PROTECT, verbose_name='новость', related_name='comments')
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='автор комментария')
	comment = models.TextField(null=False, blank=False, verbose_name='комментарий')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
	update_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

	class Meta:
		ordering = ('-created_at', )
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

	def __str__(self):
		return f'{self.comment[:20]} к новости {self.news.title}'