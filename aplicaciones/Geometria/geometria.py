from ..Cambio_de_unidades import *
import math

'-----------------------------------------------------------------------------'
'Funciones que retornan geometría del canal'

def  geom_c(d,ynd,ud):
    """ Esta función retorna la geometría de un canal circular\n
    d=diametro<br />
    ynd=relación de llenado<br />
    unidades=unidades de d (mm, cm, m, in)<br />"""
    
    d = CU_m(d,ud)

    yn=ynd*d
    theta = math.pi+2*math.asin((yn-(d/2))/(d/2))
    A= (theta-math.sin(theta))*d**2/8
    P= theta*d/2
    Rh=(1-math.sin(theta)/theta)*d/4
    T=d*math.cos(math.asin((yn-(d/2))/(d/2)))
    D=A/T
    return yn,theta,A,P,Rh,T,D

def geom_r(y,b,m1,m2,um,uy,ub):
    """ Esta función retorna la geometría de un canal geométrico no circular\n
    y=profundidad<br />
    b=base<br />
    m1=inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)
    uy=unidades de y (mm, cm, m, in)<br />
    ub=unidades de b (mm, cm, m, in)<br />"""
    
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
    
    y=CU_m(y,uy)
    b=CU_m(b,ub)
    
    A = b*y+(m1*y**2)/2+(m2*y**2)/2
    P=b+y*math.sqrt(m1**2+1)+y*math.sqrt(m2**2+1)
    Rh=A/P
    T=b+m1*y+m2*y
    D=A/T
    return A,P,Rh,T,D

'-----------------------------------------------------------------------------'
def froude(y,b,m1,m2,um,Q,v,d,uy,ub,ud,uQ):
    """Calcula el número de froude con las propiedades geométricas y el caudal\n
    y=profundidad (m)<br />
    b=base (m)<br />
    m1=inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)<br />
    Q=caudal (m3/s) <br />
    v = velocidad (m/s) <br />
    d=diámetro (m)<br />
    u_y=unidades de y (mm, cm, m, in)<br />
    u_b=unidades de b (mm, cm, m, in)<br />
    u_d=unidades de d (mm, cm, m, in)<br />
    u_Q = unidades de caudal--> L, m3 <br />
    Los parámetros que no se requieran, se dejan en 0"""
    
    y=CU_m(y,uy)
    b=CU_m(b,ub)
    d=CU_m(d,ud)
    if uQ=='L':
        Q=Q/1000
    
    if d==0:
        A,P,Rh,T,D=geom_r(y,b,m1,m2,um,"m","m")
    else:
        ynd=y/d
        yn,theta,A,P,Rh,T,D=geom_c(d,ynd,"m")
    
    if v!=0:
        Fr = v/(math.sqrt(9.81*A/T))
    elif Q!=0:
        Fr = Q/(A*math.sqrt(9.81*A/T))
    else:
        raise Exception ("Faltan datos.")
    return Fr
