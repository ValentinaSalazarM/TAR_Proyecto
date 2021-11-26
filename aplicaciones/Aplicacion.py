# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 12:59:07 2021

@author: Gabriela Bermudez
"""

'Importar librerias'
import numpy as np
import math
import scipy.integrate as integrate
from sympy.solvers import solve
from sympy import Symbol
from sympy import var,solveset, S
import numpy as np
'-----------------------------------------------------------------------------'
'Funciones para cambio de unidades'

def CU_m(x,u):
    """Cambia unidades de longitud ingresadas a metros \n
    x=valor
    u=unidades --> cm, mm, in"""
    if u=='mm':
        var=x/1000
    elif u=='cm':
        var=x/100
    elif u=='in':
        var=x*0.0254
    else:
        var=x
    return var

def CU_theta(x,u):
    """Cambia unidades de ángulo ingresado a grados \n
    x=valor
    u=unidades --> grados, radianes, m/m """
    if u=='grados':
        theta=x
    elif u=='radianes':
        theta=math.degrees(x)
    else:
        theta=math.degrees((math.atan(x)))
        
    return theta


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
        Fr=Q/(A*math.sqrt(9.81*A/T))
    else:
        raise Exception ("Faltan datos")
    return Fr

'-----------------------------------------------------------------------------'
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

'-----------------------------------------------------------------------------'
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
    
'-----------------------------------------------------------------------------'
def momentum(Q,b,m1,m2,um,y,d,uQ,ub,uy,ud):
    """Calcula momentum de una sección a partir de geometría y caudal\n
    Q = caudal (m3/s) <br />
    y = profundidad <br />
    b = base (m) <br />
    m1 = inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)<br />
    d = diámetro (m) <br />
    u_y=unidades de y (mm, cm, m, in)<br />
    u_b=unidades de b (mm, cm, m, in)<br />
    u_d=unidades de d (mm, cm, m, in)<br />
    u_Q = unidades de caudal--> L, m3 <br />"""   
    
    y=CU_m(y,uy)
    b=CU_m(b,ub)
    d=CU_m(d,ud)
    if uQ=='L':
        Q=Q/1000
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
        
    if d==0:        
        if m1==0 and m2==0:
            mom=y**2/2+(Q/b)**2/(9.81*y)
        
        else:
            mom=m1*y**3/6+m2*y**3/6+b*y**2/2+Q**2/(9.81*(b*y+(m1*y**2)/2+(m2*y**2)/2))
    
    else:
        theta = math.pi+2*math.asin((y-(d/2))/(d/2))
        mom=d**3/24*(3*math.sin(theta/2)-(math.sin(theta/2))**3-3*(theta/2)*math.cos(theta/2))+Q**2/(9.81*d**2*(theta-math.sin(theta))/8)
    return float(mom)


'-----------------------------------------------------------------------------'
'    Falta probar los no rectangulares'

def fuerzaCompuerta(y1,y2,b,Q,m1,m2,um,rho,uy1,uy2,ub,uQ):
    """Calcula fuerza sobre la compuerta en canales primáticos\n
    y1= profundidad de sección 1 <br />
    y2= profundidad de sección 2 <br />
    b = base (m) <br />
    Q = caudal (m3/s) <br />
    m1 = inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)<br />
    rho = densidad (kg/m3)
    uy1=unidades de y1 (mm, cm, m, in)<br />
    uy2=unidades de y1 (mm, cm, m, in)<br />
    ub=unidades de b (mm, cm, m, in)<br />
    uQ = unidades de caudal--> L, m3 <br />
    """
    y1=CU_m(y1,uy1)
    y2=CU_m(y2,uy2)
    ub=CU_m(b,ub)
    if uQ=='L':
        Q=Q/1000
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
    
    M1=momentum(Q,b,m1,m2,um,y1,0,"","m","m","m")
    M2=momentum(Q,b,m1,m2,um,y2,0,"","m","m","m")
    
    F_a=M1-M2
    
    if m1==0 and m2==0:
        f=rho*9.81*b*F_a
    else:
        f=rho*9.81*F_a
    return M1,M2,F_a,f


'-----------------------------------------------------------------------------'
# def ecuacionTriangulo(Q,m,y1,y2,f):
#     ecuacion= ((1/3)*(y1**3-y2**3)+(Q**2/(9.81*m)*((1/y1**2)-(1/y2**2)))-f)/(y2-y1)
#     return ecuacion
# def derivadaTriangulo(Q,m,y1,y2,f):
#     derivada=((2*Q**2)/(9.81*m*y2**3)-y2**2)/(y2-y1)-(-f+(Q**2*(1/y1**2-1/y2**2))/(9.81*m)+1/3*(y1**3-y2**3))/(y2-y1)**2
#     return derivada


# def ecuacionTrapecio(Q,m,b,y1,y2,f):
#     ecuacion=((m/3)*(y1**3-y2**3)+(b/2)*(y1**2-y2**2)+(Q**2/9.81)*((1/(m*y1**2+b*y1))-(1/(m*y2**2+b*y2)))-f)/(y2-y1)
#     return ecuacion 
# def derivadaTrapecio(Q,b,m,y1,y2,f):
#     derivada=((Q**2*(b+2*m*y2))/(9.81*(b*y2+m*y2**2)**2)-b*y2-m*y2**2)/(y2-y1)-((Q**2*(1/(b*y1+m*y1**2)-1/(b*y2+m*y2**2)))/9.81+(1/2)*b*(y1**2-y2**2)+1/3*m*(y1**3-y2**3)-f)/(y2-y1)**2
#     return derivada

def ecuacionSubsecuente(Q,b,m1,m2,y1,y2,f):
    ecuacion = ((1/6)*(m1*y1**3+m2*y1**3-m1*y2**3-m2*y2**3)+(b/2)*(y1**2-y2**2)+(Q**2/(9.81*((m1*y1**2+m2*y1**2)/2+b*(y1))))-(Q**2/(9.81*((m1*y2**2+m2*y2**2)/2+b*(y2))))-f)/(y2-y1)
    return ecuacion
def derivadaSubsecuente(Q,b,m1,m2,y1,y2,f):
    #derivada = (-(2*y2**6*9.81*(m1+m2)**3+y2**5*(11*b-(m1+m2)*y1)*9.81*(m1+m2)**2+5*y2**4*(4*b**2-3*b*(m1+m2)*y1-(m1+m2)**2*y1**2)*9.81*(m1+m2)+2*y2**3*(6*b**3-22*b**2*(m1+m2)*y1-7*b*(m1+m2)**2*y1**2-(3*f-(m1+m2)*y1**3)*(m1+m2)**2)*9.81-2*y2**2*(18*b**3*y1-6*b**2*(m1+m2)*y1**2+b*(12*f-11*(m1+m2)*y1**3)*(m1+m2)+(3*f-2*(m1+m2)*y1**3)*(m1+m2)**2*y1)*9.81+y2*(36*b**3*9.81*y1**2-4*b**2*(6*f-7*(m1+m2)*y1**3)*9.81+3*b*9.81*(m1+m2)**2*y1**4+(6*f*9.81*(m1+m2)*y1**2-9.81*(m1+m2)**2*y1**5-36*Q**2)*(m1+m2))-12*b**3*9.81*y1**3+8*b**2*(3*f-2*(m1+m2)*y1**3)*9.81*y1+b*(24*f*9.81*(m1+m2)*y1**2-7*9.81*(m1+m2)**2*y1**5-48*Q**2)+(6*f*9.81*(m1+m2)*y1**2-9.81*(m1+m2)**2*y1**5-12*Q**2)*(m1+m2)*y1))/(6*(y2-y1)**2*(y2*(m1+m2)+2*b+(m1+m2)*y1)*(y2**2*(m1+m2)+2*y2*b-(2*b+(m1+m2)*y1)*y1)*9.81)
    derivada = (-(2*y2**7*(2*b+(m1+m2)*y1)*9.81*(m1+m2)**3*y1+y2**6*(2*b+(m1+m2)*y1)*(11*b-3*(m1+m2)*y1)*9.81*(m1+m2)**2*y1+2*y2**5*b*(2*b+(m1+m2)*y1)*(10*b-9*(m1+m2)*y1)*9.81*(m1+m2)*y1+y2**4*(24*b**4*9.81*y1-60*b**3*9.81*(m1+m2)*y1**2-30*b**2*9.81*(m1+m2)**2*y1**3-b*(12*f-5*(m1+m2)*y1**3)*9.81*(m1+m2)**2*y1-(6*f*9.81*(m1+m2)*y1**2-9.81*(m1+m2)**2*y1**5-12*Q**2)*(m1+m2)**2)-4*y2**3*b*(12*b**3*9.81*y1**2+b*(12*f-5*(m1+m2)*y1**3)*9.81*(m1+m2)*y1+(6*f*9.81*(m1+m2)*y1**2-9.81*(m1+m2)**2*y1**5-12*Q**2)*(m1+m2))+4*y2**2*(6*b**4*9.81*y1**3-b**3*(12*f-5*(m1+m2)*y1**3)*9.81*y1-b**2*(6*f*9.81*(m1+m2)*y1**2-9.81*(m1+m2)**2*y1**5-12*Q**2)-18*b*Q**2*(m1+m2)*y1-9*Q**2*(m1+m2)**2*y1**2)-24*y2*(4*b**2-(m1+m2)**2*y1**2)*Q**2*y1+24*b*(2*b+(m1+m2)*y1)*Q**2*y1**2))/(6*y2**2*(y2-y1)**2*(y2*(m1+m2)+2*b)**2*(2*b+(m1+m2)*y1)*9.81*y1)
    return derivada
    
def y_subsecuente(Q,b,m1,m2,um,y1,f,uy1,ub,uQ):
    """Calcula profundidad subsecuente por medio de conservación del momento. Para canales rectangulares se utiliza la solución analítica. Para los demás se recurre a una solución numérica (Newton Raphson).\n
    Q = caudal (m3/s) <br>
    b = base (m) <br>
    m1 = inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)<br />
    y1 = profundidad de sección 1 <br>
    f=fuerza aplicada en caso de resalto forzado (si no es forzado, poner 0)
    ub = unidades de b (mm, cm, m, in)<br />
    uQ = unidades de caudal--> L, m3 <br />
    uy1 = unidades y1 (mm ,cm ,m , in)"""
    
    y1=CU_m(y1,uy1)
    b=CU_m(b,ub)
    if uQ=='L':
        Q=Q/1000
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
    
    if m1==0 and m2==0:
        Fr=froude(y1,b,0,0,"",Q,0,0,"m","m","m","m3/s")
        #froude(y1,b,m,Q,0,0,"m","m","m3")
        y2=y1/2*(math.sqrt(1+8*Fr**2)-1)
    # elif b==0:
    #     error=1
    #     y=2*y1
    #     while error>0.0001:
    #         y2=y-ecuacionTriangulo(Q,m,y1,y,f)/derivadaTriangulo(Q,m,y1,y,f)
    #         error=abs(y2-y)
    #         y=y2
    # else:
    #     error=1
    #     y=2*y1
    #     while error>0.0001:
    #         y2=y-ecuacionTrapecio(Q,m,b,y1,y,f)/derivadaTrapecio(Q,b,m,y1,y,f)
    #         error=abs(y2-y)
    #         y=y2
    else:
        error=1
        y=4*y1
        while error>0.0001:
            num=ecuacionSubsecuente(Q,b,m1,m2,y1,y,f)
            den=derivadaSubsecuente(Q,b,m1,m2,y1,y,f)
            y2=y-num/den
            error=abs(y2-y)
            y=y2
    return y2

'-----------------------------------------------------------------------------'
# def eficienciaRH(Q,b,m1,m2,um,y1,f,uy1,ub,uQ):
#     """Calcula eficiencia del RH a partir del caudal, geometría aguas arriba y fuerza en caso de ser forzado\n
#     Q = caudal (m3/s) <br>
#     b = base (m) <br>
#     m1 = inclinación lado 1<br />
#     m2 = inclinación lado 2<br />
#     um = unidades de m (grados, radianes, m/m)<br />
#     y1 = profundidad en sección 1 <br>
#     f = fuerza aplicada en caso de resalto forzado (si no es forzado, poner 0) <br>
#     ub = unidades de b (mm, cm, m, in)<br />
#     uQ = unidades de caudal--> L, m3 <br />
#     uy1 = unidades y1 (mm ,cm ,m , in)"""
    
#     y1=CU_m(y1,uy1)
#     b=CU_m(b,ub)
#     if uQ=='L':
#         Q=Q/1000
#     m1=CU_theta(m1,um)
#     m2=CU_theta(m2,um)
#     m1=math.tan(math.radians(m1))
#     m2=math.tan(math.radians(m2))
    
#     y2=y_subsecuente(Q,b,m1,m2,"m",y1,f,"m","m","m3/s")
    
#     A1,P1,Rh1,T1,D1=geom_r(y1,b,m1,m2,"m","m","m")
#     A2,P2,Rh2,T2,D2=geom_r(y2,b,m1,m2,"m","m","m")
        
#     E1=y1+Q**2/(2*9.81*A1**2)
#     E2=y2+Q**2/(2*9.81*A2**2)+f
    
#     eficiencia=abs(E1-E2)/E1*100
    
#     return (E1, E2), (eficiencia,)

'-----------------------------------------------------------------------------'
def eficienciaRH(Q,b,m1,m2,um,y1,yn,f,l,i,uQ,ub,uy1,ul,ui):
    """Calcula eficiencia del RH inclinado a partir del caudal, geometría aguas arriba, inclinación del canal y longitud de la parte inclinada del canal (utilizar gráfica)\n
    Q = caudal <br>
    b = base <br>
    m1 = inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)<br />
    y1 = profundidad en sección 1 <br>
    yn= profundidad natural del río <br>
    f = fuerza aplicada en caso de resalto forzado (si no es forzado, poner 0) <br>
    l = longitud de la parte inclinada del resalto <br>
    i = inclinación del canal (grados, radianes, m/m)
    ub = unidades de b (mm, cm, m, in)<br />
    uQ = unidades de caudal--> L, m3 <br />
    uy1 = unidades y1 (mm ,cm ,m , in) <br />
    ul = unidades de longitud--> (mm ,cm ,m , in) 
    ui = unidades de inclinacion--> grados, radianes, m/m <br />"""
    
    y1=CU_m(y1,uy1)
    b=CU_m(b,ub)
    l=CU_m(l,ul)
    if uQ=='L':
        Q=Q/1000
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
    
    if i!=0:    
        inclinacion=CU_theta(i,ui)
        z=l*math.tan(math.radians(inclinacion))
    else:
        z=0
        
    A1,P1,Rh1,T1,D1=geom_r(y1,b,m1,m2,"m","m","m")
    E1=y1+Q**2/(2*9.81*A1**2)+z
    
    if yn!=0:
        A2,P2,Rh2,T2,D2=geom_r(yn,b,m1,m2,"m","m","m")
        E2=yn+Q**2/(2*9.81*A2**2)
    else:
        y2=y_subsecuente(Q,b,m1,m2,"m",y1,f,"m","m","m3/s")
        A2,P2,Rh2,T2,D2=geom_r(y2,b,m1,m2,"m","m","m")
        E2=y2+Q**2/(2*9.81*A2**2)+f
        
    eficiencia=abs(E1-E2)/E1*100
    
    return (E1, E2, z), (eficiencia,)
'-----------------------------------------------------------------------------'
def clasificacionResalto(Q,b,m1,m2,d,ud,um,y,ub,uy,uQ):
    """Clasifica resalto con el número de Froude a partir de las propiedades geométricas aguas arriba\n
    Q = caudal (m3/s) <br>
    b = base (m) <br>
    m1 = inclinación lado 1<br />
    m2 = inclinación lado 2<br />
    um = unidades de m (grados, radianes, m/m)<br />
    y = profundidad aguas arriba <br />
    ub = unidades de b (mm, cm, m, in)<br />
    uy = unidades de y (mm, cm, m, in)<br />
    uQ = unidades de caudal--> L, m3"""
    
    y=CU_m(y,uy)
    b=CU_m(b,ub)
    d=CU_m(y,ud)
    if uQ=='L':
        Q=Q/1000
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
    
    Fr=froude(y,b,m1,m2,"m",Q,0,d,"m","m","m","m3/s")
    if Fr<1:
        return (Fr,),('Flujo subcrítico',)
    elif Fr<=1.7:
        return (Fr,),('RH ondular')
    elif Fr<=2.5:
        return (Fr,),('RH débil')
    elif Fr<=4.5:
        return (Fr,),('RH oscilante')
    elif Fr<=9:
        return (Fr,),('RH estable')
    else:
        return (Fr,),('RH fuerte')
    
'-----------------------------------------------------------------------------'
def longitudResalto(y,b,m1,m2,Q,d,uy,ub,uQ,ud,um):
    """Calcula la longitud del resalto. Círculo, rectángulo, triángulo y trapecial (m=0.5,1 o 2) con ecuaciones empíricas\n
    y = profundidad aguas arriba (m) <br>
    b = base (m) <br>
    Q = caudal (m3/s) <br>
    d = diámetro (m)<br>
    ub = unidades de b (mm, cm, m, in)<br />
    uy = unidades de y (mm, cm, m, in)<br />
    uQ = unidades de caudal--> L, m3 <br />
    ud = unidades de d (mm, cm, m, in)\n
    
    Los parámetros que no se requieran se dejan en 0"""
    if m1==m2:
        m=m1
    
        y=CU_m(y,uy)
        b=CU_m(b,ub)
        d=CU_m(y,ud)
        if uQ=='L':
            Q=Q/1000
        m=CU_theta(m,um)
        m=math.tan(math.radians(m))
        
        Fr=froude(y,b,m,m,"m",Q,0,d,"m","m","m","m3/s")
        if d!=0:
            Lr=y*(11.7*(Fr-1)**0.832)
        elif m==0:
            Lr=y*(9.75*(Fr-1)**1.01)
        elif b==0:
            Lr=y*(4.26*(Fr-1)**0.695)
        else:
            if m==0.5:
                Lr=y*(35*(Fr-1)**0.836)
            elif m==1:
                Lr=y*(23*(Fr-1)**0.885)
            elif m==2:
                Lr=y*(17.6*(Fr-1)**0.905)
        return Lr
    else:
        return "m1 tiene que ser igual a m2 para la aplicación de esté método empírico"

'-----------------------------------------------------------------------------'    
def y_asterisco(Q,b,y1,i,ub,uy1,uQ,ui):
    """Calcula y asterisco de secciones rectangulares.\n
    y1 = profundidad aguas arriba (m) <br>
    b = base (m) <br>
    Q = caudal (m3/s) <br>
    i = inclinación del canal (grados, radianes, m/m) <br />
    ub = unidades de b (mm, cm, m, in)<br />
    uy1 = unidades de y1 (mm, cm, m, in)<br />
    uQ = unidades de caudal--> L, m3 <br />
    ui = unidades de inclinacion (mm, cm, m, in)\n
    
    Los parámetros que no se requieran se dejan en 0"""
    
    y1=CU_m(y1,uy1)
    b=CU_m(b,ub)
    if uQ=='L':
        Q=Q/1000
    
    Fr=froude(y1,b,0,Q,0,"m","m","m","m3")
    
    theta=CU_theta(i,ui)
    
    Tau=10**(0.027*theta)
    y=y1/2*(math.sqrt(1+8*Fr**2*Tau**2)-1)
    return y

'-----------------------------------------------------------------------------'
def tipoResalto(Q,b,y,m1,m2,yn,theta,uQ,ub,uy,uyn,ui):
    """Establece de qué tipo de resalto se trata a partir de geometría del canal y la profundidad natural.\n
    y = profundidad aguas arriba (m) <br>
    b = base (m) <br>
    Q = caudal (m3/s) <br>
    yn = profundidad natural aguas abajo (m) <b>
    theta = inclinación del canal (grados, radianes, m/m)
    ub = unidades de b (mm, cm, m, in)<br />
    uy = unidades de y (mm, cm, m, in)<br />
    uyn = unidades de yn (mm, cm, m, in)<br />
    uQ = unidades de caudal--> L, m3 <br />
    ui = unidades de inclinacion (mm, cm, m, in)"""
    
    if m1==0 and m2==0:
        y=CU_m(y,uy)
        b=CU_m(b,ub)
        yn=CU_m(yn,uyn)
        theta=CU_theta(theta,ui)
        if uQ=='L':
            Q=Q/1000
        
        y2=y_subsecuente(Q,b,0,0,0,y,0,"m","m","m3/s")
        y_a=y_asterisco(Q,b,y,theta,"m","m","m3/s","grados")
        if y2>yn:
            return (y2,y_a),('tipo A',)
        elif y_a==yn:
            return (y2,y_a),('tipo C',)
        elif y_a>yn:
            return (y2,y_a),('tipo B',)
        elif y_a<yn:
            return (y2,y_a),('tipo D',)
    else:
        return "Este método solo está disponible para secciones rectangulares"
    
'-----------------------------------------------------------------------------'
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
'-----------------------------------------------------------------------------'
    
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



'-----------------------------------------------------------------------------'
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

def pasoDirecto(Q,n,So,b,m1,m2,um,d,y1,y2,pasos,datum,uQ,uSo,ub,ud,uy1,uy2):
    """Calcula el perfil de un flujo gradualmente variado a partir de una aproximación de diferencias finitas. Distancia entre dos profundidades conocidas\n
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
    y_control=CU_m(y1,uy1)
    y_obj=CU_m(y2,uy2)
    So=CU_theta(So,uSo)
    So=math.tan(math.radians(So))
    if uQ=='L':
        Q=Q/1000
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))
    
    plot_i=[]
    plot_yi=[]
    plot_A=[]
    plot_P=[]
    plot_R=[]
    plot_v=[]
    plot_E=[]
    plot_Sfi=[]
    plot_sfm=[]
    plot_So_Sfm=[]
    plot_deltaE=[]
    plot_deltaX=[]
    plot_x=[]
    plot_fondo=[]
    plot_y=[]
    plot_yc=[]
    plot_yn=[]
    
    
    deltaY=(y_obj-y_control)/pasos
    
    y_c=yc(Q,b,0,m1,m2,"m",d,"m","m","m")
    
    if So!=0:
        yn=yn_manning(Q,n,So,m1,m2,"m",b,d,"si","m","m","m","m")
    else:
        yn=0
        
    
    y_c,v_c,Sc=pendienteC_limite(n,Q,b,m1,m2,"m",d,"m","m","m")
    
    
    # if So<Sc:
    #     tipo='suave'
    # elif So>Sc:
    #     tipo='empinada'
    # elif So==Sc:
    #     tipo='crítica'
    # elif So==0:
    #     tipo= 'horizontal'
    # elif So<0:
    #     tipo='adversa'
    
    p=0
    y=y_control
    Sfi=0
    Ei=0
    x=0
    fondo=datum
    
    if d==0:
        while p<=pasos:
            A,P,Rh,T,D=geom_r(y,b,m1,m2,"m","m","m")
            v=Q/A
            E=y+v**2/(2*9.81)
            Sf= Q**2*n**2*P**(4/3)/(A**(10/3))
            
            
            plot_i.append(float(p))
            plot_yi.append(float(y))
            plot_A.append(float(A))
            plot_P.append(float(P))
            plot_R.append(float(Rh))
            plot_v.append(float(v))
            plot_E.append(float(E))
            plot_Sfi.append(float(Sf))

            if p>0:
                Sfm=(Sf+Sfi)/2
                So_Sfm=So-Sfm
                deltaE=E-Ei
                deltaX=deltaE/So_Sfm
                
                x=x+deltaX
                fondo=datum-x*So
                
                
                plot_sfm.append(float(Sfm))
                plot_So_Sfm.append(float(So_Sfm))
                plot_deltaE.append(float(deltaE))
                plot_deltaX.append(float(deltaX))
                plot_x.append(float(x))
                
                
     
            else:
                plot_sfm.append(0)
                plot_So_Sfm.append(0)
                plot_deltaE.append(0)
                plot_deltaX.append(0)
                plot_x.append(0)
                
            if So!=0:
                yn_grafica=yn+fondo
                plot_yn.append(float(yn_grafica))
            else:
                plot_yn.append(0)
                
            y_grafica=y+fondo
            yc_grafica=y_c+fondo
            plot_y.append(float(y_grafica))
            plot_yc.append(float(yc_grafica))
            plot_fondo.append(float(fondo))
            Sfi=Sf
            Ei=E
            y=y+deltaY
            p=p+1

    return (plot_i, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_Sfi, plot_sfm, plot_So_Sfm, plot_deltaE, plot_deltaX, plot_x, plot_fondo, plot_y, plot_yc, plot_yn)

def txt_pasoDirecto(plot_i, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_Sfi, plot_sfm, plot_So_Sfm, plot_deltaE, plot_deltaX, plot_x, plot_fondo, plot_y, plot_yc, plot_yn, ruta):
    """Exporta archivo txt con resultados del paso directo\n
    plot_i = iteracion
    plot_yi = y(m)
    plot_A = A(m2)
    plot_P = P(m)
    plot_R = R(m)
    plot_v = v(m/s)
    plot_E = E(m)
    plot_Sfi = Sfi
    plot_sfm = Sfm
    plot_So_Sfm = So-Sfm
    plot_deltaE = deltaE(m)
    plot_deltaX = deltaX(m)
    plot_x = x(m)
    plot_fondo = Fondo(m)
    plot_y = Altura(m)
    plot_yc = yc(m)
    plot_yn = yn(m)
    ruta = ruta donde se quiere guardar el archivo
    """
    
    plot_i.insert(0,"iteracion")
    plot_yi.insert(0,"y(m)")
    plot_A.insert(0,"A(m2)")
    plot_P.insert(0,"P(m)")
    plot_R.insert(0,"R(m)")
    plot_v.insert(0,"v(m/s)")
    plot_E.insert(0,"E(m)")
    plot_Sfi.insert(0,"Sfi")
    plot_sfm.insert(0,"Sfm")
    plot_So_Sfm.insert(0,"So-Sfm")
    plot_deltaE.insert(0,"deltaE(m)")
    plot_deltaX.insert(0,"deltaX(m)")
    plot_x.insert(0,"x(m)")
    plot_fondo.insert(0,"Fondo(m)")
    plot_y.insert(0,"Altura(m)")
    plot_yc.insert(0,"yc(m)")
    plot_yn.insert(0,"yn(m)")
    
    file = open(ruta + "/paso_directo.csv", 'w')
   
    for index in range(len(plot_i)):
        file.write(str(plot_i[index]) + "\t" + str(plot_yi[index]) + "\t" + str(plot_A[index]) + "\t" + str(plot_P[index]) + "\t" + str(plot_R[index]) + "\t" + str(plot_v[index]) + "\t" + str(plot_E[index]) + "\t" + str(plot_Sfi[index]) + "\t" + str(plot_sfm[index]) + "\t" + str(plot_So_Sfm[index]) + "\t" + str(plot_deltaE[index]) + "\t" + str(plot_deltaX[index]) + "\t" + str(plot_x[index]) + "\t" + str(plot_fondo[index]) + "\t" + str(plot_y[index]) + "\t" + str(plot_yc[index]) + "\t" + str(plot_yn[index]) + "\n")
    file.close()
    
def grafica_paso(plot_x,plot_fondo,plot_y,plot_yc,plot_yn,ruta):
    """Grafica resultados de paso directo o paso estándar
    plot_x = x(m)
    plot_fondo = Fondo(m) o plot_z para paso estándar
    plot_y = Altura(m)
    plot_yc = yc(m)
    plot_yn = yn(m) 
    """
    
    
    plt.plot(plot_x,plot_fondo, color = '#804000', label = 'Fondo')
    plt.plot(plot_x,plot_y, color = '#4472C4', label = 'Altura')
    plt.plot(plot_x,plot_yc, color = '#FF0000', label = 'yc')
    plt.plot(plot_x,plot_yn, color = '#70AD47', label = 'yn')
    plt.xlabel('x')
    plt.ylabel('Altura')
    titulo = 'Perfil de flujo (m)'
    plt.title(titulo)
    plt.rcParams["figure.figsize"] = (25,10)
    plt.grid()
    plt.legend()
    plt.savefig(ruta)
    plt.show() 


def conservacionE(y1,m11,m12,b1,Q,y2,m21,m22,b2,uy1,uy2,um,uQ,ub1,ub2,v1,v2,z,incognita):
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
    v1 = velocidad 1 (m/s)
    v2 = velocidad 2 (m/s)

    uQ = unidades de caudal--> L, m3 <br />
    ub1 = unidades de b1 (mm, cm, m, in)<br />
    ub2 = unidades de b2 (mm, cm, m, in)<br />
    uy1 = unidades de y1 (mm, cm, m, in)<br />
    uy2 = unidades de y2 (mm, cm, m, in)<br />
    um = unidades de inclinación (grados, rad, m/m)

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
            return y2.args[0],y2.args[1],y2.args[2], "-", "-", "-", "-", "-", "-"

    
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
        
        return E1, b2[0],y_c
        
def pendientePropia(Q,d,uQ,ud,ynd,ecuacion,n,ks,nu):
    """Calcula pendiente propia\n
    Q = caudal (m3, L) <br>
    d = diametro (m,mm,cm,in) <br>
    uQ = unidades de caudal--> L, m3 <br />
    ud = unidades de diametro--> m,mm,cm,in <br />
    ynd = máxima relación de llenao de la tubería (%)<br />
    ecuacion = manning o darcy<br />
    n = n de manning<br />
    ks = Rugosidad absoluta (m)<br />
    nu = viscosidad cinemática (m2/s)
    
    """
    d=CU_m(d,ud) 
    if uQ=='L':
        Q=Q/1000
    
    yn,theta,A,P,Rh,T,D=geom_c(d,ynd,"m")
    
    if ecuacion=="manning":
        S0=n**2*Q**2*P**(4/3)/(A**(10/3))
        return S0
    elif ecuacion=="darcy":
        s=var("s", real=True)
        S0=solveset(Q/A+2*math.sqrt(8*9.81*Rh*s)*math.log10(ks/(14.8*Rh)+2.51*nu/(4*Rh*math.sqrt(8*9.81*Rh*s))),s)
        return S0.args[0]

def pasoEstandar1(Q,n,So,b,m1,m2,y_control,x,L,pasos,pasosI,datum,direccion,uQ,ub,um,uy,uSo,uL,ux):
    """Calcula el perfil de un flujo gradualmente variado con sección transversal homogenea a partir del método del paso estándar. Distancia entre dos profundidades desconocidas\n
    Q = caudal (m3/s) <br>
    n = número de Manning<br>
    So = Inclinación del canal<br>
    b = base (m,cm,mm,in) <br>
    m1 = inclinación lado 1 <br />
    m2 = inclinación lado 2 <br />
    y_control = profundidad de control (m) <br>
    x = x inicial (m,cm,mm,in) <br>
    L = longitud (m,cm,mm,in) <br>
    pasos = número de pasos <br>
    pasosI = primero paso <br>
    datum = datum <br>
    direccion = hacia aguas abajo (positivo) hacia aguas arriba (negativo) <br>
    um = unidades de m (grados, radianes, m/m)<br />
    uL = unidades longitud (m,cm,mm,in) <br>
    uQ = unidades de caudal--> L, m3 <br />
    uSo = unidades de inclinacion (mm, cm, m, in)
    ub = unidades de b (mm, cm, m, in)<br />
    uy = unidades de y (mm, cm, m, in)<br />
    ux = unidaddes de x<br>
    """
        
    
    x=CU_m(x,ux)
    b=CU_m(b,ub)
    L=CU_m(L,uL)
    y_control=CU_m(y_control,uy)
    So=CU_theta(So,uSo)
    So=math.tan(math.radians(So))
    if uQ=='L':
        Q=Q/1000
    m1=CU_theta(m1,um)
    m2=CU_theta(m2,um)
    m1=math.tan(math.radians(m1))
    m2=math.tan(math.radians(m2))

    
    plot_pasos=[]
    plot_yi=[]
    plot_A=[]
    plot_P=[]
    plot_R=[]
    plot_v=[]
    plot_E=[]
    plot_z=[]
    plot_H21=[]
    plot_Sfi=[]
    plot_Sfm=[]
    plot_H22=[]
    plot_deltaH=[]
    plot_x=[]

    plot_y=[]
    plot_yc=[]
    plot_yn=[]

    
    if direccion=="positivo":
        deltaX=L/pasos
    elif direccion=="negativo":
        x=-x
        deltaX=-L/pasos
    Sfm=0
    H22=0
    y=y_control
    p=0
    error=0.0001
    y_c=yc(Q,b,0,m1,m2,0,0,0,0,0)
    
    while p<=pasos:
        if p==0:
            A,P,Rh,T,D=geom_r(y,b,m1,m2,"m","m","m")
            v=Q/A
            E=y+v**2/(2*9.81)
            z=datum-x*So
            H21=E+z
            Sfi = Q**2*n**2/(A**2*Rh**(4/3))
            er=0
            
        
        else:
            Sfi_1=Sfi
            H21_1=H21
            x=x+deltaX
            er=1
            while er>error:
                if H21>H22:
                    y=y-0.0001
                else:
                    y=y+0.0001
                
                A,P,Rh,T,D=geom_r(y,b,m1,m2,"m","m","m")
                v=Q/A
                E=y+v**2/(2*9.81)
                z=datum-x*So
                H21=E+z
                Sfi = Q**2*n**2/(A**2*Rh**(4/3))
                Sfm = (Sfi+Sfi_1)/2
                H22=H21_1-Sfm*deltaX
                er = abs(H22-H21)
                
        if So!=0:
            yn=yn_manning(Q,n,So,m1,m2,"m",b,0,"si","m","m","m","m")
        else:
            yn=0
        
        
           
        plot_pasos.append(p+pasosI)
        plot_yi.append(float(y))
        plot_A.append(float(A))
        plot_P.append(float(P))
        plot_R.append(float(Rh))
        plot_v.append(float(v))
        plot_E.append(float(E))
        plot_H21.append(float(H21))
        plot_Sfi.append(float(Sfi))
        plot_Sfm.append(float(Sfm))
        plot_H22.append(float(H22))
        plot_deltaH.append(float(er))
        plot_x.append(float(x))
        
        if So!=0:
            yn=yn_manning(Q,n,So,m1,m2,um,b,0,'si',0,0,0,0)
            yn_grafica=yn+z
            plot_yn.append(float(yn_grafica))
        else:
            plot_yn.append(0)
                
        y_grafica=y+z
        yc_grafica=y_c+z
        plot_y.append(float(y_grafica))
        plot_yc.append(float(yc_grafica))
        plot_z.append(float(z))
        
        p=p+1
    print (plot_yi)
    return (plot_pasos, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_z,plot_H21, plot_Sfi, plot_Sfm, plot_H22,plot_deltaH, plot_x, plot_y, plot_yc, plot_yn)

        
def pasoEstandar(Q,n1,n2,So1,So2,b1,b2,m11,m12,m21,m22,y_control,x1,x2,L1,L2,pasos1,pasos2,datum,direccion,uQ,ub1,ub2,um,uy,uSo1,uSo2,uL1,uL2,ux1,ux2,secciones):
    """Paso estándar para tramos con cambios de sección\n
    n1 = n de manning tramo 1
    n2 = n de manning tramo 2

    So1 = Inclinación del canal tramo 1
    So2 = Inclinación del canal tramo 2

    b1 = Base tramo 1 
    b2 = Base tramo 2

    m11 = pendiente lateral izquierda tramo 1
    m12 = pendiente lateral derecha tramo 1

    m21 = pendiente lateral izquierda tramo 2
    m22 = pendiente lateral derecha tramo 1 

    x1 = x de inicio tramo 1
    x2 = x de inicio tramo 2

    L1 = longitud tramo 1
    L2 = longitud tramo 2

    pasos1 = número de pasos tramo 1
    pasos2 = número de pasos tramo 2

    Q = caudal
    y_control = y de control


    datum = datum
    direccion = hacia aguas abajo (positivo) hacia aguas arriba (negativo) <br>
    secciones = numero de secciones


    uQ = unidades caudal 
    ub1 = unidades b1
    ub2 = unidades b2
    um = unidades pendiente lateral
    uy = unidades y de control
    uSo1 = unidades inclinación del canal tramo 1
    uSo2 = unidades inclinación del canal tramo 2
    uL1 = unidades longitud tramo 1
    uL2 = unidades longitud tramo 2
    ux1 = unidades x inicial tramo 1
    ux2 = unidades x inicial tramo 2
    
    """
    
    if secciones==1:
        plot_pasos, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_z, plot_H21, plot_Sfi, plot_Sfm, plot_H22,plot_deltaH, plot_x, plot_y, plot_yc, plot_yn=pasoEstandar1(Q,n1,So1,b1,m11,m12,y_control,x1,L1,pasos1,0,datum,direccion,uQ,ub1,um,uy,uSo1,uL1,ux1)
        return plot_pasos, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_z, plot_H21, plot_Sfi, plot_Sfm, plot_H22,plot_deltaH, plot_x, plot_y, plot_yc, plot_yn
    else:
        plot_pasos1, plot_yi1, plot_A1, plot_P1, plot_R1, plot_v1, plot_E1, plot_z1, plot_H211, plot_Sfi1, plot_Sfm1, plot_H221, plot_deltaH1, plot_x1, plot_y1, plot_yc1, plot_yn1=pasoEstandar1(Q,n1,So1,b1,m11,m12,y_control,x1,L1,pasos1,0,datum,direccion,uQ,ub1,um,uy,uSo1,uL1,ux1)
        plot_pasos2, plot_yi2, plot_A2, plot_P2, plot_R2, plot_v2, plot_E2, plot_z2, plot_H212, plot_Sfi2, plot_Sfm2, plot_H222, plot_deltaH2, plot_x2, plot_y2, plot_yc2, plot_yn2=pasoEstandar1(Q,n2,So2,b2,m21,m22,plot_yi1[len(plot_yi1)-1],x2,L2,pasos2,plot_pasos1[len(plot_pasos1)-1],datum,direccion,uQ,ub2,um,uy,uSo2,uL2,ux2)
        
        plot_pasos=plot_pasos1+plot_pasos2
        plot_yi=plot_yi1+plot_yi2
        plot_A=plot_A1+plot_A2
        plot_P=plot_P1+plot_P2
        plot_R=plot_R1+plot_R2
        plot_v=plot_v1+plot_v2
        plot_E=plot_E1+plot_E2
        plot_z=plot_z1+plot_z2
        plot_H21=plot_H211+plot_H212
        plot_Sfi=plot_Sfi1+plot_Sfi2
        plot_Sfm= plot_Sfm1+ plot_Sfm2
        plot_H22=plot_H221+plot_H222
        plot_deltaH=plot_deltaH1+plot_deltaH2
        plot_x=plot_x1+plot_x2
        plot_y=plot_y1+plot_y2
        plot_yn=plot_yn1+plot_yn2
        plot_yc=plot_yc1+plot_yc2
    
    print (plot_pasos,plot_x,plot_yi,plot_deltaH)
    return plot_pasos, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_z,plot_H21, plot_Sfi, plot_Sfm, plot_H22,plot_deltaH, plot_x, plot_y, plot_yc, plot_yn

#pasoEstandar(2.38,0.013,0.013,0,0,4.6,2,0,0,0,0,0.525,0,15,15,15,3,3,0,'negativo',0,0,0,0,0,0,0,0,0,0,0,2)
#pasoEstandar1(2.38,0.013,0,4.26,0,0,0.525,0,15,3,0,0,'negativo',0,0,0,0,0,0,0)
        
     
def txt_pasoEstandar(plot_pasos, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_z,plot_H21, plot_Sfi, plot_Sfm, plot_H22,plot_deltaH, plot_x, plot_y, plot_yc, plot_yn,ruta):
    """Exporta archivo txt con resultados del paso estándar\n
    plot_i = iteracion
    plot_yi = y(m)
    plot_A = A(m2)
    plot_P = P(m)
    plot_R = R(m)
    plot_v = v(m/s)
    plot_E = E(m)
    plot_z = z(m)
    plot_H21 = H2(1) (m)
    plot_Sfi = Sfi
    plot_Sfm = Sfm
    plot_H22 = H2(2)(m)
    plot_deltaH = H2-H1 (m)
    plot_x = x(m)
    plot_y = Altura(m)
    plot_yc = yc(m)
    plot_yn = yn(m)
    ruta = ruta donde se quiere guardar el archivo
    """
    
    plot_pasos.insert(0,"iteracion")
    plot_yi.insert(0,"y(m)")
    plot_A.insert(0,"A(m2)")
    plot_P.insert(0,"P(m)")
    plot_R.insert(0,"R(m)")
    plot_v.insert(0,"v(m/s)")
    plot_E.insert(0,"E(m)")
    plot_z.insert(0,"z(m)")
    plot_H21.insert(0,"H2(1)(m)")
    plot_Sfi.insert(0,"Sfi")
    plot_Sfm.insert(0,"Sfm")
    plot_H22.insert(0,"H2(2)(m)")
    plot_deltaH.insert(0,"H2-H1(m)")
    plot_x.insert(0,"x(m)")
    plot_y.insert(0,"Altura(m)")
    plot_yc.insert(0,"yc(m)")
    plot_yn.insert(0,"yn(m)")
    
    file = open(ruta, 'w')
   
    for index in range(len(plot_pasos)):
        file.write(str(plot_pasos[index]) + "\t" + str(plot_yi[index]) + "\t" + str(plot_A[index]) + "\t" + str(plot_P[index]) + "\t" + str(plot_R[index]) + "\t" + str(plot_v[index]) + "\t" + str(plot_E[index]) + "\t" + str(plot_z[index]) + "\t" + str(plot_H21[index]) + "\t" + str(plot_Sfi[index]) + "\t" + str(plot_Sfm[index]) + "\t" + str(plot_H22[index]) + "\t" + str(plot_deltaH[index]) + "\t" + str(plot_x[index]) + "\t" + str(plot_y[index]) + "\t" + str(plot_yc[index]) + "\t" + str(plot_yn[index]) + "\n")
    file.close()
    
    
    
    
    
    