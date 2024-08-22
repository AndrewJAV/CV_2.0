from django.shortcuts import render
from .models import *

def showData(request):

    person = Person.objects.first()
    languages = Language.objects.all()
    aptitudes = Aptitude.objects.all()
    skills = Skill.objects.all()
    education = Education.objects.all()

    context = {
        'person':person,
        'languages':languages,
        'aptitudes':aptitudes,
        'skills':skills,
        'education':education,
    }

    return render(request, 'CV.html', context)
# Create your views here.
