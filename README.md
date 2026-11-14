# Lista de Exercícios — Similaridade e Distância em Python

Resolução da lista de exercícios de fixação sobre cálculo de **Distância Euclidiana**, **similaridade entre registros** e **normalização de dados** em Python.

## Estrutura do Projeto

- `docs/Lista_Exercicios_Similaridade_Distancia.pdf`: Enunciado original da lista de exercícios.
- `lista_exercicios.py`: Script contendo a resolução comentada dos 6 exercícios (33 itens).

## Conteúdo Abordado

- **Parte A — Sem uso de funções prontas (`** 0.5`)**
  - **Exercício 1:** Cálculo passo a passo da distância Euclidiana entre dois clientes (2 atributos).
  - **Exercício 2:** Comparação de múltiplos clientes para encontrar o perfil mais semelhante ao cliente de referência.
  - **Exercício 3:** Distância Euclidiana estendida para 3 atributos (nota média, frequência e horas de estudo).
- **Parte B — Com uso de funções prontas**
  - **Exercício 4:** Automação do cálculo de distância utilizando `math.dist()`.
  - **Exercício 5:** Análise do impacto da escala dos atributos e normalização com `pandas` e `MinMaxScaler` (`scikit-learn`).
  - **Exercício 6:** Construção e validação de uma matriz de distâncias (`DataFrame`), verificando diagonal nula e simetria.

## Como Executar

1. Instale as dependências necessárias (para os exercícios 5 e 6):
   ```bash
   pip install pandas scikit-learn
   ```
2. Execute o script:
   ```bash
   python lista_exercicios.py
   ```
