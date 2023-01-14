from file import seidel

A = [[60,-40,0],
     [-40,150,-100],
     [0,-100,130]]

b = [200,0,230]

eps = 10**-6

x = seidel(A, b, eps)

print("\nvetor solução:")
print(x)