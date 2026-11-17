#Solicitar un presupuesto y validar que sea mayor que cero.
#Mostrar un menú.
#Solicitar un presupuesto y validar que sea mayor que cero.
# Mostrar un menú.
# Visualizar las categorías de gastos: Transporte, Comida y Entradas.
# Registrar hasta tres gastos por operación.
# Omitir los gastos negativos.
# Evitar gastos que superen el presupuesto restante.
# Mostrar el total acumulado y la cantidad de gastos.
# Clasificar el consumo del presupuesto.
# Permitir regresar al menú hasta seleccionar salir.

# ====== CATEGORIAS ======

categorias = [
    "Transporte",
    "Comida",
    "Entradas"
]

# ====== INICIALIZACION ======

presupuesto = 0
total_gastado = 0
cantidad_gastos = 0

gastos_transporte = 0
gastos_comida = 0
gastos_entradas = 0

# ====== INGRESO DEL PRESUPUESTO ======

while presupuesto <= 0:

    presupuesto = float(input("Ingrese el presupuesto disponible: C$ "))

    if presupuesto <= 0:
        print("El presupuesto debe ser mayor que cero.")

# ====== MENU PRINCIPAL ======

while True:

    print("\n===== CONTROL DE GASTOS =====")
    print("1. Mostrar categorias")
    print("2. Registrar gastos")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")

    # ====== MOSTRAR CATEGORIAS ======

    if opcion == "1":

        print("\nCategorias de gastos:")

        for categoria in categorias:
            print(categoria)

    # ====== REGISTRAR GASTOS ======

    elif opcion == "2":

        for i in range(3):

            restante = presupuesto - total_gastado

            print(f"\nPresupuesto restante: C$ {restante:.2f}")

            gasto = float(input("Ingrese el monto del gasto: C$ "))

            if gasto < 0:
                print("Monto invalido. Se omite.")
                continue

            elif gasto == 0:
                print("El gasto debe ser mayor que cero.")
                continue

            elif gasto > restante:
                print("El gasto supera el presupuesto disponible.")
                continue

            # ====== SELECCIONAR CATEGORIA ======

            print("\nSeleccione una categoria:")
            print("1. Transporte")
            print("2. Comida")
            print("3. Entradas")

            categoria = input("Seleccione una opcion: ")

            if categoria == "1":
                gastos_transporte += gasto

            elif categoria == "2":
                gastos_comida += gasto

            elif categoria == "3":
                gastos_entradas += gasto

            else:
                print("Categoria invalida. Se omite el gasto.")
                continue

            # ====== ACTUALIZAR GASTOS ======

            total_gastado += gasto
            cantidad_gastos += 1

            print("Gasto registrado correctamente.")

        # ====== MOSTRAR RESULTADOS ======

        restante = presupuesto - total_gastado
        porcentaje = (total_gastado / presupuesto) * 100

        print("\n===== RESUMEN DE GASTOS =====")
        print(f"Presupuesto inicial: C$ {presupuesto:.2f}")
        print(f"Total gastado: C$ {total_gastado:.2f}")
        print(f"Cantidad de gastos: {cantidad_gastos}")
        print(f"Saldo disponible: C$ {restante:.2f}")

        # ====== GASTOS POR CATEGORIA ======

        print("\n===== GASTOS POR CATEGORIA =====")
        print(f"Transporte: C$ {gastos_transporte:.2f}")
        print(f"Comida: C$ {gastos_comida:.2f}")
        print(f"Entradas: C$ {gastos_entradas:.2f}")

        # ====== CLASIFICAR PRESUPUESTO ======

        print(f"\nConsumo del presupuesto: {porcentaje:.2f}%")

        if porcentaje >= 90:
            print("Presupuesto casi agotado.")

        elif porcentaje >= 60:
            print("Presupuesto moderadamente utilizado.")

        else:
            print("Presupuesto bajo control.")

    # ====== SALIR ======

    elif opcion == "3":

        print("Gracias por utilizar el sistema.")
        break

    else:
        print("Opcion incorrecta. Intente nuevamente.")

