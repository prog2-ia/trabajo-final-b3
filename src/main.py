from ui.interfaz import  Interfaz
from entidades.usuarios.usuario import Usuario
from entidades.colecciones.coleccion import Coleccion
from entidades.piezas.carta import Carta 
from entidades.piezas.figura import Figura
from entidades.ficherostexto.ficherostexto import FicherosTexto

if __name__ == '__main__' :
    
    #interfaz = Interfaz()
    #interfaz.parte_usuarios()

    coel =Coleccion()
    piezq1 = Carta('j','MALO','as','Raro','ASDAR')
    piezq2 = Figura('a','MALO','ad','RARO',123,123,'PVC')
    coel.agregar_pieza(piezq1)
    coel.agregar_pieza(piezq2)
    usuario = Usuario('yo','tu')
    usuario.anyadir_coleccion(coel)

    FicherosTexto.inicializar_fichero(usuario)


