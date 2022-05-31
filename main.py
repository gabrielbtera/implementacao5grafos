import algoritimos.BellmoreENemhauser as heuristica1
import arquivosTestes.dadosFormatados as data


att48_d = open("./arquivosTestes/att48_d.txt", 'r')
dantzig42_d = open('./arquivosTestes/dantzig42_d.txt', 'r')

heuristica1.buscaGulosa( data.att48_d(att48_d), 1)


