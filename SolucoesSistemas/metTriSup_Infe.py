import numpy as np

def triSup(A,b):
    n = len(b)
    x = np.zeros(n, dtype=np.float64)

    x[n-1] = b[n-1] / A[n-1,n-1]

    for i in range(n-2,-1,-1):
        x[i] = b[i]
        for j in range(i+1,n):
           x[i] = x[i] - A[i,j] * x[j]
        x[i] = x[i] / A[i,i]
    return x

def triInferior(A, b):
    n = len(b)
    x = np.zeros(n, dtype=np.float64)

    # Calcular o primeiro valor de x[0]
    x[0] = b[0] / A[0, 0]

    # Substituição direta para os outros valores de x
    for i in range(1, n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= A[i, j] * x[j]
        x[i] /= A[i, i]
    return x

A = np.array([[3,2,-1],
              [0,3,-1],
              [0,0,4]], dtype=np.float64)

b = np.array([-6,-11,20])
x = triSup(A,b)
print("Vetor solução: ",x)

B = np.array([[1.00,0.00,0.00,0.00],
              [-0.25,1.00,0.00,0.00],
              [-0.38,-0.44,1.00,0.00],
              [-0.25,-0.29,-0.85,1.00]],dtype=np.float64)

b2 = np.array([0.5,0.4,0.3,0])

x1 = triInferior(B,b2)
print("Exercicios aula 9:")
print("Vetor Solução: ",x1)


C = np.array([[0.8,-0.2,-0.2,-0.3],
              [0,0.85,-0.25,-0.38],
              [0,0,0.61,-0.48],
              [0,0,0,0.21]])

b3 = np.array([0.5,0.53,0.72,0.89])

x2 = triSup(C, b3)

print("Vetor Solução: ",x2)