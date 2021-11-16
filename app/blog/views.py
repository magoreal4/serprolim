from django.views.generic import ListView, DetailView
from .models import Anuncio, Post

class Blog(ListView):
    template_name = "blog/blog.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super(Blog, self).get_context_data(**kwargs)
        context.update({
            'anuncio_list': Anuncio.objects.filter(display=True),
        })
        return context

    def get_queryset(self):
        return Post.objects.filter(publish=True)
    

class PostDetail(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anuncio_list'] = Anuncio.objects.filter(display=True)
        context['other_posts'] = Post.objects.all()
        return context
