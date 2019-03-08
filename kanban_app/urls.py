from django.urls import path

from .views import *

urlpatterns = [
    path('card/', CardsView.as_view()),
    path('card/add/', AddCardView.as_view()),
    path('card/delete/', DeleteCardView.as_view()),
]
