from django.contrib import admin

from .models import Article, Comment

class CommentInLine(admin.StackedInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)