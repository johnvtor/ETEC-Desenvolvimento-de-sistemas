# 💧 Controle de Níveis de Água

Sistema simples de monitoramento de um reservatório de água, feito em Python e executado no terminal. O programa exibe mensagens de alerta com cores diferentes de acordo com o nível de água do reservatório.

## 📋 Sobre o projeto

O reservatório trabalha com **5 níveis**, do mais baixo até o máximo. Cada nível tem uma situação e uma cor associada:

| Nível | Situação            | Cor      |
|-------|---------------------|----------|
| 1     | Muito baixo (crítico) | 🔴 Vermelho |
| 2     | Baixo               | 🟡 Amarelo  |
| 3     | Médio               | 🟢 Verde    |
| 4     | Alto                | 🔵 Ciano    |
| 5     | Muito alto (alerta) | 🔵 Azul     |

## 🛠️ Tecnologias utilizadas

- Python 3
- Biblioteca [colorama](https://pypi.org/project/colorama/) (para colorir o texto no terminal)

## ⚙️ Como instalar

1. Certifique-se de ter o Python instalado.
2. Instale a biblioteca `colorama`:

```bash
pip install colorama
```

Se o comando acima não funcionar, tente:

```bash
python -m pip install colorama
```

## ▶️ Como executar

No terminal, dentro da pasta do projeto, rode:

```bash
python app.py
```

## 🧠 Como funciona

- **Lista `situacoes`:** guarda as mensagens de cada nível do reservatório (do nível 1 ao nível 5).
- **Função `definir_cor(nivel)`:** recebe o nível e retorna a cor correspondente usando o `Fore` do colorama.
- **Variável `nivel_atual`:** simula o nível atual do reservatório. Os valores são definidos direto no código, sem entrada do usuário.
- **`Style.RESET_ALL`:** restaura o estilo padrão do terminal depois das mensagens coloridas.

## 🧪 Testando outros níveis

Para simular outra situação, altere o valor da variável `nivel_atual` no código (de 1 a 5):

```python
nivel_atual = 4
```

## 💻 Exemplo de saída

```
=== Monitoramento do Reservatório ===
Situação atual: Nível 2 - Baixo

=== Todos os níveis ===
Nível 1 - Muito baixo (CRÍTICO)
Nível 2 - Baixo
Nível 3 - Médio
Nível 4 - Alto
Nível 5 - Muito alto (ALERTA)
```

No terminal, cada linha aparece na cor correspondente ao seu nível.

## 📚 Conceitos praticados

- Listas
- Funções
- Estruturas condicionais (`if`, `elif`, `else`)
- Laço de repetição (`for`)
- Uso de bibliotecas externas

## 👨‍💻 Autor

Projeto desenvolvido como atividade de estudo de Python.