from django import template

from .. import models

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=3):
    return {
        'recent_post_list': models.Post.objects.all().order_by('-created_time')[:num]
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': models.Post.objects.dates('created_time', 'month', order='DESC')
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': models.Category.objects.all(),
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': models.Tag.objects.all(),
    }
