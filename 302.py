import matplotlib.pyplot as plt
import numpy as np 

def plot_graph(lnE, lnT):
  
  lnE = np.array(lnE)
  lnT = np.array(lnT)
  plt.plot(lnT, lnE,color='red',marker='o')

  plt.xlabel("ln T")
  plt.ylabel("ln ε")
  plt.title("График зависимости ln ε от ln T")
  plt.grid(True)
  plt.show()
  
x1 = [-0.598, 0.761,-0.598,-0.598]
y1 = [6.685, 7.003,7.003,6.685]
plt.plot(y1, x1, color='black')
plt.scatter(y1,x1,color='black', label=f'Δln ε = 1.359, Δln T = 0.318')
plt.legend()
plot_graph([-0.598,-0.357,-0.128,0.113,0.329,0.548,0.761],[6.685,6.745,6.802,6.856,6.908,6.956,7.003])
