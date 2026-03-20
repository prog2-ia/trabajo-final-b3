from .gestorpiezas import  GestorPiezas
from .gestorusuarios import  GestorUsuarios
from .gestorcolecciones import  Gestorcolecciones

class Coordinador  :
    """
    Coordinador principal de todos los servicios , la interfaz hace uso de esta clase


    """
    def __init__(self):
        self.__gestorusuarios = GestorUsuarios()
        self.__gestorcolecciones = None
        self.__gestorpiezas = GestorPiezas()

    #--------------- PARTE DE LA GESTION DE USUARIOS -------------------------------------
    def listar_usuarios(self):
        return self.__gestorusuarios.listar_usuarios()

    def registrar_usuario(self, email : str , nombre : str) -> str :
        return  self.__gestorusuarios.registrar_usuario(email= email, nombre= nombre)

    def iniciar_sesion_usuario(self , email : str , nombre : str) -> str :
        resultado = self.__gestorusuarios.inicio_sesion(email= email, nombre= nombre)
        return  'Usuario iniciado correctamente' if resultado else 'Usuario no encontrado '


    #------------- PARTE DE LA GESTION DE LAS COLECCIONES---------------------------------------

    def inicializar_colecciones(self) :
        self.__gestorcolecciones = Gestorcolecciones(self.__gestorusuarios.usuario_actual)
        

    def listar_colecciones(self) -> str :
        print('GOLA')
        return self.__gestorcolecciones.listar_colecciones()

    def crear_nueva_coleccion(self) -> str:
        return f'Nueva coleccion id :{self.__gestorcolecciones.crear_nueva_coleccion().identificador} creada correctamente'

    def eliminar_coleccion(self , identificador : int) -> str :
        return f'coleccion id : {identificador} eliminada correctamente' if self.__gestorcolecciones.eliminar_coleccion(identificador) == True else f'coleccion id : {identificador} no encontrada'

    def seleccionar_coleccion(self , identificador : int) -> str :
        return f'colección id : {identificador} seleccionada' if self.__gestorcolecciones.seleccionar_coleccion(identificador) == True else f'coleccion id : {identificador} no encontrada'

    def obtener_piezas(self) :
        return self.__gestorcolecciones.obtener_piezas()
    
    def obtener_figuras(self) :
        return self.__gestorcolecciones.obtener_figuras()
    
    def obtener_cartas(self) : 
        return self.__gestorcolecciones.obtener_cartas()
    

    #self.__coordinador.anyadir_figura(nombre , estado , edicion , rareza , altura , anchura , materiales )
    def anyadir_figura(self,nombre , estado , edicion , rareza , altura ,anchura , materiales) : 
        
        figura = self.__gestorpiezas.crear_figura(nombre , estado , edicion , rareza , altura ,anchura , materiales)

        if type(figura) == str :
            print (figura) 

        print('\n----Error al añadir figura----') if self.__gestorcolecciones.anyadir_pieza(figura) == False else print('\n----Figura añadida----')
        print(figura)

    #self.__coordinador.anyadir_carta(nombre , estado , edicion , rareza , imagen )

    def anyadir_carta(self , nombre , estado ,edicion , rareza , imagen) : 

        carta = self.__gestorpiezas.crear_carta(nombre , estado ,edicion , rareza , imagen)
        if type(carta) == str :
            print(carta)  
        
        print('\n----Error al añadir Carta----') if self.__gestorcolecciones.anyadir_pieza(carta) == False else print('\n----Carta añadida----')
        print(carta)

    def eliminar_pieza(self , pieza) : 
        self.__gestorcolecciones.eliminar_pieza(pieza)