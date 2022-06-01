'''
Recebe uma matriz de adjacencias e retorna 
um dicionario com 

{vertice: {"vizinhos": [...], "Marcado":0/1}
'''
def defineVizinhos(grafo):

  dic = {}
  for i in range(len(grafo)):
    dic [i + 1] = {"Vizinhos": [], "Marcado" : 0}
    for j in range(len(grafo[i])):
      
      if i != j:
        vertice = j + 1
        peso = grafo[i][j]
        if peso != 0:
            dic[i + 1]["Vizinhos"].append((vertice,  peso))
  
  return dic


'''
Recebe o arquivo com o me da fonte e retorna 
um dicionario com 
{vertice: {"vizinhos": [...], "Marcado":0/1}
'''
def att48_d(arquivo) -> dict:

  listaDistancias = [cadaString.strip().split("      ") for cadaString in arquivo.readlines()]

  tamanhoLista = 48

  for cidade in listaDistancias:
    for distancia in range(tamanhoLista):
      cidade[distancia] = int(cidade[distancia].strip())

  return  defineVizinhos(listaDistancias)

'''
Recebe o arquivo com o me da fonte e retorna 
um dicionario com 
{vertice: {"vizinhos": [...], "Marcado":0/1}
'''
def dantzig42_d(arquivo) -> dict:
  
  listaDistancias = [cadaString.strip().split() for cadaString in arquivo.readlines()]

  for cidade in listaDistancias:
    for distancia in range(len(cidade)):
      cidade[distancia] = int(cidade[distancia])

  return defineVizinhos(listaDistancias)


def five_d(arquivo) -> dict:
  listaDistancias = [cadaString.strip().split() for cadaString in arquivo.readlines()]
  listaDistancias = listaDistancias[: len(listaDistancias)-1]

  for cidade in listaDistancias:
    for distancia in range(len(cidade)):
      cidade[distancia] = int(float(cidade[distancia]))

  return defineVizinhos(listaDistancias)

def fri26_d(arquivo) -> dict:
  listaDistancias = [cadaString.strip().split() for cadaString in arquivo.readlines()]
  
  for cidade in listaDistancias:
    for distancia in range(len(cidade)):
      cidade[distancia] = int(cidade[distancia])

  return defineVizinhos(listaDistancias)


def gr17_d(arquivo) -> dict:
  listaDistancias = [cadaString.strip().split() for cadaString in arquivo.readlines()]
  
  for cidade in listaDistancias:
    for distancia in range(len(cidade)):
      cidade[distancia] = int(cidade[distancia])

  return defineVizinhos(listaDistancias)

def P01_d(arquivo) -> dict:
  listaDistancias = [cadaString.strip().split() for cadaString in arquivo.readlines()]
  
  for cidade in listaDistancias:
    for distancia in range(len(cidade)):
      cidade[distancia] = int(cidade[distancia])

  return defineVizinhos(listaDistancias)





def grafoTestes():
  lista = [[0, 5, 10, 0, 1], [5, 0, 0, 10, 1], [10, 0, 0, 2, 1], [0, 10, 2, 0, 1], [1, 1, 1, 1, 0]]

  dic = {}
  for i in range(len(lista)):
    dic[i + 1] = {"vizinhos" : [], "marcado": False, "quantidadeVizinhos": 0}

    for vizinhosVertice in range(len(lista[i])):
      if lista[i][vizinhosVertice] != 0:
        dic[i + 1]['vizinhos'].append({"peso": lista[i][vizinhosVertice], "verticeAdjacente": vizinhosVertice + 1})
        dic[ i + 1]['quantidadeVizinhos'] += 1
    
  print(dic)






