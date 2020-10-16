from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Translation

class TranslationListView(ListView):
    model = Translation
    template_name = 'translation_list.html'

class TranslationDetailView(DetailView):
    model = Translation
    template_name = 'translation_detail.html'

class TranslationUpdateView(UpdateView):
    model = Translation
    fields = ('title', 'body',)
    template_name = 'translation_edit.html'

class TranslationDeleteView(DeleteView):
    model = Translation
    template_name = 'translation_delete.html'
    success_url = reverse_lazy('article_list')

class TranslationCreateView(CreateView):
    model = Translation
    template_name = 'translation_new.html'
    fields = ('title', 'body', 'author',)
