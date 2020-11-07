from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    success_url = reverse_lazy('login')
    form_class = CustomUserCreationForm
    template_name ='signup.html'
    
