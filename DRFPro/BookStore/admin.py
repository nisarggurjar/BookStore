from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Genre)

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','author', 'book_type', 'description', "favbook"]
    list_filter = ['category', 'author', 'book_type', "favbook"]
    list_editable = ['category', 'book_type', 'description', "favbook"]