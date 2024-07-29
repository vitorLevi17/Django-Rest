from django.db import models
from django.core.validators import MinLengthValidator

class Estudantes(models.Model):

    Nome = models.CharField(max_length=100)
    Email = models.EmailField(blank=False, max_length=50)
    CPF = models.CharField(blank=False, max_length=11,unique=True)
    Data_Nascimento = models.DateTimeField(blank=False)
    Celular = models.CharField(blank=False,max_length=14)

    def __str__(self):
        return self.Nome

class Curso(models.Model):

    NIVEL = (
        ('B','BASICO'),
        ('I', 'INTERMEDIARIO'),
        ('A', 'AVANCADO'),
    )

    id_curso = models.CharField(max_length=10,unique=True,validators=[MinLengthValidator(3)])
    Descricao = models.CharField(blank=False,max_length=100)
    Nivel = models.CharField(max_length=1,choices=NIVEL,blank=False,null=False,default='B')

    def __str__(self):
        return self.id_curso

class Matricula(models.Model):
    PERIODO = (
        ('M','MATUTINO'),
        ('V', 'VESPERTINO'),
        ('N', 'NOTURNO'),
    )

    id_estudante = models.ForeignKey(Estudantes,on_delete=models.CASCADE)
    id_curs = models.ForeignKey(Curso,on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1,choices=PERIODO,blank=False,default='M')