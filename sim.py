import numpy as np
import matplotlib as plt
dientes=np.linspace(2.0, 3.0, num=5)
ng=(dientes/20)

# Definición parámetros, interfaz y adquisición de la información
m=147 #Masa total (kg)
mu=0.85 #Coeficiente de fricción de las llantas
cgx=66 #Porcentaje en eje longitudinal del CG (%)
b=cgx;
cgy=50;%Porcentaje en eje lateral del CG (%)
g=9.78;%Aceleración de la gravedad (m/s^2)
L=1.03;%Longitud total de kart (m)
vmaxtot=vmaxima(ss)/3.6;%Velocidad máxima alcanzable (m/s)
W=m*g; %Peso del kart (N)
h=0.5; %Altura del CG de Kart (m)
rho=0.95; %Densidad del aire en Bogotá (kg/m^3)
