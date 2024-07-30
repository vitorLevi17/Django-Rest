def cpf_invalido(CPF):
    return len(CPF) != 11

def nome_invalido(Nome):
    return not Nome.isalpha()

def celular_invalido(Celular):
    return len(Celular) !=13


