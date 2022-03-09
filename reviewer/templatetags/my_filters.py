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
    total_review = reviews.count()
    star_counts = {'1 star': 0, '2 stars': 0, '3 stars': 0, '4 stars': 0, '5 stars': 0}
    stats = {'5 stars':0, '4 stars':0, '3 stars':0, '2 stars':0, '1 star':0}
    if reviews:
        for review in reviews:
            if review.rating == 1:
                star_counts['1 star'] += 1
            elif review.rating == 2:
                star_counts['2 stars'] += 1 
            elif review.rating == 3:
                star_counts['3 stars'] += 1 
            elif review.rating == 4:
                star_counts['4 stars'] += 1 
            elif review.rating == 5:
                star_counts['5 stars'] += 1
    for k, v in star_counts.items():
        percentage = (v / total_review) * 100
        stats[k] = str(percentage)
    return stats.items()