# py.exe C:\Users\igorp\Desktop\VSCode\Projetos\Simulações\pendulo.py
import vpython as vp

vp.scene.width = 800
vp.scene.height = 500

# ponto de conexão
conex = vp.vector(0,0,0)

# tamanho do fio
L  = 20

# gravidade
g = 9.8

# olhando os ângulos
theta = vp.pi/6
phi = vp.pi/4

# teto
teto = vp.box(pos=conex, size=vp.vector(8,0.4,8), color=vp.color.blue)

# esfera
esf = vp.sphere(pos=vp.vector(-L*vp.sin(theta)*vp.sin(phi),-L*vp.cos(theta),-L*vp.sin(theta)*vp.cos(phi)), radius=1.2, color=vp.color.purple, make_trail=True, trail_type="points", interval=8, retain=45)

# fio
fio = vp.cylinder(pos=conex, axis=esf.pos-conex, radius=0.15, color=vp.color.white)

# definindo um dphi para atualizar dentro do while
dphi = 0.01

while True:
    vp.rate(200)

    # atualizando a posição da esfera e do fio conforme há mundança no phi
    fio.axis = esf.pos = vp.vector(-L*vp.sin(theta)*vp.sin(phi),-L*vp.cos(theta),-L*vp.sin(theta)*vp.cos(phi))

    # atualizando o valor de phi, somando o dphi
    phi += dphi

    # a velocidade angular = dphi*rate = 0.01*200 = 2