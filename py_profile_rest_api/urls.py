from django.urls import path

from py_profile_rest_api import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
