



def att48_d(arquivo) -> list:

  listaDistancias = [cadaString.strip().split("      ") for cadaString in arquivo.readlines()]

  tamanhoLista = 48

  for cidade in listaDistancias:
    for distancia in range(tamanhoLista):
      cidade[distancia] = int(cidade[distancia].strip())

  return listaDistancias

def dantzig42_d(arquivo) -> list:
  
  listaDistancias = [cadaString.strip().split() for cadaString in arquivo.readlines()]

  
  for cidade in listaDistancias:
    for distancia in range(len(cidade)):
      cidade[distancia] = int(cidade[distancia])

  return listaDistancias


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




def main():
  # dantzig42_d()
  grafoTestes()



