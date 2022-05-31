import algoritimos.BellmoreENemhauser as heuristica1
import arquivosTestes.dadosFormatados as data


att48_d = open("./arquivosTestes/att48_d.txt", 'r')
dantzig42_d = open('./arquivosTestes/dantzig42_d.txt', 'r')
five_d = open("./arquivosTestes/five_d.txt", 'r')


t  = data.five_d(five_d)
print(t)

# print("Resultado Bellmore Nemhauser att48_d:")
# heuristica1.BellmoreNemHauser( data.att48_d(att48_d), 1)

# print("Resultado Bellmore Nemhauser dantzig42_d:")
# heuristica1.BellmoreNemHauser(data.dantzig42_d(dantzig42_d), 1)

print("Resultado Bellmore Nemhauser five_d:")

five = heuristica1.BellmoreNemHauser(t, 1)
print("Caminho: :", five[0])
print("Distancia: ", five[1])
print("Tempo de execução: ", five[2])




