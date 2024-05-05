import matplotlib.pyplot as plt
import numpy as np 

def plot_graph(wave, delenieBarabana):
  
  wave = np.array(wave)
  delenieBarabana = np.array(delenieBarabana)
  plt.plot(delenieBarabana, wave,color='red',marker='o')
  plt.xlabel("Среднее значение делений шкалы барабана")
  plt.ylabel("λ, нм")
  plt.title("Градуировочный график")
  plt.grid(True)
  plt.scatter(2790,659, color='black', label=f'Среднее значение делений шкалы барабана - 2790, λ = 659 нм')
  plt.scatter(1791,488, color='blue', label=f'Среднее значение делений шкалы барабана - 1791, λ = 488 нм')
  plt.scatter(1144,434, color='green', label=f'Среднее значение делений шкалы барабана - 1144, λ = 434 нм')
  plt.legend()
  plt.show()
  
  
plot_graph([690.7,671.6,622.0,607.0,579.0,577.0,546.1,491.6,435.8,434.8,433.9,407.8,404.7],[2901,2836,2658,2587,2462,2448,2267,1839,1175,1158,1137,677,610])
