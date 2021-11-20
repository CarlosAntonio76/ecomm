from django import template
import datetime

register = template.Library()

data_e_hora_atuais = datetime.datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")


@register.simple_tag
def tempo_atual():
    return data_e_hora_em_texto
