def menu_search(str_seccion: str, controller)->None:
  
    print("="*100)
    print(" "*30,'Sistema bibliotecario de mierda')
    print(" "*30,'Buscar ' + str_seccion)
    print('='*100,'\n')    
    
    
    
    input_word = input('Ingrese el name xd: ')
    
    data_dict = controller.search(input_word)
    
    if data_dict is None:
        print('No existe '+ str_seccion )
        return
    
    for i in data_dict:
        print(i,'\n')