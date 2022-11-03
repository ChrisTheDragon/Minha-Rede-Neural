inputs = [[0, 0, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0]]
target = [1, 1, 0, 0]

peso = [0, 0, 0]
delta_peso = [0, 0, 0]
vies = 0
delta_vies = 0
lr = 0.1
voltas = 2

input_fi = []
y_input = [0, 0, 0, 0]

def neuron(inputx):
    z = 0
    for i in range(len(inputx)):
        x = inputx[i] * peso[i]
        z += x
    return z + vies


def ativacao(fi):
    if(fi > 0):
        return 1
    elif (fi <= 0):
        return 0


def treinamento(inputx, targetx, y_inputx):
    global delta_vies, vies
    for i in range(0, len(inputx)):
            delta_peso[i] = lr * (targetx - y_inputx) * inputx[i]
            peso[i] += delta_peso[i]
    delta_vies = lr * (targetx - y_inputx) * 1
    vies += delta_vies


for i in range(voltas):
    for j in range(4):
        y_input[j] = ativacao(neuron(inputs[j]))
        
        if (y_input[j] != target[j]):
            treinamento(inputs[j], target[j], y_input[j])
        
        print(peso, vies)
        print('\n')
    j = 0   

print("\n")
input_n = [0, 0, 0]
y = neuron(input_n)
print(ativacao(y))

input_n2 = [0, 0, 1]
y1 = neuron(input_n2)
print(ativacao(y1))

input_n3 = [1, 1, 1]
y2 = neuron(input_n3)
print(ativacao(y2))