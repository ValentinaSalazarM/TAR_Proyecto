from ..Cambio_de_unidades import *
from ..Geometria.geometria import *
from ..EcuacionManning.ecuacionManning import *

def pasoEstandar1(Q,n,So,b,m1,m2,y_control,x,L,pasos,pasosI,datum,direccion,uQ,ub,um,uy,uSo,uL,ux,Sfi,Sfm,H21,H22,p):
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
        deltaX=-L/pasos
    y=y_control
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
    return (plot_pasos, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_z,plot_H21, plot_Sfi, plot_Sfm, plot_H22,plot_deltaH, plot_x, plot_y, plot_yc, plot_yn)

        
def pasoEstandar(Q,n1,n2,So1,So2,b1,b2,m11,m12,m21,m22,y_control,L1,L2,pasos1,pasos2,datum,direccion,uQ,ub1,ub2,um,uy,uSo1,uSo2,uL1,uL2,ux1,ux2,secciones):
    """Paso estándar para tramos con cambios de sección\n
    Q = caudal
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
    y_control = y de control
    x1 = x de inicio tramo 1
    x2 = x de inicio tramo 2
    L1 = longitud tramo 1
    L2 = longitud tramo 2
    pasos1 = número de pasos tramo 1
    pasos2 = número de pasos tramo 2
    datum = datum
    direccion = hacia aguas abajo (positivo) hacia aguas arriba (negativo) <br>
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
    secciones = numero de secciones"""
    
    
    
    if secciones==1:
        plot_pasos, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_z, plot_H21, plot_Sfi, plot_Sfm, plot_H22,plot_deltaH, plot_x, plot_y, plot_yc, plot_yn=pasoEstandar1(Q,n1,So1,b1,m11,m12,y_control,0,L1,pasos1,0,datum,direccion,uQ,ub1,um,uy,uSo1,uL1,ux1,0,0,0,0,0)
        return plot_pasos, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_z, plot_H21, plot_Sfi, plot_Sfm, plot_H22,plot_deltaH, plot_x, plot_y, plot_yc, plot_yn
    else:
        plot_pasos1, plot_yi1, plot_A1, plot_P1, plot_R1, plot_v1, plot_E1, plot_z1, plot_H211, plot_Sfi1, plot_Sfm1, plot_H221, plot_deltaH1, plot_x1, plot_y1, plot_yc1, plot_yn1=pasoEstandar1(Q,n1,So1,b1,m11,m12,y_control,0,L1,pasos1,0,datum,direccion,uQ,ub1,um,uy,uSo1,uL1,ux1,0,0,0,0,0)
        plot_pasos2, plot_yi2, plot_A2, plot_P2, plot_R2, plot_v2, plot_E2, plot_z2, plot_H212, plot_Sfi2, plot_Sfm2, plot_H222, plot_deltaH2, plot_x2, plot_y2, plot_yc2, plot_yn2=pasoEstandar1(Q,n2,So2,b2,m21,m22,plot_yi1[len(plot_yi1)-1],plot_x1[len(plot_x1)-1],L2,pasos2,plot_pasos1[len(plot_pasos1)-1],datum,direccion,uQ,ub2,um,uy,uSo2,uL2,ux2,plot_Sfi1[len(plot_Sfi1)-1],plot_Sfm1[len(plot_Sfm1)-1],plot_H211[len(plot_H211)-1],plot_H221[len(plot_H221)-1],1)
        
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
    
    return plot_pasos, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_z,plot_H21, plot_Sfi, plot_Sfm, plot_H22,plot_deltaH, plot_x, plot_y, plot_yc, plot_yn
        
     
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
    