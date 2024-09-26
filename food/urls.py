from django.urls import re_path

from .views import index, add_meal, update_meal, login, view_meal

urlpatterns = [
    re_path(r'^$', login, name='login'),
    re_path(r'^index$', index, name='index'),
    re_path(r'^add_meal$', add_meal, name='add-meal'),
    re_path(r'^update_meal/(?P<meal_id>\d+)$', update_meal, name='update-meal'),
    re_path(r'^view_meal/(?P<meal_id>\d+)$', view_meal, name='view-meal'),

]
