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
        #Número de nodos
        self.m_numero_de_nodos = numero_de_nodos
        #Rango del número de nodos
        self.m_nodos = range(self.m_numero_de_nodos)
		
        # Especifica si es dirigido o no dirigido
        self.m_dirigido = dirigido
		
        # Representación gráfica - Lista de adyacencia
        # Utilizamos un diccionario para implementar una lista de adyacencia
        self.m_lista_adyacencia = {node: set() for node in self.m_nodos}#Setea los nodos mediante un ciclo de repetición      
	
    # Agrega una arista al grafo
    def agregar_arista(self, nodo1, nodo2, peso=1):
        """
        Agrega una arista al grafo.
        
        Pasa al siguiente grafo si el primero no se encuentra dirigido
        
        Parámetros:
        ----------
        nodo1: int
            Nodo 1 - Inicio
        nodo1: int
            Nodo 2 - Fin
        peso: int
            Peso de la arista
        
        """
        
        #Añade una arista al nodo 1 para la lista del grafo
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))

        #Se añáde al otro nodo una arista si grafo resulta no estar dirigido
        if not self.m_dirigido:
            #Añade una arista al nodo 2 para la lista del grafo
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))
    
