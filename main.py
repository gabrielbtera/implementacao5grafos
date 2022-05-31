import algoritimos.BellmoreENemhauser as heuristica1
import arquivosTestes.dadosFormatados as data


att48_d = open("./arquivosTestes/att48_d.txt", 'r')
dantzig42_d = open('./arquivosTestes/dantzig42_d.txt', 'r')


heuristica1.imprimeCicloHamiltoniano(data.dantzig42_d(dantzig42_d), 42, 1)


