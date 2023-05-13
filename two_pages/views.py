from django.shortcuts import render
from django.views.generic import TemplateView 
# Create your views here my friend.

class HomePageView(TemplateView):
    template_name = "home.html"

class MondongoPageView(TemplateView):
    template_name = "mondongo.html"
