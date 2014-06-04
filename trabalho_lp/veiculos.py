# -*- coding: iso8859-1 -*-
"""
Created on Fri May 30 11:22:19 2014

@author: i13129
"""



from collections import namedtuple

import menu


veiculosReg = namedtuple("veiculosReg", "id, marca,matricula")
listaVeiculos = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaVeiculos)):
        if listaVeiculos[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_veiculo():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    marca = raw_input("Qual a marca? ")
    matricula = raw_input("Qual a Matricula?")
    registo = veiculosReg(cod, marca,matricula)
    listaVeiculos.append(registo)


def pesquisar_veiculo():
    cod = input("Qual o codigo do veiculo a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe veiculo com esse código"
        return

    print "Código: ", listaVeiculos[pos].id
    print "Marca: ", listaVeiculos[pos].marca
    print "Matricula: ", listaVeiculos[pos].matricula
    


def listar_veiculo():
    for i in range (len(listaVeiculos)):
        print "Código: ", listaVeiculos[i].id
        print "Marca: ", listaVeiculos[i].marca
        print "Matricula: ", listaVeiculos[i].matricula
  

def eliminar_veiculo():
    cod = input ("Código do veiculo a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe veiculo com esse código"
        return

    # TODO: Confirmar eliminação
    listaVeiculos.pop(pos)


    
def alterar_veiculo():
    cod = input ("Código do veiculo a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe veiculo com esse código"
        return

    # só altera a marca
    novamarca = raw_input("Qual o marca? ")
    listaVeiculos[pos] = listaVeiculos[pos]._replace(marca=novamarca)
    novamatricula = raw_input("Qual a matricula? ")
    listaVeiculos[pos] = listaVeiculos[pos]._replace(matricula=novamatricula)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.veiculo()

        if op == '1':
            inserir_veiculo()
        elif op =='2':
            listar_veiculo()
        elif op == '3':
            pesquisar_veiculo()
        elif op == '4':
            alterar_veiculo()
        elif op == '5':
            eliminar_veiculo()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"
