
from  entidades.usuarios.usuario import  Usuario


class GestorUsuarios :
    """
    Clase que usa la interfaz  para la gestion de los objetos usuario
    """
    def __init__(self):
        self.__usuarios = []
        self.__usuario_actual = None


    @property
    def usuario_actual(self):
        return self.__usuario_actual

    #------------------------METODOS-------------------------------------
    def listar_usuarios(self):
        return [print(usuario) for usuario in self.__usuarios]

    def registrar_usuario(self , email : str , nombre : str )-> str | Usuario:

        #ELIMINAR LUEGO , SOLO PARA INDICAR DATOS INCORRECTOS
        if nombre is None or not nombre.strip() or email is None or not email.strip():
            return  'Error al registrar usuario'
        usuario = Usuario(email= email, nombre= nombre)

        if usuario in self.__usuarios :
            return 'Usuario ya existe'

        self.__usuarios.append(usuario)
        return 'Usuario registrado correctamente'


    def inicio_sesion(self , email : str ,nombre : str)->bool:
        for usuario in self.__usuarios :
            if usuario.email == email and usuario.nombre == nombre :
                self.__usuario_actual = usuario
                return True
            return False
