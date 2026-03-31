#Menú principal
def menu_principal():
    print("CONTROL DE INVENTARIO - MARLON CASTILLO")
    print(" 1. Agregar \n 2. Mostrar \n 3. Buscar \n 4. Actualizar \n 5. Eliminar \n 6. Estadísticas \n 7. Guardar CSV \n 8. Cargar CSV \n 8. Salir")
    id_menu = int(input("Digite un número (1 -9) según lo que desee hacer: "))
    return id_menu

inventory = {
    "id_product": int,
    "name": str, 
    "value": float, 
    "stock": int
    }

#Función #1 -  Permite crear productos

def create_product():
    print("----Agregar Producto----")
    cant_product = int(input("¿Cuántos productos desea agregar?: "))
    id_count = 0
    for i in range (cant_product):
        print(f"---[Producto °{i +1}]---")
        name = input("Ingrese el nombre del producto: ")
        value = input("Ingrese el valor del producto: ")
        stock = int(input("Ingrese la cantidad del producto: "))
        id_count = id_count +1
        #Agrego productos al diccionario
        inventory["id_product"] = id_count
        inventory["name"] = name
        inventory["value"] = value
        inventory["stock"] = stock    
    for i in range (id_count):
        print(inventory["id_product"])    
        print(inventory["name"])    
        print(inventory["value"])    
        print(inventory["stock"])
        print("------")    
   
#Función #2 -  Permite Mostrar productos

def show_product():
    print("Mostrar")

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
