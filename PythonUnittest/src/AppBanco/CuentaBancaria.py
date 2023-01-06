import re
import CuentaException
import AvisarHaciendaAndSaldoException
import AvisarHaciendaException

class CuentaBancaria():
    iban = None
    titular = None

    saldo = 0.0
    movimientos = None

    SALDO_MINIMO = -50.0
    AVISAR_HACIENDA = 3000.0

    valida = None

    def __init__(self, iban, titular):

        self.iban = iban
        self.titular = titular

        self.saldo = 0.0
        self.movimientos = list()

        exp_reg_iban = "^[A-Z]{2}\d{22}$"
        if re.search(exp_reg_iban, iban):
            self.valida = True
        else:
            self.valida = False
            raise CuentaException.CuentaException("El Formato del IBAN no es el correcto")

    def ingresar(self, cantidad):
        if cantidad <= 0:
            raise CuentaException.CuentaException("La cantidad a ingresar debe ser mayor que 0")
        return self.operar(cantidad)
    
    def retirar(self, cantidad):
        if cantidad <= 0:
            raise CuentaException.CuentaException("La cantidad a retirar debe ser mayor que 0")
        return self.operar(-abs(cantidad))

    def operar(self, cantidad):
        if self.saldo + cantidad < self.SALDO_MINIMO:
            raise CuentaException.CuentaException(f"La operación no se puede realizar porque tendríamos un saldo inferior a {self.SALDO_MINIMO}")
        
        self.saldo += cantidad
        self.movimientos.append(cantidad)

        if self.saldo < 0.0 and abs(cantidad) > self.AVISAR_HACIENDA:
            raise AvisarHaciendaAndSaldoException.AvisarHaciendaAndSaldoException(self.iban, self.titular, self.tipo_operacion(cantidad), abs(cantidad), "Aviso: Saldo en cuenta negativo")
        elif self.saldo < 0.0:
            raise Exception("Aviso: Saldo en cuenta negativo")
        elif abs(cantidad) > self.AVISAR_HACIENDA:
            raise AvisarHaciendaException.AvisarHaciendaException(self.iban, self.titular, self.tipo_operacion(cantidad), abs(cantidad))
        
        return True
    

    def tipo_operacion(self, cantidad):
        tipo_operacion = ""
        if cantidad > 0:
            tipo_operacion = "INGRESO"
        elif cantidad < 0:
            tipo_operacion = "RETIRADA"
        return tipo_operacion
    
    def imprimir(self):
        self.imprimir_datos()
        self.imprimir_movimientos()

    def imprimir_datos(self):
        print(f"IBAN: {self.iban} - Titular: {self.titular} - Saldo: {self.saldo}")
    
    def imprimir_movimientos(self):
        print(f"Movimientos realizados: {len(self.movimientos)}")
        i = 1
        for mov in self.movimientos:
            print(f"#{i}: {mov}")
            i+=1
