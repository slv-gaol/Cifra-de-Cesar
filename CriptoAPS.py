'''Parte 2 do trabalho de Criptografia APS Herbet
            VERSÃO 1.0 '''


#Importar biblioteca

import cryptography

#variaveis

menu = ""
chave = ""
cripto =""

#Menu de escolha
menu = input('Digite: \n0 se você quer criptografar \n1 se você quer descriptografar\n')

#Criptografar
if (menu == '0'):
    chave = input ('Digite o valor que você deseja criptografar: ')

#descriptografar
elif (menu == '1'):
    chave = input ('Digite o valor que você deseja descriptografar: ')

    
#opção invalida
elif (menu != '0' and menu != '1'):
    print ('opção invalida, tente novamente')

#Mostrar dados
