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
       
@register.filter(name='comment_count')
def vote_count(review):
    comment_count = review.count()
    if comment_count == 0:
        return ''
    elif comment_count >= 1000000:
        count = comment_count / 1000000
        return f'{count:.2f}M'
    elif comment_count >= 1000:
        count = comment_count / 1000
        return f'{count:.2f}K'
    else:
        return f'{comment_count}'
        
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