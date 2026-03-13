
from  entidades.usuarios.usuario import  Usuario


class GestorUsuarios :
    """
    Clase que usa la interfaz  para la gestion de los objetos usuario

    """

    def __init__(self):

        self.__usuarios :list[Usuario]= []
        self.__usuario_actual = None

    #-----------------PROPIEDADES---------------------------------------
    @property
    def usuario_actual(self)->Usuario:
        return self.__usuario_actual


    #------------------------METODOS-------------------------------------
    def registrar_usuario(self , email : str , nombre : str )->bool:

        #ELIMINAR LUEGO , SOLO PARA INDICAR DATOS INCORRECTOS
        if nombre is None or not nombre.strip() or email is None or not email.strip():
            return  False

        usuario = Usuario(email= email, nombre= nombre)

        if usuario in self.__usuarios:
            return False

        self.__usuarios.append(usuario)
        return True


    def inicio_sesion(self , email : str ,nombre : str)->bool:
        for usuario in self.__usuarios :
            if usuario.email == email and usuario.nombre == nombre :
                self.__usuario_actual = usuario
                return True
            return False

    def lista_usuarios(self):
        for usuario in self.__usuarios :
            print(usuario)
