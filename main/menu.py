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


# Primer ejemplo
def inicio_visible():
    print("Inicio de la sección")
    intento = input("Ingrese la clave de acceso: ")
    if intento == CLAVE:
        print("Bienvenido")
        return True
    else:
        print("Clave incorrecta, vuelva a intentarlo, por favor.")
        return False

# Segundo ejemplo
def inicio_oculto():
    intento = getpass.getpass("Ingrese la clave de acceso: ")
    if intento == CLAVE:
        print("Acceso concedido")
        return True
    else:
        print("Acceso denegado, escriba la clave correcta.")
        return False

# Tercer ejemplo
def agregar_usuario(usuario, clave):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario},{clave}\n")
        
# ejemplo de uso
agregar_usuario("admin", "Blanca2025")
agregar_usuario("user1", "Clave125")

# Función para cargar el archivo usuarios.txt
def cargar_usuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 2:
                    usuario, clave = partes
                    usuarios[usuario.strip()] = clave.strip()
    return usuarios

def inicio_usuario():
    print("Inicio de la sección")
    usuarios = cargar_usuarios()
    usuario = input("Usuario: ")
    clave_ingresada = pwinput.pwinput(prompt='Clave: ', mask='*')
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
opcion = input("Seleccione el tipo de inicio (1, 2 o 3): ")
def main():
    while True:
        menu()
        opcion = input()
        if opcion == '1':
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
            
        elif opcion == '2':
            print("Editar estudiante: ")
            for idx, estudiante in enumerate(Estudiantes):
                print(f"{idx+1}. {estudiante.nombres} {estudiante.apellidos} - CIF: {estudiante.cif}")
            # Aquí puedes agregar lógica para editar un estudiante
            
        elif opcion == '3':
            cif = int(input("Ingrese el CIF del estudiante a eliminar: "))
            Estudiantes[:] = [e for e in Estudiantes if e.cif != cif]
            print("Estudiante eliminado si existía.")
        
        elif opcion == '6':
            print("Adiós")
            break
        
        else:
            print("Opcion no valida, intente de nuevo")

if opcion == '1':
    if inicio_visible():
        main()
elif opcion == '2':
    if inicio_oculto():
        main()
elif opcion == '3':
    if inicio_usuario():
        main()
    menu()