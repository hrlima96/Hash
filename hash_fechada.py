class Hash_fechada():
    
    tabela = []
    tam = 0
    num_elementos = 1
    
    def __init__(self, tam):
        self.tam = tam
        self.tabela = ["vazio" for num in range(tam)]
        
    def __str__(self):
        return str(self.tabela)
    
    def inserir(self, elemento):
        if self.num_elementos == self.tam - 1:
            print "Nao pode mais inserir!"
            return
        
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
            
            self.num_elementos += 1
            print self.num_elementos
            
    def remover(self, indice):
        pos = indice % self.tam
        
        if self.tabela[pos] != "vazio" and indice == int(self.tabela[pos][:self.tabela[pos].find(":")]):
            self.tabela.pop(pos)
            self.tabela.insert(pos, "vazio")
            
            for elem in self.tabela:
                if elem != "vazio" and int(elem[:elem.find(":")]) % self.tam == pos:
                    self.tabela.pop(self.tabela.index(elem))
                    self.tabela.insert(pos, elem)
                    break
        else:
            while self.tabela[pos] != "vazio" and indice != int(self.tabela[pos][:self.tabela[pos].find(":")]):
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
                
    def busca(self, indice):
        pos = indice % self.tam
        if self.tabela[pos] != "vazio" and indice == int(self.tabela[pos][:self.tabela[pos].find(":")]):
            print self.tabela[pos]
        else:
            while self.tabela[pos] != "vazio" and indice != int(self.tabela[pos][:self.tabela[pos].find(":")]):
                if pos + 1 == self.tam:
                    pos = 0
                else:
                    pos += 1
                   
                if indice == int(self.tabela[pos][:self.tabela[pos].find(":")]):
                    return self.tabela[pos][self.tabela[pos].find(":") + 2:]
