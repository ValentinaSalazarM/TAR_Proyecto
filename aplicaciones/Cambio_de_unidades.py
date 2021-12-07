import math

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