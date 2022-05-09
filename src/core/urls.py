from django.urls import path
from core.views import ListDefectAPI


urlpatterns = [
    path("defects/", ListDefectAPI.as_view()),
]