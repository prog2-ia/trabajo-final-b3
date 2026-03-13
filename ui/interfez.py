import  servicios

def  interfaz():

    print('Elija que opción quiere realizar \n'
        
          '0 : salir del programa \n'
          '1 : Crear usuario \n'
          '2 : Crear una colección \n'
          ''
          ''
          '')
    entrada = int( input('Escriba un valor : ') )


    match entrada :
        case 1 :
            gestor = servicios.gestorusuarios.GestorUsuarios('crear')
            gestor.funcion()
        case 2 :
            pass
        case 0 :
            print('Saliendo del programa')
        case _:
            print('Valor incorrecto')