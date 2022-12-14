from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.get_entrypage, name="entry"),
    path("search/", views.search_entry, name="search"),
    path("new/", views.new_page, name="new"),
    path("edit/", views.edit_page, name="edit"),
    path("save/", views.save_page, name="save"),
    path("random/", views.random_page, name="random"),
]
