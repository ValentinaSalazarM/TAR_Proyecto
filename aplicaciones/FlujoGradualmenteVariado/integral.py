from ..Cambio_de_unidades import *

import math
import numpy as np
import scipy.integrate as integrate

def funcionIntegral_rectangular(y,Q,n,So,b,m1,m2):
    A = b*y+(m1*y**2)/2+(m2*y**2)/2
    P=b+y*np.sqrt(m1**2+1)+y*np.sqrt(m2**2+1)
    T=b+m1*y+m2*y
    f =((1-(Q**2*(T))/(9.81*(A)**3))/(So-((n**2*Q**2*(P)**(4/3))/((A)**(10/3)))))
    return f

def funcionIntegral_circular(y,Q,n,So,d):
    theta = np.pi+2*np.arcsin((y-(d/2))/(d/2))
    A= (theta-np.sin(theta))*d**2/8
    P= theta*d/2
    T=d*np.cos(np.arcsin((y-(d/2))/(d/2)))
    f =((1-(Q**2*(T))/(9.81*(A)**3))/(So-((n**2*Q**2*(P)**(4/3))/((A)**(10/3)))))
    return f

def fgv_int(Q,n,So,b,m1,m2,um,d,y1,y2,uQ,uSo,ub,ud,uy1,uy2):
    """Calcula la longitud que requiere el flujo para pasar de una profundidad a otra\n
    Q = caudal (m3/s) <br>
    n = número de Manning <br>
    So = Inclinación del canal <br>
    b = base (m) <br>
    m1 = inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)<br />
    d = diámetro (m) <br>
    y1 = profundidad de control (m) <br>
    y2 = profundidad objetivo (m)
    uQ = unidades de caudal--> L, m3 <br />
    uSo = unidades de inclinacion (mm, cm, m, in)
    ub = unidades de b (mm, cm, m, in)<br />
    ud = unidades de d (mm, cm, m, in)<br />
    uy1 = unidades de uy1 (mm, cm, m, in)<br />
    uy2 = unidades de uy2 (mm, cm, m, in)<br />"""
    
    b=CU_m(b,ub)
    d=CU_m(d,ud)
    y1=CU_m(y1,uy1)
    y2=CU_m(y2,uy2)
    So=CU_theta(So,uSo)
    So=math.tan(math.radians(So))
    if uQ=='L':
        Q=Q/1000
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
    
    
    if d==0:
        x=integrate.quadrature(funcionIntegral_rectangular,y1,y2,args=(Q,n,So,b,m1,m2),tol=1e-8)[0]
    else:
        x=integrate.quadrature(funcionIntegral_circular,y1,y2,args=(Q,n,So,d),tol=1e-8)[0] #no cuadra con el resultado de calculadora
    return x