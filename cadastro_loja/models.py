from django.db import models

# Create your models here.
class TBPessoa(models.Model):
    nome = models.CharField(max_length=180)
    celular = models.CharField(max_length=12)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=180)
    bairro = models.CharField(max_length=120)
    cep = models.CharField(max_length=8)
    referencia = models.CharField(max_length=120)
    email = models.EmailField()
    
    def __str__(self):
        return self.name