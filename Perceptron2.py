import numpy as np
import pandas as pd

#Classe Perceptron
class Perceptron:
    #Construtor
    def __init__(self, lr=0.1, voltas=4):
        self.lr = lr                            #Learning Rate
        self.voltas = voltas                    #Epochs


    #Treina a rede neural com loops
    def treinamento(self, inputs, targets):
        self.pesos = np.zeros(1 + inputs.shape[1])   #Inicializa os pesos com um vetor de 0
        self.erros_ = []
        
        for _ in range(self.voltas):
            erros = 0
            for y_input, target in zip(inputs, targets):
                delta_peso = self.lr * (target - self.ativacao(y_input)) * y_input
                self.pesos[1:] += delta_peso    #Update dos Pesos
                self.pesos[0] += delta_peso     #Update do Viés
                erros += int(delta_peso != 0.0)
            self.erros_.append(erros)
    
    
    #Retorna a resposta Sim[1] ou Não[0]
    def ativacao(self, inputs):
        return np.where(self.neuron(inputs) >= 0.0, 1, -1)
    
    
    #Somatoria de [input * peso]
    def neuron(self, inputs):
        return np.dot(inputs, self.pesos[1:]) + self.pesos[0]
    
    