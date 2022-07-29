# py.exe C:\Users\igorp\Desktop\VSCode\Projetos\Simulações\satorbplaneta.py
import vpython as vp

vp.scene.tile = 'Sátelite orbitando um Planeta'
vp.scene.width = vp.scene.height = 800 #tamanho da janela

#Definindo os objetos
planeta = vp.sphere(pos=vp.vector(0,0,0), radius=1, color=vp.color.red)
satelite = vp.sphere(pos=vp.vector(10,0,0), radius=0.2, color=vp.color.blue, make_trail = True)

#Definindo os valores das massas e da constante da gravitação universal
G = 1
m = 1
M = 100

#Definindo a velocidade do satélite
projvsat = vp.vector(0,vp.pi,0)

#Definindo o momento linear
projp = m * projvsat

#Definindo a distância ao quadrado do satélite do centro do planeta
projr = satelite.pos - planeta.pos
versorr = vp.hat(projr)
modulor = vp.mag2(projr)

projFg = (G*M*m)/(modulor) * -1*versorr

t0 = 0
dt = 0.001
tfinal = 2

while (t0 < tfinal) and (satelite.pos != planeta.pos):
    vp.rate(100)
    
    projp = projp + projFg*t0
    
    satelite.pos = satelite.pos + (projp/m)*t0
    
    projr = satelite.pos - planeta.pos
    versorr = vp.hat(projr)
    modulor = vp.mag2(projr)

    projFg = (G*M*m)/(modulor) * -1*versorr
    t0 += dt