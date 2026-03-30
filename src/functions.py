#Menú principal
def menu_principal():
    print("CONTROL DE INVENTARIO - MARLON CASTILLO")
    print(" 1. Agregar \n 2. Mostrar \n 3. Buscar \n 4. Actualizar \n 5. Eliminar \n 6. Estadísticas \n 7. Guardar CSV \n 8. Cargar CSV \n 8. Salir")
    id_menu = int(input("Digite un número (1 -9) según lo que desee hacer: "))
    return id_menu

def create_product():
    print("Crear")

def show_product():
    print("Mostrar")

def search_product():
    print("Buscar")

def update_product():
    print("Actualizar")

def delete_product():
    print("Eliminar")

def statistics_product():
    print("Estadísticas")

def save_csv():
    print("Guardar csv")

def upload_csv():
    print("Cargar cvs")

def exit_program():
    print("Salir del programa")
