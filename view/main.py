import os
from controller.AutorController import AutorController
from controller.BookController import BookController
from controller.LoadController import LoanController
from controller.UserController import UserController 

def menu_principal() -> bool:
    
    while True:
        print("="*100)
        print(" "*30,'Sistema bibliotecario de mierda')
        print('='*100,'\n')
        
        print('''
    1. Autores
    2. Libros
    3. Usuarios
    4. Prestamos
    5. Salir
        
            ''')
        
        input_selection = input('Ingrese la opccion: ')
        os.system('cls')
        match input_selection:
            
            case '1':
                AutorController.index()
            case '2':
                BookController.index()
            case '3':
                UserController.index()
            case '4':
                LoanController.index()
            case '5':
                break
            case _:
                print('no existe esa opccion, sorry :(')