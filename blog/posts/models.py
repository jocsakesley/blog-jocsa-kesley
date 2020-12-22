from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from blog.categorias.models import Categoria
from PIL import Image
from django.conf import settings
import os

class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name="Título")
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Autor")
    data_post = models.DateTimeField(default=timezone.now, verbose_name="Data")
    conteudo_post = models.TextField(verbose_name="Conteúdo")
    excerto_post = models.TextField(verbose_name="Excerto")
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="Categoria")
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', verbose_name="Imagem", blank=True, null=True)
    publicado_post = models.BooleanField(default=False, verbose_name="Publicado")

    def __str__(self):
        return self.titulo_post

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize(self.imagem_post.name, 1060)

    @staticmethod
    def resize(image,new_width):
        image_path = os.path.join(settings.MEDIA_ROOT, image)
        img = Image.open(image_path)
        width, height = img.size
        new_height = round((new_width * height) / width)

        if width <= new_width:
            img.close()
            return
        new_image = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_image.save(image_path, optimize=True, quality=60)
        new_image.close()