class Estudiante:
    def __init__(self, nombres, apellidos, cif, carrera, promedio):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cif = cif
        self.carrera = carrera
        self.promedio = promedio
        
    def __str__(self):
        return f"\nNombres:{self.nombres} \nApellidos:{self.apellidos} \nCIF:{self.cif} \n Carrera:{self.carrera} \nPromedio:{self.promedio}"