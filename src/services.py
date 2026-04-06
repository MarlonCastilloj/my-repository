#Menú principal
import csv
def menu_principal():
    while True:
        print("\nCONTROL DE INVENTARIO - MARLON CASTILLO")
        print(" 1. Agregar \n 2. Mostrar \n 3. Buscar \n 4. Actualizar \n 5. Eliminar \n 6. Estadísticas \n 7. Guardar CSV \n 8. Cargar CSV \n 9. Salir")
        
        try:
            id_menu = int(input("\nDigite un número (1 -9) según lo que desee hacer: \n"))
            
            if 1 <= id_menu <= 9:
                return id_menu
            else:
                print("⚠️ Ingrese un número válido entre 1 y 9")
        
        except ValueError:
            print("❌ Error: Debe ingresar un número entero")
            
#Función #1 -  Permite crear productos

inventory_list = [] 
def create_product():
    print("🟩 ​Agregar Producto 🟩​")
    cant_product = int(input("¿Cuántos productos desea agregar?: "))
    for i in range(cant_product):
        cant_actual = len(inventory_list) + 1
        print(f"\n ---[Producto °{cant_actual}]---")
        name = input("Ingrese el nombre del producto: ")
        value = input("Ingrese el valor del producto: ")
        stock = int(input("Ingrese la cantidad del producto: "))
        
        product = {
            "id_product": cant_actual,
            "name": name,
            "value": value,
            "stock": stock
        }
        inventory_list.append(product)
        print(f"\n[{len(inventory_list)} productos agregados ✅​]\n")
  
 
#Función #2 -  Permite Mostrar productos

def show_product():
    if not inventory_list:
        print("\n[0] productos en inventario. ❌")
    else:
        for p in inventory_list:
            print(f"\nID: {p['id_product']} | Nombre: {p['name']} |  Valor: {p['value']} | Stock: {p['stock']}\n")

#Función #3 -  Permite Buscar productos

def search_product():
    print("🔍 Buscar Producto")

    if len(inventory_list) == 0:
        print("No hay productos en el inventario ❌")
        return

    search = input("Ingrese el nombre del producto a buscar: ").lower()
    encontrado = False

    for product in inventory_list:
        if search in product["name"].lower():
            print("\n--- Producto encontrado ---")
            print(f"ID: {product['id_product']}")
            print(f"Nombre: {product['name']}")
            print(f"Valor: {product['value']}")
            print(f"Stock: {product['stock']}\n")
            encontrado = True

    if not encontrado:
        print("Producto no encontrado ❌")

#Función #4 -  Permite Actualizar productos

def update_product():
    print("✏️ Actualizar Producto")

    if not inventory_list:
        print("No hay productos en el inventario ❌")
        return

    try:
        name_search = input("Ingrese el nombre del producto a actualizar: ")
    except ValueError:
        print("Debe ingresar un número válido ❌")
        return

    for product in inventory_list:
        if product["name"] == name_search:
            print("\nProducto encontrado:")
            print(f"Nombre actual: {product['name']}")
            print(f"Valor actual: {product['value']}")
            print(f"Stock actual: {product['stock']}")

            new_name = input("Nuevo nombre (ENTER para no cambiar): ")
            new_value = input("Nuevo valor (ENTER para no cambiar): ")
            new_stock = input("Nuevo stock (ENTER para no cambiar): ")

            if new_name != "":
                product["name"] = new_name

            if new_value != "":
                product["value"] = new_value

            if new_stock != "":
                try:
                    product["stock"] = int(new_stock)
                except ValueError:
                    print("Stock inválido, no se actualizó ❌")

            print("✅ Producto actualizado correctamente\n")
            return

    print("Producto no encontrado ❌")

#Función #5 -  Permite Eliminar productos

def delete_product():
    print("🗑️ Eliminar Producto")

    if not inventory_list:
        print("No hay productos en el inventario ❌")
        return

    try:
        name_delete = input("Ingrese el nombre del producto a eliminar: ")
    except ValueError:
        print("Debe ingresar un nombre válido ❌")
        return

    for product in inventory_list:
        if product["name"] == name_delete:
            print("\nProducto encontrado:")
            print(f"Nombre: {product['name']}")
            print(f"Valor: {product['value']}")
            print(f"Stock: {product['stock']}")

            confirm = input("¿Está seguro que desea eliminarlo? (s/n): ").lower()

            if confirm == "s":
                inventory_list.remove(product)
                print("✅ Producto eliminado correctamente\n")
            else:
                print("❌ Eliminación cancelada")

            return

    print("Producto no encontrado ❌")

#Función #6 -  Permite ver Estadísticas

def statistics_product():
    print("📊 Estadísticas del Inventario")
    for p in inventory_list:
            print(f"\nID: {p['id_product']} | Nombre: {p['name']} |  Valor: {p['value']} | Stock: {p['stock']}")

    if not inventory_list:
        print("No hay productos en el inventario ❌")
        return

    total_productos = len(inventory_list)
    total_unidades = 0
    valor_total = 0

    producto_mayor_stock = inventory_list[0]
    producto_menor_stock = inventory_list[0]

    for p in inventory_list:
        total_unidades += p["stock"]
        valor_total += float(p["value"]) * p["stock"]

        if p["stock"] > producto_mayor_stock["stock"]:
            producto_mayor_stock = p

        if p["stock"] < producto_menor_stock["stock"]:
            producto_menor_stock = p

    print(f"\nTotal de productos: {total_productos}")
    print(f"Total de unidades en inventario: {total_unidades}")
    print(f"Valor total del inventario: ${valor_total:,.2f}")

    print("\n📈 Producto con MÁS stock:")
    print(f"{producto_mayor_stock['name']} ({producto_mayor_stock['stock']} unidades)")

    print("\n📉 Producto con MENOS stock:")
    print(f"{producto_menor_stock['name']} ({producto_menor_stock['stock']} unidades)")

#Función #7 -  Permite cuardar csv

def save_csv():
    if not inventory_list:
        print("No hay productos para guardar ❌")
        return

    with open("inventario.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id_product", "name", "value", "stock"])
        writer.writeheader()
        writer.writerows(inventory_list)

    print("✅ Inventario guardado en inventario.csv")

#Función #8 -  Permite Cargar cvs

def upload_csv():
    try:
        with open("inventario.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            inventory_list.clear()  

            for row in reader:
                product = {
                    "id_product": int(row["id_product"]),
                    "name": row["name"],
                    "value": row["value"],
                    "stock": int(row["stock"])
                }
                inventory_list.append(product)

        print("✅ Inventario cargado correctamente")

    except FileNotFoundError:
        print("❌ No existe el archivo inventario.csv")

#Función #9 -  Permite Salir del programa

def exit_program():
    print("Salir del programa")
