from time import time

# Esta é uma função auxiliar que define os grafos para uma estrutura dicionario
def defineVizinhos(grafo):

  dic = {}
  for i in range(len(grafo)):
    dic [i + 1] = {"Vizinhos": [], "Marcado" : 0}
    for j in range(len(grafo[i])):
      
      if i != j:
        vertice = j + 1
        peso = grafo[i][j]
        verticeOrigem = i + 1
        if peso != 0:
            dic[i + 1]["Vizinhos"].append((verticeOrigem,  peso, vertice))
  
  return dic


# Rota Inicial 1 -> k -> 1, tal que k é o mais distante do vertice 1
def vizinhoMaximoVertice(grafo, vertice):
    maiorDistanciaVertice =  max(grafo[vertice]["Vizinhos"], key=lambda x: x[1])
    caminhoInicial = [vertice, int(maiorDistanciaVertice[2])]

    grafo[vertice]["Marcado"] = 1
    grafo[maiorDistanciaVertice[2]]["Marcado"] = 1


    tup = maiorDistanciaVertice

    return caminhoInicial, tup[1]

# faz um lista da menor distancia da rota de vertices que ainda não foram
# visitados e retorna o vertice mais distante.
def menorDistanciaRota(visitados, grafo):
    listaMenorPeso = []
   
    for j in grafo.keys():
        if j not in visitados:
            listaVizinhos = [(v,w,u) for v, w, u in grafo[j]["Vizinhos"] if u in visitados]
            minimo = min(listaVizinhos, key=lambda x: x[1])
            listaMenorPeso.append(minimo)
    return max(listaMenorPeso, key=lambda x: x[1])

# Responsável pela inserção do vertice j entre um i e k pertencentes a rota
def inserir(grafo, vertice, visitados, custoAtual):
    vizinhos = [(v,w,u) for v, w, u in grafo[vertice]["Vizinhos"] if u in visitados]
    
    j = 1
    i = 0
    tamanho = len(vizinhos)
    listapesos = []
    while j < tamanho:
        primeiro = vizinhos[i][1]
        segundo = vizinhos[j][1]
        custo = primeiro + segundo - custoAtual
        listapesos.append((vizinhos[i][2],custo))

        i += 1
        j += 1
    
    minimoExtraido = min(listapesos, key=lambda x: x[1])
    verticeExtraido = minimoExtraido[0]
    custoAtual += minimoExtraido[1]
   
    indice = visitados.index(verticeExtraido)

    visitados.insert(indice + 1, vertice)

    return custoAtual

# Funcao auxiliar para calcular os pesos da rota encontrada.
def calculaPesos(matriz, vizinhos):
    tamanhoMatriz = len(vizinhos)
    j = 1
    i = 0
    contador = 0
    while j < tamanhoMatriz:
        x = vizinhos[i] -1
        y = vizinhos[j] -1
        contador += matriz[x][y]

        i += 1
        j += 1
    
    return contador



# funcao principal da implementação. 
def inserirUm(matriz, vertice=1):
    grafo = defineVizinhos(matriz) 
    qntVertices = len(matriz)

    inicio = time()

    # Encontra  o vertice  mais distante do vertice inicial e pega o peso atual
    # deles dois.
    visitados, pesoAtual = vizinhoMaximoVertice(grafo, vertice)
    

    while len(visitados) < qntVertices:
      # Pega o maior vertice de uma lista de menores distancias
      menorDistancia = menorDistanciaRota(visitados, grafo)
      verticeMenor = menorDistancia[0]
      # faz a insercao de j entre i e k
      pesoAtual += inserir(grafo, verticeMenor, visitados, pesoAtual)
    
    # fecha o ciclo
    visitados.append(vertice)

    tempo = time() - inicio

    return  visitados, calculaPesos(matriz, visitados),  round(tempo, 5)
    

