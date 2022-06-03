import math
from time import time

"""
Algoritimo de prim, recebe uma lista de adjacencia
e retorna uma arvore geradora minima.
"""
def algoritimoPrim(matrizAdjacencia):
  
  qntdVertices = len(matrizAdjacencia[0])

  verticesSelecionados = [0 for i in range(qntdVertices)] 

  nVertices = 0
  verticesSelecionados[0] = 1 

  def checaM(v1, v2):
    return matrizAdjacencia[v1][v2]

  arvore = []
  
  while nVertices < qntdVertices-1:
    menorValor = math.inf
    v1 = 0
    v2 = 0
    temp = range(qntdVertices)
    for vertice in temp:
      if verticesSelecionados[vertice]:
        for verticeInterno in range(qntdVertices):
          if  checaM(vertice, verticeInterno) and not verticesSelecionados[verticeInterno]:
            if menorValor > checaM(vertice, verticeInterno):
              menorValor = checaM(vertice, verticeInterno)
              v1 = vertice
              v2 = verticeInterno
    verticesSelecionados[v2] = 1
    arvore.append((v1 + 1, matrizAdjacencia[v1][v2],  v2 + 1))
    nVertices += 1
  
  return arvore


# g2 = [[0, 2, 1, 7, 4], [2, 0, 3, 5, 3], [1, 3, 0, 3, 2], [7, 5, 3, 0, 4], [4, 3, 2, 4, 0,]]

# g3= [[0,1,4,9,8,2],
# [1,0,5,5,7,6],
# [4,5,0,10,7,4],
# [9,5,10,0,1,7],
# [8,7,7,1,0,3],
# [2,6,4,7,3,0]]



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
    



def contaPesosCaminhos(caminhoHamiltoniano, grafo):
  contador = 0
  coordenadas = [] 
  for i in range(len(caminhoHamiltoniano)-1):
    coordenadas.append((caminhoHamiltoniano[i]-1, caminhoHamiltoniano[i+1]-1))

  for i, j in coordenadas:
    contador += grafo[i][j]

  return contador


# Ler G = (N, M)
""" Retorna um tripla, com o 
    (ciclo Hamiltoniano, custo do Caminho, tempo de execucao)

"""
def twiceAround(grafo):
  inicio = time()
  # Determinar T uma árvore geradora mínima de G
  arvore = algoritimoPrim(grafo)

  # Dobrar as arestas de T e construir um ciclo euleriano L 
  grafoEuleriano = duplicaArestas(arvore)

  # Ciclo Euleriano sendo convertido em um hamiloniano
  # através da ideia do atalho.
  cicloHamiltoniano = DefineCicloHAmiltoniano(grafoEuleriano)

  # Escolher sequencialmente l k ∈ L
  custoCaminho = contaPesosCaminhos(cicloHamiltoniano, grafo)
  fim = time() - inicio

  return cicloHamiltoniano, custoCaminho, round(fim, 5)


