#Desarrollo Tarea 3 Geodinamica
#Juan Diego Dumez Garcia
#Carlos Fabian Sanchez Suarez

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

W=1000000         #Width
H=15000000        #Height
Vxo=10**-9        #Scaling value of horizontal velocity
Vyo=10**-9        #Scaling value of vertical velocity

#Creacion de la grilla 31x31
m=31
n=31

x=np.linspace(0,W,m)
y=np.linspace(0,H,n)

#Inicializacion de V para cada caso

Vx=np.zeros((31,31))
Vy=np.zeros((31,31))
dVx=np.zeros((31,31))
dVy=np.zeros((31,31))
divV=np.zeros((31,31))

#Model

for i in range(len(x)):
    for j in range(len(y)):
        Vx[i][j]=-Vxo*np.sin(2*np.pi*x[i]/W)*np.cos(np.pi*y[j]/H)
        Vy[i][j]=Vyo*np.cos(2*np.pi*x[i]/W)*np.sin(np.pi*y[j]/H)
        dVx[i][j]=-Vxo*2*np.pi*(1/W)*np.cos(2*np.pi*x[i]/W)*np.cos(np.pi*y[j]/H)
        dVy[i][j]=Vyo*np.pi*(1/H)*np.cos(2*np.pi*x[i]/W)*np.cos(np.pi*y[j]/H)
        divV[i][j]=dVx[i][j]+dVy[i][j]
       
#Vx
plt.imshow(Vx, cmap='seismic')      
plt.colorbar()
plt.title('Analisis para Vx')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.savefig('Vx.png')
plt.show()

        
#Vy
plt.imshow(Vy, cmap='seismic')      
plt.colorbar()
plt.title('Analisis para Vy')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.savefig('Vy.png')
plt.show()


#dVx
plt.imshow(dVx, cmap='winter')      
plt.colorbar()
plt.title('Analisis para dVx')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.savefig('dVx.png')
plt.show()

#dVy
plt.imshow(dVy, cmap='winter')      
plt.colorbar()
plt.title('Analisis para dVy')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.savefig('dVy.png')
plt.show()

#divV
plt.imshow(dVx, cmap='hot')      
plt.colorbar()
plt.title('Analisis para divV')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.savefig('divV.png')
plt.show()

#Arrow field for V

fig,ax=plt.subplots()
ax.quiver(x,y,Vx,Vy)
plt.title('Arrow field for V')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.savefig('Arrow field for V')
plt.show()


