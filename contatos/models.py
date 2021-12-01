from django.db import models

# Create your models here.

class Contato(models.Model):
    """docstring for Contato."""

    def __init__(self, arg):
        super(Contato, self).__init__()
        self.arg = arg
    nome = models.Charfield(max_lengh=255)    


# CONTATOS
# id: INT (automático)
# nome: STR * (obrigatório)
# sobrenome: STR (opcional)
# telefone: STR * (obrigatório)
# email: STR (opcional)
# data_criacao: DATETIME (automático)
# descricao: texto
# categoria: CATEGORIA (outro model)

#  CATEGORIA
#  id: INT
#  nome: STR * (obrigatório)
