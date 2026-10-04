from model.usuario import Usuario, Tutor, Veterinario
from model.animal import Animal, Cachorro
from view.view import *

def cadastrar_tutor(dados):
    cpf_encontrado = None
    for t in Usuario.tutores:
        if dados["cpf"] == t.cpf:
            cpf_encontrado = t.cpf
    if cpf_encontrado is None:
        tutor = Tutor(dados["nome"], dados["cpf"])
        Usuario.tutores.append(tutor)
        cadastro_confirmado()
    else:
        erro_cpf()

def cadastrar_veterinario(dados):
    cpf_encontrado = None
    for v in Usuario.veterinarios:
        if dados["cpf"] == v.cpf:
            cpf_encontrado = v.cpf
    if cpf_encontrado is None:
        veterinario = Veterinario(dados["especialidade"], dados["nome"], dados["cpf"])
        Usuario.veterinarios.append(veterinario)
        cadastro_confirmado()
    else:
        erro_cpf()

def cadastrar_cachorro(dados):
    tutor_encontrado = None
    for t in Usuario.tutores:
        if dados["tutor"] == t.cpf:
            tutor_encontrado = t
            break
    if tutor_encontrado is None:
        tutor_nao_encontrado()
    else:       
        nome_encontrado = None
        for c in Animal.cachorros:
            if dados["nome"] == c.nome:
                nome_encontrado = c.nome
        if nome_encontrado is None:
            cachorro = Cachorro(dados["raca"], dados["cor"], dados["nome"], dados["peso"], tutor_encontrado)
            Animal.cachorros.append(cachorro)
            cadastro_confirmado()
        else:
            nome_existente()
        