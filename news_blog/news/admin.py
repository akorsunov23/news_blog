from django.contrib import admin
from news.models import News, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	list_display = 'id', 'title', 'author'


admin.site.register(Comment)
