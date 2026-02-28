from django.urls import path
from core import views

urlpatterns = [
    path("search/", views.livingoption_search, name="livingoption_search"),
    path("set-language/", views.set_ui_language, name="set_ui_language"),
    path("track-click/", views.track_click, name="track_click"),
    path("providers/<int:pk>/", views.provider_detail, name="provider_detail"),
    path("saved/", views.saved_list, name="saved_list"),
    path("providers/register/", views.provider_register, name="provider_register"),
    path("providers/register/thanks/", views.provider_register_thanks, name="provider_register_thanks"),
    path("providers/manage/", views.provider_manage_search, name="provider_manage_search"),
    path("providers/manage/<int:pk>/", views.provider_manage_request, name="provider_manage_request"),
    path("providers/magic/<str:token>/", views.provider_magic_enter, name="provider_magic_enter"),
    path("providers/edit/", views.provider_edit_me, name="provider_edit_me"),
    path("providers/options/new/", views.livingoption_create, name="livingoption_create"),
    path("providers/options/<int:pk>/edit/", views.livingoption_edit, name="livingoption_edit"),
    path("providers/options/<int:pk>/delete/", views.livingoption_delete, name="livingoption_delete"),
    path("how-it-works/", views.how_it_works, name="how_it_works"),
]
