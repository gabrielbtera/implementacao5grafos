import algoritimos.BellmoreENemhauser as heuristica1
import arquivosTestes.dadosFormatados as data


att48_d = open("./arquivosTestes/att48_d.txt", 'r')
dantzig42_d = open('./arquivosTestes/dantzig42_d.txt', 'r')
five_d = open("./arquivosTestes/five_d.txt", 'r')
fri26_d = open("./arquivosTestes/fri26_d.txt", 'r')
gr17_d =  open("./arquivosTestes/gr17_d.txt", 'r')
P01_d = open("./arquivosTestes/P01_d.txt", 'r')


def imprimeResultado(tupla):
  print("Ciclo encontrado: :", tupla[0])
  print("Custo do Ciclo Encontrado: ", tupla[1])
  print("Tempo de execução: ", tupla[2])
  print()



# t  = 
# print(t)

print("Resultado Bellmore Nemhauser att48_d:")
att48 = heuristica1.BellmoreNemHauser( data.att48_d(att48_d), 1)
imprimeResultado(att48)

print("Resultado Bellmore Nemhauser dantzig42_d:")
zig42 = heuristica1.BellmoreNemHauser(data.dantzig42_d(dantzig42_d), 1)
imprimeResultado(zig42)

print("Resultado Bellmore Nemhauser five_d:")
five = heuristica1.BellmoreNemHauser(data.five_d(five_d), 1)
imprimeResultado(five)

print("Resultado Bellmore Nemhauser fri26_d:")
fri26 = heuristica1.BellmoreNemHauser(data.fri26_d(fri26_d),1)
imprimeResultado(fri26)


print("Resultado Bellmore Nemhauser gr17_d:")
gr17 = heuristica1.BellmoreNemHauser(data.gr17_d(gr17_d),1)
imprimeResultado(gr17)

print("Resultado Bellmore Nemhauser P01_d:")
p01 = heuristica1.BellmoreNemHauser(data.P01_d(P01_d),1)
imprimeResultado(p01)