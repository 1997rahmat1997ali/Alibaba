from django.urls import path
from . import views


urlpatterns=[
            path('new',views.new),
            path('',views.signupin),
            path('sig',views.sig),
            path('log_in',views.log_in),
            ]