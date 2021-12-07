
from ..Cambio_de_unidades import *
from ..EcuacionManning.ecuacionManning import *
import math
import os


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
    
    file = open(ruta + os.path.sep + "paso_directo.csv", 'w')
   
    for index in range(len(plot_i)):
        file.write(str(plot_i[index]) + "\t" + str(plot_yi[index]) + "\t" + str(plot_A[index]) + "\t" + str(plot_P[index]) + "\t" + str(plot_R[index]) + "\t" + str(plot_v[index]) + "\t" + str(plot_E[index]) + "\t" + str(plot_Sfi[index]) + "\t" + str(plot_sfm[index]) + "\t" + str(plot_So_Sfm[index]) + "\t" + str(plot_deltaE[index]) + "\t" + str(plot_deltaX[index]) + "\t" + str(plot_x[index]) + "\t" + str(plot_fondo[index]) + "\t" + str(plot_y[index]) + "\t" + str(plot_yc[index]) + "\t" + str(plot_yn[index]) + "\n")
    file.close()