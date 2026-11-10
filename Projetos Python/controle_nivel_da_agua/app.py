from colorama import Fore, Style

# Lista com as situações do reservatório (do nível 1 ao nível 5)
situacoes = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# Função que define a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    else:
        return Fore.BLUE

# Simulação: valores definidos no código (níveis de 1 a 5)
nivel_atual = 2

print("=== Monitoramento do Reservatório ===")

# Mostra a situação atual do reservatório
cor = definir_cor(nivel_atual)
mensagem = situacoes[nivel_atual - 1]
print(cor + "Situação atual: " + mensagem)

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL)

# Mostra todos os níveis para exemplo
print("=== Todos os níveis ===")
for i in range(1, 6):
    cor = definir_cor(i)
    print(cor + situacoes[i - 1])

# Restaura o estilo padrão no final
print(Style.RESET_ALL)