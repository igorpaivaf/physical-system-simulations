# py.exe C:\Users\igorp\Desktop\VSCode\Projetos\Simulações\movproj_comresistquic.py
import vpython as vp

raio = 1
bola = vp.sphere(pos=vp.vector(0,0,0), radius=raio, color=vp.color.red, make_trail=True)
chao = vp.box(pos=vp.vector(0,0,0), size=vp.vector(900,2,200), color=vp.color.green)

bola.v = vp.vector(10,20,0)
g = vp.vector(0,-9.8,0)

C = 0.005
Far = (-1)*C*vp.mag(bola.v)*vp.norm(bola.v)

m = 0.143
Fp = m*g

t = 0.0
dt = 0.0001
tf = 50

dist = 0

while t < tf:
    vp.rate(100000)
    Fr = Fp + Far
    
    a = Fr/m
    
    bola.v += a*dt
    bola.pos += bola.v*dt
    
    t += dt
    
    dist += bola.v.x * dt
    
    if bola.pos.y < 0:
        bola.v.y = (-bola.v.y)
        bola.v.x = bola.v.x
    
    Far = (-1)*C*vp.mag(bola.v)*vp.norm(bola.v)
    
    vp.scene.camera.follow(bola)