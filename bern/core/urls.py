from django.urls import path
from core import views

urlpatterns = [
    path("search/", views.livingoption_search, name="livingoption_search"),
    path("set-language/", views.set_ui_language, name="set_ui_language"),
    path("track-click/", views.track_click, name="track_click"),
]
