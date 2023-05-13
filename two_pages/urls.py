from django.urls import path
from .views import HomePageView 
from .views import MondongoPageView

urlpatterns = [
    path("", HomePageView.as_view(), name = "home"),
    path("mondongo/", MondongoPageView.as_view(), name = "mondongo")
]