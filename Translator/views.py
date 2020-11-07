from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Translation

class TranslationListView(ListView):
    model = Translation
    template_name = 'translation_list.html'
    login_url = 'login'

class TranslationDetailView(DetailView):
    model = Translation
    template_name = 'translation_detail.html'
    login_url = 'login'

class TranslationUpdateView(UpdateView):
    model = Translation
    fields = ('title', 'body',)
    template_name = 'translation_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TranslationDeleteView(DeleteView):
    success_url = reverse_lazy('translation_list')
    model = Translation
    template_name = 'translation_delete.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class TranslationCreateView(CreateView):
    success_url = reverse_lazy('translation_list')
    model = Translation
    template_name = 'translation_new.html'
    fields = ('title', 'body', 'author')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def from_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
