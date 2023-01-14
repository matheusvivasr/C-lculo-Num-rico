import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np

def func(t):
  return 0.0402213138747154*np.sin(np.pi*t/60) - 0.0888257416818708*np.sin(np.pi*t/30) - 0.105897721605232*np.sin(np.pi*t/20) + 0.234160449848083*np.sin(np.pi*t/15) + 0.107994930876682*np.sin(np.pi*t/12) + 0.366526848162786*np.sin(np.pi*t/10) - 0.0770483404495945*np.sin(7*np.pi*t/60) + 0.126749013285124*np.sin(2*np.pi*t/15) - 0.203941564486727*np.sin(3*np.pi*t/20) - 3.22362798931777*np.sin(np.pi*t/6) - 0.0810292378938861*np.cos(np.pi*t/60) - 0.23930888719918*np.cos(np.pi*t/30) + 0.0562266623949216*np.cos(np.pi*t/20) + 0.20475256643302*np.cos(np.pi*t/15) - 0.195504485990989*np.cos(np.pi*t/12) + 0.0603975721723265*np.cos(np.pi*t/10) + 0.49875497126937*np.cos(7*np.pi*t/60) + 0.111052640325436*np.cos(2*np.pi*t/15) - 0.0640637566538481*np.cos(3*np.pi*t/20) + 2.21118943138031*np.cos(np.pi*t/6) + 9.73141666666667

rawData = read_csv('dados_temperatura_minima.csv', header=0, names=['x', 'y'])
month = rawData['x']; temperature = rawData['y']

x = np.linspace(1, 135, 1000)
x2 = np.linspace(1, 120, 1000)

y = func(x2)
y132 = func(132)
y135 = func(x)

print(f"a estimativa para o mês 132 é de uma temperatura mínima de aproximadamente {y132:.2f}°C")
print(y132)

plt.figure(1)
plt.title('Função aproximada pelo MMQ Trigonométrico expandida até o 132')
plt.gcf().set_size_inches(9, 6)
plt.plot(x, y135, color ='black', label = 'Função trigonométrica' )
plt.scatter(132, y132, color = 'black', label = 'Ponto do mês 132', zorder = 1)
plt.plot(month, temperature,'.-', zorder = 0, color='lightgray', label='Dados fornecidos')
plt.xticks(np.arange(1, 135, 12))
plt.legend(loc='lower left')
plt.ylabel('Temperatura mínima')
plt.xlabel('Mês')
plt.savefig('grafico-top.png', dpi=100)


plt.figure(2)
plt.title('Função aproximada pelo MMQ: Trigonométrico')
plt.gcf().set_size_inches(9,6)
plt.plot(x2, y, zorder = 1, color ='black', label = 'Função trigonométrica' )
plt.plot(month, temperature,'.-', zorder = 0, color='lightgrey', label='Dados fornecidos')
plt.xticks(np.arange(1, 132, 12))
plt.legend(loc='lower left')
plt.ylabel('Temperatura mínima')
plt.xlabel('Mês')
plt.savefig('grafico-top2.png', dpi=100)

plt.show()