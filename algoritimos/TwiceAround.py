import math

INFINITO = math.inf

def algoritimoPrim(matrizAdjacencia):
  tamanho = len(matrizAdjacencia[0])

  verticesSelecionados = [0 for i in range(tamanho)]

  nVertices = 0
  verticesSelecionados[0] = 1

  arvore = []

  while nVertices < tamanho-1:
    menorValor = INFINITO
    v1 = 0
    v2 = 0
    temp = range(tamanho)
    for vertice in temp:
      if verticesSelecionados[vertice]:
        for verticeInterno in range(tamanho):

          if not verticesSelecionados[verticeInterno] and  matrizAdjacencia[vertice][verticeInterno]:
            if menorValor > matrizAdjacencia[vertice][verticeInterno]:
              menorValor = matrizAdjacencia[vertice][verticeInterno]
              v1 = vertice
              v2 = verticeInterno
    verticesSelecionados[v2] = 1
    arvore.append((v1 + 1, matrizAdjacencia[v1][v2],  v2 + 1))
    nVertices += 1
  
  return arvore


g2 = [[0, 2, 1, 7, 4], [2, 0, 3, 5, 3], [1, 3, 0, 3, 2], [7, 5, 3, 0, 4], [4, 3, 2, 4, 0,]]

g3= [[0,1,4,9,8,2],
[1,0,5,5,7,6],
[4,5,0,10,7,4],
[9,5,10,0,1,7],
[8,7,7,1,0,3],
[2,6,4,7,3,0]]

arvore = algoritimoPrim(g3)
print(arvore)

# print(arvore)


def duplicaArestas(arvore):
  listaeuleriano = []
  for v1, w, v2 in arvore:
    listaeuleriano.append((v1,w,  v2))
    listaeuleriano.append((v2,w, v1))
  return listaeuleriano

def DefineCicloHAmiltoniano(listaEuleriano):
  cicloHamiltoniano = []
  for i in range(len(listaEuleriano)):
    if listaEuleriano[i][0] not in cicloHamiltoniano:
      cicloHamiltoniano.append(listaEuleriano[i][0])
  
  cicloHamiltoniano.append(listaEuleriano[0][0])
    
  return cicloHamiltoniano
    

print(DefineCicloHAmiltoniano(duplicaArestas(arvore)))


