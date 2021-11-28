from ..Cambio_de_unidades import *
from ..Geometria.geometria import *

import math

def ecuacion_yc_Rectangulo(Q,v,b,m1,m2,y):
    if Q!=0:
        ecuacion=((Q/math.sqrt(9.81))-(b*y+(m1*y**2)/2+(m2*y**2)/2)*math.sqrt(b*y+(m1*y**2)/2+(m2*y**2)/2)/(math.sqrt(b+m1*y+m2*y)))
    elif v!=0:
        ecuacion=v/math.sqrt(9.81)-((b*y+(m1*y**2)/2+(m2*y**2)/2)/(b+m1*y+m2*y))^(1/2)
    else:
        raise Exception ("faltan datos")
    return ecuacion

def derivada_yc_Rectangulo(Q,v,b,m1,m2,y):
    if Q!=0:
        derivada=((m1+m2)*(b*y+(m1*y**2)/2+(m2*y**2)/2)**(3/2))/(2*(b+m1*y+m2*y)**(3/2)) - (3/2)*math.sqrt(b+m1*y+m2*y)*math.sqrt(b*y+(m1*y**2)/2+(m2*y**2)/2)
    elif v!=0:
        derivada=-(1-((m1+m2)*(b*y+(m1*y**2)/2+(m2*y**2)/2))/(b+m1*y+m2*y)**2)/(2*math.sqrt((b*y+(m1*y**2)/2+(m2*y**2)/2)/(b+m1*y+m2*y)))
    else:
        raise Exception ("faltan datos")

    return derivada

def ecuacion_yc_Circulo(Q,v,d,y):
    if Q!=0:
        ecuacion=(Q/math.sqrt(9.81))-((((d**2)/8)*(math.pi+2*math.asin((y-(d/2))/(d/2))-math.sin(math.pi+2*math.asin((y-(d/2))/(d/2)))))**(3/2)/(d*math.sin((math.pi+2*math.asin((y-(d/2))/(d/2)))/2))**(1/2))
    elif v!=0:
        ecuacion=(v/math.sqrt(9.81))-((((d**2)/8)*(math.pi+2*math.asin((y-(d/2))/(d/2))-math.sin(math.pi+2*math.asin((y-(d/2))/(d/2)))))**(1/2)/(d*math.sin((math.pi+2*math.asin((y-(d/2))/(d/2)))/2))**(1/2))
    return ecuacion

def derivada_yc_Circulo(Q,v,d,y):
    if Q!=0:
        derivada=((d**2*(2*math.asin((2*(y-d/2))/d)+math.sin(2*math.asin((2*(y-d/2))/d))+math.pi))**(3/2)*math.cos(1/2*(2*math.asin((2*(y-d/2))/d)+math.pi)))/(16*math.sqrt(2)*math.sqrt(1-(4*(y-d/2)**2)/d**2)*(d*math.sin(1/2*(2*math.asin((2*(y-d/2))/d)+math.pi)))**(3/2))-(3*d**2*math.sqrt(d**2*(2*math.asin((2*(y-d/2))/d)+math.sin(2*math.asin((2*(y-d/2))/d))+math.pi))*(4/(d*math.sqrt(1-(4*(y-d/2)**2)/d**2))+(4*math.cos(2*math.asin((2*(y-d/2))/d)))/(d*math.sqrt(1-(4*(y-d/2)**2)/d**2))))/(32*math.sqrt(2)*math.sqrt(d*math.sin(1/2*(2*math.asin((2*(y-d/2))/d)+math.pi))))        
    elif v!=0:
        derivada=(math.sqrt(d**2*(2*math.asin((2*(y-d/2))/d)+math.sin(2*math.asin((2*(y-d/2))/d))+math.pi))*math.cos(1/2*(2*math.asin((2*(y-d/2))/d)+math.pi)))/(2*math.sqrt(2)*math.sqrt(1-(4*(y-d/2)**2)/d**2)*(d*math.sin(1/2*(2*math.asin((2*(y-d/2))/d)+math.pi)))**(3/2))-(d**2*(4/(d*math.sqrt(1-(4*(y-d/2)**2)/d**2))+(4*math.cos(2*math.asin((2*(y-d/2))/d)))/(d*math.sqrt(1-(4*(y-d/2)**2)/d**2))))/(4*math.sqrt(2)*math.sqrt(d**2*(2*math.asin((2*(y-d/2))/d)+math.sin(2*math.asin((2*(y-d/2))/d))+math.pi))*math.sqrt(d*math.sin(1/2*(2*math.asin((2*(y-d/2))/d)+math.pi))))
    return derivada

def yc(Q,b,v,m1,m2,um,d,ub,ud,uQ):  
    """Calcula la profundidad crítica. Para secciones rectángulares se recurre a una solución analítica. Para las demás se recurre a una solución numérica (Newton-Raphson)\n
    Q = caudal (m3/s) <br />
    b = base (m) <br />
    v= velocidad m/s <br />
    m1 = inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)<br />
    d = diámetro (m) \n  
    u_b=unidades de b (mm, cm, m, in)<br />
    u_d=unidades de d (mm, cm, m, in)<br />
    u_Q = unidades de caudal--> L, m3 <br />
    Los parámetros que no se requieran, se dejan en 0"""
    
    b=CU_m(b,ub)
    d=CU_m(d,ud)
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
    
    if uQ=='L':
        Q=Q/1000

    
    if d==0:        
        if m1==0 and m2==0:
            yc=((Q**2)/(9.81*(b**2)))**(1/3)
        else:
            error=1
            y=b+1
            
            while error>0.0001:
                yc=y-ecuacion_yc_Rectangulo(Q,v,b,m1,m2,y)/derivada_yc_Rectangulo(Q,v,b,m1,m2,y)
                error=abs(yc-y)
                y=yc
    else:
        error=1
        y=d/2
        while error>0.0001:
            yc=y-ecuacion_yc_Circulo(Q,v,d,y)/derivada_yc_Circulo(Q,v,d,y)
            error=abs(yc-y)
            y=yc

    return float(yc)

def vc (m1,m2,um,b,yc,d,uy,ub,ud):
    """Calcula la velocidad crítica a partir de Froude y geometría crítica\n
    m1 = inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)<br />
    b = base (m) <br>
    yc = profundidad crítica (m) <br>
    d = diámetro (m) \n
    u_y=unidades de y (mm, cm, m, in)<br />
    u_b=unidades de b (mm, cm, m, in)<br />
    u_d=unidades de d (mm, cm, m, in)<br />
    
    Los parámetros que no sean necesarios se dejan en 0"""
    yc=CU_m(yc,uy)
    b=CU_m(b,ub)
    d=CU_m(d,ud)
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
    
    if d==0:
        A,P,Rh,T,D=geom_r(yc,b,m1,m2,um,"m","m")
    else:
        ynd=yc/d
        yn,theta,A,P,Rh,T,D=geom_c(d,ynd,"m")
    
    v=math.sqrt(9.81*A/T)
    return v