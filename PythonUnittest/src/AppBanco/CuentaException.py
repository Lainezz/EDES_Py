class CuentaException(Exception) :
    msj = None
    def __init__(self, msj) :
        self.msj = msj
    
    def __str__(self) :
        return "Excepcion Cuenta: " + self.msj