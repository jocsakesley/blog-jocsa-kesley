from django.urls import path
from .views import SobreIndex

urlpatterns = [
    path("", SobreIndex.as_view(), name="sobre_index")
]