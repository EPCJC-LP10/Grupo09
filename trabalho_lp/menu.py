# -*- coding: iso8859-1 -*-
"""
Created on Fri May 30 11:26:19 2014

@author: i13129
"""

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gest�o de Clientes"
    print "   2. Gest�o de Veiculos"
    print "   3. Gest�o de Servi�os"
    print "   4. Registar Servi�o"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Op��o: ")
    return op


def clientes():
    print
    print " *** Menu Clientes **** "
    print
    print "1. Inserir novo cliente"
    print "2. Listar todos clientes"
    print "3. Pesquisar cliente"
    print "4. Alterar dados de um cliente"
    print "5. Eliminar cliente"
    print 
    print "0. Menu Anterior"

    op = raw_input("Op��o: ")
    return op
    
def veiculos():
    print
    print " *** Menu Veiculos **** "
    print
    print "1. Inserir novo veiculo"
    print "2. Listar todos veiculos"
    print "3. Pesquisar veiculo"
    print "4. Alterar dados de um veiculo"
    print "5. Eliminar veiculo"
    print 
    print "0. Menu Anterior"

    op = raw_input("Op��o: ")
    return op
    
def gestao_servicos():
    print
    print " *** Menu Servi�o **** "
    print
    print "1. Inserir novo Servi�o"
    print "2. Listar todos Servi�os"
    print "3. Pesquisar Servi�o"
    print "4. Alterar dados de um Servi�o"
    print "5. Eliminar Servi�o"
    print 
    print "0. Menu Anterior"

    op = raw_input("Op��o: ")
    return op
    
def registar_servicos():
    print
    print " *** Menu Servi�o **** "
    print
    print "1. Inserir novo Servi�o"
    print "2. Listar todos Servi�os"
    print "3. Pesquisar Servi�o"
    print "4. Alterar dados de um Servi�o"
    print "5. Eliminar Servi�o"
    print 
    print "0. Menu Anterior"

    op = raw_input("Op��o: ")
    return op
    



if __name__ == "__main__":
    print "Este programa n�o deve ser executado diretamente"