from ..Cambio_de_unidades import *
from ..Geometria.geometria import *

import math

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
        y2=y1/2*(math.sqrt(1+8*Fr**2)-1)
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

def eficienciaRH(Q,b,m1,m2,um,y1,yn,f,l,i,uQ,ub,uy1,uyn,ul,ui,d):
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
    uyn = unidades yn (mm ,cm ,m , in) <br />
    ul = unidades de longitud--> (mm ,cm ,m , in) 
    ui = unidades de inclinacion--> grados, radianes, m/m <br />"""
    
    if d!=0:
        return "no aplica"
    y1=CU_m(y1,uy1)
    yn=CU_m(yn,uyn)
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
    if d!=0:
        return (Fr,),('No aplica')
    
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