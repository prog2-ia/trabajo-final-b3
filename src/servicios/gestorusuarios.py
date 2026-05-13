
from  entidades.usuarios.usuario import  Usuario
from entidades.excepciones import UserInvalidError

class GestorUsuarios :
    """
        Clase usada por el coordinador para gestionar los usuarios.

        ---ATRIBUTOS---

            __lista_usuarios : list[Usuario]  
            __usuario_actual : Usuario -> Propiedad de lectura 

        ---MÉTODOS---

            listar_usuarios() -> list[Usuario] : 
                Devuelve una copia de  lista_usuarios
            
            registar_usuario(email : str , nombre : str ) -> str | Usuario  : 
                Registra un usuario 
            
            inicio_sesion(email : str , nombre : str) -> bool : 
                Busca si el usuario está almacenado y permite iniciar sesión 



    """
    def __init__(self):
        self.__lista_usuarios : list[Usuario] = []
        self.__usuario_actual : Usuario = None


    @property
    def usuario_actual(self):
        return self.__usuario_actual


    def listar_usuarios(self) -> list[Usuario]:
        return self.__lista_usuarios.copy()

    def registrar_usuario(self , email : str , nombre : str )-> str | Usuario:
        
        try :
            usuario = Usuario(email= email, nombre= nombre)
        except ValueError as val:
            raise UserInvalidError ( str(val)  ) 

        if usuario in self.__lista_usuarios :
            raise UserInvalidError ( 'Usuario ya existe' ) 

        self.__lista_usuarios.append(usuario)
        return 'Usuario registrado correctamente'


    def inicio_sesion(self , email : str ,nombre : str)->bool:
        for usuario in self.__lista_usuarios :
            if usuario.email == email and usuario.nombre == nombre :
                self.__usuario_actual = usuario
                return True
        return False
