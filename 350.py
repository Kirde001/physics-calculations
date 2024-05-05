import matplotlib.pyplot as plt
import numpy as np 

def plot_graph(photoI, voltU,wave):
  
  photoI = np.array(photoI)
  voltU = np.array(voltU)
  plt.plot(voltU, photoI,color='red',marker='o')
  minx1 = voltU.min()
  maxx1 = voltU.max()
  miny1 = photoI.min()
  maxy1 = photoI.max()
  plt.xlabel("Uф, В")
  plt.ylabel("Iф, мА")
  plt.title("Вольтамперная характеристика фоторезистора для света с длиной волны "+f'{wave}'+' нм')
  plt.grid(True)
  plt.plot([minx1,maxx1,maxx1,minx1],[miny1,maxy1,miny1,miny1],color='black',label=f'ΔUф = {maxx1}, ΔIф = {maxy1}')
  plt.legend()
  plt.show()
  
  
def second_plot(photoI, wave):

  photoI = np.array(photoI)
  wave = np.array(wave)
  plt.plot(wave, photoI,color='red',marker='o',label=f'U = 18 B, E = 30 Лк')

  plt.xlabel("λ, нм")
  plt.ylabel("Iф, мА")
  plt.title('Спектральная характеристика фоторезистора')
  plt.plot([wave[1], wave[3],661.449], [photoI[1], photoI[3],0], color='blue', linestyle='-')
  plt.scatter(661.449,0, color='blue', label=f'Красная граница = 661 нм')
  plt.grid(True)
  plt.legend()
  plt.show()

  
Voltage = [0,3,6,9,12,15,18,21,24,27,29]
plot_graph([0,2.84,5.78,8.52,11.46,14.2,17.14,19.98,22.72,25.56,28.46],Voltage,410)
plot_graph([0,2.74,5.28,8.02,10.76,13.4,15.94,18.68,21.32,24.06,25.86],Voltage,450)
plot_graph([0,1.44,2.72,4.32,5.76,7.4,8.84,10.28,11.72,13.16,14.16],Voltage,540)
plot_graph([0,1.04,2.08,3.12,4.06,5,6.14,7.08,8.12,9.06,9.76],Voltage,580)
plot_graph([0,0.71,1.42,2.13,2.84,3.56,4.26,4.97,5.68,6.4,6.88],Voltage,650)
second_plot([17.14,15.94,8.84,6.14,4.26],[410,450,540,580,650])