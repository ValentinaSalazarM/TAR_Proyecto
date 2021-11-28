from ..Cambio_de_unidades import *
from ..Geometria.geometria import *

from sympy import var,solveset, S

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