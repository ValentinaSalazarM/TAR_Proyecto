from ..Cambio_de_unidades import *
from ..Geometria.geometria import *
from ..EcuacionManning.flujoCritico import *

import math
from sympy.solvers import solve
from sympy import Symbol
from sympy import var,solveset, S

def conservacionE(y1,m11,m12,b1,Q,y2,m21,m22,b2,uy1,uy2,um,uQ,ub1,ub2,v1,v2,z,uz,incognita):
    """Encuentra el parámetro que falta por medio de la ecuación de conservación de energía y de masa\n
    y1 = profundidad 1 (mm, cm, m, in) <br>
    y2 = profundidad 2 (mm, cm, m, in) <br>
    b1 = base 1 (mm, cm, m, in) <br>
    b2 = base 2 (mm, cm, m, in) <br>
    Q = caudal (m3, L) <br>
    m11 = inclinación izquierda 1 (grados, rad, m/m)<br>
    m12 = inclinación derecha 1 (grados, rad, m/m)<br>
    m21 = inclinación izquierda 2 (grados, rad, m/m)<br>
    m22 = inclinación derecha 2 (grados, rad, m/m)<br>
    uQ = unidades de caudal--> L, m3 <br />
    ub1 = unidades de b1 (mm, cm, m, in)<br />
    ub2 = unidades de b2 (mm, cm, m, in)<br />
    uy1 = unidades de y1 (mm, cm, m, in)<br />
    uy2 = unidades de y2 (mm, cm, m, in)<br />
    um = unidades de inclinación (grados, rad, m/m)
    v1 = velocidad 1 (m/s)
    v2 = velocidad 2 (m/s)
    z = elevación del fondo <br />
    uz = unidades de z (mm, cm, m, in)<br />
    incognita = lo que se busca (caudal, y1, y2, b1, b2, m11, m12, m21, m22, v1, v2)
    El/los parámetros que no se conocen se dejan como 0
    """
    b1=CU_m(b1,ub1)
    b2=CU_m(b2,ub2)
    y1=CU_m(y1,uy1)
    y2=CU_m(y2,uy2) 
    if uQ=='L':
        Q=Q/1000
        
    m11=CU_theta(m11,um)
    m12=CU_theta(m12,um)
    m21=CU_theta(m21,um)
    m22=CU_theta(m22,um)
    
    m11=math.tan(math.radians(m11))
    m12=math.tan(math.radians(m12))
    m21=math.tan(math.radians(m21))
    m22=math.tan(math.radians(m22))
    
    "Caudal --> se tiene geometría de ambos lados y z"
    if incognita =="caudal":
        
        x = Symbol("x") #v1
                
        A1,P1,Rh1,T1,D1=geom_r(y1, b1, m11, m12, um, uy1, ub1)
        A2,P2,Rh2,T2,D2=geom_r(y2, b2, m21, m22, um, uy2, ub2)
        
        v1=solve(x**2/(2*9.81)+y1-(A1/A2*x)**2/(2*9.81)-y2-z,x)
        v = [x for x in v1 if x > 0]
        Q=v[0]*A1
        return v[0],Q
    
    "y2 con geometría 1 y 2 y Q o velocidad 1 --> y1,b1,m11,m12,um,uy1,ub1,v1 o Q,z"
    if incognita=='y':
        A1,P1,Rh1,T1,D1=geom_r(y1, b1, m11, m12, um, uy1, ub1)
        if Q==0:
            if v1==0:
                return "Debe ingresar caudal o velocidad"
            else:
                Q=A1*v1
        else:
            v1=Q/A1
        y=var("y", real=True) #y2
        y2=solveset(y1+Q**2/(A1**2*2*9.81)-y-Q**2/(2*9.81*(b2*y+(m21*y**2)/2+(m22*y**2)/2)**2)-z,y)
        y=Symbol("y",real=True) #y2
        reales=solve(y1+Q**2/(A1**2*2*9.81)-y-Q**2/(2*9.81*(b2*y+(m21*y**2)/2+(m22*y**2)/2)**2)-z,y)
        
        #Fenomeno de choque. Calcula represamiento
        if len(reales)<2:
            y_c=yc(Q,b2,0,m21,m22,"m",0,"m",0,"m3")
            Ac,Pc,Rhc,Tc,Dc=geom_r(y_c, b2, m21, m22, um, uy2, ub2)
            Ec=y_c+Q**2/((Ac)**2*2*9.81)
         
        
            y=var("y", real=True) #y2
            y1_n=solveset(-Ec+y+Q**2/((b1*y+(m11*y**2)/2+(m12*y**2)/2)**2*2*9.81),y)
            Represamiento = max(y1_n.args[0],y1_n.args[1],y1_n.args[2])-y1
        
            return y2.args[0],y2.args[1],y2.args[2],y_c,Ec,y1_n.args[0],y1_n.args[1],y1_n.args[2],Represamiento
        else:
            return y2.args[0],y2.args[1],y2.args[2],"","","","","",""
    
    # máximo deltaZ para que no haya fenónemo de choque
    if incognita=='maximoZ':
        A1,P1,Rh1,T1,D1=geom_r(y1, b1, m11, m12, um, uy1, ub1)
        if Q==0:
            if v1==0:
                return "Debe ingresar caudal o velocidad"
            else:
                Q=A1*v1
        else:
            v1=Q/A1
        
        y_c=yc(Q,b2,0,m21,m22,"m",0,"m",0,"m3")
        Ac,Pc,Rhc,Tc,Dc=geom_r(y_c, b2, m21, m22, um, uy2, ub2)
        Ec=y_c+Q**2/((Ac)**2*2*9.81)
        
        E1=y1+Q**2/((A1)**2*2*9.81)
        z = E1-Ec
                
        return z, y_c
    
    # mínimo b2 para que no haya fenónemo de choque
    if incognita=='minimoB':
        A1,P1,Rh1,T1,D1=geom_r(y1, b1, m11, m12, um, uy1, ub1)
        if Q==0:
            if v1==0:
                return "Debe ingresar caudal o velocidad"
            else:
                Q=A1*v1
        else:
            v1=Q/A1
        
        E1 = y1+Q**2/((A1)**2*2*9.81)-z
        y_c=yc(Q,b1,0,m11,m12,"m",0,"m",0,"m3")
        
        b=var("b", real=True) #y2
        b2=solveset(-E1+y_c+Q**2/((b*y_c+(m21*y_c**2)/2+(m22*y_c**2)/2)**2*2*9.81),b)
        b2 = [x for x in b2 if x > 0]
        
        return E1, b2[0]