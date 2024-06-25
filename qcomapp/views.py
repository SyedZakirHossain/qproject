from django.shortcuts import render, get_object_or_404
from .models import Translator, Sura, Verse

def home(request):
    suras = Sura.objects.all()
    return render(request, 'home.html', {'suras': suras})

def sura_view(request, sura_number):
    sura = get_object_or_404(Sura, number=sura_number)
    translator = get_object_or_404(Translator, name='মাওলানা মিরাজ রহমান')
    verses = Verse.objects.filter(sura=sura, translator=translator)
    return render(request, 'sura.html', {'sura': sura, 'verses': verses})




def compare_verses(request, sura_number, verse_number):
    sura = get_object_or_404(Sura, number=sura_number)
    translator = get_object_or_404(Translator, name='মাওলানা মিরাজ রহমান')
    verses = Verse.objects.filter(sura=sura, number=verse_number)
    return render(request, 'compare.html', {'sura': sura, 'verses': verses,'translator':translator})
