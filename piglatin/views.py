from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    txt = request.GET['originaltext']

    words = txt.split()

    translation = ''

    for word in words:
        if word[0] not in 'aeiouAEIOU':
            translation += word + '<-consonant '
        else:
            translation += word + '<-vowel '

    return HttpResponse(translation)