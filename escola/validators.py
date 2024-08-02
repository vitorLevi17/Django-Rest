import re
from validate_docbr import CPF

def cpf_invalido(n_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(n_cpf)
    return not cpf_valido


def nome_invalido(Nome):
    return not Nome.isalpha()

def celular_invalido(Celular):
    padrao = f'[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(padrao,Celular)
    return  resposta


