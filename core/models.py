from django.db import models


class Product(models.Model):
    nome = models.CharField(max_length=256)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=12, decimal_places=2)