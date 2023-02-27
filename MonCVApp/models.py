from django.db import models

class Experience(models.Model):
    titre = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    description = models.TextField()

class Formation(models.Model):
    diplome = models.CharField(max_length=100)
    etablissement = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    description = models.TextField()

class Competence(models.Model):
    nom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=100)
