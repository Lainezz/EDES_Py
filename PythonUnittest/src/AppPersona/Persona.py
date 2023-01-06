class Persona():
    
    edad = None
    nombre = None

    trabajo = "Desempleado"

    def __init__(self, edad, nombre) -> None:
        
        #Compruebo que la edad no es negativa
        if edad < 0:
            raise Exception("La edad no puede ser negativa")
        else:
            self.edad = edad

        self.nombre = nombre
    
    def asignar_trabajo(self, trabajo):

        if self.edad < 18:
            raise Exception("No se cumple la edad mínima para trabajar")
        else:
            self.trabajo = trabajo
        