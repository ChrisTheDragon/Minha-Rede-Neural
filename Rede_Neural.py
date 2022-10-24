input1 = [0, 0, 1]
input2 = [1, 0, 1]
input3 = [1, 1, 1]
input4 = [1, 1, 0]
target = [1, 1, 0, 0]

w1_peso = 0
w2_peso = 0
w3_peso = 0
delta_peso1 = 0
delta_peso2 = 0
delta_peso3 = 0
b_vies = 0
delta_vies = 0
lr_taxaAprendizado = 0.1


def print_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'[{matriz[i][j]}]', end='')
        print()


def perception(inputx):
    z = inputx[0] * w1_peso + inputx[1] * w2_peso + inputx[2] * w3_peso + b_vies
    return z


def ativacao(fi):
    if(fi > 0):
        return 1
    elif (fi <= 0):
        return 0



pare = 0

while (pare < 4):
    y_predi1 = perception(input1)
    y1_predi1 = ativacao(y_predi1)

    if(y1_predi1 != target[0]):
        delta_peso1 = lr_taxaAprendizado * (target[0] - y1_predi1) * input1[0]
        delta_peso2 = lr_taxaAprendizado * (target[0] - y1_predi1) * input1[1]
        delta_peso3 = lr_taxaAprendizado * (target[0] - y1_predi1) * input1[2]

        w1_peso += delta_peso1
        w2_peso += delta_peso2
        w3_peso += delta_peso3

        delta_vies = lr_taxaAprendizado * (target[0] - y1_predi1) * 1
        b_vies += delta_vies

        print("\n")
        print(w1_peso)
        print(w2_peso)
        print(w3_peso)
        print(b_vies)

    y_predi2 = perception(input2)
    y2_predi2 = ativacao(y_predi2)

    if (y2_predi2 != target[1]):
        delta_peso1 = lr_taxaAprendizado * (target[1] - y2_predi2) * input2[0]
        delta_peso2 = lr_taxaAprendizado * (target[1] - y2_predi2) * input2[1]
        delta_peso3 = lr_taxaAprendizado * (target[1] - y2_predi2) * input2[2]

        w1_peso += delta_peso1
        w2_peso += delta_peso2
        w3_peso += delta_peso3

        delta_vies = lr_taxaAprendizado * (target[1] - y2_predi2) * 1
        b_vies += delta_vies

        print("\n")
        print(w1_peso)
        print(w2_peso)
        print(w3_peso)
        print(b_vies)

    y_predi3 = perception(input3)
    y3_predi3 = ativacao(y_predi3)

    if (y3_predi3 != target[2]):
        delta_peso1 = lr_taxaAprendizado * (target[2] - y3_predi3) * input3[0]
        delta_peso2 = lr_taxaAprendizado * (target[2] - y3_predi3) * input3[1]
        delta_peso3 = lr_taxaAprendizado * (target[2] - y3_predi3) * input3[2]

        w1_peso += delta_peso1
        w2_peso += delta_peso2
        w3_peso += delta_peso3

        delta_vies = lr_taxaAprendizado * (target[2] - y3_predi3) * 1
        b_vies += delta_vies

        print("\n")
        print(w1_peso)
        print(w2_peso)
        print(w3_peso)
        print(b_vies)
        
    y_predi4 = perception(input4)
    y4_predi4 = ativacao(y_predi4)

    if (y4_predi4 != target[3]):
        delta_peso1 = lr_taxaAprendizado * (target[3] - y4_predi4) * input4[0]
        delta_peso2 = lr_taxaAprendizado * (target[3] - y4_predi4) * input4[1]
        delta_peso3 = lr_taxaAprendizado * (target[3] - y4_predi4) * input4[2]

        w1_peso += delta_peso1
        w2_peso += delta_peso2
        w3_peso += delta_peso3

        delta_vies = lr_taxaAprendizado * (target[3] - y4_predi4) * 1
        b_vies += delta_vies

        print("\n")
        print(w1_peso)
        print(w2_peso)
        print(w3_peso)
        print(b_vies)
        
    pare+=1


print("\n")
input_n = [0, 0, 0]
y = perception(input_n)
print(ativacao(y))