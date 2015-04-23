class Hash_aberta():
    tabela = []
    tam = 0
    #construtor    
    def __init__(self, tam):
        self.tam = tam
        self.tabela = [[] for num in range(tam)]
        
    def __str__(self):
        return str(self.tabela)
    
    def inserir(self, elemento):
        #Procura o elemento antes dos ":" e checa o resto da divisão com o 
        #tamanho da lista
        pos = int(elemento[:elemento.find(":")]) % self.tam
        #Insere o elemento na lista referente a posição 
        self.tabela[pos].append(elemento)
        
    def remover(self, indice):
        #Calcula a posição de acordo com o indice
        pos = indice % self.tam
        #para cada string dentro da lista na referida posição
        for elem in self.tabela[pos]:
            #verifica se o indice é igual ao que existe na lista
            if indice == int(elem[:elem.find(":")]):
                #remove de acordo com a posição da lista
                self.tabela[pos].pop(self.tabela[pos].index(elem))
                
    def busca(self, indice):
        
        pos = indice % self.tam
        #para cada posição da lista
        for elem in self.tabela[pos]:
            #verifica se o indice procurado é igual ao indice do elemento da lista
            if indice == int(elem[:elem.find(":")]): 
                #faz um Slice(corte da string)
                return elem[elem.find(":") + 2:]
