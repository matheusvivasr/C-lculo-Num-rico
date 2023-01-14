import file as p

# QUESTÃO 1
A = [[60,40,0],[-40,150,-100],[0,-100,130]]
b = [200,0,230]
eps = 10**-6
x = p.seidel(A, b, eps)
print("\nQuestão 1)")
print(f"Corrente I1 = {x[0]:.3} A\nCorrente I2 = {x[1]:.3} A\nCorrente I3 = {x[2]:.3} A")

#  QUESTÃO 2
U = [2, 3, 4, 5, 7, 10]
I = [5.2, 7.8, 10.7, 13, 19.3, 27.5]
F = p.liners(I, U)
x1 = p.linspace(1, 30, 50)
y1 = F[0]*x1+F[1]
xp1 = 3.5
yp1 = F[0]*xp1+F[1]
p.GRAFICO(1, I, U, xp1, yp1, x1, y1)
#O GRAFICO SAIRÁ COMO 'grafico1.png' NA MESMA PASTA DO CODIGO
print("\nQuestão 2)")
print(f"Reta de regressão: y = {F[1]:.3}.x + {F[0]:.3}")
print (f"Estimativa para {xp1} V = {yp1:.3} A")


# QUESTAO 3
P = [0.5, 2, 10, 100, 200]
B = [286.6, 202.7, 135.5, 76.2, 64.1]
G = p.logas(P, B)
xp2 = 80
yp2 = 10**(G[0]*p.log(xp2,10)+G[1])
print("\nQuestão 3)")
print(f"Reta de regressão: log(y) = {G[1]:.3}.log(x) + {G[0]:.3}")
print (f"Estimativa para {xp2} Kg = {yp2:.3} Bpm")