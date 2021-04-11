from graphviz.dot import Graph
from lista_enlazada import double_linked_list, contacto
import os
from graphviz import Digraph

lista_contactos = double_linked_list()

def Menu():
    #os.system('clear')
    print('**************** Bienvenido ****************')
    print('********* Pedro Castro, 201900612 *********')
    print()
    print('1. Crear nuevo contacto')
    print('2. Buscar contacto')
    print('3. Ver agenda de contactos')
    print('4. Salir')
    print()
  
def crearContacto():
    nom_contacto = ''
    ape_contacto = ''
    num_contacto = 0

    nom_contacto = input('Ingrese el nombre: ')
    ape_contacto = input('Ingrese el apellido: ')
    num_contacto = input('Ingrese el número de teléfono: ')
    print()

    buscar = lista_contactos.buscar_numero(num_contacto)

    if buscar == 'ERROR':
        print('ERROR: El contacto ya existe.')
    elif buscar == 'SUCCESS':
            lista_contactos.insertar(contacto(nom_contacto,ape_contacto,num_contacto))
            print('¡El contacto se ha agregado exitosamente!')
            print()
    else:
        pass

    print()

def buscarContacto():
    num_a_buscar = input('Ingrese el número a buscar: ')
    print()
    mensaje = lista_contactos.buscar_numero(num_a_buscar)

    if mensaje == 'SUCCESS':
        entrada = input('El número de teléfono no existe ¿Desea agregarlo? si es así, presione s, sino, presione cualquier tecla para salir')
        if entrada == 's':
            nom_contacto = input('Ingrese el nombre: ')
            ape_contacto = input('Ingrese el apellido: ')
            lista_contactos.insertar(contacto(nom_contacto,ape_contacto,num_a_buscar))
            print('¡El contacto se ha agregado exitosamente!')
    elif mensaje == 'ERROR':
        print('Nombre: ', lista_contactos.devolver_nombre(num_a_buscar))
        print('Apellido: ', lista_contactos.devolver_apellido(num_a_buscar))
        print('Número de teléfono: ', lista_contactos.devolver_numero(num_a_buscar))
        print()
    
def verAgenda():
    lista_contactos.visualizarGraphviz()

def Salir():
    pass

while True:
    Menu()

    opcion = input('Ingrese la opción deseada: ')
    print()

    if opcion == "1":
        crearContacto()
    elif opcion == "2":
        buscarContacto()
    elif opcion == "3":
        verAgenda()
    elif opcion == "4":
        break
    else:
        print('No se ingresó una opción válida.')



