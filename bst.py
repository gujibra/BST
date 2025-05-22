from graphviz import Digraph

class No:
    def __init__(self, valor:int):
        self.valor = valor
        self.esq = None
        self.dir = None


class Arvore:
    def __init__(self):
        self.raiz = None

    def imprimir(self):
        def em_ordem(no):
            if no is not None:
                em_ordem(no.esq)
                print(no.valor, end=' ')
                em_ordem(no.dir)
    
        em_ordem(self.raiz)
        print() 


    def inserir(self, valor):
      if isinstance(valor, list):
        for i in valor:
            self._inserir_valor(i)
      else:
        self._inserir_valor(valor)

    def _inserir_valor(self, valor:int):
        no = No(valor)
        if(self.raiz == None):
            self.raiz = no
            return        
        noAtual = self.raiz
        while True:
            if(no.valor < noAtual.valor):
                if noAtual.esq == None:
                    noAtual.esq = no
                    return
                noAtual = noAtual.esq
            if(no.valor > noAtual.valor):
                if noAtual.dir == None:
                    noAtual.dir = no
                    return
                noAtual = noAtual.dir
            if(no.valor == noAtual.valor):
                return
        
    def buscar(self, valor):
        pai = None
        noAtual = self.raiz
        while noAtual is not None:
            if noAtual.valor == valor:
                return pai, noAtual
            elif valor < noAtual.valor:
                pai = noAtual
                noAtual = noAtual.esq
            else:
                pai = noAtual
                noAtual = noAtual.dir
        return None, None
    
    def remover(self, valor):
      pai, no = self.buscar(valor)
      if no is None:
          return  
      if no.esq is None and no.dir is None:
          if pai is None:
              self.raiz = None
          else:
              self.remover_aux(pai, no, None)
      elif no.esq is None:
          if pai is None:
              self.raiz = no.dir
          else:
              self.remover_aux(pai, no, no.dir)
      elif no.dir is None:
          if pai is None:
              self.raiz = no.esq
          else:
              self.remover_aux(pai, no, no.esq)     
      else:        
          sucessor_pai = no
          sucessor = no.dir
          while sucessor.esq is not None:
              sucessor_pai = sucessor
              sucessor = sucessor.esq

          no.valor = sucessor.valor 
          if sucessor.dir is not None:
              self.remover_aux(sucessor_pai, sucessor, sucessor.dir)
          else:
              self.remover_aux(sucessor_pai, sucessor, None)

    
    def plotar(self):
        dot = Digraph()
        
        def adicionar_nos(no):
            if no is None:
                return
            dot.node(str(id(no)), str(no.valor))  

            if no.esq is not None:
                dot.edge(str(id(no)), str(id(no.esq)), label="esq")
                adicionar_nos(no.esq)
            if no.dir is not None:
                dot.edge(str(id(no)), str(id(no.dir)), label="dir")
                adicionar_nos(no.dir)

        adicionar_nos(self.raiz)
        return dot

                   
    def remover_aux(self, pai: No, no: No, substituto: No):
        if pai.dir == no:
            pai.dir = substituto
        elif pai.esq == no:
            pai.esq = substituto


        
