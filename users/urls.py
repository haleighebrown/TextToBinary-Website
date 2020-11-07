from django.urls import path
from .views import SignUpView
from django.urls import reverse_lazy

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup')]
