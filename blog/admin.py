from django.contrib import admin
from blog.models import Post, Comment


class CommentField(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentField, ]
    list_display = ['title', 'author', ]
    prepopulated_fields = {'slug': ('title',)}

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, change, **kwargs)
        form.base_fields['author'].initial = request.user
        return form


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_text', ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(CommentAdmin, self).get_form(request, obj, change, **kwargs)
        form.base_fields['commenter'].initial = request.user
        return form

#
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     pass
#     # list_display = ['name', ]
