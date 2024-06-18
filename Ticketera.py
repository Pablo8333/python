import pickle
import sys
import os
import random

def guardar_ticket(ticket):
    numero_ticket = random.randrange(1000, 9999)
    nombre_archivo = f"respaldo_{numero_ticket}.bin"
    with open(nombre_archivo, "wb") as f:
        pickle.dump(ticket, f)
    return numero_ticket

def abrir_ticket(numero):
    nombre_archivo = f"respaldo_{numero}.bin"
    if os.path.isfile(nombre_archivo):
        with open(nombre_archivo, "rb") as f:
            return pickle.load(f)
    else:
        print("Ticket no encontrado.")
        return None

def alta_ticket():
    while True:
        nombre = input("Ingresá tu nombre: ")
        sector = input("Ingresá tu sector: ")
        asunto = input("Ingresá el asunto: ")
        problema = input("Describí el problema: ")
        ticket = {'nombre': nombre, 'sector': sector, 'asunto': asunto, 'problema': problema}
        numero_ticket = guardar_ticket(ticket)
        print(f"Ticket N° {numero_ticket} generado. Por favor, recordá tu número de ticket.")
        if input("¿Querés crear otro ticket? (s/n): ").lower() != 's':
            break

def leer_ticket():
    while True:
        numero = input("Ingresá el número de ticket: ")
        ticket = abrir_ticket(numero)
        if ticket:
            for key, value in ticket.items():
                print(f"{key.capitalize()}: {value}")
        if input("¿Querés leer otro ticket? (s/n): ").lower() != 's':
            break

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n1. Alta Ticket\n2. Leer Ticket\n3. Salir")
        opcion = input("Seleccioná una opción: ")
        if opcion == '1':
            alta_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            if input("¿Estás seguro que querés salir? (s/n): ").lower() == 's':
                sys.exit()
        else:
            print("Opción no válida.")

menu()
