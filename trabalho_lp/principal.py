# -*- coding: iso8859-1 -*-
"""
Created on Fri May 30 11:27:00 2014

@author: i13129
"""


import menu
import clientes
import veiculos
import gestao_servicos
import util
import registar_servicos


# nome dos ficheiros
fxClientes = "fxclientes.dat"
fxVeiculos = "fxveiculos.dat"
fxgestao_servicos = "fxgestao_servicos.dat"
fxregistar_servicos="fxregistar_servicos.dat"

def ler_ficheiros():
	# adicionar todos ficheiros a ler
    clientes.listaClientes = util.ler_ficheiro(fxClientes)
    veiculos.listaVeiculos = util.ler_ficheiro(fxVeiculos)
    gestao_servicos.listaServicos = util.ler_ficheiro(fxgestao_servicos)
    registar_servicos.listaServicos = util.ler_ficheiro(fxregistar_servicos)    


def escrever_ficheiros():
	# adicionar todos ficheiros a guardar
    util.escrever_ficheiro(fxClientes, clientes.listaClientes)
    util.escrever_ficheiro(fxVeiculos, veiculos.listaVeiculos)
    util.escrever_ficheiro(fxgestao_servicos, gestao_servicos.listaServicos)
    util.escrever_ficheiro(fxregistar_servicos, registar_servicos.listaServicos)
 

# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        clientes.gerir()
    elif op == '2':
        veiculos.gerir()
    elif op == '3':
        gestao_servicos.gerir()
    elif op == '4':
        registar_servicos.gerir()
    elif op == '0':
        terminar = True


escrever_ficheiros()