class AvisarHaciendaException(Exception) :
    # Atributos
    iban = None
    titular = None
    tipoOperacion = None
    cantidad = 0.0
    # Constructor
    def __init__(self, iban,  titular,  tipoOperacion,  cantidad) :
        self.iban = iban
        self.titular = titular
        self.tipoOperacion = tipoOperacion
        self.cantidad = cantidad
    
    def __str__(self) :
        msj = "Aviso: El titular " + self.titular + " de la cuenta " + self.iban + " ha realizado un/a " + self.tipoOperacion + " de " + str(self.cantidad)
        return "Excepcion Avisar Hacienda: " + msj