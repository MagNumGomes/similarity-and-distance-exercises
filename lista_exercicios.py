"""
Lista de Exercícios de Fixação — Similaridade e Distância em Python
"""

# ==============================================================================
# Parte A — Sem uso de funções prontas de distância
# ==============================================================================

print("=" * 70)
print("EXERCÍCIO 1 — Distância Euclidiana entre dois clientes")
print("=" * 70)

# 1. Armazene os dados dos clientes em listas (idade, compras por mês)
cliente_a = [25, 2]
cliente_b = [28, 6]

# 2. Calcule a diferença entre as idades
dif_idade = cliente_a[0] - cliente_b[0]

# 3. Calcule a diferença entre as quantidades de compras
dif_compras = cliente_a[1] - cliente_b[1]

# 4. Eleve cada diferença ao quadrado
quad_idade = dif_idade ** 2
quad_compras = dif_compras ** 2

# 5. Some os resultados obtidos
soma_quadrados = quad_idade + quad_compras

# 6. Calcule a raiz quadrada da soma (sem usar math.dist ou funções prontas de distância)
distancia_ab = soma_quadrados ** 0.5

# 7. Exiba a distância Euclidiana entre os dois clientes
print(f"Cliente A: {cliente_a}")
print(f"Cliente B: {cliente_b}")
print(f"Diferença de idade: {dif_idade} (ao quadrado: {quad_idade})")
print(f"Diferença de compras: {dif_compras} (ao quadrado: {quad_compras})")
print(f"Soma dos quadrados: {soma_quadrados}")
print(f"Distância Euclidiana entre A e B: {distancia_ab:.4f}\n")


print("=" * 70)
print("EXERCÍCIO 2 — Qual cliente é mais semelhante ao cliente A?")
print("=" * 70)

cliente_a = [25, 2]
cliente_b = [27, 3]
cliente_c = [45, 10]
cliente_d = [52, 12]

# 8. Calcule manualmente a distância Euclidiana entre A e B
dist_ab = ((cliente_a[0] - cliente_b[0]) ** 2 + (cliente_a[1] - cliente_b[1]) ** 2) ** 0.5

# 9. Calcule manualmente a distância Euclidiana entre A e C
dist_ac = ((cliente_a[0] - cliente_c[0]) ** 2 + (cliente_a[1] - cliente_c[1]) ** 2) ** 0.5

# 10. Calcule manualmente a distância Euclidiana entre A e D
dist_ad = ((cliente_a[0] - cliente_d[0]) ** 2 + (cliente_a[1] - cliente_d[1]) ** 2) ** 0.5

# 11. Compare os três resultados e 12. Determine qual cliente possui a menor distância
distancias_ex2 = {
    "B": dist_ab,
    "C": dist_ac,
    "D": dist_ad
}

cliente_mais_proximo = min(distancias_ex2, key=distancias_ex2.get)
menor_distancia = distancias_ex2[cliente_mais_proximo]

# 13. Exiba todas as distâncias e o cliente mais próximo
print(f"Distância entre A e B: {dist_ab:.4f}")
print(f"Distância entre A e C: {dist_ac:.4f}")
print(f"Distância entre A e D: {dist_ad:.4f}")
print(f"Cliente mais próximo de A: Cliente {cliente_mais_proximo} (distância = {menor_distancia:.4f})\n")

# Explicação solicitada ao final do Exercício 2:
# Por que a menor distância indica maior semelhança segundo os atributos utilizados?
# Resposta: No espaço geométrico formado pelos atributos (idade e compras por mês), cada
# cliente é representado como um ponto. A distância Euclidiana mede o comprimento do
# segmento de reta entre dois pontos. Quanto menor a diferença numérica entre a idade e
# o número de compras de dois clientes, menor será a soma dos quadrados dessas diferenças
# e, consequentemente, menor será a distância entre eles — indicando que possuem perfis
# mais parecidos (maior similaridade).


print("=" * 70)
print("EXERCÍCIO 3 — Distância Euclidiana com três atributos")
print("=" * 70)

# Atributos: [nota média, frequência (%), horas de estudo por semana]
aluno_a = [8.0, 92, 10]
aluno_b = [7.8, 90, 9]
aluno_c = [5.2, 68, 3]

# 14. Implemente manualmente a distância Euclidiana entre A e B
dist_aluno_ab = (
    (aluno_a[0] - aluno_b[0]) ** 2 +
    (aluno_a[1] - aluno_b[1]) ** 2 +
    (aluno_a[2] - aluno_b[2]) ** 2
) ** 0.5

# 15. Implemente manualmente a distância Euclidiana entre A e C
dist_aluno_ac = (
    (aluno_a[0] - aluno_c[0]) ** 2 +
    (aluno_a[1] - aluno_c[1]) ** 2 +
    (aluno_a[2] - aluno_c[2]) ** 2
) ** 0.5

# 16. Exiba os dois resultados
print(f"Distância Euclidiana entre Aluno A e Aluno B: {dist_aluno_ab:.4f}")
print(f"Distância Euclidiana entre Aluno A e Aluno C: {dist_aluno_ac:.4f}")

# 17. Informe qual aluno está mais próximo de A
if dist_aluno_ab < dist_aluno_ac:
    aluno_proximo = "B"
    menor_dist_aluno = dist_aluno_ab
else:
    aluno_proximo = "C"
    menor_dist_aluno = dist_aluno_ac

print(f"O aluno mais próximo de A é o Aluno {aluno_proximo} (distância = {menor_dist_aluno:.4f}).")
# Observação ao final: A mesma lógica usada em 2 dimensões (soma dos quadrados das
# diferenças tirando a raiz quadrada) generaliza-se diretamente para 3 ou N atributos.
print("Observação: A fórmula da distância Euclidiana se estende naturalmente de 2D para 3D (ou n-dimensões) bastando somar os quadrados das diferenças de cada atributo adicional.\n")


# ==============================================================================
# Parte B — Com uso de funções prontas
# ==============================================================================

print("=" * 70)
print("EXERCÍCIO 4 — Comparando vários clientes com math.dist()")
print("=" * 70)

# 18. Importe o módulo math
import math

clientes = {
    "A": [25, 2],
    "B": [27, 3],
    "C": [30, 5],
    "D": [45, 10],
    "E": [52, 12]
}

# 19. Utilize math.dist() para calcular a distância de A para B, C, D e E
distancias_ex4 = {}
for nome, dados in clientes.items():
    if nome != "A":
        distancias_ex4[nome] = math.dist(clientes["A"], dados)

# 20. Exiba cada distância calculada
for nome, dist in distancias_ex4.items():
    print(f"Distância de A para {nome}: {dist:.4f}")

# 21. Identifique automaticamente o cliente mais próximo de A
mais_proximo_ex4 = min(distancias_ex4, key=distancias_ex4.get)

# Ao final: exiba uma frase informando qual cliente possui o perfil mais próximo de A
print(
    f"\nConclusão: Considerando os atributos de idade e compras por mês, o cliente {mais_proximo_ex4} "
    f"possui o perfil mais próximo de A (menor distância = {distancias_ex4[mais_proximo_ex4]:.4f}).\n"
)


print("=" * 70)
print("EXERCÍCIO 5 — Influência da escala e normalização")
print("=" * 70)

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 22. Crie um DataFrame utilizando pandas
dados_ex5 = {
    "Cliente": ["A", "B", "C", "D", "E"],
    "Idade": [20, 25, 40, 55, 70],
    "Renda": [2000, 3000, 6000, 9000, 12000]
}
df_clientes = pd.DataFrame(dados_ex5).set_index("Cliente")
print("DataFrame Original:")
print(df_clientes)
print()

# 23. Calcule com math.dist() a distância Euclidiana entre A e B usando os valores originais
dist_original_ab = math.dist(df_clientes.loc["A"], df_clientes.loc["B"])
print(f"Distância Euclidiana original entre A e B: {dist_original_ab:.4f}\n")

# 24. Normalize as colunas Idade e Renda utilizando MinMaxScaler, do scikit-learn
scaler = MinMaxScaler()
valores_normalizados = scaler.fit_transform(df_clientes[["Idade", "Renda"]])

df_normalizado = pd.DataFrame(
    valores_normalizados,
    index=df_clientes.index,
    columns=["Idade", "Renda"]
)

# 25. Exiba o DataFrame com os valores normalizados
print("DataFrame Normalizado (MinMaxScaler [0, 1]):")
print(df_normalizado)
print()

# 26. Calcule novamente a distância Euclidiana entre A e B usando os valores normalizados
dist_norm_ab = math.dist(df_normalizado.loc["A"], df_normalizado.loc["B"])
print(f"Distância Euclidiana normalizada entre A e B: {dist_norm_ab:.4f}")

# 27. Compare os dois resultados
print(f"\nComparação:")
print(f"  - Sem normalização: {dist_original_ab:.4f} (diferença de idade = 5 -> 5² = 25; diferença de renda = 1000 -> 1000² = 1.000.000)")
print(f"  - Com normalização: {dist_norm_ab:.4f} (ambas as diferenças normalizadas valem 0.1 -> 0.1² + 0.1² = 0.02)")
print(
    "\nExplicação: Quando os valores originais são utilizados, a Renda está na casa dos milhares (2.000 a 12.000), "
    "enquanto a Idade está na casa das dezenas (20 a 70). Como a distância Euclidiana eleva as diferenças ao quadrado, "
    "uma diferença de 1.000 reais gera 1.000.000 na soma, ao passo que uma diferença de 5 anos gera apenas 25. "
    "Assim, a variável de maior ordem de grandeza (Renda) domina quase 100% do cálculo da distância (1000.0125 vs 1000). "
    "A normalização coloca ambos os atributos na mesma escala [0, 1], garantindo que ambos tenham peso equivalente.\n"
)


print("=" * 70)
print("EXERCÍCIO 6 — Matriz de distâncias entre registros")
print("=" * 70)

registros = {
    "A": [1, 1],
    "B": [4, 5],
    "C": [2, 2],
    "D": [5, 4]
}

# 28. Utilize math.dist() para calcular a distância Euclidiana entre todos os pares de registros
# 29. Construa uma matriz de distâncias utilizando pandas.DataFrame
nomes_registros = list(registros.keys())
matriz_dados = {}

for r1 in nomes_registros:
    matriz_dados[r1] = {}
    for r2 in nomes_registros:
        matriz_dados[r1][r2] = math.dist(registros[r1], registros[r2])

df_matriz = pd.DataFrame(matriz_dados)
print("Matriz de Distâncias:")
print(df_matriz.round(4))
print()

# 30. Identifique o menor valor diferente de zero e 31. Informe qual é o par de registros mais próximo
valores_nao_zero = [
    df_matriz.loc[r1, r2]
    for i, r1 in enumerate(nomes_registros)
    for j, r2 in enumerate(nomes_registros)
    if i < j and df_matriz.loc[r1, r2] > 0
]
menor_valor = min(valores_nao_zero)

pares_mais_proximos = [
    (r1, r2)
    for i, r1 in enumerate(nomes_registros)
    for j, r2 in enumerate(nomes_registros)
    if i < j and math.isclose(df_matriz.loc[r1, r2], menor_valor)
]

print(f"Menor valor diferente de zero: {menor_valor:.4f}")
pares_str = ", ".join(f"({p[0]}, {p[1]})" for p in pares_mais_proximos)
print(f"Par(es) de registros mais próximo(s): {pares_str}")

# 32. Verifique que a diagonal principal possui apenas zeros
diagonal_zeros = all(df_matriz.loc[r, r] == 0.0 for r in nomes_registros)
print(f"Diagonal principal possui apenas zeros? {diagonal_zeros}")

# 33. Verifique que a matriz é simétrica
simetrica = df_matriz.equals(df_matriz.T)
print(f"A matriz é simétrica (d(X,Y) == d(Y,X))? {simetrica}")

# Comentários solicitados ao final do Exercício 6:
# 1) Por que a diagonal principal é zero?
#    Porque cada elemento da diagonal principal representa a distância de um registro para
#    ele mesmo, isto é, d(A, A). Como os atributos são idênticos, a diferença em cada
#    coordenada é 0, resultando em distância 0.
#
# 2) Por que d(A, B) = d(B, A)?
#    Porque na fórmula da distância Euclidiana as diferenças entre as coordenadas são
#    elevadas ao quadrado: (x_A - x_B)² = (-(x_B - x_A))² = (x_B - x_A)². O sinal da
#    subtração desaparece ao elevar ao quadrado, tornando a distância uma métrica simétrica
#    (a distância de A até B é exatamente igual à distância de B até A).
