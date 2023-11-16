from django.urls import path

from .views import TextListView, TextDetailView, SearchResultsView

urlpatterns = [
    path('search_results/', SearchResultsView.as_view(), name='search_results'),
    path('<int:pk>/', TextDetailView.as_view(), name='text_detail'),
    path('', TextListView.as_view(), name='home'),
]
