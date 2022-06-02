#Importamos la librería Queue
from queue import Queue

#Se crea la clase Grafo
class Grafo:
    """
    Clase que identifica a un grafo.
    
    ...
    
    Atributos
    ---------
    numero_de_nodos : int
        número de nodos
    dirigido: boolean
        grafo dirigido
    
    Métodos
    -------
    agregar_arista(nodo1, nodo2, peso=1):
        Agregar arista al grafo.
    
    imprimir_lista_adyacencia():
        Imprime la lista de adyacencia.
    
    bfs_traversal(inicio_nodo):
        Recorre el grafo.
    """
    
    # Constructor
    def __init__(self, numero_de_nodos, dirigido=True):
        """
        Construye todos los atributos necesarios para el objeto grafo.
        
        Parámetros:
        ----------
            numero_de_nodos: int
                Número de nodos del grafo
            dirigido: boolean
                Grafo dirigido o No dirgido
        """
