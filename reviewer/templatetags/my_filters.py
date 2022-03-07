from django.template import Library

register = Library()

@register.filter(name='stars')
def stars(num):
    return range(num)

@register.filter(name='length')
def length(follow):
    return len(follow)

@register.filter(name='vote_count')
def vote_count(votes):
    if votes == 0:
        return ''
    elif votes >= 1000000:
        count = votes / 1000000
        return f'{count:.2f}M'
    elif votes >= 1000:
        count = votes / 1000
        return f'{count:.2f}K'
    else:
        return f'{votes}'
        
