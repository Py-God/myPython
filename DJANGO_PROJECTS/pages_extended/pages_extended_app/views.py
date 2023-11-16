from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'base.html'

class BooksPageView(TemplateView):
    template_name = 'books.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'
