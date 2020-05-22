import re

from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
# Create your views here.
from blog.models import Post

import markdown


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):

    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
                                'markdown.extensions.extra',
                                'markdown.extensions.codehilite',
                                # 记得在顶部引入 TocExtension 和 slugify
                                TocExtension(slugify=slugify),
    ])

    post.body = md.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    # post.toc = md.toc
    return render(request, 'blog/detail.html', context={'post': post})


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})