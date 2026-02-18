preço = float(input("Qual o preço do livro?: "))
novo = preço - (preço * 25 / 100)
print('O preço original era {}R$, e com o desconto de 25% vai ficar {}R$'.format(preço, novo))