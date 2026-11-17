# Programa que calcule precio de las entradas
# Menores de 12 años = C$50
# De 12 a 17 años = C$80
# De 18 a 64 años = C$120
# De 65 años a más = C$70
# si tiene código promocional aplicar 10%
# Mostrar: categoría, precio, descuento y total a pagar

edad = int(input("Ingrese su edad: "))
codigo = input("¿Tiene código promocional? (s/n): ")

if edad < 12:
    categoria = "Niño"
    tarifa = 50

elif edad <= 17:
    categoria = "Adolescente"
    tarifa = 80

elif edad <= 64:
    categoria = "Adulto"
    tarifa = 120

else:
    categoria = "Adulto mayor"
    tarifa = 70

if codigo.lower() == "s":
    descuento = tarifa * 0.10
else:
    descuento = 0

total_pagar = tarifa - descuento

print("============ FESTIVAL ============")
print(f"Categoría: {categoria}")
print(f"Precio original: C$ {tarifa:.2f}")
print(f"Descuento aplicado: C$ {descuento:.2f}")
print(f"Total a pagar: C$ {total_pagar:.2f}")

print("==================================")
print("¡Disfrute del festival!")