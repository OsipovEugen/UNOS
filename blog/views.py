from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from blog.forms import PostForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'current_post'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete_confirm.html'
    success_url = reverse_lazy('blog_list')


class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = ''


class PostUpdateView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        form = PostForm(instance=post)
        context = {'post': post, 'form': form}
        return render(request, 'blog/post_update.html', context)

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        form = PostForm(request.POST,request.FILES, instance=post)
        context = {'post': post, 'form': form}
        if form.is_valid():
            new_post = form.save()
            return redirect(new_post)
        return render(request, 'blog/post_update.html', context)
