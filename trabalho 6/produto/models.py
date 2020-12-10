from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=70, db_index=True, unique=True)

    class Meta:
        db_table='categoria'
        ordering = ('nome',)


    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.nome