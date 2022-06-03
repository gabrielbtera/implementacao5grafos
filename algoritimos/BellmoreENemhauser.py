from time import time


def vizinhoMinimoPeso(vertice):
    return min(vertice, key= lambda x: x[1])

def findVertice(grafo, marcados, verticeAtual):
    vizinhos = grafo[verticeAtual]['Vizinhos']
    novalista = [vizinho for vizinho in vizinhos if vizinho[0] not in marcados]
    return vizinhoMinimoPeso(novalista)

def BellmoreNemHauser(graf, inicial) -> tuple:
    tempoinicio = time()

    vertices_grafos = len(graf)
    #Escolher vertice inicial  e inclui no ciclo
    marcados = [inicial]
    v1 = 1

    custoCaminho = 0

    while len(marcados) < vertices_grafos:
        # encontrar um vertice pertecente ao ciclo mais
        # próximo do vertice atual.
        v = findVertice(graf, marcados, v1)
        custoCaminho += v[1]
        # inserir o vertice no ciclo hamiltoniano
        marcados.append(v[0])
        v1 = v[0]

    
    verticeFaltanteVizinhos = graf[v[0]]["Vizinhos"]
    for vertice, peso in verticeFaltanteVizinhos:
        if vertice == inicial:
            custoCaminho += peso
    
    # completa o co ciclo
    marcados.append(inicial)

    tempo = time()-tempoinicio

    return marcados, custoCaminho, round(tempo, 5)
    
