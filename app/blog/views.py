from django.views.generic import ListView, DetailView
from .models import Post

class Blog(ListView):
    template_name = "blog/blog.html"
    model = Post

class PostDetail(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context ['posts'] = Post.postobjects.all()
#         return context

# class PostDetailView(DetailView):
#     model = Post
#     template_name = "blog/post-detail.html"
#     context_object_name = 'post'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = Post.objects.filter(slug=self.kwargs.get('slug'))
#         return context
