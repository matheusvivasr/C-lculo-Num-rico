import matplotlib.pyplot as plt
from numpy import linspace
from math import log


# FUNCOES DE GAUSS-SEIDEL
def norma(x0,x): 
    n = len(x0)
    maxnum = 0
    maxden = 0
    
    for i in range(0, n):
      num = abs(x0[i]-x[i])
      if num > maxnum:
        maxnum = num
      den = abs(x0[i])
      if den > maxden:
        maxden = den
    return maxnum/maxden

def seidel(A, b, epsilon, iterMax=50):
    n = len(A)
    x = n * [0]
    x0 = n * [0]

    for i in range(0, n):
      for j in range(0, n):
        if i != j:
          A[i][j] = A[i][j]/A[i][i]
      b[i] = b[i]/A[i][i]

    for k in range(1, iterMax+1):
      for i in range(0, n):
        S = 0
        for j in range(0, n):
          if i != j:
            S = S + A[i][j] * x[j]
        x[i] = b[i] - S
      d = norma(x, x0)
      if d <= epsilon:
        return x

      x0 = x[:]

    print("ERRO: número máximo de iterações atingido")


# FUNCOES PARA REGRESSAO LINEAR 
def liners(X, F):
  sX = 0
  sXq = 0
  sXF = 0
  sF = 0
  N = len(X)

  for i in range(N):
    sX += X[i]
    sXq += (X[i])**2
    sXF += X[i]*F[i]
    sF += F[i]
    
  A = [[sXq,sX],[sX,N]]
  b = [sXF,sF]
  eps = 10**-6
  func = seidel(A, b, eps)
  return func

def logas(X, F):

  sXl = 0
  sXq = 0
  sXF = 0
  sFl = 0
  N = len(X)

  for i in range(N):
    sXl += log(X[i],10)
    sXq += (log(X[i],10))**2
    sXF += (log(X[i],10)*log(F[i],10))
    sFl += log(F[i],10)

  A = [[sXq,sXl],[sXl,N]]
  b = [sXF,sFl]
  eps = 10**-6
  func = seidel(A, b, eps)
  return func


# FUNCAO DO GRAFICO
def GRAFICO(N, A, B, x, y, xf, yf):
  plt.figure(N)
  plt.gcf().set_size_inches(9, 6)
  plt.plot(xf, yf, color ='black', label = 'Regressão linear' )
  plt.plot(A, B,'.-', zorder = 0, color='lightgray', label='Dados fornecidos')
  plt.scatter(x, y, color = 'black', label = 'Valor estimado', zorder = 1)
  plt.legend(loc='upper right')
  nome = f'grafico{N}.png'
  plt.savefig(nome, dpi=100)