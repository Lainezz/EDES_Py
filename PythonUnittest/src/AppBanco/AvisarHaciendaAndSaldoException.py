class AvisarHaciendaAndSaldoException(Exception) :
    # Atributos
    iban = None
    titular = None
    tipoOperacion = None
    cantidad = 0.0
    msjSaldo = None
    # Constructor
    def __init__(self, iban,  titular,  tipoOperacion,  cantidad,  msjSaldo) :
        self.iban = iban
        self.titular = titular
        self.tipoOperacion = tipoOperacion
        self.cantidad = cantidad
        self.msjSaldo = msjSaldo
    
    def __str__(self) :
        msj = "Aviso: El titular " + self.titular + " de la cuenta " + self.iban + " ha realizado un/a " + self.tipoOperacion + " de " + str(self.cantidad) + "\n"
        msj += self.msjSaldo
        return "Excepcion Avisar Hacienda y Saldo Negativo: \n" + msj