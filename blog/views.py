from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import ModelFormMixin
from taggit.models import Tag, TaggedItem

from blog.forms import CommentForm, PostCreateForm
from blog.models import Post

#
# class HomeTemplateView(generic.TemplateView):
#     template_name = 'blog/home.html'


class HomeView(generic.ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/home.html'


class PostDetailView(ModelFormMixin, generic.DetailView):
    model = Post
    form_class = CommentForm
    template_name = 'blog/post_detail.html'
    success_message = 'Comment added successfully  !!'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.instance.commenter = self.request.user
            form.instance.comment_text = form.cleaned_data['comment_text']
            form.instance.post = self.get_object()
            form.save()
        messages.success(request, self.success_message)
        return HttpResponseRedirect(self.get_object().get_absolute_url())

    # # The name of the field on the model that contains the slug. By default, slug_field is 'slug'.
    # slug_field = 'uuid'

    # The name of the URLConf keyword argument that contains the slug. By default, slug_url_kwarg is 'slug'.
    # slug_url_kwarg = 'slug_uuid'

    # If True, causes get_object() to perform its lookup using both the primary key and the slug. Defaults to False.
    # query_pk_and_slug = True  #

    # pk_url_kwarg = 'uuid'


class PostCreateView(generic.CreateView):
    # model = Post
    template_name = 'blog/post_create.html'
    form_class = PostCreateForm


class PostByTagListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list_with_tag.html'

    def get_queryset(self):
        return super().get_queryset().filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_object'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context
