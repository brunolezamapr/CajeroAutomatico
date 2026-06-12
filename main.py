'''
#REQUISITOS:
#
# 1. Autenticación
#    - Solicitar un PIN al usuario.
#    - Si el PIN es incorrecto, no permitir operaciones.
#    - Si el PIN es correcto, mostrar mensaje de bienvenida.
#
# 2. Menú principal
#    - Consultar saldo.
#    - Depositar dinero.
#    - Retirar dinero.
#    - Transferir dinero.
#    - Salir.
#
# 3. Consulta de saldo
#    - Mostrar saldo actual.
#    - Mostrar categoría del cliente:
#        * Bronce   -> saldo < 5,000
#        * Plata    -> saldo entre 5,000 y 20,000
#        * Oro      -> saldo entre 20,000 y 50,000
#        * Diamante -> saldo > 50,000
#
# 4. Depósito
#    - Solicitar monto.
#    - Validar que sea positivo.
#    - Actualizar saldo.
#    - Mostrar comprobante.
#
# 5. Retiro
#    - Solicitar monto.
#    - Validar que sea positivo.
#    - Validar fondos suficientes.
#    - Bloquear operaciones mayores a $20,000.
#
# 6. Clientes Premium y Normal
#    - Premium:
#         límite de retiro = $10,000
#    - Normal:
#         límite de retiro = $3,000
#
# 7. Transferencia
#    - Solicitar número de cuenta destino.
#    - Solicitar monto.
#    - Validar monto positivo.
#    - Validar fondos suficientes.
#    - Mostrar comprobante.
#
# 8. Salir
#    - Mostrar mensaje de despedida.
#
# 9. Manejo de errores
#    - Detectar opciones inválidas del menú.
#    - Detectar tipo de cliente inválido.
#

'''


pin_correcto = 2358

pin_usuario = int(input("Ingrese su PIN: "))

if pin_usuario != pin_correcto: 
    print("Error: No puedes hacer operaciones bancarias")
else: 
    print("---------- BIENVENIDO AL CAJERO AUTOMATICO -------")
    saldo = 100000

    cuenta_cliente = input("Eres cliente premium o normal?: ")

    cliente_premium = cuenta_cliente == "premium" or cuenta_cliente == "Premium"

    cliente_normal = cuenta_cliente == "normal" or cuenta_cliente == "Normal"

    if not cliente_premium and not cliente_normal:
        print("Tipo de cliente inválido")
    else: 


        print("1.Consultar saldo")
        print("2.Depositar dinero")
        print("3.Retirar dinero")
        print("4.Transferir dinero")
        print("5.Salir")

        opcion_usuario = int(input("Ingresa una opcion: (1-4): "))

       
        match opcion_usuario:
            case 1: 

                if saldo < 5000: 
                    categoria = "Bronce"
                elif saldo <= 20000:
                    categoria = "Plata"
                elif saldo <= 50000:
                    categoria = "Oro"
                else:
                    categoria = "Diamante"

                print(f"Tu saldo actual es {saldo}")
                print(f"Estas en categoria: {categoria}")

            
            case 2: 
                monto_deposito = float(input("Ingresa el monto a depositar: "))
                operacion_tipo = "Deposito"
                if monto_deposito <= 0:
                    print("El monto es menor o igual que 0")
                else:
                    saldo_actual = saldo + monto_deposito
                    print("Deposito exitoso")
                    print("---- COMPROBANTE ----")
                    print(f"Tipo de operacion: {operacion_tipo}")
                    print(f"Saldo actual: {saldo_actual}")

            case 3: 
                monto_a_retirar = float(input("Ingresa el monto a retirar: "))
                operacion_tipo = "Retiro"
                
                if monto_a_retirar <= 0: 
                    print("El monto debe ser positivo")
                elif monto_a_retirar > saldo: 
                    print("Fondos insuficientes")
                elif monto_a_retirar > 20000:
                    print("Operacion bloqueada por seguridad")
                else:
                    
                        if cliente_premium:
                            if monto_a_retirar > 10000 : 
                                print("Error: No puedes retirar mas de tu limite")
                            else: 
                                    retiro_saldo = saldo - monto_a_retirar
                                    print("---- COMPROBANTE ----")
                                    print(f"Tipo de operacion: {operacion_tipo}")
                                    print(f"Saldo restante: {retiro_saldo}")
                        elif cliente_normal: 
                                if monto_a_retirar > 3000: 
                                    print("Error: No puedes retirar más de tu limite")
                                else:
                                    retiro_saldo = saldo - monto_a_retirar
                                    print("---- COMPROBANTE ----")
                                    print(f"Tipo de operacion: {operacion_tipo}")
                                    print(f"Saldo restante: {retiro_saldo}")
                    
                    
            case 4:
                nro_cuenta_destino = int(input("Ingresa el numero de cuenta destino: "))
                monto_a_transferir = float(input("Ingresa el monto a transferir: "))
                operacion_tipo = "Transferencia"
                
                if monto_a_transferir <= 0:
                    print("Error: El monto debe ser positivo")
                elif monto_a_transferir > saldo:
                    print("Fondos insuficientes")
                else:
                    saldo = saldo - monto_a_transferir
                    print("---- COMPROBANTE ----")
                    print(f"Tipo de operacion: {operacion_tipo}")
                    print(f"Cuenta destino: {nro_cuenta_destino}")
                    print(f"Monto transferido: {monto_a_transferir}")
                    print(f"Saldo restante: {saldo}")
                    
                

            case 5: 
                print("Gracias por usar el cajero")

            case _:
                print("Opcion no valida")

        

                
