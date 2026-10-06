from model.usuario import Usuario, Tutor, Veterinario
from model.animal import Animal, Cachorro, Gato
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
            Animal.pets.append(cachorro)
            tutor_encontrado.pets.append(cachorro)
            cadastro_confirmado()
        else:
            nome_existente()

def cadastrar_gato(dados):
    tutor_encontrado = None
    for tutor in Usuario.tutores:
        if dados["tutor"] == tutor.nome:
            tutor_encontrado = tutor
            break
    if tutor_encontrado is None:
        tutor_nao_encontrado()
    else:
        nome_encontrado = None
        for pet in Animal.pets:
            if dados["nome"] == pet.nome:
                nome_encontrado = pet
                break
        if nome_encontrado is None:
            gato = Gato(dados["cor"], dados["nome"], dados["peso"], tutor_encontrado)
            Animal.gatos.append(gato)
            Animal.pets.append(gato)
            tutor_encontrado.pets.append(gato)
            cadastro_confirmado()
        else:
            nome_existente()


def listar_tutores():
    lista = ""
    if len(Usuario.tutores) > 0:
        for tutor in Usuario.tutores:
            lista += f"\n\nNome: {tutor.nome}\nCPF: {tutor.cpf}\nPets: "
            if len(tutor.pets) > 0:
                for pet in tutor.pets:
                    lista += f"{pet.nome}; "
            else:
                lista += "Sem pets."
    else:
        lista += "Sem tutores cadastrados."
    return lista

def listar_pets():
    lista = ""
    lista += "Cachorro: \n"
    if len(Animal.cachorros) > 0:
        for cachorro in Animal.cachorros:
            lista += f"Nome: {cachorro.nome}\nPeso: {cachorro.peso}\nRaça: {cachorro.raca}\nCor: {cachorro.cor}\nTutor: {cachorro.tutor.nome}\n\n"
    else:
        lista += "\nSem cachorros cadastrados.\n\n"
    lista += "Gato: \n"
    if len (Animal.gatos) > 0:
        for gato in Animal.gatos:
            lista += f"Nome: {gato.nome}\nPeso: {gato.peso}\nRaça: {gato.raca}\nCor: {gato.cor}\nTutor: {gato.tutor.nome}"
    else:
        lista += "\nSem gatos cadastrados.\n\n"
    return lista

def listar_veterinarios():
    lista = ""
    lista += "Veterinários: "
    if len(Usuario.veterinarios) > 0:
        for veterinario in Usuario.veterinarios:
            lista += f"\n\nNome: {veterinario.nome}\nCPF: {veterinario.cpf}\nEspecialidade: {veterinario.especialidade}"
    else:
        lista += "Sem veterinários cadastrados."
    return lista
