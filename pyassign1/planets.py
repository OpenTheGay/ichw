from turtle import *
import math

wn = Screen()
wn.bgcolor("black")

M_sun = 1.988 * 10**30
G = 6.6738 * 10**-11
sun,mer,ven,ear,mar,jup,sat=Turtle(),Turtle(),Turtle(),Turtle(),Turtle(),Turtle(),Turtle()

data = {mer: (0.698, 0.460, 'red'), ven: (1.089, 1.075, 'orange'), ear: (1.521, 1.471, 'blue'),
        mar: (2.492, 2.067, 'gray'), jup: (8.166, 7.405, 'brown'), sat: (15.145, 13.525, 'green')}

def velocity_at_aphelion(aphelion, perihelion):
    a = (aphelion + perihelion) / 2
    c = (aphelion - perihelion) / 2
    return math.sqrt((a-c) * G * M_sun / (a+c) / a)

def acceleration_at_position(P):
    a = G * M_sun / P[0]**2
    return a * t

def cartesian_to_polar(p):
    x,y = p[0], p[1]
    r = math.sqrt(x*x + y*y)
    if x>=0:
        return (r, math.asin(y/r))
    else:
        return (r, math.pi-math.asin(y/r))

velocity = {planet: (velocity_at_aphelion(value[0] * 10**11, value[1] * 10**11), math.pi/2) for planet, value in data.items()}

t = 86400

sun.shape('circle')
sun.color('yellow')
for planet, value in data.items():
    planet.shapesize(0.3)
    planet.shape('circle')
    planet.color(value[2])
    planet.up()
    planet.forward(value[0]*10**11*10**-9.5)
    planet.down()

while 1:
    for planet in velocity:
        V = velocity[planet]
        pseudo_p = planet.position()
        p = (pseudo_p[0] * 10**9.5, pseudo_p[1] * 10**9.5)
        P = cartesian_to_polar(p)
        U = (acceleration_at_position(P), math.pi + P[1])
        w = (V[0] * math.cos(V[1]) + U[0] * math.cos(U[1]), V[0]*math.sin(V[1]) + U[0]*math.sin(U[1]))
        W = cartesian_to_polar(w)
        q = (p[0] + w[0] * t, p[1] + w[1] * t)
        pseudo_q = (q[0] / 10**9.5, q[1] / 10**9.5)
        planet.speed(W[0]* 10**-3)
        planet.goto(pseudo_q)
        velocity[planet] = W
