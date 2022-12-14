def seleccion (minCC, maxCC, minOM, maxOM, rp, re, so, ro, ra, en, criterio, minCriterio, maxCriterio, priorizar):
    pesosEquilibrado = [0.083, 0.0833, 0.125, 0.125, 0.083, 0.0833, 0.0833, 0.25, 0.0833]
    pesosAmbiental = [0.167, 0.167, 0.0833, 0.0833, 0.0556, 0.0556, 0.0556, 0.167, 0.167]
    pesosEconomico = [0.0556, 0.0556, 0.25, 0.25, 0.0556, 0.0556, 0.0556, 0.167, 0.0556]
    pesosTecnico = [0.0556, 0.0556, 0.0833, 0.0833, 0.167, 0.167, 0.167, 0.167, 0.0556]
    pesosSocial = [0.0556, 0.0556, 0.0833, 0.0833, 0.0556, 0.0556, 0.0556, 0.5, 0.0556]

    PT = [-3,-3,2,-3,4,4,-3,-9]
    RemocionPT = [2,2,1,1,3]

    CEPT = [-3,-3,5,-2,3,4,-2,-10]
    RemocionCEPT = [3,3,2,3,4]

    CAS = [-4,-2,3,-4,4,4,-3,-12]
    RemocionCAS = [5,5,3,1,5]

    SBR = [-2,-4,4,-4,3,4,-2,-10]
    RemocionSBR = [5,5,4,3,5]

    TF = [-2,-1,3,-2,2,2,-4,-11.5]
    RemocionTF = [4,4,3,3,4]

    RBC = [-4,-2,3,-2,4,4,-2,-7]
    RemocionRBC = [5,5,4,4,3]

    UASB = [-4,-3,4,-2,2,3,-2,-10]
    RemocionUASB = [4,4,3,3,3]

    MBR = [-4,-5,4,-5,1,4.5,-2,-10]
    RemocionMBR = [5,5,4,3,5]

    Lagunas = [-1,-3,2,-2,4,3,-5,-7]
    RemocionLagunas = [4,5,3,3,4]

    Humedales = [-3,-2,2,-1,3,3,-3,-4]
    RemocionHumedales = [4,4.5,3,3,4.5]

    AO = [-2,-2,3,-1,2,3,-1,-10]
    RemocionAO = [1,1,3,5,1]

    PhoStrip = [-5,-5,4,-4,3,5,-5,-11]
    RemocionPhoStrip = [1,1,1,5,1]

    Bardenpho = [-4,-5,4,-3,1,1,-5,-11]
    RemocionBardenpho = [4,4,5,4,3]

    categorias = {"Muy alto":5, "Alto":4, "Moderado":3, "Bajo":2, "Muy bajo":1}
    ubicacionRemocion = {"DQO":0, "DBO":1, "Nitrógeno Total":2, "Fósforo Total":3, "SST":4}

    valorCostoConstruccion = 1.5
    if (minCC >= 120 ):
        valorCostoConstruccion = 5
    elif (minCC >= 90):
        if (maxCC <= 120):
            valorCostoConstruccion = 4
        else:
            valorCostoConstruccion = 4.5
    elif (minCC >= 60):
        if (maxCC <= 90):
            valorCostoConstruccion = 3
        else:
            valorCostoConstruccion = 3.5
    elif (minCC >= 30):
        if (maxCC <= 60):
            valorCostoConstruccion = 2
        else:
            valorCostoConstruccion = 2.5
    elif (maxCC < 30):
        valorCostoConstruccion = 1

    valorCostoOM = 1.5
    if (minOM >= 3000000 ):
        valorCostoOM = 5
    elif (minOM >= 1000000):
        if (maxOM <= 3000000):
            valorCostoOM = 4
        else:
            valorCostoOM = 4.5
    elif (minOM >= 500000):
        if (maxOM <= 1000000):
            valorCostoOM = 3
        else:
            valorCostoOM = 3.5
    elif (minOM >= 200000):
        if (maxOM <= 500000):
            valorCostoOM = 2
        else:
            valorCostoOM = 2.5
    elif (maxOM < 200000):
        valorCostoOM = 1

    valorCostoOM *= -1
    valorProductos = categorias[rp]
    valorReqEnergia = -1 * categorias[re]
    valorSimplicidad = categorias[so]
    valorRobustez = categorias[ro]
    valorReqArea = -1 *categorias[ra]
    valorEfectosNegativos = -1 *categorias[en]

    valorEficiencia = 1.5
    if (minCriterio >= 80):
        valorEficiencia = 5
    elif (minCriterio >= 60):
        if (maxCriterio <= 80):
            valorEficiencia = 4
        else:
            valorEficiencia = 4.5
    elif (minCriterio >= 40):
        if (maxCriterio <= 60):
            valorEficiencia = 3
        else:
            valorEficiencia = 3.5
    elif (minCriterio >= 20):
        if (maxCriterio <= 40):
            valorEficiencia = 2
        else:
            valorEficiencia = 2.5
    elif (maxCriterio < 20):
        valorEficiencia = 1

    valoresUsuario = [valorCostoConstruccion, valorCostoOM, valorProductos, valorReqEnergia, valorSimplicidad, valorRobustez, valorReqArea, valorEfectosNegativos, valorEficiencia]
    pesos = []
    if (priorizar == "Equilibrado"):
        pesos = pesosEquilibrado
    elif (priorizar == "Económico"):
        pesos = pesosEconomico
    elif (priorizar == "Ambiental"):
        pesos = pesosAmbiental
    elif (priorizar == "Técnico"):
        pesos = pesosTecnico
    elif (priorizar == "Social"):
        pesos = pesosSocial

    PTConRemocion = PT + [RemocionPT[ubicacionRemocion[criterio]]] +  ["PT"]
    CEPTConRemocion = CEPT + [RemocionCEPT[ubicacionRemocion[criterio]]] +  ["CEPT"]
    CASConRemocion = CAS + [RemocionCAS[ubicacionRemocion[criterio]]] +  ["CAS"]
    SBRConRemocion = SBR + [RemocionSBR[ubicacionRemocion[criterio]]] +  ["SBR"]
    TFConRemocion = TF + [RemocionTF[ubicacionRemocion[criterio]]] +  ["TF"]
    RBCConRemocion = RBC + [RemocionRBC[ubicacionRemocion[criterio]]] +  ["RBC"]
    UASBConRemocion = UASB + [RemocionUASB[ubicacionRemocion[criterio]]] +  ["UASB"]
    MBRConRemocion = MBR + [RemocionMBR[ubicacionRemocion[criterio]]] +  ["MBR"]
    LagunasConRemocion = Lagunas + [RemocionLagunas[ubicacionRemocion[criterio]]] +  ["Lagunas"]
    HumedalesConRemocion = Humedales + [RemocionHumedales[ubicacionRemocion[criterio]]] +  ["Humedales"]
    AOConRemocion = AO + [RemocionAO[ubicacionRemocion[criterio]]] +  ["AO"]
    PhoStripConRemocion = PhoStrip + [RemocionPhoStrip[ubicacionRemocion[criterio]]] +  ["PhoStrip"]
    BardenphoConRemocion = Bardenpho + [RemocionBardenpho[ubicacionRemocion[criterio]]] + ["Bardenpho"]

    tecnologias = [PTConRemocion, CEPTConRemocion, CASConRemocion, SBRConRemocion, TFConRemocion, RBCConRemocion, UASBConRemocion, MBRConRemocion, LagunasConRemocion, HumedalesConRemocion, AOConRemocion, PhoStripConRemocion, BardenphoConRemocion]
    vector = [0]*13
    maximo = -100
    mejorTecnologia = ""
    for i in range(0, len(pesos)):
        for j in range(0, len(tecnologias)):
            vector[j] += tecnologias[j][i] * pesos[i] * valoresUsuario[i]

    for i in range (0, len(vector)):
        if (vector[i] >= maximo):
            maximo = vector[i]
            mejorTecnologia = tecnologias[i]
    #print (vector)
    #print ("Máximo: ", maximo, " | Tecnología: ", mejorTecnologia[-1])

    return vector
