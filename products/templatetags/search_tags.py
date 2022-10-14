from django import template

from products.forms import SearchForm
register = template.Library()


@register.inclusion_tag('./components/navbar_search.html', name="search_form")
def search_form():
    return {'form': SearchForm}
