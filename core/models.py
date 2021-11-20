from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User

ESTADO_UF = (
    ("MG", "Minas Gerais"),
    ("RJ", "Rio de Janeiro"),
    ("SP", "São Paulo"),
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AM", "Amazonas"),
    ("AP", "Amapa"),
    ("BA", "Bahia"),
    ("DF", "Distrito Federal"),
    ("ES", "Espirito Santo"),
    ("GO", "Goias"),
    ("MA", "Maranhão"),
    ("MS", "Mato Grosso do Sul"),
    ("MT", "Mato Grosso"),
    ("PA", "Pará"),
    ("PB", "Paraiba"),
    ("PE", "Pernambuco"),
    ("PI", "Piaui"),
    ("PR", "Paraná"),
    ("RN", "Rio Grande do Norte"),
    ("RO", "Rondonia"),
    ("RR", "Roraima"),
    ("RS", "Rio Grande do Sul"),
    ("SC", "Santa Catarina"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
)

class Funcionario(models.Model):
    codfunc = models.IntegerField(
        primary_key=True, serialize=False, verbose_name='codfunc',
        default=0
    )

    nome = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )

    endereco = models.CharField(
        max_length=60,
        null=False,
        blank=False,
        default="Rua Mariquinha Maciel"
    )

    numero = models.CharField(
        max_length=8,
        null=False,
        blank=False,
        default="305/201"
    )

    bairro = models.CharField(
        max_length=60,
        null=False,
        blank=False,
        default="Santo Antonio"
    )

    cidade = models.CharField(
        max_length=60,
        null=False,
        blank=False,
        default="Vicosa"
    )

    estado = models.CharField(
        max_length=9,
        choices=ESTADO_UF,
        default="MG"
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
        )

    telefone = models.CharField(
        max_length=13,
        null=False,
        blank=False,
        default="31"
    )

    tempo_de_servico = models.IntegerField(
        default=0,
        null=False,
        blank=False
        )

    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
        )

    objetos = models.Manager()

    def __str__(self):
        return self.nome


