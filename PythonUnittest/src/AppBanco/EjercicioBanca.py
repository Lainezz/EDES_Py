import CuentaBancaria
import CuentaException
import AvisarHaciendaException
import AvisarHaciendaAndSaldoException

#Cuenta bancaria del cliente
cuenta = None

error_cuenta = True
print("***BIENVENID2 AL BANCO X***")

while error_cuenta:
    try:
        iban = input("Introduzca el numero IBAN: ")
        titular = input("Introduzca el titular de la cuenta: ")
        cuenta = CuentaBancaria.CuentaBancaria(iban, titular)
        error_cuenta = False
    except CuentaException.CuentaException as cuentaException:
        print(cuentaException)

opcion = None
cantidad = None

while opcion != 0:
    print("Elija una opcion")
    print("1. Datos de la cuenta")
    print("2. IBAN")
    print("3. Titular")
    print("4. Saldo")
    print("5. Ingreso")
    print("6. Retirada")
    print("7. Movimientos")
    print("0. Salir")

    opcion = int(input("\n#: "))

    match opcion:
        case 1:
            cuenta.imprimir_datos()
            
        case 2:
            print(f"IBAN: {cuenta.iban}")
            
        case 3:
            print(f"Titular: {cuenta.titular}")
            
        case 4:
            print(f"Saldo: {cuenta.saldo}")
            
        case 5:
            cantidad = float(input("Inserte la cantidad a ingresar: "))
            try:
                cuenta.ingresar(cantidad)
            except CuentaException.CuentaException as cuentaException:
                print(cuentaException)
            except AvisarHaciendaException.AvisarHaciendaException as haciendaException:
                print(haciendaException)
            except AvisarHaciendaAndSaldoException.AvisarHaciendaAndSaldoException as haciendaYsaldoException:
                print(haciendaYsaldoException)
            except Exception as e:
                print(e)

        case 6:
            cantidad = float(input("Inserte la cantidad a retirar: "))
            try:
                cuenta.retirar(cantidad)
            except CuentaException.CuentaException as cuentaException:
                print(cuentaException)
            except AvisarHaciendaException.AvisarHaciendaException as haciendaException:
                print(haciendaException)
            except AvisarHaciendaAndSaldoException.AvisarHaciendaAndSaldoException as haciendaYsaldoException:
                print(haciendaYsaldoException)
            except Exception as e:
                print(e)

        case 7:
            cuenta.imprimir_movimientos()

        case 0:
            print("GRACIAS POR USAR NUESTRA APLICACION")

        case default:
            print("Opcion incorrecta")