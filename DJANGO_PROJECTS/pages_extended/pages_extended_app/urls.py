from django.urls import path
from pages_extended_app.views import BooksPageView, ContactPageView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('books/', BooksPageView.as_view(), name='books'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
