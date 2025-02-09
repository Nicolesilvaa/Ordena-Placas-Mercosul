# Objetivo: 🚀

- Reforçar a importância do estudo da análise de sua complexidade na avaliação de algoritmos;
- Analisar os requisitos de um problema real, propondo uma solução computacional;
- Construir um protótipo de teste baseado na solução proposta;
- Entender os processos de manipulação de arquivos em Python.


# O Problema: 📍
Uma startup está iniciando o desenvolvimento de uma aplicação para monitorar o tráfego de veículos em várias cidades da América Latina, a procura de carros roubados ou com alguma pendência judicial. O sistema irá captar imagens dos carros através de câmeras de monitoramento de tráfego. Um sistema de visão computacional extrairá a numeração da placa e informará ao sistema. Uma busca pela placa do veículo será feita e caso seja encontrado algum problema, um alerta será disparado para que o veículo possa ser rastreado pelas câmeras dos arredores, até que a força policial o alcance.

A base de dados do sistema é formada pela integração de diversas bases regionais/nacionais fornecidas pelos países latino-americanos. Essas bases são atualizadas em tempos distintos, e portanto, devem ser integradas/ordenadas regularmente. Todo o processamento da base de dados será feito em um datacenter/nuvem, com diversos nós formados por GPUs com alto poder de processamento paralelo. Portanto, a escolha dos algoritmos que irão processar esses dados deve considerar que o algoritmo poderá fazer uso de paralelismo na sua versão de produção [5].

Nesse momento a empresa está interessada em contratar programadores capazes de propor soluções criativas e eficientes para os problemas do sistema a ser desenvolvido. Como parte da avaliação para as vagas de programador, foi solicitado que os candidatos propusessem um algoritmo para a etapa de ordenação da base de dados de placas de veículos, no formato PIV. As melhores propostas serão consideradas para que os candidatos prossigam no processo seletivo.

# Produtos Esperados: ✅

A avaliação dos candidatos será baseada em dois produtos:

    Um pequeno relatório técnico onde o candidato demonstre sua capacidade de comunicação, deixando claros os critérios de escolha do algoritmo de ordenação, o quanto ele é aderente aos requisitos do problema e indicando a sua complexidade 2;
    Uma aplicação protótipo, codificada em Python, que permita comprovar a eficiencia do algoritmo de ordenação escolhido.

Para a construção do protótipo o candidato deve seguir os seguintes critérios:

    O protótipo deve ser codificado em Python, sem dependencias externas 3 e sem o uso de estruturas de dados prontas da linguagem 4.
    Como entrada o seu protótipo deve ler um arquivo texto (ASCII) com uma base de dados de placas PIV não ordenadas;
    Como saída, seu protótipo produzirá um novo arquivo texto (ASCII) com a base de dados ordenada lexicograficamente;
    O código do seu protótipo deve utilizar os conceitos de Tipo Abstrato de Dados / Classes e Modularização;


# Relatório da solução proposta📋

## Algoritmo de ordenação Utilizado: _Radix Sort_ 

> Esse algoritmo de ordenação seleciona os dígitos mais à direita dos elementos e, por meio da ordenação dos elementos com base nesses dígitos, ele organiza o vetor. O processo é repetido para os  dígitos subsequentes dos elementos até que o vetor esteja ordenado. Vale ressaltar que o Radix Sort utiliza uma ordenação estável para ordenar o arranjo (Cormen et al., 2024, p. 138). Nesta solução, utilizarei o Counting Sort.

### Funcionamento básico do Counting Sort:
> - Primeiro, é necessário criar uma vetor de índices que tenha o tamanho do valor máximo  que será encontrado no vetor principal que desejamos ordenar. 
> - Logo após, um novo vetor é criado para fazer a contagem da ocorrência de cada valor no vetor principal.Esse vetor tem o mesmo tamanho do vetor dos índices e todos seus elementos são iguais a zero.
> - Para cada elemento do vetor principal, localizamos o índice correspondente no vetor de índices e incrementamos a contagem nessa posição.
Por exemplo, se temos o número 5 no vetor original, procuramos a posição 5 no vetor de contagem e somamos 1 na posição 5. 
> - Após todo o processo, para cada posição do vetor de contagem, somamos o valor das posições anteriores.
> - Por fim, criaremos um vetor de saída que terá o mesmo tamanho do vetor de entrada. Primeiro pegamos os elementos do vetor principal de trás para frente  e analisamos elemento por elemento. 
> - Tomamos como exemplo o elemento 5 (presente no vetor principal): no vetor dos índices procuramos qual valor está na posição 5. Suponha que esse valor seja 6. Logo, no vetor de saída, na posição 6, teremos o elemento 5. Assim ordenamos todos os elementos. Vale ressaltar que, no processo de determinar a posição correta dos elementos, decrementamos a contagem do vetor à medida que os elementos são posicionados. 

### Complexidade: ⛓️

> O radix será linear quando o número de dígitos  k for pequeno em relação ao número de elementos do vetor. Ou seja, quando cada dígito está no intervalo de 0 a k-1  e k não é muito grande.(Cormen et al., 2024, p. 139)

- **Melhor caso:** O(n+k)
- **Caso Médio:** O(n+k)
- **Pior caso:** O(n+k)

### Demonstração em vídeo do algoritmo💻

![RadixSort](https://github.com/MATA40-EDA-2024-2/atividade-unidade-i-Nicolesilvaa/blob/main/imgs/RadixSort.gif)

_Fonte: https://www.sortvisualizer.com/radixsort/_

*** 
## Justificativa da escolha 📌

> Como as placas serão lidas como elementos que precisam ser ordenados pelos seus dígitos e na ordem lexicográfica, essa solução pode ser ideal para o problema. Além disso, o Radix Sort tem sua complexidade baseada no número de elementos(n) da lista e no número de dígitos(k) de cada elemento. Esse fator só seria preocupante em problemas onde o número de dígitos é variável. No problema apresentado, o número de dígitos é fixo (k=7), ou seja, uma constante, o que faz com que a complexidade do algoritmo seja linear e se adeque perfeitamente ao problema.

> **_Por que não usar outros algoritmos, como os apresentados na sala de aula: Merge,Quick e Bubble Sort?_**   
O **Merge** vai gerar divisões  sucessivas e isso pode não funcionar para uma quantidade grande de elementos. O **Quick** no seu pior caso pode chegar na ordem O(n²), que é o que não queremos. Por fim, o **Bubble sort** não é eficiente para uma grande quantidade de elemntos, uma vez que sua ordem é O(n²). Além disso, nenhum desses algoritmos trabalham bem a ideia de ordenação a partir dos dígitos individuais de cada elemento do vetor.

***
## Código base do algoritmo de ordenação 👾
(Fora do contexto da atividade)

```python

def contagem_por_digito(vet, posicao_digito): 

    n = len(vet)
    vetOrdenado = [0] * n
    contaDigitos = [0] * 10

    for num in vet:
        digito = (num // posicao_digito) % 10
        contaDigitos[digito] += 1

    # Atualizando o vetor de contagem para representar as posições acumuladas
    for i in range(1, 10):
        contaDigitos[i] += contagem_digitos[i - 1]

    # Construção do vetor ordenado a partir do vetor original
    for i in range(n - 1, -1, -1):  # Começando do final do vetor
        num = vet[i]
        digito = (num // posicao_digito) % 10
        vetOrdenado[contagem_digitos[digito] - 1] = num
        contaDigitos[digito] -= 1

    # Copiando o vetor ordenado de volta para o vetor original
    for i in range(n):
        vet[i] = vetOrdenado[i]

def ordenacao_radix(vet):

    maior_valor = max(vet)
    posicao_digito = 1

    # Ordena até que o maior número não tenha mais dígitos a processar
    while maior_valor // posicao_digito > 0:
        contagem_por_digito(vet, posicao_digito)
        posicao_digito *= 10

```
_Fonte: https://www.sortvisualizer.com/radixsort/_

***
#### **Obs: Para rodar corretamente a solução é necessário está dentro do diretório "solucao"**

## Referências: 📚

- Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C.**Algoritmos – Teoria e Prática.** Gen LTC. 4a Edição, 2024.
- **Quick Sort**. Disponível em: https://www.youtube.com/watch?v=qRHSJ_EoFAQ. Acesso em: 21 nov. 2024.

- **Ordenação Radix Sort - Ordenação por Dígitos.** YouTube, 2024. Disponível em: https://www.youtube.com/watch?v=Lb_1R6JGD6o. Acesso em: 21 nov. 2024.

- **Counting Sort - Ordenação po Contagem.** Youtube,2024. Disponível em: https://www.youtube.com/watch?v=zzjEhqwvQZI&t=10s.

- N. Satish, M. Harris, and M. Garland. **Designing efficient sorting algorithms for manycore GPUs**. NVIDIA Technical Report NVR-2008-001, September 2008. Disponível em: https://mgarland.org/files/papers/nvr-2008-001.pdf

- SCHOUERY, Rafael C. S. Unidade 21: **Ordenação Linear**. 2024. Universidade Estadual de Campinas. Disponível em: https://www.ic.unicamp.br/~rafael/slides/mc202/unidade21-ordenacao-linear-handout.pdf. Acesso em: 21 nov. 2024.

### Autora: Nicole Silva 🧙🏿‍♀️
