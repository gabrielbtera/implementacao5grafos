# def checkInclusao(grafo, qntvertice , posicao, listaCaminho) -> bool:
#   if grafo[listaCaminho [posicao -1]][qntvertice] == 0:
#     return 0

#   for flag in listaCaminho:
#     if flag == qntvertice:
#       return 0

#   return 1


# def backTrackingCicloHamiltoniano(grafo, qntVertices, listaCaminho, posicao):
  

#   if posicao == qntVertices:
#     if grafo[listaCaminho[posicao -1 ]][listaCaminho[0]] == 1:
#       return 1
#     else:
#       return 0

#   for vertice in range(1, qntVertices):
#     if checkInclusao(grafo, vertice, posicao, listaCaminho):
#       listaCaminho[posicao] = vertice

#       if backTrackingCicloHamiltoniano(grafo, qntVertices, listaCaminho, posicao + 1):
#         return 1

#       listaCaminho[posicao] = -1
#   return 0


# grafo = [[0, 5, 10, 0, 1], [5, 0, 0, 10, 1], [10, 0, 0, 2, 1], [0, 10, 2, 0, 1], [1, 1, 1, 1, 0]]

# g2 = [[0, 2, 1, 7, 4], [2, 0, 3, 5, 3], [1, 3, 0, 3, 2], [7, 5, 3, 0, 4], [4, 3, 2, 4, 0,]]
# g3 = [[0, 3, 2, 4], 
#       [3, 0, 7, 1], 
#       [2, 7, 0, 7], 
#       [4, 1, 7, 0]]



# def imprimeCicloHamiltoniano(grafo, qntVertices, posicao):
#   caminhoHamiltonianio = listaPivot(qntVertices)
#   caminhoHamiltonianio[0] = 0

#   if not backTrackingCicloHamiltoniano(grafo, qntVertices, caminhoHamiltonianio, posicao):
#     return 0


#   for vertice in caminhoHamiltonianio:
#     print (vertice + 1, end = " ")
#   print (caminhoHamiltonianio[0] + 1, "\n")

#   return caminhoHamiltonianio

# def listaPivot(numeroVertices):
#   return [-1] * numeroVertices

# # print()


# def main():
#   imprimeCicloHamiltoniano(g3, 4 , 1)

# # main()




def vizinhoMinimoPeso(vertice):
    return min(vertice['Vizinhos'], key= lambda x: x[1])


def buscaGulosa(graf, inicial):
    vertices_grafos = graf.keys()
    marcados = [inicial]


    
    
    minimo = vizinhoMinimoPeso(graf[inicial])
    vertice = minimo[0]


    print(graf)
    print(vertice, minimo)

    # print( graf[vertice]["Vizinhos"])

    while len(marcados) < len(vertices_grafos):
        

        if vertice not in marcados:
            marcados.append(vertice)

            minimo = vizinhoMinimoPeso(graf[vertice])
            graf[vertice]["Vizinhos"].remove(minimo)

            minimo = vizinhoMinimoPeso(graf[vertice])
            vertice = minimo[0]
            
        else:
            minimo = vizinhoMinimoPeso(graf[vertice])
            if minimo[0] in marcados:
                graf[vertice]["Vizinhos"].remove(minimo)
            minimo = vizinhoMinimoPeso(graf[vertice])
            vertice = minimo[0]
    marcados.append(inicial)
    print(marcados)
