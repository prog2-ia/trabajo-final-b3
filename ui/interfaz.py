from servicios.gestorusuarios import GestorUsuarios
from servicios.gestorcolecciones import Gestorcolecciones

def  interfaz():

    print('-------------------------------------------------------------------------------------------------')
    print('-------------------------------GESTOR DE PIEZAS DE COLECCION-------------------------------------')
    print('-------------------------------------------------------------------------------------------------')

    gestor = GestorUsuarios()

    while True :

        print( '0. Lista de usuarios'
              '\n 1.Registrar nuevo usuario'
              '\n 2.Iniciar sesion con un usuario'
              '\n 3.Salir'
              )

        entrada = input('> ')


        match entrada :
            case '0' :
                gestor.lista_usuarios()
            case '1' :

                email =  input('Email : ')
                nombre = input('Nombre : ')
                sol =  gestor.registrar_usuario(email= email , nombre= nombre)
                print('\n Usuario registrado correctamente') if sol == True else print('\n Usuario registrado incorrecto')

            case '2' :

                email = input('Email : ')
                nombre = input('Nombre : ')
                sol = gestor.inicio_sesion(email= email , nombre= nombre)
                print('\n Usuario encontrado') if sol == True else print('\n Usuario no encontrado')
                interfaz_usuario_personal(gestor.usuario_actual)

            case '3' :
                return
            case _ :
                print('\n Valor incorrecto')


def interfaz_usuario_personal(usuario) :

    print('-------------------------------------------------------------------------------------------------------------------')
    print(f'-------------------------------  Sesion iniciada Usuario : {usuario.nombre}  -------------------------------------')
    print('-------------------------------------------------------------------------------------------------------------------')

    gestor = Gestorcolecciones(usuario)
    while True:

        print('\n 1.Obtener info de usuario'
              '\n 2.Gestionar colecciones'
              '\n 3.Salir'
              )
        hola = input('> ')
        match hola:
                case '1':
                    print(usuario)

                case '2':
                    print('Colecciones del usuario')
                    gestor.mostrar_colecciones()
                    interfaz_colecciones(gestor)

                case '3':
                    return
                case _:
                    print('\n Valor incorrecto')

def interfaz_colecciones(gestor) :

    while True:

        print('\n 1.Crear coleccion'
              '\n 2.Eliminar coleccion'
              '\n 3.Entrar en la coleccion'
              '\n 4.Salir'
              )
        hola = input('> ')
        match hola:
            case '1':
                gestor.añadir_coleccion()
            case '2':
                gestor.eliminar_coleccion()
            case '3':
                gestor.obtener_coleccion()
            case '4':
                return
            case _:
                print('\n Valor incorrecto')


def interfaz_pieza(coleccion) :

    while True:

        print('\n 1.Mirar piezas'
              '\n 2.Añadir pieza'
              '\n 3.Eliminar pieza'
              '\n 4.Seleccionar pieza'
              '\n 4.Salir'
              )
        hola = input('> ')
        match hola:
            case '1':
                gestor.añadir_coleccion()
            case '2':
                gestor.eliminar_coleccion()
            case '3':
                gestor.obtener_coleccion()
            case '4':
                return
            case _:
                print('\n Valor incorrecto')

