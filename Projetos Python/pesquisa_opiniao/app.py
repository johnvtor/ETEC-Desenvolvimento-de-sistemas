# Contadores para as opiniões
excelente = 0
bom = 0
ruim = 0

# Repete 50 vezes (uma para cada entrevistado)
for i in range(50):
    print("\nEntrevistado", i + 1)

    # Coleta os dados
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Digite a opinião (1, 2 ou 3): "))

    # Estrutura de decisão para verificar a opinião
    if opiniao == 1:
        excelente = excelente + 1
    elif opiniao == 2:
        bom = bom + 1
    elif opiniao == 3:
        ruim = ruim + 1
    else:
        print("Opinião inválida! Essa resposta não foi contada.")

# Resultado final
print("\n--- RESULTADO DA PESQUISA ---")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)