from ..Cambio_de_unidades import *
from ..Geometria.geometria import *
from .flujoCritico import *

import math


def ecuacionManning_canal(Q,n,So,m1,m2,b,y,kn):    
    ecuacion=n*Q/math.sqrt(So)-kn*(b*y+(m1*y**2)/2+(m2*y**2)/2)**(5/3)/(b+y*math.sqrt(m1**2+1)+y*math.sqrt(m2**2+1))**(2/3)
    return ecuacion
def derivadaManning_canal(Q,n,So,m1,m2,b,y,kn):
    derivada=(2*kn*(math.sqrt(m1**2+1)+math.sqrt(m2**2+1))*(b*y+(m1*y**2)/2+(m2*y**2)/2)**(5/3))/(3*(b+math.sqrt(m1**2+1)*y+math.sqrt(m2**2+1)*y)**(5/3))-(5*kn*(b+m1*y+m2*y)*(b*y+(m1*y**2)/2+(m2*y**2)/2)**(2/3))/(3*(b+math.sqrt(m1**2+1)*y+math.sqrt(m2**2+1)*y)**(2/3))
    return derivada

def ecuacionManning_circ(Q,n,So,y,d,kn):
    ecuacion=n*Q/math.sqrt(So)-kn*((((math.pi+2*math.asin((y-(d/2))/(d/2)))-math.sin(math.pi+2*math.asin((y-(d/2))/(d/2))))*d**2/8)**(5/3))/(((math.pi+2*math.asin((y-(d/2))/(d/2)))*d/2)**(2/3))
    return ecuacion
def derivadaManning_circ(Q,n,So,y,d,kn):
    derivada=-(d**2*kn*(d**2*(-2*math.asin(1-(2*y)/d)-math.sin(2*math.asin(1-(2*y)/d))+math.pi))**(2/3)*(2*math.sin(2*math.asin(1-(2*y)/d))+5*math.pi*math.cos(2*math.asin(1-(2*y)/d))-2*math.asin(1-(2*y)/d)*(5*math.cos(2*math.asin(1-(2*y)/d))+3)+3*math.pi))/(24*2**(1/3)*math.sqrt((y*(d-y))/d**2)*(d*(math.pi-2*math.asin(1-(2*y)/d)))**(5/3))
    return derivada

def yn_manning(Q,n,So,m1,m2,um,b,d,i,uQ,ub,ud,uSo):
    """calcula yn con la ecuación de Manning por medio de Newton-Raphson\n
    Q = caudal (m3/s) <br>
    n = número de Manning <br>
    So = inclinación del canal <br>
    m1 = inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)<br />
    b = base (m) <br>
    d = diámetro (m) <br>
    i = sistema inglés (in) o sistema internacional (si)
    ub = unidades de b (mm, cm, m, in)<br />
    ud = unidades de d (mm, cm, m, in)<br />
    uQ = unidades de caudal--> L, m3 <br />
    uSo = unidades de inclinacion (mm, cm, m, in)"""
    
    d=CU_m(d,ud)
    b=CU_m(b,ub)
    So=CU_theta(So,uSo)
    So=math.tan(math.radians(So))
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
    
    if uQ=='L':
        Q=Q/1000
    
    if i.lower()=='in':
        kn=1.49
        
    elif i.lower()=='si':
        kn=1
       
    if d==0:
        error=1
        y=1
        while error>0.0001:
            yn=y-ecuacionManning_canal(Q,n,So,m1,m2,b,y,kn)/derivadaManning_canal(Q,n,So,m1,m2,b,y,kn)
            error=abs(yn-y)
            y=yn
    else: 
        error=1
        y=1
        while error>0.0001:
            yn=y-ecuacionManning_circ(Q,n,So,y,d,kn)/derivadaManning_circ(Q,n,So,y,d,kn)
            error=abs(yn-y)
            y=yn
    return y

def pendienteC_limite(n,Q,b,m1,m2,um,d,uQ,ub,ud):
    """Calcula la pendiente crítica a partir de la geometría, el caudal máximo y el n de Manning\n
    n = número de Manning <br>
    Q = caudal (m3/s) <br>
    b = base (m) <br>
    m1 = inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)<br />
    d = diámetro\n
    ub = unidades de b (mm, cm, m, in)<br />
    ud = unidades de d (mm, cm, m, in)<br />
    uQ = unidades de caudal--> L, m3 <br />
    Los parámetros que no sean necesarios se dejan como 0"""
    
    d=CU_m(d,ud)
    b=CU_m(b,ub)
    if uQ=='L':
        Q=Q/1000
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
    
    y = yc(Q,b,0,m1,m2,"m",d,"m","m","m3/s")
    v=vc(m1,m2,um,b,y,d,"m","m","m")
    
    if d == 0:
        A,P,Rh,T,D=geom_r(y,b,m1,m2,"m","m","m")
    else:
        ynd=y/d
        yn,theta,A,P,Rh,T,D=geom_c(d,ynd,"m")
    
    Sc = Q**2*n**2*P**(4/3)/(A**(10/3))
    return y,v,Sc

def pendienteC_especifica(n,y,b,m1,m2,um,d,ub,ud,uy):
    """Calcula la pendiente crítica a partir de la geometría, yc y el n de Manning\n
    n = número de Manning <br>
    yc = profundidad crítica <br>
    b = base (m) <br>
    m1 = inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)<br />
    d = diámetro\n
    ub = unidades de b (mm, cm, m, in)<br />
    ud = unidades de d (mm, cm, m, in)<br />
    uy = unidades de y (mm, cm, m, in) <br />
    Los parámetros que no sean necesarios se dejan como 0"""
    
    d=CU_m(d,ud)
    b=CU_m(b,ub)
    y=CU_m(y,uy)
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
    
    v=vc(m1,m2,"m",b,y,d,"m","m","m")
    if d == 0:
        A,P,Rh,T,D=geom_r(y,b,m1,m2,"m","m","m")
    else:
        ynd=y/d
        yn,theta,A,P,Rh,T,D=geom_c(d,ynd,"m")
    Sc=v**2*n**2/(Rh**(4/3))
    return Sc

