# Gestor de piezas de colección 
Sistema desarrollado para administrar, clasificar y tasar colecciones personales 
de objetos, concretamente cartas y figuras. 

##  Descripción | Propósito del proyecto

 Este proyecto es un sistema de gestión orientado a objetos, estructurado en capas
 (entidades, servicios e interfaz) que permite a los usuarios tener un registro 
 detallado de sus pertenencias.

- **¿Qué problema resuelve?**

    Resuelve la falta de organización y la dificultad para calcular el valor económico 
    de grandes inventarios de objetos físicos coleccionables. Facilita la gestión de 
    múltiples colecciones, permitiendo buscar, añadir y eliminar piezas fácilmente.


- **¿Para quién está pensado?**

    Está diseñado tanto para coleccionistas aficionados como profesionales debido a su 
    fácil manejo, así como para tiendas o tasadores que manejen inventarios de figuras y
    cartas y necesiten llevar un control cercano de su catálogo.


- **¿Qué lo hace diferente?**

    Su sistema de tasación. El programa no solo almacena datos, sino que calcula 
    automáticamente el precio de los objetos basándose en ciertos parámetros. Tiene
    en cuenta el estado de conservación, la rareza, el tamaño, el material (PVC, Resina, Metal)
    e incluso si una carta cuenta con la firma del autor original.

---
## Ejemplos

El sistema funciona a través de una interfaz en la consola que funciona por menús. Ahora veremos
un ejemplo de como un usuario inicia sesión, crea una colección, entra en esa colección y añade 
una figura

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

## Instalación

Instrucciones para instalar el proyecto paso a paso.

```bash
# Clonar repositorio
git clone <url-del-repo>

# Entrar en la carpeta
cd <nombre-del-proyecto>

# Instalar dependencias
pip install -r requirements.txt

