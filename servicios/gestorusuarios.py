from  entidades.usuarios.usuario import  Usuario
class GestorUsuarios :

    def __init__(self , instruccion : str ):
        if instruccion is None or not instruccion.strip() :
            print('La instrucción indicada es errónea')
            return
        self.__instruccion = instruccion

    def funcion(self):
        pass