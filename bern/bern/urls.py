from django.urls import path,re_path

from . import views
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]
