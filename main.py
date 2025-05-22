from bst import Arvore

arvore = Arvore()
arvore.inserir([10,5,16,1,6,15,3,7])


arvore.imprimir()
pai, no = arvore.buscar(5)
if no:
    print(f"Valor encontrado: {no.valor} com seu pai: {pai.valor}")
else:
    print("Valor não encontrado.")
arvore.remover(5)
arvore.imprimir()
dot = arvore.plotar()
dot.render('arvore', format='png', view=True) 