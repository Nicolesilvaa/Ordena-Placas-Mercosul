# Módulo para fazer a leitura e processamento dos dados
import Cvetor

#variaveis globais
n = 1110000 #Total de placas segundo os nomes dos arquivos que foram passados
armazenaPlacas = Cvetor.Cvetor(n)

def lerData(datas):

    arquivos = open(datas,'r')

    for linhas in arquivos:

        placas =  linhas.strip()
        armazenaPlacas.setElementos(placas) #Adicionando conteúdo dos arquivos em um vetor, removendo espaços e quebras de linha

    arquivos.close()

#Declaração de dados,variaveis e vetores
data1 = "../data/PIVs-DB/PIVs-10000.piv"
data2 = "../data/PIVs-DB/PIVs-100000.piv"
data3 = "../data/PIVs-DB/PIVs-1000000.piv"

#Lendo dados fornecidos
lerData(data1)
lerData(data2)
lerData(data3)

tamanhoVet = armazenaPlacas.leng()

# Fazendo a gravação de arquivos
vetorFinal = armazenaPlacas.radixSort()

docPlacasOrdenadas = open("docPlacasOrdenadas.piv", "w")
for i in  vetorFinal:
    docPlacasOrdenadas.write(i + "\n") #Escreve placas ordenadas no novo arquivos uma por linha

docPlacasOrdenadas.close() # Garante que as mudanças foram salvas

