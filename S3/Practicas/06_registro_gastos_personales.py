# Solicitar el monto de cada gasto.
# Si el usuario introduce 0, terminar el registro con break.
# Si introduce un monto negativo, mostrar un mensaje y omitirlo con continue.
# Acumular los gastos válidos.
# Contabilizar cuántos gastos fueron registrados.
# Mostrar el total y la cantidad de gastos.


# ====== REGISTRO DE GASTOS PERSONALES ======

total_gastos = 0
cantidad_gastos = 0

# ====== INGRESO Y VALIDACION DE DATOS ======

while True:

    monto = float(input("Ingrese un gasto (0 para finalizar): "))

    if monto == 0:
        break

    if monto < 0:
        print("Monto inválido. Se omite.")
        continue

    # ====== ACUMULAR GASTOS VALIDOS ======

    total_gastos += monto
    cantidad_gastos += 1


# ====== RESUMEN DE GASTOS ======

print("\n===== RESUMEN DE GASTOS =====")
print(f"Cantidad de gastos: {cantidad_gastos}")
print(f"Total gastado: C$ {total_gastos:.2f}")
print("==============================")
