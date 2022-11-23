import numpy as np

inputs = np.array([[0, 0, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0]])  #Base de dados
target = np.array([1, 1, 0, 0])                                 #Resultados alvos da base de dados

pesos = delta_peso = [0, 0, 0]
vies = delta_vies = 0
lr = 0.1
voltas = 4
input_y = [0, 0, 0, 0]

   
#Retorna a resposta Sim[1] ou Não[0]
def ativacao(inputs):
    return np.where(neuron(inputs) > 0.0, 1, 0)  #Onde o neuron for maior que 0, passa a ser 1, se não, -1

    
#Somatoria de [input * peso]
def neuron(inputs):
    return np.dot(inputs, pesos) + vies


#Treina a rede neural com loops
def treinamento(inputy, targetx):
    global vies, delta_vies, pesos
    
    for _ in range(voltas):
        for input, target in zip(inputy, targetx):
            print(pesos, vies)
            if(ativacao(input) != target):
                delta_peso = lr * (target - ativacao(input)) * input
                pesos += delta_peso
            delta_vies = lr * (target - ativacao(input)) * 1
            vies += delta_vies
    
treinamento(inputs, target)
#print(pesos, vies)