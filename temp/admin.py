from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'created_at')
    list_display_links = ('first_name', 'last_name', 'birth_date', 'created_at')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'image', 'price', 'count', 'created_at')
    list_display_links = ('title', 'description', 'author', 'image', 'price', 'count', 'created_at')

# @admin.register(Comments)
# class CommentsAdmin(admin.ModelAdmin):
#     list_display = ('user', 'text', 'book', 'created_at')
#     list_display_links = ('user', 'text', 'book', 'created_at')