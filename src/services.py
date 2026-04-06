#Menú principal
def menu_principal():
    while True:
        print("\nCONTROL DE INVENTARIO - MARLON CASTILLO")
        print(" 1. Agregar \n 2. Mostrar \n 3. Buscar \n 4. Actualizar \n 5. Eliminar \n 6. Estadísticas \n 7. Guardar CSV \n 8. Cargar CSV \n 9. Salir")
        
        try:
            id_menu = int(input("\nDigite un número (1 -9) según lo que desee hacer: "))
            
            if 1 <= id_menu <= 9:
                return id_menu
            else:
                print("⚠️ Ingrese un número válido entre 1 y 9")
        
        except ValueError:
            print("❌ Error: Debe ingresar un número entero")
            
#Función #1 -  Permite crear productos

inventory_list = [] 
def create_product():
    print("🟩​Agregar Producto🟩​")
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
            print(f"\nID: {p['id_product']} | Nombre: {p['name']} | Stock: {p['stock']}\n")

#Función #3 -  Permite Buscar productos

def search_product():
    print("Buscar")

#Función #4 -  Permite Actualizar productos

def update_product():
    print("Actualizar")

#Función #5 -  Permite Eliminar productos

def delete_product():
    print("Eliminar")

#Función #6 -  Permite ver Estadísticas

def statistics_product():
    print("Estadísticas")

#Función #7 -  Permite cuardar csv

def save_csv():
    print("Guardar csv")

#Función #8 -  Permite Cargar cvs

def upload_csv():
    print("Cargar cvs")

#Función #9 -  Permite Salir del programa

def exit_program():
    print("Salir del programa")
