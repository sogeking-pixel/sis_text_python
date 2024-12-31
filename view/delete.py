def menu_delete(str_seccion: str, controller)->None:
  
    print("="*100)
    print(" "*30,'Sistema bibliotecario de mierda')
    print(" "*30,'Eliminar' + str_seccion)
    print('='*100,'\n')    
    
    
    
    input_id = input('Ingrese el id: ')
    
    data_dict = controller.show(input_id)
    
    if data_dict is None:
        print('No existe '+ str_seccion )
        return
    
    input_delete = input('Quiere eliminarlo?').lower()
    
    if input_delete == 'si':
        controller.destroy(input_id)
        print('eliminado!')
    print('tremendo maricon!!')
    
    