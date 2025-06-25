class EstudianteDao:
    def __init__(self):
        self.estudiantes = []
        
    def add (self, estudiante):
        self.estuantes.append(estudiante)
        
    def edit (self, estudiante):
        for i, est in enumerate (self.estudiantes):
            if est['cif'] == estudiante['id']
                self.estudiantes[i] = estudiante
                return True
        return False
    
    def delete (self, estudiante):
        
    
    def show (self, estudiante):
        return self.estudiantes
    
        