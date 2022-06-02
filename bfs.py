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
    
    # Imprime la representación del grafo
    def imprimir_lista_adyacencia(self):
        '''Imprime la lista de adyacencia'''
        #Recorrido en la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            #Imprime los nodos que estan en la lista de adyacencia
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])

    # Función que imprime el recorrido BFS
    def bfs_traversal(self, inicio_nodo):
        """
        Realiza el recorrido del grafo generando unas colas y listas de
        los nodos que visitó.
        
        Parámetros:
        ------------
        inicio_nodo : int
            Nodo de inicio del recorrido
        """
        # Conjunto de nodos visitados para evitar bucles
        visitado = set()#Inicializa lista de nodos visitados
        cola = Queue()#Inicializa cola del grafo

        # Añade el nodo de inicio a la cola 
        cola.put(inicio_nodo)
        #Añade el nodo inicial a la lista de visitados
        visitado.add(inicio_nodo)

        #Se encuentra en un bucle siempre y cuando no este vacía la cola
        while not cola.empty():
            # Quita el primer nodo de la cola
            actual_nodo = cola.get()
            # Imprime el nodo actual
            print(actual_nodo, end = " ")

            #Recorre toda la lista adyacencia del nodo actual
            for (siguiente_nodo, peso) in self.m_lista_adyacencia[actual_nodo]:
                #Si el nodo no fue visitado agrega nodos a la cola y a la lista de visitados
                if siguiente_nodo not in visitado:
                    #Añade a la cola el siguiente nodo
                    cola.put(siguiente_nodo)
                    #Añade a la lista de nodos visitados el siguiente nodo
                    visitado.add(siguiente_nodo)

#Función Main de la clase
if __name__ == "__main__":


    # Crear una instancia de la clase `Grafo`.
    # Este grafo es no dirigido y tiene 5 nodos
    g = Grafo(5, dirigido=False)

    # Añáde las aristas (0,1) con peso=1
    g.agregar_arista(0, 1)
    # Añáde las aristas (0,2) con peso=1
    g.agregar_arista(0, 2)
    # Añáde las aristas (1,2) con peso=1
    g.agregar_arista(1, 2)
    # Añáde las aristas (1,4) con peso=1
    g.agregar_arista(1, 4)
    # Añáde las aristas (2,3) con peso=1
    g.agregar_arista(2, 3)

# Imprime la lista de adyacencia
    g.imprimir_lista_adyacencia()

    print ("Lo siguiente es la primera travesía de la amplitud"
                    " (a partir del vértice 0)")
    #Imprime la lsita de las colas visitadas
    g.bfs_traversal(0)
    print()
    
    #Imprime la documentanción
    help(Grafo)