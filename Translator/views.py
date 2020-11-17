from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Translation
from django.http import HttpResponse
from .translator import encode_binary_string, decode_binary_string
from django.http import HttpResponseRedirect



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
    fields = ('title', 'choice', 'Input')
    template_name = 'translation_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
    def form_valid(self, form):
        form.instance.author = self.request.user

        if (self.request.POST['choice'] == 'Text to Binary'):
            form.instance.Output = encode_binary_string(self.request.POST['Input'])
        else:
            binary = True
            for i in range (len(self.request.POST['Input'])):
                if self.request.POST['Input'][i] != '0' and self.request.POST['Input'][i] != '1' and self.request.POST['Input'][i] != ' ':
                    binary = False
                    
            if (self.request.POST['Input'].replace(" ","")).isdigit() and binary == True:
                form.instance.Output = decode_binary_string(self.request.POST['Input'])
            else:
                form.instance.Output =  "Please input proper Binary with correct spacing for translation into Text"
        return super().form_valid(form)



class TranslationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    success_url = reverse_lazy('translation_list')
    model = Translation
    template_name = 'translation_delete.html'
    login_url = 'login'
    
    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            object = self.get_object()
            url = object.get_absolute_url()
            return HttpResponseRedirect(url)
        else:
            return super(TranslationDeleteView, self).post(request, *args, **kwargs)
        
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

        if (self.request.POST['choice'] == 'Text to Binary'):
            form.instance.Output = encode_binary_string(self.request.POST['Input'])
        else:
            binary = True
            for i in range (len(self.request.POST['Input'])):
                if self.request.POST['Input'][i] != '0' and self.request.POST['Input'][i] != '1' and self.request.POST['Input'][i] != ' ':
                    binary = False

            if (self.request.POST['Input'].replace(" ","")).isdigit() and binary == True:
                form.instance.Output = decode_binary_string(self.request.POST['Input'])
            else:
                form.instance.Output =  "Please input proper Binary with correct spacing for translation into Text"
        return super().form_valid(form)


    
