# -*- coding: iso8859-1 -*-
"""
Created on Mon Jun 02 09:21:18 2014

@author: i13129
"""

from collections import namedtuple

import menu


clienteReg = namedtuple("clienteReg", "id, nome")
listaClientes = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaClientes)):
        if listaClientes[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_cliente():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    
    registo = clienteReg(cod, nome)
    listaClientes.append(registo)


def pesquisar_cliente():
    cod = input("Qual o codigo do cliente a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe cliente com esse código"
        return

    print "Código: ", listaClientes[pos].id
    print "Nome: ", listaClientes[pos].nome
    


def listar_cliente():
    for i in range (len(listaCLientes)):
        print "Código: ", listaClientes[i].id
        print "Nome: ", listaClientes[i].nome
        
  

def eliminar_cliente():
    cod = input ("Código do Cliente a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe Cliente com esse código"
        return

    # TODO: Confirmar eliminação
    listaClientes.pop(pos)


    
def alterar_cliente():
    cod = input ("Código do cliente a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe cliente com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    listaClientes[pos] = listaClientes[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.clientes()

        if op == '1':
            inserir_cliente()
        elif op =='2':
            listar_cliente()
        elif op == '3':
            pesquisar_cliente()
        elif op == '4':
            alterar_cliente()
        elif op == '5':
            eliminar_cliente()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"