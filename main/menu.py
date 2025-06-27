import models.classes as c
import getpass
import pwinput

Estudiantes = []

#seleccione el tipo de inicio que sección
print("Seleccione el tipo: ")
print("1. inicio de sección con contraseña visible")
print("2. Inicio de sección con contraseña oculta")
print("3. Incio de sección con usuarios y claves")
import os
import getpass

ARCHIVO = "estudiantes.txt"
CLAVE = "Blanca2025"


#Primer ejemplo
def inicio():
    print("Inicio de la sección")
    intento = input("Ingrese la clave de acceso: ")
    if intento == CLAVE:
        print("Bienvenido")
        return True
    else:
        print("Clave incorrecta,vualva a intentarlo, por favor.")
        return False

#Segundo ejemplo
def inicio():
    intento = getpass.getpass("Ingrese la clave de acceso: ")
    if intento == CLAVE:
        print("Acceso concedido")
        return True
    else:
        print("Acceso denegado, escirba la clave correcta.")
        return False

#Tercer ejemplo
def agregar_usuario(usuario, clave):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario}, {clave}\n")
        
#ejemplo de uso
agregar_usuario("admin", "Blanca2025")
agregar_usuario("user1", "Clave125")

#Función para carga el archivo usurarios.txt
def cargar_usuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario, clave = linea.strip().split(",")
                usuarios[usuario]= clave
    return usuarios

def inicio():
    print("Inicio de la sección")
    usuarios = cargar_usuarios()
    usuario = input("Usuario: ")
    #clave_ingresada = getpas.getpass("CLave: ")
    clave_ingresada = pwinput(prompt='Clave: ', mask='*')
    if usuario in usuarios and usuarios[usuario] == clave_ingresada:
        print("Bienvenido")
        return True
    else:
        print("Usuario o clave incorrectos. Por favor, intente de nuevo.\n")
        return False



def menu():
    print("""
          1. Agregar
          2. Editar
          3. Eliminar
          6. Salir
          Digite una opcion:
          """)
def main():
        while (True):
            menu()
            opción = input()
            if opción == '1':
                nombres = input("Nombres del estudiante: ")
                apellidos = input("Apellidos del estudiante: ")
                cif = int(input("Ingrese el CIF del estudiante: "))
                carrera = input("Carrera del estudiante: ")
                promedio = float(input("Promedio del estudiante: "))
                if promedio < 0 or promedio > 100:
                    print("El promedio debe estar entre 0 y 100.")
                else:
                    print("El promedio es correcto.")
                estudiante = c.Estudiante(nombres, apellidos, cif, carrera, promedio)
                Estudiantes.append(estudiante)
                
            elif opción == '2':
                print("Editar estudiante: ")
                Estudiantes.show()
            
            elif opción == '3':
                cif = int(input("Ingrese el CIF del estudiante a eliminar: "))
                estudiante = c.Estudiantes("", "", cif, "", 0)
            
            elif opción == '6':
                print("Ádios")
                break
            
            else:
                print("Opcion no valida, intente de nuevo")
                
if inicio():
    menu()