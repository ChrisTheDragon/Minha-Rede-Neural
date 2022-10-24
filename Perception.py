input1 = [0, 0, 1]
input2 = [1, 0, 1]
input3 = [1, 1, 1]
input4 = [1, 1, 0]
target = [1, 1, 0, 0]

peso = [0, 0, 0]
delta_peso = [0, 0, 0]
vies = 0
delta_vies = 0
lr = 0.1
voltas = 2
        

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
    for i in range(0, len(inputx)):
            delta_peso[i] = lr * (targetx - y_inputx) * inputx[i]
            peso[i] += delta_peso[i]


cont = 0
while(cont < voltas):
    
    input1_fi = neuron(input1)
    y_input1 = ativacao(input1_fi)
    
    if(y_input1 != target[0]):
        treinamento(input1, target[0], y_input1)
        
        delta_vies = lr * (target[0] - y_input1) * 1
        vies += delta_vies
    
    print(peso, vies)
    print('\n')

    input2_fi = neuron(input2)
    y_input2 = ativacao(input2_fi)
    
    if(y_input2 != target[1]):
        treinamento(input2, target[1], y_input2)
        
        delta_vies = lr * (target[1] - y_input2) * 1
        vies += delta_vies
    
    print(peso, vies)
    print('\n')
    
    input3_fi = neuron(input3)
    y_input3 = ativacao(input3_fi)
    
    if(y_input3 != target[2]):
        treinamento(input3, target[2], y_input3)
        
        delta_vies = lr * (target[2] - y_input3) * 1
        vies += delta_vies

    print(peso, vies)
    print('\n')
    
    input4_fi = neuron(input4)
    y_input4 = ativacao(input4_fi)
    
    if(y_input4 != target[3]):
        treinamento(input4, target[3], y_input4)
        
        delta_vies = lr * (target[3] - y_input4) * 1
        vies += delta_vies
    
    print(peso, vies)
    print('\n')
    
    cont += 1
    

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