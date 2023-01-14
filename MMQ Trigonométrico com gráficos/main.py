import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv
from sympy import Symbol, pi

from lsq import trigLSQ

rawData = read_csv('dados_temperatura_minima.csv', header=0, names=['x', 'y'])
x = rawData['x']; y = rawData['y']

noMonths = len(rawData)
noYears = int(noMonths/12)

# t = 1,2, 3, 4, 5, ..., 60
# x = t*pi/30 --> pi/30, pi/15, ..., 2pi
data60 = {
    'x': [(2*pi*t)/noMonths for t in range(1, noMonths+1)],
    'y': [p for p in y]
}


order60 = 10 # max 29
F60, aux60 = trigLSQ(data60, order60); F60 = F60.subs(Symbol('x'), (2*pi/noMonths)*Symbol('t'))

f60 = lambda t: float(F60.subs(Symbol('t'), t).evalf()) # f60(t)

x60 = np.linspace(0, noMonths, 100); y60 = 0
for j, i in aux60[0]: y60 += aux60[1][j][0] * (np.cos(i['index'] * 2*np.pi/noMonths * x60) if i['cos'] else np.sin(i['index'] * 2*np.pi/noMonths * x60))

with open('./funcao.txt', 'w') as f:
    f.write(f't: {list(range(1, noMonths+1))}\n\n')
    f.write(f'x: {data60["x"]}\n\n')
    f.write(f'y: {data60["y"]}\n\n')
    f.write(f'F(t) = {F60}\n\n')
    f.write(f'F(132) = {f60(132)}')


plt.title('Função aproximada pelo MMQ: Trigonométrico')
plt.scatter(range(1, noMonths+1), data60['y'], label='Dados da temperatura', color = 'gray')
plt.plot(range(1, noMonths+1), data60['y'], '--', color = 'gray')
plt.plot(x60, y60, '-', lw=2.5, label=f'Função aproximada (ordem {order60})')
plt.legend(loc='upper right')
plt.ylabel('Temperatura mínima')
plt.xlabel('Mês')
plt.grid()
plt.gcf().set_size_inches(15,10)
plt.xticks(np.arange(0, 121, 6))
plt.savefig('grafico-mal arrumado.png', dpi=100)

plt.show()
