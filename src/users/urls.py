from django.urls import path
from users.views import CreateUserAPI


urlpatterns = [
    path("signup", CreateUserAPI.as_view()),
]