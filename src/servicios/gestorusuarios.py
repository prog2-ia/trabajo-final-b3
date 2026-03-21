
from  entidades.usuarios.usuario import  Usuario


class GestorUsuarios :
    """
        Clase usada por el coordinador para gestionar los usuarios.


        ---ATRIBUTOS---
```
================================================================================
                GESTOR DE PIEZAS DE COLECCIÓN -> USUARIOS
================================================================================
 0. Lista de usuarios
 1. Registrar nuevo usuario
 2. Iniciar sesion con un usuario
 3. Salir

 Seleccione una opción > 1

................................................................
                REGISTRO DE USUARIO
................................................................

Email : ejemplo
Nombre : Pepe
----Usuario registrado correctamente----
================================================================================
                GESTOR DE PIEZAS DE COLECCIÓN -> USUARIOS
================================================================================
 0. Lista de usuarios
 1. Registrar nuevo usuario
 2. Iniciar sesion con un usuario
 3. Salir

 Seleccione una opción > 2

................................................................
                INICIO DE SESIÓN
................................................................

Email : ejemplo
Nombre : Pepe
----Usuario iniciado correctamente----

================================================================================
                GESTOR DE COLECCIONES DEL USUARIO : Pepe
================================================================================
0 .  Lista de Colecciones
 1. Crear coleccion
 2. Eliminar Coleccion
 3. Seleccionar coleccion
 4. Retroceder

 Seleccione una opción > 1

................................................................
                CREACIÓN DE COLECCIÓN
................................................................

----Nueva coleccion id :1 creada correctamente----

================================================================================
                GESTOR DE COLECCIONES DEL USUARIO : Pepe
================================================================================
0 .  Lista de Colecciones
 1. Crear coleccion
 2. Eliminar Coleccion
 3. Seleccionar coleccion
 4. Retroceder

 Seleccione una opción > 3

................................................................
                SELECCIONAR COLECCIÓN
................................................................

Identificador >  1
----colección id : 1 seleccionada----

================================================================================
        ```
================================================================================
                GESTOR DE PIEZAS DE COLECCIÓN -> USUARIOS
================================================================================
 0. Lista de usuarios
 1. Registrar nuevo usuario
 2. Iniciar sesion con un usuario
 3. Salir

 Seleccione una opción > 1

................................................................
                REGISTRO DE USUARIO
................................................................

Email : ejemplo
Nombre : Pepe
----Usuario registrado correctamente----
================================================================================
                GESTOR DE PIEZAS DE COLECCIÓN -> USUARIOS
================================================================================
 0. Lista de usuarios
 1. Registrar nuevo usuario
 2. Iniciar sesion con un usuario
 3. Salir

 Seleccione una opción > 2

................................................................
                INICIO DE SESIÓN
................................................................

Email : ejemplo
Nombre : Pepe
----Usuario iniciado correctamente----

================================================================================
                GESTOR DE COLECCIONES DEL USUARIO : Pepe
================================================================================
0 .  Lista de Colecciones
 1. Crear coleccion
 2. Eliminar Coleccion
 3. Seleccionar coleccion
 4. Retroceder

 Seleccione una opción > 1

................................................................
                CREACIÓN DE COLECCIÓN
................................................................

----Nueva coleccion id :1 creada correctamente----

================================================================================
                GESTOR DE COLECCIONES DEL USUARIO : Pepe
================================================================================
0 .  Lista de Colecciones
 1. Crear coleccion
 2. Eliminar Coleccion
 3. Seleccionar coleccion
 4. Retroceder

 Seleccione una opción > 3

................................................................
                SELECCIONAR COLECCIÓN
................................................................

Identificador >  1
----colección id : 1 seleccionada----

================================================================================
                GESTOR DE COLECCIÓN : 1
================================================================================
0.  Lista de Piezas de la colección
 1. Obtener todas las piezas de colección tipo figura
 2. Obtener todas las piezas de colección tipo Carta
 3. Añadir una pieza a la colección
 4. Eliminar una pieza de la colección
 5. Reparar una pieza de la colección
 6. Mejorar una pieza de la colección
 7. Tasar una pieza de la colección
 8. Retroceder

 Seleccione una opción > 3

................................................................
                AÑADIR PIEZA DE COLECCIÓN
................................................................

Nombre >  Pieza
Estado : valores posibles [PERFECTO,BUENO,ACEPTABLE,MALO]  >Perfecto
Edicion >primera
Rareza : valores posibles [LEGENDARIO,RARO,COMÚN] > legendario
Tipo de pieza de colección : valores posibles [CARTA , FIGURA] > figura
altura de la figura > 20
anchura de la figura > 25
materiale del que está hecha : valores posibles [PVC,RESINA,METAL] > metal

----Figura añadida----
  Nombre: Pieza, Estado: PERFECTO, Edición: primera, Rareza: LEGENDARIO, Precio: 0,Altura: 20, Anchura: 25, Material: METAL
```
        GESTOR DE COLECCIÓN : 1
================================================================================
0.  Lista de Piezas de la colección
 1. Obtener todas las piezas de colección tipo figura
 2. Obtener todas las piezas de colección tipo Carta
 3. Añadir una pieza a la colección
 4. Eliminar una pieza de la colección
 5. Reparar una pieza de la colección
 6. Mejorar una pieza de la colección
 7. Tasar una pieza de la colección
 8. Retroceder

 Seleccione una opción > 3

................................................................
                AÑADIR PIEZA DE COLECCIÓN
................................................................

Nombre >  Pieza
Estado : valores posibles [PERFECTO,BUENO,ACEPTABLE,MALO]  >Perfecto
Edicion >primera
Rareza : valores posibles [LEGENDARIO,RARO,COMÚN] > legendario
Tipo de pieza de colección : valores posibles [CARTA , FIGURA] > figura
altura de la figura > 20
anchura de la figura > 25
materiale del que está hecha : valores posibles [PVC,RESINA,METAL] > metal

----Figura añadida----
  Nombre: Pieza, Estado: PERFECTO, Edición: primera, Rareza: LEGENDARIO, Precio: 0,Altura: 20, Anchura: 25, Material: METAL
```

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

        #ELIMINAR LUEGO , SOLO PARA INDICAR DATOS INCORRECTOS
        if nombre is None or not nombre.strip() or email is None or not email.strip():
            return  'Error al registrar usuario'
        usuario = Usuario(email= email, nombre= nombre)

        if usuario in self.__lista_usuarios :
            return 'Usuario ya existe'

        self.__lista_usuarios.append(usuario)
        return 'Usuario registrado correctamente'


    def inicio_sesion(self , email : str ,nombre : str)->bool:
        for usuario in self.__lista_usuarios :
            if usuario.email == email and usuario.nombre == nombre :
                self.__usuario_actual = usuario
                return True
        return False
