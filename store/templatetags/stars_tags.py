from django import template

register = template.Library()


register.filter(name='check_star',
                filter_func=lambda rate, check: int(rate) >= int(check), is_safe=True)
