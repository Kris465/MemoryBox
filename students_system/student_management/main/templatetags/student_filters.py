from django import template

register = template.Library()


@register.filter
def filter_schedule(queryset, day):
    return queryset.filter(day=day)


@register.filter
def filter_time(queryset, time):
    return queryset.filter(start_time=time)
