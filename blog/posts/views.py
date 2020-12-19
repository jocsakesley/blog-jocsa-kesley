from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, When, Case, Count, IntegerField
from blog.comentarios.forms import FormComantario
from blog.comentarios.models import Comentario

class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = "posts"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by("-id").filter(publicado_post=True)
        qs = qs.annotate(
            numero_comentario=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1), output_field=IntegerField()
                )
            )
        )

        return qs


class PostCategoria(PostIndex):
    pass

class PostBusca(PostIndex):
    template_name = "posts/post_busca.html"

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')
        qs = qs.filter(
            Q(titulo_post__icontains=termo) |
            Q(autor_post__first_name__iexact=termo) |
            Q(conteudo_post__icontains=termo) |
            Q(excerto_post__icontains=termo) |
            Q(categoria_post__nome_cat__iexact=termo)
        )
        return qs

class PostDetalhes(UpdateView):
    template_name = "posts/post_detalhes.html"
    model = Post
    form_class = FormComantario
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentario.objects.filter(post_comentario=post.id, publicado_comentario=True)
        relacionados = Post.objects.filter(categoria_post=post.categoria_post).order_by("-id")
        contexto['comentarios'] = comentarios
        contexto['relacionados'] = relacionados[:3]
        return contexto


    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post

        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user

        comentario.save()
        messages.success(self.request, "Comentário enviado para avaliação", extra_tags="alert-success")
        return redirect("post_detalhes", pk=post.pk)