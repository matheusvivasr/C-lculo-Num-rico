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