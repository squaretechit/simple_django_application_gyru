from django.urls import path, include
from gyruapptheme.views import IndexView as theme


urlpatterns = [
    path('', theme.home, name='home'),
    path('about/', theme.about, name='about'),
    path('contact/', theme.contact, name='contact'),
    path('privacy-policy/', theme.policy, name='policy'),
]