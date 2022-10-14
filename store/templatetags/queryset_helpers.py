from django import template

from base.models import Customer
register = template.Library()


@register.filter("liked")
def contains_check(queryset, customer: Customer):
    if not isinstance(customer, Customer):
        return False
    return queryset.contains(customer)
