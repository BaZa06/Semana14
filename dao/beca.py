"""Porcentajes de becas"""
class beca:
    def __init__(self):
        if self.estudiante > 85 and self.estudiante <= 90:
            print("El estudiante ha obtenido una beca del 25%")
        elif self.estudiante > 90 and self.estudiante <= 95:
            print("El estudiante ha obtenido una beca del 50%")
        elif self.estudiante > 95 and self.estudiante <= 98:
            print("El estudiante ha obtenido una beca del 75%")
        else:
            self.estudiante > 98 and self.estudiante <= 100
            print("El estudiante ha obtenido una beca del 100%")
            
    
