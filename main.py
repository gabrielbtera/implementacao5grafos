import algoritimos.BellmoreENemhauser as heuristica1
import algoritimos.TwiceAround as heuristica2

import arquivosTestes.dadosFormatados as data


saida = open("resultados.txt", "w")

att48_d = open("./arquivosTestes/att48_d.txt", 'r')
dantzig42_d = open('./arquivosTestes/dantzig42_d.txt', 'r')
five_d = open("./arquivosTestes/five_d.txt", 'r')
fri26_d = open("./arquivosTestes/fri26_d.txt", 'r')
gr17_d =  open("./arquivosTestes/gr17_d.txt", 'r')
P01_d = open("./arquivosTestes/P01_d.txt", 'r')


def imprimeResultado(tupla):
  saida.write(f"Ciclo encontrado: {tupla[0]}\n")
  saida.write(f"Custo do Ciclo Encontrado: {tupla[1]}\n")
  # print("Custo do Ciclo Encontrado: ", tupla[1])
  saida.write(f"Tempo de execucao: {tupla[2]}\n\n")

def imprimeTitulo(txt):
  saida.write(txt + '\n')

 



# t  = 
# print(t)
def bellmore():

  imprimeTitulo("Resultado Bellmore Nemhauser att48_d:")
  att48 = heuristica1.BellmoreNemHauser( data.att48_d(att48_d)[0], 1)
  imprimeResultado(att48)

  imprimeTitulo("Resultado Bellmore Nemhauser dantzig42_d:")
  zig42 = heuristica1.BellmoreNemHauser(data.dantzig42_d(dantzig42_d)[0], 1)
  imprimeResultado(zig42)

  imprimeTitulo("Resultado Bellmore Nemhauser five_d:")
  five = heuristica1.BellmoreNemHauser(data.five_d(five_d)[0], 1)
  imprimeResultado(five)

  imprimeTitulo("Resultado Bellmore Nemhauser fri26_d:")
  fri26 = heuristica1.BellmoreNemHauser(data.fri26_d(fri26_d)[0],1)
  imprimeResultado(fri26)


  imprimeTitulo("Resultado Bellmore Nemhauser gr17_d:")
  gr17 = heuristica1.BellmoreNemHauser(data.gr17_d(gr17_d)[0],1)
  imprimeResultado(gr17)

  imprimeTitulo("Resultado Bellmore Nemhauser P01_d:")
  p01 = heuristica1.BellmoreNemHauser(data.P01_d(P01_d)[0],1)
  imprimeResultado(p01)

bellmore()

imprimeTitulo("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| \n")

att48_d = open("./arquivosTestes/att48_d.txt", 'r')
dantzig42_d = open('./arquivosTestes/dantzig42_d.txt', 'r')
five_d = open("./arquivosTestes/five_d.txt", 'r')
fri26_d = open("./arquivosTestes/fri26_d.txt", 'r')
gr17_d =  open("./arquivosTestes/gr17_d.txt", 'r')
P01_d = open("./arquivosTestes/P01_d.txt", 'r')

def twiceAround():
  imprimeTitulo("Resultado Twice-Around att48_d:")
  att48 = heuristica2.twiceAround( data.att48_d(att48_d)[1])
  imprimeResultado(att48)

  imprimeTitulo("Resultado Twice-Around dantzig42_d:")
  zig42 = heuristica2.twiceAround(data.dantzig42_d(dantzig42_d)[1])
  imprimeResultado(zig42)

  imprimeTitulo("Resultado Twice-Around five_d:")
  five = heuristica2.twiceAround(data.five_d(five_d)[1])
  imprimeResultado(five)

  imprimeTitulo("Resultado Twice-Around fri26_d:")
  fri26 = heuristica2.twiceAround(data.fri26_d(fri26_d)[1])
  imprimeResultado(fri26)

  imprimeTitulo("Resultado Twice-Around gr17_d:")
  gr17 = heuristica2.twiceAround(data.gr17_d(gr17_d)[1])
  imprimeResultado(gr17)


  imprimeTitulo("Resultado Bellmore Nemhauser P01_d:")
  p01 = heuristica2.twiceAround(data.P01_d(P01_d)[1])
  imprimeResultado(p01)






  







twiceAround()
