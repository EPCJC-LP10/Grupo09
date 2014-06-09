# -*- coding: iso8859-1 -*-
"""
Created on Fri May 30 11:26:19 2014

@author: i13129
"""

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de Clientes"
    print "   2. Gestão de Veiculos"
    print "   3. Gestão de Serviços"
    print "   4. Registar Serviço"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Opção: ")
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

    op = raw_input("Opção: ")
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

    op = raw_input("Opção: ")
    return op
    
def gestao_servicos():
    print
    print " *** Menu Serviço **** "
    print
    print "1. Inserir novo Serviço"
    print "2. Listar todos Serviços"
    print "3. Pesquisar Serviço"
    print "4. Alterar dados de um Serviço"
    print "5. Eliminar Serviço"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op
    
def registar_servicos():
    print
    print " *** Menu Serviço **** "
    print
    print "1. Inserir novo Serviço"
    print "2. Listar todos Serviços"
    print "3. Pesquisar Serviço"
    print "4. Alterar dados de um Serviço"
    print "5. Eliminar Serviço"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op
    



if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"