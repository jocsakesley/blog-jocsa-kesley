from django import template

register = template.Library()

@register.filter(name='check_comentarios')
def check_comentarios(valor):
    try:
        valor = int(valor)
        if valor == 0:
            result = "Nenhum comentário"
        elif valor == 1:
            result = f"{valor} comentário"
        else:
            result = f"{valor} comentários"
    except:
        result = "Erro!"
    return result