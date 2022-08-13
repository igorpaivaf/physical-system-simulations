# py.exe C:\Users\igorp\Desktop\VSCode\Projetos\Simulações\satorbplaneta.py
import vpython as vp

G = 1
m = 1
M = 100
R = 1.0
rs = 0.2

pA = vp.sphere(pos=vp.vector(0,0,0), radius=R, color=vp.color.green)
sat = vp.sphere(pos=vp.vector(10,0,0), radius=rs, make_trail=True, color=vp.color.white)

sat.v = vp.vector(0,vp.pi,0)
r = sat.pos - pA.pos

F = G*(M*m)*(vp.norm(r))/(vp.mag2(r))

a = F/m

t = 0.0
dt = 0.001

while True:
    vp.rate(1000)
    
    sat.v += a*dt
    sat.pos -= sat.v*dt
    
    r = sat.pos - pA.pos
    F = G*(M*m)*(vp.norm(r))/(vp.mag2(r))
    
    a = F/m
    t += dt