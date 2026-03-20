# from ui.interfaz import  Interfaz
from entidades.piezas.figura import Figura

if __name__ == '__main__' :
    figura_1= Figura(nombre='Diego', estado= 'Bueno', edicion='primera', rareza='legendario', altura=12, anchura=12, material='PVC' )
    print(figura_1.tasar())
