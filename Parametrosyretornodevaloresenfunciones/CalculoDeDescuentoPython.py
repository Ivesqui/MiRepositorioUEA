# Tarea de Programación: Cálculo de Descuento en Compras

# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento sobre un monto total.
    :param monto_total: Monto total de la compra
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%)
    :return: Valor del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
def main():
    print("=======================================")
    print("   🛍️  CALCULADORA DE DESCUENTOS 💸   ")
    print("=======================================\n")

    compras = []  # Lista para guardar todas las compras

    while True:
        print("\n📌 Nueva compra")
        monto = float(input("👉 Ingrese el monto total de la compra: $"))

        print("\nElija una opción:")
        print("1. Aplicar descuento por defecto (10%)")
        print("2. Ingresar un descuento personalizado")
        opcion = input("➡️  Opción: ")

        if opcion == "1":
            porcentaje = 10
        elif opcion == "2":
            porcentaje = float(input("👉 Ingrese el porcentaje de descuento: %"))
        else:
            print("⚠️ Opción no válida, aplicando 10% por defecto.")
            porcentaje = 10

        descuento = calcular_descuento(monto, porcentaje)
        total = monto - descuento

        print("\n✅ RESULTADO DE LA COMPRA")
        print(f"Monto total:       ${monto:.2f}")
        print(f"Descuento ({porcentaje:.0f}%): -${descuento:.2f}")
        print(f"Monto a pagar:     ${total:.2f}")
        print("---------------------------------------")

        # Guardar la compra en la lista
        compras.append({
            "monto": monto,
            "porcentaje": porcentaje,
            "descuento": descuento,
            "total": total
        })

        # Preguntar si quiere continuar
        continuar = input("\n¿Desea ingresar otra compra? (s/n): ").lower()
        if continuar != "s":
            break

    # Mostrar resumen final
    print("\n=======================================")
    print("         📊 RESUMEN DE COMPRAS")
    print("=======================================")

    total_general = 0
    ahorro_total = 0
    for i, compra in enumerate(compras, start=1):
        print(f"\nCompra {i}:")
        print(f"   Monto:       ${compra['monto']:.2f}")
        print(f"   Descuento:   {compra['porcentaje']}% (-${compra['descuento']:.2f})")
        print(f"   Total a pagar: ${compra['total']:.2f}")
        total_general += compra["total"]
        ahorro_total += compra["descuento"]

    print("\n=======================================")
    print(f"💰 Total gastado (con descuentos): ${total_general:.2f}")
    print(f"🎉 Ahorro total acumulado:        ${ahorro_total:.2f}")
    print("=======================================")
    print("¡Gracias por usar la calculadora! 🙌")


# Ejecutar el programa
if __name__ == "__main__":
    main()
