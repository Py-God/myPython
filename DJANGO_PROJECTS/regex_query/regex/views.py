from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Text

class TextListView(ListView):
    model = Text
    template_name = 'home.html'

class TextDetailView(DetailView):
    model = Text
    template_name = 'text_detail.html'

class SearchResultsView(ListView):
    model = Text
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Text.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
            )
        return object_list