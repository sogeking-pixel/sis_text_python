def menu_edit(str_seccion: str, controller , data:list)->None:
  
    print("="*100)
    print(" "*30,'Sistema bibliotecario de mierda')
    print(" "*30,'EDITAR' + str_seccion)
    print('='*100,'\n')    
    
    
    
    input_id = input('Ingrese el id: ')
    
    data_dict = controller.show(input_id)
    
    
    if data_dict is None:
        print('No existe '+ str_seccion )
        return
        
    
    print(data_dict,'\n')
    
    print('Por favor cambie lo que necesite, en el caso que no quiera cambiar NO ESCRIBA NADA')
    dict_data = dict()
    dict_data['id'] = data_dict['id']
    for i in data:
        input_selection = input('Ingrese el nuevo {}: '.format(i))
        if input_selection != "":
            dict_data[i] =  input_selection
    
    
    controller.update( **dict_data )
    
    
    print('Guadardo correctamente, eso creo :)')