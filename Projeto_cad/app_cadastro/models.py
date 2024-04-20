from django.db import models
     

class usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'usuarios'
