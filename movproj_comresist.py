# py.exe C:\Users\igorp\Desktop\VSCode\Projetos\Simulações\movproj_comresist.py
import vpython as vp

vp.scene.title='Movimento Projétil com Resistência do Ar'
vp.scene.width=vp.scene.height= 800

theta = 70.0
thetar = theta*vp.pi/180.0
vini = 300.0
g = vp.vector(0.0,-9.8,0.0)

chão = vp.box(pos=vp.vector(0,0.0,0), size=vp.vector(8000,10,1000.0), color=vp.color.green)

raio = 0.04
proj = vp.sphere(pos=vp.vector(-500,raio,0), radius=raio, color=vp.color.white, make_trail=True)

projvini = vp.vector(vini*vp.cos(thetar), vini*vp.sin(thetar), 0)

projm = 0.5 # massa

projp = projm*projvini # momento linear

Fp = projm*g

projA = vp.pi*(raio**2) # area

projC = 0.01 # coeficiente de arrasto projetil

roar = 1.2 # densidade ar

Far = (-1/2)*roar*projA*projC*vp.mag(projvini)**2*vp.norm(projvini)

t = 0.0
dt = 0.001

arscale = 2
vetor = vp.arrow(pos=proj.pos, axis=arscale*projp, color=vp.color.red)

while (proj.pos.y >= raio):
    Fres = Fp + Far
    vp.rate(10000)
    
    a = Fres/projm
    projvini = projvini + a*dt
    projp = projm*projvini
    proj.pos += projvini*dt
    
    vetor.axis = arscale*projp
    vetor.pos = proj.pos
    
    Far = (-1/2)*roar*projA*projC*vp.mag(projvini)**2*vp.norm(projvini)
    
    t += dt