# -*- coding: iso8859-1 -*-
"""
Created on Mon Jun 02 09:49:41 2014

@author: i13129
"""

from collections import namedtuple

import menu


servicoReg = namedtuple("servicoReg", "id, servico, preco")
listaServicos = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaServicos)):
        if listaServicos[i].id == codigo:
            pos = i
            break
                            
    return pos


def registar_servico():
    cod = raw_input("Qual o codigo cliente ? ")
    
        
    

    pos = encontrar_posicao(cod)
    print pos

    if pos == -1:
        print "Não existe esse cliente"
        return

    #ler dados
    servico = raw_input("Qual o servico? ")
    preco = raw_input("Qual o preço?")
    registo = servicoReg(cod, servico, preco)
    listaServicos.append(registo)


def pesquisar_servico():
    cod = raw_input("Qual o codigo do serviço a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe serviço com esse código"
        return

    print "Código: ", listaServicos[pos].id
    print "Serviço: ", listaServicos[pos].servico
    print "Preço: ", listaServicos[pos].preco


def listar_servico():
    for i in range (len(listaServicos)):
        print "Código: ", listaServicos[i].id
        print "Serviço: ", listaServicos[i].servico
        print "Preço: ", listaServicos[i].preco
  

def eliminar_servico():
    cod = raw_input ("Código do Serviço a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe Serviço com esse código"
        return

    # TODO: Confirmar eliminação
    listaServicos.pop(pos)


    
def alterar_servico():
    cod = raw_input ("Código do Serviço a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe Serviço com esse código"
        return

    # só altera o nome
    novoservico = raw_input("Qual o Serviço? ")
    listaServicos[pos] = listaServicos[pos]._replace(servico=novoservico)
    novopreco = raw_input("Qual o preço? ")
    listaServicos[pos] = listaServicos[pos]._replace(preco=novopreco)
    


        

def gerir():

    terminar = False

    while not terminar:
        op = menu.servicos()

        if op == '1':
            registar_servico()
        elif op =='2':
            listar_servico()
        elif op == '3':
            pesquisar_servico()
        elif op == '4':
            alterar_servico()
        elif op == '5':
            eliminar_servico()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"