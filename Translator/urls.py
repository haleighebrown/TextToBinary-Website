from django.urls import path
from .views import (TranslationListView,TranslationUpdateView,TranslationDetailView,TranslationDeleteView,TranslationCreateView,)

urlpatterns = [
    path('<int:pk/edit/', TranslationUpdateView.as_view(), name='translation_edit'),
    path('<int:pk>/', TranslationDetailView.as_view(), name='translation_detail'),
    path('int:pk>/delete/', TranslationDeleteView.as_view(), name='translation_delete'),
        path('new/', TranslationCreateView.as_view(), name='translation_new'),
    path('', TranslationListView.as_view(), name ='translation_list'),
    ]
