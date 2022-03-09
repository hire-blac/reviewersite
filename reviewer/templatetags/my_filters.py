from django.template import Library

register = Library()

@register.filter(name='stars')
def stars(num):
    return range(num)

@register.filter(name='length')
def length(follow):
    return len(follow)

@register.filter(name='_count')
def _count(elements):
    if elements == 0:
        return ''
    elif elements >= 1000000:
        count = elements / 1000000
        return f'{count:.2f}M'
    elif elements >= 1000:
        count = elements / 1000
        return f'{count:.2f}K'
    else:
        return f'{elements}'
        
@register.filter(name='review_stats')
def length(reviews):
    print(reviews)
    stats = {'5 stars':0, '4 stars':0, '3 stars':0, '2 stars':0, '1 star':0}
    if reviews:
        for review in reviews:
            if review.rating == 1:
                stats['1 star'] += 1
            elif review.rating == 2:
                stats['2 stars'] += 1 
            elif review.rating == 3:
                stats['3 stars'] += 1 
            elif review.rating == 4:
                stats['4 stars'] += 1 
            elif review.rating == 5:
                stats['5 stars'] += 1

    return stats.items()