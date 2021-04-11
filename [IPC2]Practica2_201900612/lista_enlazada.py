class contacto:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono


class node:
    def __init__(self, contacto=None, next=None, previous=None):
        self.contacto = contacto 
        self.previous = previous
        self.next = next

from typing import Text
from graphviz import Digraph
class double_linked_list:
    def __init__(self, head=None):
        self.head = head
        self.last = head
        self.size = 0

    def insertar(self, contacto):
        if self.size == 0:
            self.head = node(contacto=contacto)
            self.last = self.head
        else:
            new_node = node(contacto=contacto, next=self.head)
            self.head.previous = new_node
            self.head = new_node
        self.size += 1

    def imprimir(self):
        if self.head is None:
            return
        node = self.head
        print(node.contacto.nombre, end = " => ")
        while node.next:
            node = node.next
            print(node.contacto.nombre, end = " => ")
        print()

    def eliminar(self, nombre):
        node = self.head
        while node is not None:
            if node.contacto.nombre == nombre:
                if node.next:
                    node.previous.next = node.next
                    node.next.previous = node.previous
                else:
                    node.previous.next = None
                    node.next.previous = self.head
                self.size += 1
                return True
            else:
                node = node.next
            return False

    def buscar_numero(self, num):
        mensaje = 'ERROR'
        mensaje_2 = 'SUCCESS'
        current = self.head
        while current != None:
            if current.contacto.telefono == num:
                return mensaje
            current = current.next
        return mensaje_2

    def devolver_nombre(self, num):
        mensaje = 'ERROR'
        mensaje_2 = 'SUCCESS'
        current = self.head
        while current != None:
            if current.contacto.telefono == num:
                return current.contacto.nombre 
            current = current.next
        return mensaje_2

    def devolver_numero(self, num):
        mensaje = 'ERROR'
        mensaje_2 = 'SUCCESS'
        current = self.head
        while current != None:
            if current.contacto.telefono == num:
                return current.contacto.telefono
            current = current.next
        return mensaje_2

    def devolver_apellido(self, num):
        mensaje = 'ERROR'
        mensaje_2 = 'SUCCESS'
        current = self.head
        while current != None:
            if current.contacto.telefono == num:
                return current.contacto.apellido
            current = current.next
        return mensaje_2

    def visualizarGraphviz(self):
        gra = Digraph(edge_attr={'shape': 'box'})
        if self.head is None:
            return
        node = self.head
        gra.node(node.contacto.nombre)
        while node.next:
            node = node.next
            gra.edge(node.contacto.nombre , node.previous.contacto.nombre, dir='both')
        gra.render('h.png', view=True)
            
        

