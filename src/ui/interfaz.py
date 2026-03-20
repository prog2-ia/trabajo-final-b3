from servicios.coordinador import Coordinador

class Interfaz :

    def __init__(self):
        self.__coordinador = Coordinador()

    def parte_usuarios(self):

        while True :
            print ('================================================================================')
            print('                GESTOR DE PIEZAS DE COLECCIÓN -> USUARIOS               ')           
            print('================================================================================')

            print(
                ' 0. Lista de usuarios'
                '\n 1. Registrar nuevo usuario'
                '\n 2. Iniciar sesion con un usuario'
                '\n 3. Salir'
                )

            entrada = input('\n Seleccione una opción > ')


            match entrada :
                case '0' :
                    print('\n................................................................')
                    print('                LISTA DE USUARIOS              ')           
                    print('................................................................\n')
                    for usuario in self.__coordinador.listar_usuarios() :
                        print(usuario)
                case '1' :
                    print('\n................................................................')
                    print('                REGISTRO DE USUARIO              ')           
                    print('................................................................\n')

                    email =  input('Email : ')
                    nombre = input('Nombre : ')
                    print(f'----{self.__coordinador.registrar_usuario(email= email , nombre= nombre)}----')

                case '2' :

                    print('\n................................................................')
                    print('                INICIO DE SESIÓN              ')           
                    print('................................................................\n')

                    email = input('Email : ')
                    nombre = input('Nombre : ')
                    resultado = self.__coordinador.iniciar_sesion_usuario(email= email , nombre= nombre)
                    print(f'----{resultado}----')
                    if resultado == 'Usuario iniciado correctamente' : 
                        self.parte_colecciones(nombre)
                case '3' :
                    return
                case _ :
                    print('\n ---- Valor incorrecto ----')

    def parte_colecciones(self , nombre):
        
        self.__coordinador.inicializar_colecciones()
        while True:
            print ('\n================================================================================')
            print(f'                GESTOR DE COLECCIONES DEL USUARIO : {nombre}              ')           
            print('================================================================================')

            print(
                '0 .  Lista de Colecciones'
                '\n 1. Crear coleccion'
                '\n 2. Eliminar Coleccion'
                '\n 3. Seleccionar coleccion'
                '\n 4. Retroceder'
            )

            entrada = input('\n Seleccione una opción > ')

            match entrada:
                case '0':
                    print('\n................................................................')
                    print('                LISTA DE COLECCIÓN              ')           
                    print('................................................................\n')
                    for coleccion in self.__coordinador.listar_colecciones() : 
                        print(coleccion)

                case '1':
                    print('\n................................................................')
                    print('                CREACIÓN DE COLECCIÓN              ')           
                    print('................................................................\n')

                    print(f'----{self.__coordinador.crear_nueva_coleccion()}----')

                case '2':
                    print('\n................................................................')
                    print('                ELIMINAR COLECCIÓN              ')           
                    print('................................................................\n')
                    id = input('Identificador >  ')
                    print(f'----{self.__coordinador.eliminar_coleccion(id)}----')

                case '3':
                    print('\n................................................................')
                    print('                SELECCIONAR COLECCIÓN              ')           
                    print('................................................................\n')
                    id = input('Identificador >  ')
                    resultado = self.__coordinador.seleccionar_coleccion(id)
                    print(f'----{resultado}----')
                    if resultado != f'coleccion id : {id} no encontrada' : 
                        self.parte_gestion_coleccion_unica(id, nombre)

                case '4':
                    break 
                case _:
                    print('\n Valor incorrecto')

    def parte_gestion_coleccion_unica(self,id , usuario ) : 

        while True:

            print ('\n================================================================================')
            print(f'                GESTOR DE COLECCIÓN : {id}               ')           
            print('================================================================================')

            print(
                '0.  Lista de Piezas de la colección'
                '\n 1. Obtener todas las piezas de colección tipo figura'
                '\n 2. Obtener todas las piezas de colección tipo Carta'
                '\n 3. Añadir una pieza a la colección'
                '\n 4. Eliminar una pieza de la colección'
                '\n 5. Reparar una pieza de la colección'
                '\n 6. Mejorar una pieza de la colección'
                '\n 7. Tasar una pieza de la colección'
                '\n 8. Retroceder'
            )

            entrada = input('\n Seleccione una opción > ')

            match entrada:
                case '0':
                    print('\n................................................................')
                    print('                LISTA DE PIEZAS DE COLECCIÓN              ')           
                    print('................................................................\n')
                    
                    for pieza in self.__coordinador.obtener_piezas() : 
                        print(pieza)

                case '1':
                    print('\n................................................................')
                    print('                LISTA DE FIGURAS              ')           
                    print('................................................................\n')

                    for pieza in self.__coordinador.obtener_figuras() : 
                        print(pieza)


                case '2':
                    print('\n................................................................')
                    print('                LISTA DE CARTAS               ')           
                    print('................................................................\n')

                    for pieza in self.__coordinador.obtener_cartas() : 
                        print(pieza)

                case '3':
                    print('\n................................................................')
                    print('                AÑADIR PIEZA DE COLECCIÓN              ')           
                    print('................................................................\n')
                    #nombre: str, estado: str, edicion: str, rareza: str

                    nombre = input('Nombre >  ')
                    estado = input('Estado : valores posibles [PERFECTO,BUENO,ACEPTABLE,MALO]  >')
                    edicion = input('Edicion >')
                    rareza = input('Rareza : valores posibles [LEGENDARIO,RARO,COMÚN] > ')
                    tipo = input('Tipo de pieza de colección : valores posibles [CARTA , FIGURA] > ')

                    if tipo.upper() == 'CARTA' :

                        imagen = input('imagen de la carta(str) > ')
                        print(self.__coordinador.anyadir_carta(nombre , estado , edicion , rareza , imagen ) )

                    elif tipo.upper() =='FIGURA' :

                        altura = input('altura de la figura > ')
                        anchura = input('anchura de la figura > ')
                        materiales = input('materiale del que está hecha : valores posibles [PVC,RESINA,METAL] > ')
                        print( self.__coordinador.anyadir_figura(nombre , estado , edicion , rareza , altura , anchura , materiales ) ) 
                    else  : 
                        print('\n----Tipo indicado incorrecto----')
                case '4' : 
                    print('\n................................................................')
                    print('                ELIMINAR PIEZA DE COLECCIÓN              ')           
                    print('................................................................\n')
                    nombre = input('\n Nombre de la pieza > ')
                    print ( self.__coordinador.eliminar_pieza(nombre) )
                case '5' :
                    print('\n................................................................')
                    print('                REPARAR PIEZA DE COLECCIÓN              ')           
                    print('................................................................\n')
                    nombre = input('\n Nombre de la pieza > ')
                    print( self.__coordinador.reparar_pieza(nombre) ) 

                case '6' : 
                    print('\n................................................................')
                    print('                MEJORAR PIEZA DE COLECCIÓN              ')           
                    print('................................................................\n')
                    nombre = input('\n Nombre de la pieza > ')
                    print ( self.__coordinador.mejorar_pieza(nombre) )

                case '7' :
                    print('\n................................................................')
                    print('                TASAR PIEZA DE COLECCIÓN              ')           
                    print('................................................................\n')
                    nombre = input('\n Nombre de la pieza > ')
                    print ( self.__coordinador.tasar_pieza(nombre) )
                case '8':
                    break 
                case _:
                    print('\n Valor incorrecto')