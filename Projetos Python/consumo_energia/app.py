#entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em watts): "))
horasDia = float(input("Digite o número de horas de uso por dia: "))

#processamento dos dados
valorwatt = 0.75
consumoMensal = (potencia * horasDia * 30) / 1000
customensal = (consumoMensal * valorwatt)

#saida dos dados
print(f"\nAparelho: {aparelho}")
print(f"O consumo mensal do {aparelho} é de {consumoMensal:.2f} kWh.")
print(f"O consumo mensal da{aparelho} é de R$ {customensal:.2f}.")