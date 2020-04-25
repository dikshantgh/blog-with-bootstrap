# blog/forms.py
from django import forms
from blog.models import Post, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', ]


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'dp', 'body', 'status', 'publishable_date', 'tags', ]