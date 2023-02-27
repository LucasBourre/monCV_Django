from django.shortcuts import render
from .models import Experience, Formation, Competence


def index(request):
    experiences = Experience.objects.all()
    formations = Formation.objects.all()
    competences = Competence.objects.all()
    return render(request, 'index.html',
                  {'experiences': experiences, 'formations': formations, 'competences': competences})
