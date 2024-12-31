def menu_loan( controller)->None:
  
    print("="*100)
    print(" "*30,'Sistema bibliotecario de mierda')
    print(" "*30,'DEVOLUCION DE PRESTAMO')
    print('='*100,'\n')    
    
    input_word = input('Ingrese el id del prestamo: ')
    
    b = controller.return_loan(input_word)
    
    if b:
        print('se devolvio correctamente')
    else:
        print('caca pene teta culo, no se devolvio')