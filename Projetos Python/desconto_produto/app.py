#entrada de dados para o cálculo do desconto
preco = float(input("Digite o preço do produto: R$ "))

#processamento do desconto com base no preço do produto
if preco < 200:
    desconto = 5
elif preco >= 200 and preco < 300:
    desconto = 10
else:
    desconto = 15

valor_final = preco - (preco * desconto / 100)

#saida do valor final do produto com desconto
print(f"\nPreço do produto com desconto: R${valor_final:.2f}")