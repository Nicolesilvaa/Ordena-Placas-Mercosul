# Classe para criar EAD vetor

class Cvetor:

# *******************************************************
    def __init__(self, n):

        self.vet        = [None] * n
        self.maxObjs    = n
        self.len    = 0

    def setElementos(self,elemento):

        if self.len < self.maxObjs:
            self.vet[self.len] = elemento
            self.len += 1

    def getElementos(self):

        elementos = []
        for i in range(self.len):
            elementos.append(self.vet[i])

        return elementos


    def leng(self):
        return self.len

    #Funções de ordenação ----------------------------------------------
    def radixSort(self):

        #Criando funções para o couting sort

        #Função de ordenação para as placas ------------------------------------------------------------------
        def countingSort(posicaoDigito):

            k =  self.len
            maxElem = 256 # Uma vez que estou trabalhado com caracteres ASCII esqueci desse detalhe na última solução
            vetorOrdenado = [' '] * k
            contador = [0] * maxElem 

            # Conta e armazena a ocorrência dos elementos do vetor principal
            for i in range(k):

                digito = self.vet[i][posicaoDigito] 
                index =  ord(digito) # A função ord retorna um valor númerico de um caracter, de acordo com a tabela ASCII
                contador[index] += 1

            #Armazena a contagem acumulada
            for i in range(1, maxElem):
                contador[i] += contador[i - 1]

            # Encontra o índice de cada elemento da matriz original na matriz de contagem e coloca os elementos na matriz de saída
            i = k - 1
            while i  >= 0:

                digito = self.vet[i][posicaoDigito] 
                index =  ord(digito)
                vetorOrdenado[contador[index] - 1] =  self.vet[i]
                contador[index] -= 1 # Decrementa a contagem

                i -= 1

            return vetorOrdenado

        
        # Código principal Radix --------------------------------------------------------------------------------

        maiorValor = 7

        #Ordenando strings, sempre de trás para frente
        for posicaoDigito in range(maiorValor - 1, -1, -1):
            self.vet = countingSort(posicaoDigito)

        return self.vet
        #----------------------------------------------------------------------------------------------------------



 