from django.urls import path
from . import views

# przestrzeń nazw
app_name = "blog"
urlpatterns = [
    # linki url

    # do przestrzeni nazw dodajemy widok (funkcję) oraz nadajemy jej alias
    # path("", views.post_list, name="post_list"),

    path("", views.PostListView.as_view(), name="post_list"),
    # do przestrzeni nazwa dodajemy rok miesiąc dzień i slug, widok, alias
    path("<int:year>/<int:month>/<int:day>/<slug:post>/",
         views.post_detail, name="post_detail"),
    path("<int:post_id>/share", views.post_share, name="post_share"),
]
