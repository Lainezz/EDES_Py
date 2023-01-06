import unittest
import Persona as persona

class TestPersona(unittest.TestCase):
    
    def test_inicializacion(self):

        #*************************
        #SIN MIRAR EL CÓDIGO
        #*************************

        #PRUEBAS DE CAJA NEGRA
        #PRUEBAS DE CLASES DE EQUIVALENCIA
        #Aquí probamos clases de equivalencia pensando:
        #Si funciona para -1 y funciona para -10, supongo que para todos los números negativos funcionan
        with self.assertRaises(Exception):
            persona.Persona(-1, "Diego")
        with self.assertRaises(Exception):
            persona.Persona(-10, "Diego")
        #Si funciona para 0
        cero = persona.Persona(0, "Test")
        self.assertEqual(cero.edad, 0)
        #Si funciona para los numeros positivos
        test1 = persona.Persona(1, "Test")
        test2 = persona.Persona(10, "Test")
        self.assertEqual(test1.edad, 1)
        self.assertEqual(test2.edad, 10)

        #Haciendo uso de las clases de equivalencia hemos probado que la edad se 
        #inicializa correctamente desde -infinito hasta +infinito

        #PRUEBAS DE VALORES LÍMITE
        #Probamos ahora los casos limite. ¿Qué casos límite establecemos?
        #Hay que mirar las especificaciones de nuestro programa
        #En este caso, en la edad, sólo tenemos 1 límite, y es al pasar de enteros positivos a enteros negativos
        #El límite está en 0
        test3 = persona.Persona(0, "TestLimite")
        self.assertEqual(test3.edad, 0)
        
        #**********************
        #MIRANDO EL CÓDIGO
        #**********************

        #PRUEBAS DE CAJA BLANCA
        #PRUEBAS DE CUBRIMIENTO
        #Consisten en probar todas y cada una de las líneas de código
        #Creamos un objeto correcto, debe pasar por las líneas de creacion de un objeto correctamente
        diego = persona.Persona(10, "Diego")
        self.assertEqual(diego.edad, 10)
        self.assertEqual(diego.nombre, "Diego")
        #Sólo nos quedaría pasar por donde comprueba lo de la edad, y ver que se lanza una excepción
        with self.assertRaises(Exception):
            persona.Persona(-1, "Diego")

        #PRUEBAS DE CONDICIONES
        #¿Qué condiciones tenemos al crear el objeto? Únicamente la que comprueba la edad


if __name__ == "__main__":
    unittest.main()