# Pesquisa de Satisfação

Programa em Python que coleta e exibe o resultado de uma pesquisa de opinião sobre o atendimento ao cliente da empresa de marketing **TudoWeb**.

## Objetivo

Descobrir o grau de satisfação dos clientes com o atendimento prestado, entrevistando **50 pessoas**.

## Como funciona

Para cada entrevistado, o programa pede:

- **Nome**
- **Idade**
- **Opinião** sobre o atendimento:
  - `1` - EXCELENTE
  - `2` - BOM
  - `3` - RUIM

Ao final das entrevistas, o programa exibe na tela:

- a) Quantidade de respostas **EXCELENTE**
- b) Quantidade de respostas **RUIM**

## Conceitos utilizados

- Estrutura de repetição `for` (com `range`)
- Estruturas de decisão (`if`, `elif`, `else`)
- Entrada de dados com `input()`
- Contadores (variáveis que somam 1 a cada resposta)


## Como executar

1. Salve o código em um arquivo, por exemplo `pesquisa.py`.
2. Abra o terminal na pasta do arquivo.
3. Execute:

```bash
python pesquisa.py
```

**Resultado esperado:**

```
--- RESULTADO DA PESQUISA ---
Quantidade de respostas EXCELENTE: 5
Quantidade de respostas RUIM: 2
```

Depois do teste, volte para `range(50)` na versão final.

## Observações

- Se for digitado um número diferente de 1, 2 ou 3, o programa avisa que a opinião é inválida e **não conta** essa resposta.
