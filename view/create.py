


def menu_create(str_seccion: str, controller , data:list)->None:
  
    print("="*100)
    print(" "*30,'Sistema bibliotecario de mierda')
    print(" "*30,'CREACION DE ' + str_seccion)
    print('='*100,'\n')
    
    dict_data = {}
    
    for i in data:
        input_selection = input('Ingrese el valor {}: '.format(i))
        dict_data[i] = input_selection
    
    controller.store( **dict_data )
    
    
    print('Guadardo correctamente, eso creo :)')
        
        