from  entidades.colecciones.coleccion import Coleccion

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
        self.__lista_colecciones : list[Coleccion] = usuario.colecciones
        self.__coleccione_actual : Coleccion = None

    def listar_colecciones(self) -> list[Coleccion]:
        return self.__lista_colecciones.copy()

    def crear_nueva_coleccion(self) -> Coleccion :
        nueva = Coleccion()
        self.__lista_colecciones.append(nueva)
        return nueva
    
    def buscar_coleccion(self , identificador ) -> Coleccion : 

        for coleccion in self.__lista_colecciones:
            if coleccion.identificador == int(identificador):
                return coleccion
        return None 

    def eliminar_coleccion(self , identificador : int )-> bool :

                coleccion = self.buscar_coleccion(identificador)
                if coleccion is None : 
                    return False
                self.__colecciones.remove(coleccion)
                return True

    def seleccionar_coleccion(self, identificador : int )-> bool:

        coleccion = self.buscar_coleccion(identificador)
        if coleccion is None : 
                return False
        self.__coleccione_actual = coleccion
        return True


    def obtener_piezas(self) -> list['Pieza']: 
        piezas =  self.__coleccione_actual.get_cartas() + self.__coleccione_actual.get_figuras()
        return piezas


    def obtener_figuras(self) -> list['Pieza']:

        return  self.__coleccione_actual.get_figuras()

    def obtener_cartas(self) -> list['Pieza']:
        return self.__coleccione_actual.get_cartas()
    
    def anyadir_pieza(self , pieza)-> bool  : 
        return self.__coleccione_actual.agregar_pieza(pieza)
    
    def eliminar_pieza(self ,pieza)-> True :
        
        nueva_lista = self.__coleccione_actual.piezas
        pieza_eliminar = self.obtener_pieza(pieza)
        
        if pieza_eliminar is not None : 
            nueva_lista.remove(pieza_eliminar)
            self.__coleccione_actual.piezas = nueva_lista
            return True 
        return False

    def obtener_pieza(self , pieza) ->  'Pieza'  : 
        
        for pieza_encoleccion in self.__coleccione_actual.piezas :
            if pieza_encoleccion == pieza : 
                return pieza_encoleccion 
        return None 
