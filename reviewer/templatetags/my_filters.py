from django.template import Library

register = Library()

@register.filter(name='stars')
def stars(num):
    return range(num)