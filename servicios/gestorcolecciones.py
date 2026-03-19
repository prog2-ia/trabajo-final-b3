from  entidades.colecciones.coleccion import Coleccion

class Gestorcolecciones:

    def __init__(self, usuario ):

        self.__usuario = usuario
        self.__colecciones = usuario.colecciones
        self.__coleccione_actual = None

    def listar_colecciones(self):
        return [print(coleccion) for coleccion in self.__colecciones]

    def crear_nueva_coleccion(self):
        nueva = Coleccion()
        self.__colecciones.append(nueva)
        return nueva
    
    def buscar_coleccion(self , identificador ) -> 'Coleccion' : 

        for coleccion in self.__colecciones:
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


    def obtener_piezas(self) : 
        piezas =  self.__coleccione_actual.get_cartas() + self.__coleccione_actual.get_figuras()
        return [print(pieza) for pieza in piezas]


    def obtener_figuras(self):

        return [print(figura) for figura in self.__coleccione_actual.get_figuras()]

    def obtener_cartas(self):
        return [print(carta) for carta in self.__coleccione_actual.get_cartas()]
    
    def anyadir_pieza(self , pieza) : 
        return self.__coleccione_actual.agregar_pieza(pieza)
    
    def eliminar_pieza(self ,pieza) : 
        pass