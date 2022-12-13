from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
# Create your models here.


class Atleta(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)
    nome = models.CharField(max_length=100, default="Atleta")
    image = models.ImageField(upload_to="images", null=True)
    esporte = models.CharField(max_length=100)
    posicao = models.CharField(max_length=100)
    altura = models.CharField(max_length=100)
    peso = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)

    is_anonymous = False
    is_authenticated = True

    objects = UserManager()

    def __str__(self):
        return self.nome


class Modalidade(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Treino(models.Model):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    linkStrava = models.CharField(max_length=200, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)

    def __str__(self):
        return self
