from django.shortcuts import render
from django.views.generic import TemplateView
from blog.posts.models import Post

class SobreIndex(TemplateView):
    template_name = "sobre/sobre.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['ultimos'] = Post.objects.filter(publicado_post=True).order_by('-id')[:2]
        contexto['sobre'] = 'sobre'
        return contexto