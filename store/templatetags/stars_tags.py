from django import template
from django.db.models.query import QuerySet
from store.models import Review

register = template.Library()


register.filter(name='check_star',
                filter_func=lambda rate, check: int(rate) >= int(check), is_safe=True)


@register.filter(name="avg_ratings")
def average_ratings(reviews):
    if not isinstance(reviews, QuerySet[Review]):
        return 0
    if not reviews.count():
        return 0
    avg = sum([review.ratings for review in reviews])/reviews.count()
    return round(avg, 1)


@register.filter(name="avg_star_percentage")
def average_percentage_ratings(reviews):
    return average_ratings(reviews)*100


@register.filter(name="get_ratings")
def review_ratings(reviews):
    counter = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
    if not isinstance(reviews, QuerySet[Review]):
        return {}.items()
    if not reviews.count():
        return 0
    for review in reviews:
        if review.ratings:
            counter[review.ratings] += 1
    for key in counter.keys():
        counter[key] = round(counter[key] / reviews.count()*100, 2)
    return counter.items()


@register.simple_tag(name="stars")
def stars(*args, **kwags):
    return [1, 2, 3, 4, 5]
