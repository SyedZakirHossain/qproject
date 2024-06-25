
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sura/<int:sura_number>/', views.sura_view, name='sura_view'),
    path('compare/<int:sura_number>/<int:verse_number>/', views.compare_verses, name='compare_verses'),
]

 



