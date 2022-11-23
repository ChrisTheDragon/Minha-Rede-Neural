#---------------------------------------------------#
'''              Rede Neural Perception
Uma rede neural com um neuron, ou seja, processa um 
dado de cada vez
Esta rede neural responde com SIM[1] ou NÃO[0] com 
base em Entrada[inputs] de 3 pesos.

Exemplo: Ir em uma viagem

Uma tupla é gerada conforme as perguntas:
[Tem amigos para ir junto?,
 A passagem está cara?, 
 O meio de transporte é seguro?
]

input: [1, 0, 0] 
-> Esta pessoa Vai[1] com amigos,
-> A passagem Não[0] está cara,
-> O meio de transporte Não[0] é seguro

output: [0] 
-> Esta pessoa Não[0] deve viajar

'''
#---------------------------------------------------#

inputs = [[0, 0, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0]] #Base de dados
target = [1, 1, 0, 0]                                 #Resultados alvos da base de dados

#Inicialização das variaveis---#
peso = [0, 0, 0] 
delta_peso = [0, 0, 0]
vies = 0
delta_vies = 0
lr = 0.1
voltas = 3
y_input = [0, 0, 0, 0]
participantes = len(inputs)
#------------------------------#

#Somatoria de [input * peso]
def neuron(inputx):
    z = 0
    for i in range(len(inputx)):
        x = inputx[i] * peso[i]
        z += x
    return z + vies


#Retorna a resposta Sim[1] ou Não[0]
def ativacao(fi):
    if(fi > 0):
        return 1
    elif (fi <= 0):
        return 0


#Treina a rede neural com loops
def treinamento(inputx, targetx, y_inputx):
    global delta_vies, vies
    for i in range(0, len(inputx)):
            delta_peso[i] = lr * (targetx - y_inputx) * inputx[i]
            peso[i] += delta_peso[i]
    delta_vies = lr * (targetx - y_inputx) * 1
    vies += delta_vies


#Etapa de trinamento, se a rede neural errar, ela treina ate acertar.
for i in range(voltas):
    for j in range(participantes):
        print(peso, vies, y_input)
        y_input[j] = ativacao(neuron(inputs[j]))
        
        if (y_input[j] != target[j]):
            treinamento(inputs[j], target[j], y_input[j])
    j = 0   


#Novos dados para verificar se a rede neural esta pronta
'''[1, 0, 0] -> [Tem amigos, A passagem não esta cara, o Transporte não é seguro] logo [0] Não vai
   [0, 0, 1] -> [Não tem amigos, A passagem não esta cara, o Transporte é Seguro] logo [1] Vai
   [1, 1, 1] -> [Tem amigos, A passagem está cara, o Transporte é seguro]         logo [0] Não vai'''
print("\n")
input_n = [[1, 0, 0], [0, 0, 1], [1, 1, 1]]

print(ativacao(neuron(input_n[0])))
print(ativacao(neuron(input_n[1])))
print(ativacao(neuron(input_n[2])))
