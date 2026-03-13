class Gestorcolecciones:

    def __init__(self , usuario):

        self.__usuario_actual = usuario
        self.__colecciones = usuario.colecciones

    def mostrar_colecciones(self):
        for coleccion in self.__usuario_actual.colecciones :
            print(coleccion)

    def anyadir_coleccion(self):
        pass

    def eliminar_coleccion(self):
        pass

    def obtener_coleccion(self):
        return