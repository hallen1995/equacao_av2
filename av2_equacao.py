from matplotlib import pyplot as plt

# menu buscar o resultado da equação y = a*x + b*x - c trazendo os valores y1, y2 e y3. 
def menu(x, a, b, c):
    y = a*x +b*x -c
    return y

# importando valor randôminicos para x1, x2 e x3 
import random
x1 = ra = random.randint(1,10)
x2 = rb = random.randint(1,10)
x3 = rc = random.randint(1,10)

# valores definidos de acordo com 3 primeiro números do RU = 160 (obs: 0 subistituído por 5)
a = 1
b = 6
c = 5

# legenda e gráfico
plt.title('Equação linear: y = a*x + b*x -c')
plt.grid()

# definindo
plt.plot(x1,menu(x1, a, b, c), marker="o",markersize=10,markerfacecolor='black')
plt.plot(x2,menu(x2, a, b, c), marker="o",markersize=10,markerfacecolor='red')
plt.plot(x3,menu(x3, a, b, c), marker="o",markersize=10,markerfacecolor='blue')

plt.legend([f'x={x1} y={menu(x1, a, b, c)}', f'x={x2} y={menu(x2, a, b, c)}',f'x={x3} y={menu(x3, a, b, c)}'])

plt.show()