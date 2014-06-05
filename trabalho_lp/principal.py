# -*- coding: iso8859-1 -*-
"""
Created on Fri May 30 11:27:00 2014

@author: i13129
"""


import menu
import clientes
import veiculos
import servicos
import util


# nome dos ficheiros
fxClientes = "fxclientes.dat"
fxVeiculos = "fxveiculos.dat"
fxServicos = "fxservicos.dat"

def ler_ficheiros():
	# adicionar todos ficheiros a ler
    clientes.listaClientes = util.ler_ficheiro(fxClientes)
    veiculos.listaVeiculos = util.ler_ficheiro(fxVeiculos)
    servicos.listaServicos = util.ler_ficheiro(fxServicos)



def escrever_ficheiros():
	# adicionar todos ficheiros a guardar
    util.escrever_ficheiro(fxClientes, clientes.listaClientes)
    util.escrever_ficheiro(fxVeiculos, veiculos.listaVeiculos)
    util.escrever_ficheiro(fxServicos, servicos.listaServicos)
 

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
        servicos.registar_servico()
    elif op == '0':
        terminar = True


escrever_ficheiros()