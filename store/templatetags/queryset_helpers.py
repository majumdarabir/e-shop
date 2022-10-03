from django import template
register = template.Library()


register.filter("liked",
                filter_func=lambda queryset, customer: queryset.contains(customer))
