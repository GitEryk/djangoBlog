from django import template
from blog.models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()
@register.inclusion_tag("blog/post/tag_bar.html")
def get_all_tags():
    tags = Post.tags.all().values_list("name", flat=True)
    return {"tags": tags}

@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by("-publish")[:count]
    return {"latest_posts": latest_posts}

@register.inclusion_tag("blog/post/comments_posts.html")
def show_comments_posts(count=5):
    comments_posts = Post.published.annotate(total_comments=Count("comments")
                                   ).order_by("-total_comments")[:count]
    return {"comments_posts":  comments_posts}

@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
