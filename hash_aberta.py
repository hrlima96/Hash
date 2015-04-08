class Hash_aberta():
    tabela = []
    tam = 0
    
    def __init__(self, tam):
        self.tam = tam
        self.tabela = [[] for num in range(tam)]
        
    def __str__(self):
        return str(self.tabela)
    
    def inserir(self, elemento):
        pos = int(elemento[:elemento.find(":")]) % self.tam
        
        self.tabela[pos].append(elemento)
        
    def remover(self, indice):
        pos = indice % self.tam
        
        for elem in self.tabela[pos]:
            if indice == int(elem[:elem.find(":")]):
                self.tabela[pos].pop(self.tabela[pos].index(elem))
