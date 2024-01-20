from django.urls import path
from . import views
from .feeds import LatestPostsFeed

# przestrzeń nazw
app_name = "blog"
urlpatterns = [
    # linki url

    # do przestrzeni nazw dodajemy widok (funkcję) oraz nadajemy jej alias
    path("", views.post_list, name="post_list"),
    # url do szukania postów tylko z danym tagiem
    path("tag/<slug:tag_slug>/", views.post_list, name="post_list_by_tag"),
    # url dla listy postów
    # path("", views.PostListView.as_view(), name="post_list"),
    # do przestrzeni nazwa dodajemy rok miesiąc dzień i slug, widok, alias
    # url dla szczegółów posta
    path("<int:year>/<int:month>/<int:day>/<slug:post>/",
         views.post_detail, name="post_detail"),
    # url dla formularza udostępniania posta
    path("<int:post_id>/share", views.post_share, name="post_share"),
    # ulr dla formularza komentowania
    path("<int:post_id>/comment/", views.post_comment, name="post_comment"),
    path("feed/", LatestPostsFeed(), name="post_feed"),

]
