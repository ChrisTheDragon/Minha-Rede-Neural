inputs = [[0, 0, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0]]
target = [1, 1, 0, 0]

w_peso = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
delta_peso = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
b_vies = 0
delta_vies = 0
lr_taxaAprendizado = 0.1


def print_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'[{matriz[i][j]}]', end='')
        print()


def perception(input, peso):
    for inp, pes in zip(input, peso):
        z = inp * pes + b_vies
    return z


out = [perception(inp, pes) for inp, pes in zip(inputs, w_peso)]

for i in range(len(delta_peso)):
    for j in range(len(delta_peso[i])):
        delta_peso[i][j] = lr_taxaAprendizado * (target[i] - out[i]) * inputs[i][j]
        w_peso[i][j] += delta_peso[i][j]
    delta_vies = lr_taxaAprendizado * (target[i] - out[i]) * 1
    b_vies += delta_vies

print(out)
print_matriz(w_peso)
print(b_vies)