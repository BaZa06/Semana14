class EstudianteDao:
    def __init__(self):
        self.estudiantes = []
        
    def add (self, estudiante):
        self.estuantes.append(estudiante)
        
    def edit (self, estudiante):
        for i, est in enumerate (self.estudiantes):
            if est['cif'] == estudiante['cif']:
                self.estudiantes[i] = estudiante
                return True
        return False
    
    def remove(self, estudiante):
        for i, est in enumerate(self.estudiantes):
            if est['cif'] == estudiante['cif']:
                removed = self.estudiantes.pop(i)
                print(f"El estudiante {removed['cif']} ha sido eliminado del inventario")
                return
        print(f"El estudiante {estudiante['cif']} no ha sido encontrado")
    
    def show (self, estudiante):
        return self.estudiantes
    
        