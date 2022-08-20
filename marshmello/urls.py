from django.urls import path
from .views import MarshmelloList, MarshmelloDetail

urlpatterns = [
    path("", MarshmelloList.as_view(), name="marshmello_list"),
    path("<int:pk>/", MarshmelloDetail.as_view(), name="marshmello_detail"),
]
