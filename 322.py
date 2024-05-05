import matplotlib.pyplot as plt
import numpy as np 

def plot_graph(resist_me, MyBadTemperament,name):
  
  resist_me = np.array(resist_me)
  MyBadTemperament = np.array(MyBadTemperament)
  plt.plot(MyBadTemperament, resist_me,color='red',marker='o')

  plt.xlabel("t, ℃")
  plt.ylabel("R, кОм")
  plt.title(name)
  plt.grid(True)
  plt.show()
  

def second_plot(LNres, tempMinus):

  LNres = np.array(LNres)
  tempMinus = np.array(tempMinus)
  plt.plot(tempMinus, LNres,color='red',marker='o')

  plt.xlabel("1/T, 10^(-3)*K^(-1)")
  plt.ylabel("ln R")
  plt.title('График зависимости логарифма сопротивления полупроводника ln R от обратной абсолютной температуры 1/Т')
  plt.grid(True)
  plt.show()

res_deviation = [1.165, 1.700]  
temp_deviation = [35, 115]  

plt.plot(temp_deviation, res_deviation,color='black')
plt.scatter(temp_deviation[0], res_deviation[0], color='black', label=f'(нижняя точка: t = {temp_deviation[0]} ℃, R = {res_deviation[0]} кОм)')
plt.scatter(temp_deviation[1], res_deviation[1], color='black', label=f'(верхняя точка: t = {temp_deviation[1]} ℃, R = {res_deviation[1]} кОм)')
plt.legend()

temperature_data = [40,45,50,55,60,65,70,75,80,85,90,95,100,105,110]

plot_graph([1.195,1.226,1.264,1.298,1.332,1.368,1.401,1.435,1.470,1.503,1.535,1.568,1.600,1.635,1.680],temperature_data,'График зависимости сопротивления металла от температуры')
plot_graph([12.305,8.375,6.543,4.897,3.632,2.698,2.032,1.503,1.155,0.9693,0.7551,0.5923,0.4687,0.3734,0.2965],temperature_data,'График зависимости сопротивления полупроводника от температуры')
res_deviation = [5.5,9.5]  
temp_deviation = [2.58, 3.21]  
plt.plot(temp_deviation, res_deviation,color='black')
plt.scatter(temp_deviation[0], res_deviation[0], color='black', label=f'(нижняя точка: 1/T = {temp_deviation[0]} 10^(-3)*K^(-1), ln R = {res_deviation[0]})')
plt.scatter(temp_deviation[1], res_deviation[1], color='black', label=f'(верхняя точка: 1/T = {temp_deviation[1]} 10^(-3)*K^(-1), ln R = {res_deviation[1]})')
plt.legend()
second_plot([9.42,9.03,8.79,8.50,8.19,7.90,7.62,7.32,7.05,6.88,6.63,6.38,6.15,5.92,5.69],[3.19,3.14,3.1,3.05,3,2.96,2.91,2.87,2.83,2.79,2.75,2.72,2.68,2.64,2.61])
