# El programa debe solicitar:
# Saldo disponible.
# Monto que desea retirar.
# Reglas:
# Si el saldo es negativo, mostrar que existe un error en la información.
# Si el monto a retirar es igual o inferior a cero, rechazar la operación.
# Si el monto supera el saldo disponible, rechazar el retiro.
# Si cumple todas las condiciones, autorizar el retiro y mostrar el saldo restante.


# ====== INGRESO DE DATOS ======

saldo = float(input("Saldo disponible: C$ "))
retiro = float(input("Monto a retirar: C$ "))

# ====== VALIDACION DE RETIRO ======

print("\n===== CAJERO AUTOMÁTICO =====")

if saldo < 0:
    print("Error: el saldo disponible contiene información inválida.")

elif retiro <= 0:
    print("Retiro rechazado. El monto debe ser mayor que cero.")

elif retiro > saldo:
    print("Retiro rechazado. Saldo insuficiente.")

else:
    saldo_restante = saldo - retiro
    print("Retiro autorizado.")
    print(f"Saldo restante: C$ {saldo_restante:.2f}")
