from django.db import models

class Teste(models.Model):
    nome = models.charfield(max_lengnt=100);
