import tensorflow as tf

n_input = [[0, 0, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0]]
n_hidden_1 = [1, 1, 0, 0]
x = 0
 # Pesos da camada 1 
w1 = tf.Variable(tf.random.normal([n_input, n_hidden_1]))
 # Bias da camada 1
b1 = tf.Variable(tf.random.normal([n_hidden_1]))
 # Aplicando a função sigmoide na camada 1
camada_1 = tf.nn.sigmoid(tf.add(tf.matmul(x,w1),b1))