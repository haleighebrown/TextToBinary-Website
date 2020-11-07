from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Translation


class TranslationListView(LoginRequiredMixin, ListView):
    model = Translation
    template_name = 'translation_list.html'
    login_url = 'login'

class TranslationDetailView(LoginRequiredMixin, DetailView):
    model = Translation
    template_name = 'translation_detail.html'
    login_url = 'login'

class TranslationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Translation
    fields = ('title', 'chioce', 'Input')
    template_name = 'translation_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TranslationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    success_url = reverse_lazy('translation_list')
    model = Translation
    template_name = 'translation_delete.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class TranslationCreateView(LoginRequiredMixin, CreateView):
    model = Translation
    template_name = 'translation_new.html'
    fields = ('title', 'choice', 'Input')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
