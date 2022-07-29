# py.exe C:\Users\igorp\Desktop\VSCode\Projetos\Simulações\movproj_comresist.py
import vpython as vp

vp.scene.tile = 'Movimento Projétil sem Resistência do Ar'
vp.scene.width = vp.scene.height = 800 #tamanho da janela

theta = 70 #ângulo inicial em graus
thetarad = theta*vp.pi/180
velinicial = 300

g = vp.vector(0.0,-9.8,0.0) #aceleração da gravidade

chao = vp.box(pos=vp.vector(0,0,0), size=vp.vector(5000,10,5000), color=vp.color.green) #Piso
eixo_x = vp.cylinder(pos=vp.vector(0,1000,0), size=vp.vector(1000,10,10), axis=vp.vector(1,0,0), color=vp.color.magenta)
eixo_y = vp.cylinder(pos=vp.vector(0,1000,0), size=vp.vector(1000,10,10), axis=vp.vector(0,1,0), color=vp.color.magenta)
eixo_z = vp.cylinder(pos=vp.vector(0,1000,0), size=vp.vector(1000,10,10), axis=vp.vector(0,0,1), color=vp.color.magenta)
ponta_x = vp.cone(pos=vp.vector(1000,1000,0), size=vp.vector(100,100,100), axis=vp.vector(1,0,0), color=vp.color.magenta)
ponta_y = vp.cone(pos=vp.vector(0,2000,0), size=vp.vector(100,100,100), axis=vp.vector(0,1,0), color=vp.color.magenta)
ponta_z = vp.cone(pos=vp.vector(0,1000,1000), size=vp.vector(100,100,100), axis=vp.vector(0,0,1), color=vp.color.magenta)
legenda_x = vp.label(pos=vp.vector(1000,1200,0), text='X', box=0, opacity=0, color=vp.color.white)
legenda_y = vp.label(pos=vp.vector(-200,2000,0), text='Y', box=0, opacity=0, color=vp.color.white)
legenda_z = vp.label(pos=vp.vector(-200,1000,1000), text='Z', box=0, opacity=0, color=vp.color.white)

#projetil esfera
raio = 0.04
ro = 1.2
A = vp.pi*(raio**2)
C = 0.47

proj = vp.sphere(pos=vp.vector(-500,raio,0), radius=raio, color=vp.color.white, make_trail=True)

#velocidade inicial projetil
projvelinicial = vp.vector(velinicial*vp.cos(thetarad), velinicial*vp.sin(thetarad),0)

projmassa = 0.5 #massa

projp = projmassa * projvelinicial #momento linear

projFar = (-ro/2)*(A*C*(vp.mag(projvelinicial)**2)*(vp.norm(projvelinicial)))
Fres = (projmassa*g) + projFar #Força resultante

t0 = 0
dt = 0.001
arscale = 2
vetor = vp.arrow(pos=proj.pos, axis=arscale*projp, color=vp.color.red)

while proj.pos.y >= raio:
    vp.rate(50)
    
    projp = projp + Fres*t0
    
    proj.pos = proj.pos + (projp/projmassa)*t0
    
    vetor.pos = proj.pos
    vetor.axis = arscale*projp
    projv = projp/projmassa
    
    projFar = (-ro/2)*(A*C*(vp.mag(projv)**2)*(vp.norm(projv)))
    Fres = (projmassa*g) + projFar
    
    t0 += dt