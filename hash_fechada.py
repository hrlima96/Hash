class Hash_fechada():
    
    tabela = []
    tam = 0
    
    def __init__(self, tam):
        self.tam = tam
        self.tabela = ["vazio" for num in range(tam)]
        
    def __str__(self):
        return str(self.tabela)
    
    def inserir(self, elemento):
        pos = int(elemento[:elemento.find(":")]) % self.tam
        
        if self.tabela[pos] == "vazio":
            self.tabela.pop(pos)
            self.tabela.insert(pos, elemento)
        else:
            while self.tabela[pos] != "vazio":
                if pos + 1 == self.tam:
                    pos = 0
                else:
                    pos += 1
            
            self.tabela.pop(pos)
            self.tabela.insert(pos, elemento)
            
    def remover(self, indice):
        pos = indice % self.tam
        
        if self.tabela[pos] != "vazio" and indice == int(self.tabela[pos][:self.tabela.find(":")]):
            self.tabela.pop(pos)
            self.tabela.insert(pos, "vazio")
            
            for elem in self.tabela:
                if elem != "vazio" and int(elem[:elem.find(":")]) % self.tam == pos:
                    self.tabela.pop(self.tabela.index(elem))
                    self.tabela.insert(pos, elem)
                    break
        else:
            while self.tabela[pos] != "vazio" and indice != int(self.tabela[pos][:self.tabela.find(":")]):
                if pos + 1 == self.tam:
                    pos = 0
                else:
                    pos += 1
            
            self.tabela.pop(pos)
            self.tabela.insert(pos, "vazio")
            
            for elem in self.tabela:
                if elem != "vazio" and int(elem[:elem.find(":")]) % self.tam == pos:
                    self.tabela.pop(self.tabela.index(elem))
                    self.tabela.insert(pos, elem)
                    break
