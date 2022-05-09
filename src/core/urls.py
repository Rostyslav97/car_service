from django.urls import path
from core.views import ListDefectAPI, RetrieveDefectAPI, CreateDefectAPI, UpdateDefectAPI, DestroyDefectAPI


urlpatterns = [
    path("defects/", ListDefectAPI.as_view()),
    path("defects/<int:id>/", RetrieveDefectAPI.as_view()),
    path("defects/create/", CreateDefectAPI.as_view()),
    path("defects/update/<int:id>/", UpdateDefectAPI.as_view()),
    path("defects/destroy/<int:id>/", DestroyDefectAPI.as_view())
]