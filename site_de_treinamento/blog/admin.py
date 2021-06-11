from django.contrib import admin
from .models import Post
# Register your models here.

"""mostrar na pagina admin os blogs que tem no sqlite e caso queira editar ou salvar ele faz"""
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}
"""blog/models.py"""