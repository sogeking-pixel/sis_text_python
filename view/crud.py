# from controller.mainController import MainController


def menu_crud(str_seccion: str, controller)->None:
  while True:
        print("="*100)
        print(" "*30,'Sistema bibliotecario de mierda')
        print(" "*30,str_seccion)
        print('='*100,'\n')
        
        print('''
    1. Registrar
    2. Actualizar
    3. Buscar
    4. Eliminar
    5. <== Volver 
        Eliga una opccion porfavor...
              ''')
        input_selection = input('Ingrese la opccion: ')
        match input_selection:
            
            case '1':
                controller.create()
            case '2':
                controller.edit()
            case '3':
                controller.search_IU()
            case '4':
                controller.delete()
            case '5':
                break
            case _:
                print('no existe esa opccion, sorry :(')
                
                
def menu_crud_prestamo( controller)->None:
  while True:
        print("="*100)
        print(" "*30,'Sistema bibliotecario de mierda')
        print(" "*30,'Prestamo')
        print('='*100,'\n')
        
        print('''
    1. Registrar
    2. Devolver
    3. Eliminar
    4. <== Volver 
        Eliga una opccion porfavor...
              ''')
        input_selection = input('Ingrese la opccion: ')
        match input_selection:
            
            case '1':
                controller.create()
            case '2':
                controller.edit()
            case '3':
                controller.delete()
            case '4':
                break
            case _:
                print('no existe esa opccion, sorry :(')