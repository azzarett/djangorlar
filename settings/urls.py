# Django modules
from django.contrib import admin
from django.urls import path

# Project modules
from apps.tasks.views import hello_view
from apps.tasks.views import home_view
from apps.tasks.views import users_view
from apps.tasks.views import city_time_view
from apps.tasks.views import crn_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path(route="hello/", view=hello_view, name="hello-view"),
    path(route="users/", view=users_view, name="users-view"),
    path(route="city-time/", view=city_time_view, name="city-time-view"),
    path(route="crn/", view=crn_view, name="crn-view"),
]