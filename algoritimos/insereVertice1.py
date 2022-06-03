from time import time



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

def vizinhoMaximoVertice(grafo, vertice):
    maiorDistanciaVertice =  max(grafo[vertice]["Vizinhos"], key=lambda x: x[1])
    caminhoInicial = [vertice, int(maiorDistanciaVertice[2])]

    grafo[vertice]["Marcado"] = 1
    grafo[maiorDistanciaVertice[2]]["Marcado"] = 1


    tup = maiorDistanciaVertice

    return caminhoInicial, tup[1]

def menorDistanciaRota(visitados, grafo):
    listaMenorPeso = []
   
    for j in grafo.keys():
        if j not in visitados:
            listaVizinhos = [(v,w,u) for v, w, u in grafo[j]["Vizinhos"] if u in visitados]
            minimo = min(listaVizinhos, key=lambda x: x[1])
            listaMenorPeso.append(minimo)

 

    return max(listaMenorPeso, key=lambda x: x[1])


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




def inserirUm(matriz, vertice=1):
    grafo = defineVizinhos(matriz)
    qntVertices = len(matriz)

    inicio = time()
    visitados, pesoAtual = vizinhoMaximoVertice(grafo, vertice)
    menorDistancia = menorDistanciaRota(visitados, grafo)
    verticeMenor = menorDistancia[0]

    while len(visitados) < qntVertices:
        menorDistancia = menorDistanciaRota(visitados, grafo)
        verticeMenor = menorDistancia[0]
        pesoAtual += inserir(grafo, verticeMenor, visitados, pesoAtual)
     

    visitados.append(vertice)

    tempo = time() - inicio

    return  visitados, calculaPesos(matriz, visitados),  round(tempo, 5)
    


    
       


