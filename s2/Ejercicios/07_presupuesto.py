# El programa debe solicitar:
# descripcion del producto
# presupuesto disponible
# precio del producto cantidad
# Debe calcular el total, el saldo disponible y comprobar si el presupuesto es suficiente
# total
# saldo = presupuesto - total
# es_suficiente saldo >presupuesto


# ====== INGRESO DE DATOS ======

descripcion = input("Descripción del producto: ")
presupuesto = float(input("Presupuesto disponible: C$ "))
precio = float(input("Precio del producto: C$ "))
cantidad = int(input("Cantidad de productos: "))


# ====== CALCULOS ======

total = precio * cantidad
saldo = presupuesto - total
es_suficiente = saldo >= 0


# ====== RESULTADOS ======

print("\n========== RESUMEN DE COMPRA ==========")

print(f"Producto: {descripcion}")
print(f"Presupuesto: C$ {presupuesto:.2f}")
print(f"Total de compra: C$ {total:.2f}")
print(f"Saldo disponible: C$ {saldo:.2f}")

if es_suficiente:
    print("El presupuesto es suficiente.")
else:
    print("El presupuesto es insuficiente.")

print("=======================================")
