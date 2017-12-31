import math
import pylab as pl
mass_sun=4*math.pi*math.pi
mass_jupiter=0
mass_earth=mass_sun

x_earth=[-1]
y_earth=[0]
x_sun=[1]
y_sun=[0]
x_jupiter=[0]
y_jupiter=[0]

velocity=math.sqrt(0.5*mass_sun)
vx_e=[0]
vy_e=[-velocity]
vx_j=[0]
vy_j=[0]
vx_s=[0]
vy_s=[velocity]

timestep=0.001
t=[0]

while t[-1]<=100:
	r_es=math.sqrt((x_earth[-1]-x_sun[-1])**2+(y_earth[-1]-y_sun[-1])**2)
	r_ej=math.sqrt((x_earth[-1]-x_jupiter[-1])**2+(y_earth[-1]-y_jupiter[-1])**2)
	r_js=math.sqrt((x_jupiter[-1]-x_sun[-1])**2+(y_jupiter[-1]-y_sun[-1])**2)
	vx_e2=vx_e[-1]-mass_sun*(x_earth[-1]-x_sun[-1])*timestep/r_es**3-mass_jupiter*(x_earth[-1]-x_jupiter[-1])*timestep/r_ej**3
	vy_e2=vy_e[-1]-mass_sun*(y_earth[-1]-y_sun[-1])*timestep/r_es**3-mass_jupiter*(y_earth[-1]-y_jupiter[-1])*timestep/r_ej**3
	vx_j2=vx_j[-1]-mass_sun*(x_jupiter[-1]-x_sun[-1])*timestep/r_js**3-mass_earth*(x_jupiter[-1]-x_earth[-1])*timestep/r_ej**3
	vy_j2=vy_j[-1]-mass_sun*(y_jupiter[-1]-y_sun[-1])*timestep/r_js**3-mass_earth*(y_jupiter[-1]-y_earth[-1])*timestep/r_ej**3
	vx_s2=vx_s[-1]-mass_jupiter*(x_sun[-1]-x_jupiter[-1])*timestep/r_js**3-mass_earth*(x_sun[-1]-x_earth[-1])*timestep/r_es**3
	vy_s2=vy_s[-1]-mass_jupiter*(y_sun[-1]-y_jupiter[-1])*timestep/r_js**3-mass_earth*(y_sun[-1]-y_earth[-1])*timestep/r_es**3
	vx_e.append(vx_e2)
	vy_e.append(vy_e2)
	vx_j.append(vx_j2)
	vy_j.append(vy_j2)
	vx_s.append(vx_s2)
	vy_s.append(vy_s2)
	x_earth.append(x_earth[-1]+vx_e[-1]*timestep)
	y_earth.append(y_earth[-1]+vy_e[-1]*timestep)
	x_jupiter.append(x_jupiter[-1]+vx_j[-1]*timestep)
	y_jupiter.append(y_jupiter[-1]+vy_j[-1]*timestep)
	x_sun.append(x_sun[-1]+vx_s[-1]*timestep)
	y_sun.append(y_sun[-1]+vy_s[-1]*timestep)
	t.append(t[-1]+timestep)

pl.plot(x_earth,y_earth,label='earth')
pl.plot(x_jupiter,y_jupiter,label='jupiter')
pl.plot(x_sun,y_sun,label='sun')
pl.show