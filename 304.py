import matplotlib.pyplot as plt
import numpy as np  

def plot_graph(resist_me, Voltage,pointV,pointI,secV,secI,Wavelength):
  
  resist_me = np.array(resist_me)
  Voltage = np.array(Voltage)
  plt.plot(Voltage, resist_me,color='red',marker='.')

  plt.ylabel("I, мкА")
  plt.xlabel("V, В")
  plt.title("График вольт-амперной характеристики")
  plt.grid(True)
  plt.plot(pointV,pointI,color='black')
  plt.scatter(pointV[0], pointI[0], color='black', label=f'точка быстрого роста: {pointV[0]} В, {pointI[0]} мкА, {Wavelength} нм')
  plt.legend()
  plt.plot(secV,secI,color='black')
  plt.show()



def second_plot(frec, Volt):

  frec = np.array(frec)
  Volt = np.array(Volt)
  plt.plot(frec, Volt,color='red',marker='o')

  plt.xlabel("ν, 10^(14) Гц")
  plt.ylabel("Uз, В")
  plt.title('График зависимости задерживающего напряжения от частоты')
  plt.grid(True)
  plt.show()
  
Volt = [-2,-1.9,-1.8,-1.7,-1.6,-1.5,-1.4,-1.3,-1.2,-1.1,-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0]

plot_graph([-24.5,-24.5,-24.5,-24.5,-24.5,-24.5,-24.3,-23.9,-22.4,-21.3,-20.3,-18.5,-17.0,-15.3,-13,-10.6,-7.8,-5.3,-0.4,3.1,7.2],Volt,[-1.3,-1.3],[-23.9,-25],[-1.3,-2],[-23.9,-23.9],410)
plot_graph([-10.9,-10.9,-10.9,-10.9,-10.9,-10.9,-10.8,-10.6,-10.6,-10.6,-10.5,-9.8,-9.4,-8.6,-7.9,-7.2,-6.3,-5.2,-4.4,-3.0,-1.5],Volt,[-1,-1],[-10.5,-11],[-1,-2],[-10.5,-10.5],450)
plot_graph([-8.5,-8.5,-8.5,-8.5,-8.5,-8.5,-8.4,-8.4,-8.4,-8.3,-8.3,-8.3,-8.3,-8.3,-8.3,-8.1,-7.6,-7.2,-6.4,-6.1,-5.5],Volt,[-0.5,-0.5],[-8.1,-9],[-0.5,-2],[-8.1,-8.1],540)
plot_graph([-5.8,-5.8,-5.8,-5.8,-5.8,-5.8,-5.8,-5.8,-5.7,-5.7,-5.7,-5.7,-5.7,-5.7,-5.7,-5.7,-5.7,-5.6,-5.2,-4.9,-4.4,],Volt,[-0.3,-0.3],[-5.6,-6],[-0.3,-2],[-5.6,-5.6],580)
Frec_deviation = [7.52, 4.96]  
Volt_deviation = [-1.4, -0.2]  
plt.plot(Frec_deviation, Volt_deviation,color='black')
plt.scatter(Frec_deviation[0], Volt_deviation[0], color='black', label=f'(верхняя точка: ν = {Frec_deviation[0]} 10^(14) Гц, V = {Volt_deviation[0]} В)')
plt.scatter(Frec_deviation[1], Volt_deviation[1], color='black', label=f'(нижняя точка: ν = {Frec_deviation[1]} 10^(14) Гц, V = {Volt_deviation[1]} В)')
plt.legend()
second_plot([7.317,6.667,5.556,5.172],[-1.3,-1.0,-0.5,-0.3])
