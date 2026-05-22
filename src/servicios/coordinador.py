from .gestorpiezas import  GestorPiezas
from .gestorusuarios import  GestorUsuarios
from .gestorcolecciones import  Gestorcolecciones
from entidades.excepciones import UserInvalidError , ColeccionInvalidError , PiezaInvalidError
from entidades.ficherostexto import FicherosTexto 

class Coordinador  :
    """
        Clase principal que se comunica con la interfaz , cordina la gestión de los servicios : gestor colecciones 
        gestor piezas y gestor usuarios.


        ---ATRIBUTOS---

            __gestorusuarios : GestorUsuarios
            __gestorcolecciones : GestorColecciones
            __gestorpiezas : GestorPiezas

        ---MÉTODOS---

            listar_usuarios() -> list[Usuario] 
                Se comunica con __getusuarios para obtener la lista de usuarios almacenados 

            registrar_usuario(email : str , nombre : str)-> str 
                Almacena el nuevo usurio en __gestorusuarios

            iniciar_sesion_usuario(email : str , nombre : str) -> str :
                Permite iniciar sesión con un usuario guardado 
            
            inicializar_colecciones() -> None  :
                Inicializa en __gestorcolecciones la lista de colecciones en valor de lista vacía , para luego poder añadir 
                colecciones 
            
            listar_colecciones() -> str : 
                Se comunica con __gestorcolecciones para obtener la lista de colecciones que pertenencen al usuario actual 

            crear_nueva_coleccion()-> str : 
                Crea y almacena una nueva colección vacía  con __gestorcolecciones 

            eliminar_coleccion(identificador : int)-> str :  
                Elimina la coleccion indicada 
            
            seleccionar_coleccion(identificador : int)-> str :
                Selecciona la coleccion indicada para poder actuar sobre ella 
            
            obtener_piezas()-> list[Pieza] : 
                Devuelve una lista con todas las piezas de la colección
            
            obtener_figuras() -> list[ Pieza | Figura ] : 
                Devuelve una lista con todas las piezas de tipo Figura en la colección

            obtener_cartas() -> list[Pieza | Carta]
                Devuelve una lista con todas las piezas de tipo Carta en la colección

            anyadir_figura(nombre , estado , edicion , rareza , altura ,anchura , materiales) -> str :
                Se comunica con __gestorcolecciones y  __gestorpiezas para crear y almacenar una pieza Figura en la colección

            anyadir_carta( nombre , estado ,edicion , rareza , imagen) -> str 
                Se comunica con __gestorcolecciones y  __gestorpiezas para crear y almacenar una pieza Carta en la colección

            eliminar_pieza(self , nombre) -> str  
                Se comunica con __gestorcolecciones y  __gestorpiezas para eliminar la pieza indicada

            reparar_pieza(nombre) -> str 
                Se comunica con __gestorpiezas para reparar la pieza indicada

            mejorar_pieza(nombre) -> str 
                Se comunica con __gestorpiezas para mejorar la pieza indicada

            tasar_pieza(nombre) -> str 
                Se comunica con __gestorpiezas para tasar la pieza indicada


    """

    def __init__(self):
        self.__gestorusuarios = GestorUsuarios()
        self.__gestorcolecciones = None
        self.__gestorpiezas = GestorPiezas()
    
    
    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                PARTE DE USUARIO
    -------------------------------------------------------------------------------------------------------------------------------------
    """


    def listar_usuarios(self) -> list['Usuario'] :
        return self.__gestorusuarios.listar_usuarios()

    def registrar_usuario(self, email : str , nombre : str) -> str :
        try : 
            self.__gestorusuarios.registrar_usuario(email= email, nombre= nombre)
        except UserInvalidError as user : 
            return str (user)
        else : 
            return 'Usuario registrado correctamente'

    def iniciar_sesion_usuario(self , email : str , nombre : str) -> str :
        try :
            self.__gestorusuarios.inicio_sesion(email= email, nombre= nombre)
        except UserInvalidError as user: 
            return str (user)
        else : 
            return 'Inicio de sesión correcto'



    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                PARTE DE LA GESTION DE LAS COLECCIONES
    -------------------------------------------------------------------------------------------------------------------------------------
    """


    def inicializar_colecciones(self) -> None :
        # Usamos 'is' para comparar identidad, no solo valores
        if self.__gestorcolecciones is not None and self.__gestorcolecciones.usuario is self.__gestorusuarios.usuario_actual:
            return
        
        # Si entramos aquí, creamos el gestor con el objeto REAL que vive en GestorUsuarios
        self.__gestorcolecciones = Gestorcolecciones(self.__gestorusuarios.usuario_actual)
                

    def listar_colecciones(self) -> list['Coleccion'] :
        return self.__gestorcolecciones.listar_colecciones()

    def crear_nueva_coleccion(self) -> str:
        return f'Nueva coleccion id :{self.__gestorcolecciones.crear_nueva_coleccion().identificador} creada correctamente'

    def eliminar_coleccion(self , identificador : int) -> str :
        try : 
            self.__gestorcolecciones.eliminar_coleccion(identificador)
        except ColeccionInvalidError as c  : 
            return str (c)
        else : 
            return f'coleccion id : {identificador} eliminada correctamente' 

    def seleccionar_coleccion(self , identificador : int) -> str :
        try:
            self.__gestorcolecciones.seleccionar_coleccion(identificador)
        except ColeccionInvalidError as error:
            return str(error)
        else:
            return  f'colección id: {identificador} seleccionada'

        # return f'colección id : {identificador} seleccionada' if self.__gestorcolecciones.seleccionar_coleccion(identificador) == True else f'coleccion id : {identificador} no encontrada'


    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                PARTE DE LA GESTION DE LA COLECCIÓN INDICADA 
    -------------------------------------------------------------------------------------------------------------------------------------
    """

    def obtener_piezas(self)  -> list['Pieza']:
        return self.__gestorcolecciones.obtener_piezas()
    
    def obtener_figuras(self)  -> list['Pieza']:
        return self.__gestorcolecciones.obtener_figuras()
    
    def obtener_cartas(self) -> list['Pieza'] : 
        return self.__gestorcolecciones.obtener_cartas()
    

    def anyadir_figura(self,nombre , estado , edicion , rareza , altura ,anchura , materiales)-> str : 
        try:
            figura = self.__gestorpiezas.crear_figura(nombre , estado , edicion , rareza , altura ,anchura , materiales)
        except PiezaInvalidError as error:
            return str(error)
        try:
            self.__gestorcolecciones.anyadir_pieza(figura)
        except PiezaInvalidError as error:
            return str(error)
        else:
            return f'\n----Figura añadida---- \n {figura} '

# return '\n----Error al añadir figura compruebe que no haya otra pieza con el mismo nombre----' if self.__gestorcolecciones.anyadir_pieza(figura) == False else f'\n----Figura añadida---- \n {figura} '


    def anyadir_carta(self , nombre , estado ,edicion , rareza , imagen) -> str  : 
        try:
            carta = self.__gestorpiezas.crear_carta(nombre , estado ,edicion , rareza , imagen)
        except PiezaInvalidError as error:
            return str(error)
        try:
            self.__gestorcolecciones.anyadir_pieza(carta)
        except PiezaInvalidError as error:
            return str(error)
        else:
            return f'\n----Carta añadida----\n {carta}'
        
        #  return '\n----Error al añadir Carta compruebe que no haya otra pieza con el mismo nombre----'  if self.__gestorcolecciones.anyadir_pieza(carta) == False else f'\n----Carta añadida----\n {carta}'
        

    def eliminar_pieza(self , nombre) -> str : 
        try:
            pieza = self.__gestorpiezas.crear_carta(nombre , 'MALO','FALSA','COMUN','IMAGEN')
        except PiezaInvalidError as error:
            return str(error)
        try:
            self.__gestorcolecciones.eliminar_pieza(pieza)
        except PiezaInvalidError as error:
            return str(error)
        else:
            return f'----Pieza {nombre} eliminada----'


        # return f'----Pieza {nombre} eliminada----' if self.__gestorcolecciones.eliminar_pieza(pieza) == True else f'----Pieza {nombre} no encontrada----'
        
    

    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                PARTE DE LA GESTION DE LA GESTIÓN DE CADA PIEZA  
    -------------------------------------------------------------------------------------------------------------------------------------
    """

    def reparar_pieza(self , nombre) -> str : 
        try:
            pieza_falsa = self.__gestorpiezas.crear_carta(nombre , 'MALO','FALSA','COMUN','IMAGEN')
        except PiezaInvalidError as error:
            return str(error)
        try:
            pieza_real = self.__gestorcolecciones.obtener_pieza(pieza_falsa)
        except PiezaInvalidError as error:
            return str(error)
        try:
            self.__gestorpiezas.reparar_pieza(pieza_real)
        except PiezaInvalidError as error:
            return str(error)
        else:
            return f'----Pieza : {nombre} reparada---- '
        
        # return f'----Pieza : {nombre} reparada---- ' if self.__gestorpiezas.reparar_pieza(pieza_real) == True else '----Error al reparar la pieza----'
        
    def mejorar_pieza(self , nombre) -> str  : 
        try:
            pieza_falsa = self.__gestorpiezas.crear_carta(nombre , 'MALO','FALSA','COMUN','IMAGEN')
        except PiezaInvalidError as error:
            return str(error)
        try:
            pieza_real = self.__gestorcolecciones.obtener_pieza(pieza_falsa)
        except PiezaInvalidError as error:
            return str(error)
        try:
            self.__gestorpiezas.mejorar_pieza(pieza_real)
        except PiezaInvalidError as error:
            return str(error)
        else:
            return f'----Pieza : {nombre} Mejorada---- '


            # return f'----Pieza : {nombre} Mejorada---- ' if self.__gestorpiezas.mejorar_pieza(pieza_real) == True else  '----Error al Mejorar la pieza----'

    def tasar_pieza(self , nombre) -> str :
        try:
            pieza_falsa = self.__gestorpiezas.crear_carta(nombre , 'MALO','FALSA','COMUN','IMAGEN')
        except PiezaInvalidError as error:
            return str(error)
        try:
            pieza_real = self.__gestorcolecciones.obtener_pieza(pieza_falsa)
        except PiezaInvalidError as error:
            return str(error)
        else:
            precio = self.__gestorpiezas.tasar_pieza(pieza_real)
            return f'----Precio : {precio}€ -----'
    
    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                PARTE DE    Ficheros de texto 
    -------------------------------------------------------------------------------------------------------------------------------------
    """
    
    def guardar_base_datos(self) -> None : 

        if self.__gestorcolecciones is None : 
            return
        self.__gestorusuarios.usuario_actual = self.__gestorcolecciones.usuario

        contado = 0 
        for usuario in self.__gestorusuarios.listar_usuarios() : 
            if contado == 0 :
                FicherosTexto.inicializar_fichero(usuario = usuario) 
            else : 
                FicherosTexto.anyadir_usuario_fichero(usuario = usuario) 
            contado+= 1 
    
