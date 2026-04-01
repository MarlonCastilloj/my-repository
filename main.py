from src.services import *
program = False

while program == False:
    option = menu_principal()
    if option == 1:
        create_product()
    elif option == 2: 
        show_product()
    elif option == 3: 
        search_product()
    elif option == 4:  
        update_product()
    elif option == 5:
        delete_product()
    elif option == 6:
        statistics_product()
    elif option == 7:
        save_csv()
    elif option == 8:
        upload_csv()
    else: exit_program()