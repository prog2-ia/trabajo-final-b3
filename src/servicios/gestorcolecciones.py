from entidades.colecciones import Coleccion
from entidades.excepciones import PiezaInvalidError , ColeccionInvalidError
class Gestorcolecciones:
    """
        Clase usada por coordinador para gestionar las colecciones almacenadas


        ---ATRIBUTOS---

            __usuario : Usuario 
            __lista_colecciones : list[Coleccion]
            __coleccione_actual : Coleccion

        ---MÉTODOS---

            listar_colecciones()-> list[Coleccion] :
                devuelve una copia del atributo __colecciones (la lista de las colecciones del usuario)

            crear_nueva_coleccion()-> Coleccion :
                Añade una nueva colección a la lista de colecciones 

            buscar_coleccion(identificador : int)-> Coleccion :
                Devuelve la colección indicada si está almacenada 

            eliminar_coleccion(identificador : int)->bool : 
                Elimina la colección indicada

            seleccionar_coleccion(identificador : int) -> bool : 
                Selecciona la colección indicada y la almacena en  __coleccione_actual   
            
            obtener_piezas()->list[Pieza] : 
                Obtiene las piezas de la colección actual 
            
            obtener_cartas()->list[Pieza] :
                obtiene las piezas de tipo carta de la colección actual
            
            obtener_figuras()->list[Pieza] :
                obtiene las piezas de tipo figura de la colección actual
            
            anyadir_pieza(pieza) -> bool : 
                Añade una pieza a la colección actual 
            
            eliminar_pieza(pieza) -> bool : 
                Elimina la pieza indicada de la colección actual 
            
            obtener_pieza(pieza) -> Pieza : 
                Busca y devuelve la pieza indicada en la colección actual 


    """
    def __init__(self, usuario ):

        self.__usuario : 'Usuario' = usuario
        self.__coleccione_actual : Coleccion = None

    @property
    def usuario (self) : 
        return self.__usuario
    def listar_colecciones(self) -> list[Coleccion]:
        return self.__usuario.colecciones.copy()

    def crear_nueva_coleccion(self) -> Coleccion :

        nueva = Coleccion()
        try :
            self.__usuario.anyadir_coleccion(nueva)
        except  ValueError as error :
            raise ColeccionInvalidError(str (error))

        return nueva
    
    def buscar_coleccion(self , identificador ) -> Coleccion : 

        for coleccion in self.__usuario.colecciones:
            if coleccion.identificador == int(identificador):
                return coleccion
        raise ColeccionInvalidError('Coleccion no encontrada')

    def eliminar_coleccion(self , identificador : int )-> bool :
        try :
            coleccion = self.buscar_coleccion(identificador)
        except ColeccionInvalidError:
            raise ColeccionInvalidError('Coleccion no encontrada')
        
        try :
            self.__usuario.eliminar_coleccion(coleccion)
            return True
        except : 
            raise ColeccionInvalidError('La coleccion no existe')

    def seleccionar_coleccion(self, identificador : int )-> bool:
        try : 
            coleccion = self.buscar_coleccion(identificador)
            self.__coleccione_actual = coleccion
            return True 
        except ColeccionInvalidError : 
            raise ColeccionInvalidError('Coleccion no encontrada')


    def obtener_piezas(self) -> list['Pieza']: 
        piezas =  self.__coleccione_actual.get_cartas() + self.__coleccione_actual.get_figuras()
        return piezas


    def obtener_figuras(self) -> list['Pieza']:

        return  self.__coleccione_actual.get_figuras()

    def obtener_cartas(self) -> list['Pieza']:
        return self.__coleccione_actual.get_cartas()
    
    def anyadir_pieza(self , pieza)-> bool  : 
        try :
            self.__coleccione_actual.agregar_pieza(pieza)
            return True
        except Exception as error :
            raise PiezaInvalidError(str(error))
        
    def eliminar_pieza(self, pieza) -> bool :
        try:
            pieza_eliminar = self.obtener_pieza(pieza)
            self.__coleccione_actual.eliminar_pieza(pieza_eliminar)
            return True
        except Exception:
            raise PiezaInvalidError('Pieza no encontrada')

    def obtener_pieza(self , pieza) ->  'Pieza'  : 
        
        for pieza_encoleccion in self.__coleccione_actual.piezas :
            if pieza_encoleccion == pieza : 
                return pieza_encoleccion 
        raise PiezaInvalidError('Pieza no encontrada')
