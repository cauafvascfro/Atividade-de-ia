import numpy as np
import matplotlib.pyplot as plt


def funcao_ativacao(u):
    return 1 if u > 0 else -1


taxa_aprendizado = 0.1


dados = np.array([
    [-1, -0.6508, 0.1097, 4.0009, -1.0000],
    [-1, -1.4492, 0.8896, 4.4005, -1.0000],
    [-1, 2.0850,0.6876, 12.0710, -1.0000],
    [-1, 0.2626,1.1476, 7.7985, 1.0000],
    [-1, 0.6418,1.0234, 7.0427, 1.0000],
    [-1, 0.2569,0.6730, 8.3265, -1.0000],
    [-1, 1.1155,0.6043, 7.4446, 1.0000],
    [-1, 0.0914,0.3399, 7.0677, -1.0000],
    [-1, 0.0121,0.5256, 4.6316, 1.0000],
    [-1, -0.0429, 0.4660, 5.4323, 1.0000],
    [-1, 0.4340,0.6870 ,8.2287, -1.0000],
    [-1, 0.2735,1.0287, 7.1934, 1.0000],
    [-1, 0.4839,0.4851, 7.4850, -1.0000],
    [-1, 0.4089,-0.1267, 5.5019, -1.0000],
    [-1, 1.4391,0.1614, 8.5843, -1.0000],
    [-1, -0.9115, -0.1973, 2.1962, -1.0000],
    [-1, 0.3654,1.0475, 7.4858, 1.0000],
    [-1, 0.2144,0.7515, 7.1699, 1.0000],
    [-1, 0.2013,1.0014 ,6.5489, 1.0000],
    [-1, 0.6483,0.2183, 5.8991, 1.0000],
    [-1, -0.1147, 0.2242, 7.2435, -1.0000],
    [-1, -0.7970, 0.8795, 3.8762, 1.0000],
    [-1, -1.0625, 0.6366, 2.4707,1.0000],
    [-1, 0.5307,0.1285, 5.6883, 1.0000],
    [-1, -1.2200, 0.7777, 1.7252, 1.0000],
    [-1, 0.3957,0.1076, 5.6623, -1.0000],
    [-1, -0.1013, 0.5989, 7.1812, -1.0000],
    [-1, 2.4482,0.9455, 11.2095, 1.0000],
    [-1, 2.0149,0.6192, 10.9263, -1.0000],
    [-1, 0.2012,0.2611, 5.4631, 1.0000]
])


np.random.shuffle(dados)
split = int(len(dados) * (2/3))
dados_treino = dados[:split]
dados_teste = dados[split:]


pesos = np.random.uniform(-1, 1, dados.shape[1] - 1)


acuracias_por_epoca = []
epocas = 0
acuracia = 0


while acuracia < 70:
    erro_total = 0
    for amostra in dados_treino:
        x = amostra[:-1]
        y_real = amostra[-1]

        u = np.dot(x, pesos)
        y_pred = funcao_ativacao(u)

        erro = y_real - y_pred
        erro_total += abs(erro)

        pesos += taxa_aprendizado * erro * x

  
    acertos = 0
    for amostra in dados_teste:
        x_teste = amostra[:-1]
        y_real = amostra[-1]

        u = np.dot(x_teste, pesos)
        y_pred = funcao_ativacao(u)

        if y_pred == y_real:
            acertos += 1

    acuracia = (acertos / len(dados_teste)) * 100
    acuracias_por_epoca.append(acuracia)
    epocas += 1

    if epocas > 50:
        print("Não atingiu 70% de acurácia em 50 épocas.")
        break


print(f"\nAcurácia final: {acuracia:.2f}% após {epocas} épocas")
print(f"Pesos finais: {pesos}")

plt.figure(figsize=(10, 5))
plt.plot(range(1, epocas + 1), acuracias_por_epoca, marker='o', linestyle='-')
plt.title("Acurácia por Época até atingir 70%")
plt.xlabel("Época")
plt.ylabel("Acurácia (%)")
plt.ylim(0, 100)
plt.grid()
plt.show()
