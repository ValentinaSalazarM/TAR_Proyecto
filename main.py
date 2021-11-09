# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
from aplicaciones.Aplicacion import *
from tkinter.filedialog import askdirectory

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
#os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "C:/Users/Usuario/anaconda3/envs/py39-demo/Lib/site-packages/PyQt5/Qt5/plugins/platforms"
#os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "C:/Users/Usuario/venv/Lib/site-packages/PyQt5/Qt5/bin/platforms"
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "C:/Users/Usuario/anaconda3/envs/py39-demo/Library/plugins"

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
cambioUnidadesLongitud = {"Milímetros": "mm" , "Centímetros": "cm", "Metros": "m", "Pulgadas": "in"}
cambioUnidadesAngulo = {"Adimensional":"m/m", "Grados": "grados", "Radianes": "radianes"}

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "HidrApp Uniandes"
        description = "La forma más fácil de diseñar canales y estructuras hidráulicas"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)


        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


        # ///////////////////////////////////////////////////////////////
        # GEOMETRIA

        # Menú principal
        widgets.botonMenuGeometria.clicked.connect(self.pagGeometriaSeleccionada)
        
        # Sección Circular
        widgets.geoCBotonCalcular.clicked.connect(self.geometriaCircular)
        widgets.geoCBotonReiniciar.clicked.connect(self.reiniciarCamposGeoC)

        # Sección No Circular
        widgets.geoRBotonCalcular.clicked.connect(self.geometriaRectangular)
        widgets.geoRBotonReiniciar.clicked.connect(self.reiniciarCamposGeoR)

        # Sección Froude
        widgets.geoFroudeBotonCalcular.clicked.connect(self.geometriaFroude)
        widgets.geoFroudeBotonReiniciar.clicked.connect(self.reiniciarCamposGeoFroude)

        # ///////////////////////////////////////////////////////////////
        # CONSERVACION MOMENTUM
        
        # Menú principal
        widgets.botonMenuConservacionM.clicked.connect(self.pagConservacionMSeleccionada)
        
        # Sección Análisis RH
        widgets.RHAnalisisBotonCalcular.clicked.connect(self.RHAnalisis)

        # Sección Propiedades RH
        widgets.RHPropiedadesBotonCalcular.clicked.connect(self.RHPropiedades)

        # Sección Tipo resalto
        widgets.RHTipoBotonCalcular.clicked.connect(self.RHTipo)

        # Sección Compuertas
        widgets.RHCompuertasBotonCalcular.clicked.connect(self.RHCompuertas)

        # ///////////////////////////////////////////////////////////////
        # FLUJO GRADUALMENTE VARIADO

        # Menú principal
        widgets.botonMenuFGV.clicked.connect(self.pagFGVSeleccionada)
        widgets.FGVBotonCalcular.clicked.connect(self.FGVIntegracion)
        widgets.FGVPasoDBotonCalcular.clicked.connect(self.FGVPasoDirecto)
        widgets.FGVPasoDBotonDescargarCSV.clicked.connect(self.RGVTxt_pasoDirecto)
        widgets.FGVPasoDBotonDescargarPerfil.clicked.connect(self.RGVGrafica_pasoDirecto)


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # //////////////////////////////////////////////////////////////

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.menu_principal) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

   
    # ///////////////////////////////////////////////////////////////
    # MENÚ PRINCIPAL

    def pagGeometriaSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_geometria)

    def pagConservacionMSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_conservacionM)
    
    def pagFGVSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_FGV)

    # ///////////////////////////////////////////////////////////////
    # GEOMETRÍA
    def geometriaCircular (self):
        d =  float (widgets.geoCFieldDiametro.text())
        ynd =  float (widgets.geoCFieldRelacionLlenado.text())

        ud = widgets.geoCComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        yn,theta,A,P,Rh,T,D = geom_c(d, ynd, ud)

        widgets.geoCFieldAngulo.setText(str(round(theta, 3)) + " radianes")
        widgets.geoCFieldProfundidadNormal.setText(str(round(yn, 3)) + " m")
        widgets.geoCFieldArea.setText(str(round(A, 3)) + " m²")
        widgets.geoCFieldPerimetro.setText(str(round(P, 3)) + " m")
        widgets.geoCFieldRadio.setText(str(round(Rh, 3)) + " m")
        widgets.geoCFieldAnchoSuperficial.setText(str(round(T, 3))+ " m")
        widgets.geoCFieldProfundidadHidraulica.setText(str(round(D, 3)) + " m")

    def reiniciarCamposGeoC(self):
        widgets.geoCFieldDiametro.setText("")
        widgets.geoCFieldRelacionLlenado.setText("")

        widgets.geoCComboBoxDiametro.setCurrentIndex(0)

        widgets.geoCFieldAngulo.setText("")
        widgets.geoCFieldProfundidadNormal.setText("")
        widgets.geoCFieldArea.setText("")
        widgets.geoCFieldPerimetro.setText("")
        widgets.geoCFieldRadio.setText("")
        widgets.geoCFieldAnchoSuperficial.setText("")
        widgets.geoCFieldProfundidadHidraulica.setText("")

    def geometriaRectangular (self):
        
        y =  float (widgets.geoCFieldProfundidadSeccion.text())
        b =  float (widgets.geoCFieldAncho.text())
        m1 = float (widgets.geoCFieldPendienteLateral.text())
        m2 = float (widgets.geoCFieldPendienteLateral2.text())

        um = widgets.geoRComboBoxPendienteLateral.currentText()
        um = cambioUnidadesAngulo[um]

        uy = widgets.geoRComboBoxProfundidad.currentText()
        uy = cambioUnidadesLongitud[uy]

        ub = widgets.geoRComboBoxAncho.currentText()
        ub = cambioUnidadesLongitud[ub]

        # Colocar imagen del canal dependiendo de su geometría
        if (y != 0 and b != 0):
            #Trapecio
            widgets.geoRImagenCanal.setStyleSheet(u"background-image: url(:/geometria/images/geometria/Geometria-trapecial.PNG);")
        elif (y != 0 and b == 0):
            widgets.geoRImagenCanal.setStyleSheet(u"background-image: url(:/geometria/images/geometria/Geometria-triangular.PNG);")
        else:
            widgets.geoRImagenCanal.setStyleSheet(u"background-image: url(:/geometria/images/geometria/Geometria-rectangular.PNG);")


        A,P,Rh,T,D = geom_r(y,b,m1,m2,um,uy,ub)
        print(A)

        widgets.geoRFieldArea.setText(str(round(A, 3)) + " m²")
        widgets.geoRFieldPerimetro.setText(str(round(P, 3)) + " m")
        widgets.geoRFieldRadio.setText(str(round(Rh, 3)) + " m")
        widgets.geoRFieldAnchoSuperficial.setText(str(round(T, 3))+ " m")
        widgets.geoRFieldProfundidadHidraulica.setText(str(round(D, 3)) + " m")
    
    def reiniciarCamposGeoR(self):
        widgets.geoCFieldProfundidadSeccion.setText("")
        widgets.geoCFieldAncho.setText("")
        widgets.geoCFieldPendienteLateral.setText("")
        widgets.geoCFieldPendienteLateral2.setText("")

        widgets.geoRComboBoxPendienteLateral.setCurrentIndex(0)
        widgets.geoRComboBoxProfundidad.setCurrentIndex(0)
        widgets.geoRComboBoxAncho.setCurrentIndex(0)

        widgets.geoRFieldArea.setText("")
        widgets.geoRFieldPerimetro.setText("")
        widgets.geoRFieldRadio.setText("")
        widgets.geoRFieldAnchoSuperficial.setText("")
        widgets.geoCFieldRadio.setText("")
        widgets.geoRFieldProfundidadHidraulica.setText("")

    def geometriaFroude (self):
        y =  float (widgets.geoFroudeFieldProfundidadSeccion.text())
        b =  float (widgets.geoFroudeFieldAncho.text())
        m1 = float (widgets.geoFroudeFieldPendienteLateral.text())
        m2 = float (widgets.geoFroudeFieldPendienteLateral2.text())
        Q = float (widgets.geoFroudeFieldCaudal.text())
        v = float (widgets.geoFroudeFieldVelocidad.text())
        d = float (widgets.geoFroudeFieldDiametro.text())
         
        um = widgets.geoFroudeComboBoxPendienteLateral.currentText()
        um = cambioUnidadesAngulo[um]

        uy = widgets.geoFroudeComboBoxProfundidad.currentText()
        uy = cambioUnidadesLongitud[uy]

        ub = widgets.geoFroudeComboBoxAncho.currentText()
        ub = cambioUnidadesLongitud[ub]

        uQ = widgets.geoFroudeComboBoxCaudal.currentText()
        uQ = "L" if "Litros/segundos" else "Metros cúbicos/segundos"

        ud = widgets.geoFroudeComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        Fr = froude(y,b,m1,m2,um,Q,v,d,uy,ub,ud,uQ)
    
        widgets.geoFroudeFieldFroude.setText(str(round(Fr, 3)))

    def reiniciarCamposGeoFroude(self):
        widgets.geoFroudeFieldProfundidadSeccion.setText("")
        widgets.geoFroudeFieldAncho.setText("")
        widgets.geoFroudeFieldPendienteLateral.setText("")
        widgets.geoFroudeComboBoxProfundidad.setText("")
        widgets.geoFroudeFieldCaudal.setText("")
        widgets.geoFroudeFieldVelocidad.setText("")
        widgets.geoFroudeFieldDiametro.setText("")

        widgets.geoFroudeComboBoxPendienteLateral.setCurrentIndex(0)
        widgets.geoFroudeComboBoxProfundidad.setCurrentIndex(0)
        widgets.geoFroudeComboBoxAncho.setCurrentIndex(0)

        widgets.geoFroudeFieldFroude.setText("")

    # ///////////////////////////////////////////////////////////////
    # CONSERVACIÓN DE MOMENTUM

    def RHAnalisis (self):
        b =  float (widgets.RHAnalisisFieldAncho.text())
        m1 =  float (widgets.RHAnalisisFieldPendienteLateral.text())
        m2 =  float (widgets.RHAnalisisFieldPendienteLateral2.text())
        y1 =  float (widgets.RHAnalisisFieldProfundidad1.text())
        Q =  float (widgets.RHAnalisisFieldCaudal.text())
        
        l =  widgets.RHAnalisisFieldLongitudInclinada.text()
        l = float(l) if l else 0

        yn =  widgets.RHAnalisisFieldProfundidad.text()
        yn = float(yn) if yn else 0

        i =  widgets.RHAnalisisFieldInclinacion.text()
        i = float(i) if i else 0

        f =  widgets.RHAnalisisFieldFuerza.text()
        f = float(f) if f else 0

        um = widgets.RHAnalisisComboBoxPendienteLateral.currentText()
        um = cambioUnidadesAngulo[um]

        uy1 = widgets.RHAnalisisComboBoxProfundidad1.currentText()
        uy1 = cambioUnidadesLongitud[uy1]

        ub = widgets.RHAnalisisComboBoxAncho.currentText()
        ub = cambioUnidadesLongitud[ub]

        uQ = widgets.RHAnalisisComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else "Metros cúbicos/segundos"

        ul = widgets.RHAnalisisComboBoxLongitudInclinada.currentText()
        ul = cambioUnidadesLongitud[ul]

        ui = widgets.RHAnalisisComboBoxPendienteLateral.currentText()
        ui = cambioUnidadesAngulo[ui]

        calculos, resultados = eficienciaRH(Q,b,m1,m2,um,y1,yn,f,l,i,uQ,ub,uy1,ul,ui)
        E1, E2, z = calculos

        widgets.RHAnalisisFieldAltura.setText(str(round(z, 3)) + " m")
        widgets.RHAnalisisFieldE1.setText(str(round(z, 3)) + " m")
        widgets.RHAnalisisFieldE2.setText(str(round(z, 3)) + " m")

        widgets.RHAnalisisFieldEficiencia.setText(str(round(resultados[0], 3)) + " %")

    def RHPropiedades(self):
        b =  float (widgets.RHPropiedadesFieldBase.text())
        y =  float (widgets.RHPropiedadesFieldProfundidad.text())       
        m1 =  float (widgets.RHPropiedadesFieldPendienteLateral.text())
        m2 =  float (widgets.RHPropiedadesFieldPendienteLateral2.text())
        y =  float (widgets.RHPropiedadesFieldProfundidad.text())
        Q =  float (widgets.RHPropiedadesFieldCaudal.text())
        d =  float (widgets.RHPropiedadesFieldDiametro.text())
        
        um = widgets.RHPropiedadesComboBoxPendienteLateral.currentText()
        um = cambioUnidadesAngulo[um]

        uy = widgets.RHPropiedadesComboBoxProfundidad.currentText()
        uy = cambioUnidadesLongitud[uy]

        ub = widgets.RHPropiedadesComboBoxBase.currentText()
        ub = cambioUnidadesLongitud[ub]

        uQ = widgets.RHPropiedadesComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else "Metros cúbicos/segundos"
        
        ud = widgets.RHPropiedadesComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        opcionales, resultados = clasificacionResalto(Q,b,m1,m2,d,ud,um,y,ub,uy,uQ)
        widgets.RHPropiedadesFieldFroude.setText(str(round(opcionales[0], 3)))
        widgets.RHPropiedadesFieldClasificacion.setText(resultados[0])

        Lr = longitudResalto(y,b,m1,m2,Q,d,uy,ub,uQ,ud,um)
        widgets.RHPropiedadesFieldLongitud.setText(str(round(Lr, 3)) + " m")

    def RHTipo (self):
        b =  float (widgets.RHTipoFieldBase.text())
        y =  float (widgets.RHTipoFieldProfundidad.text())       
        yn =  float (widgets.RHTipoFieldNormal.text())       
        m1 =  float (widgets.RHTipoFieldPendienteLateral.text())
        m2 =  float (widgets.RHTipoFieldPendienteLateral2.text())
        s0 =  float (widgets.RHTipoFieldInclinacion.text())
        Q =  float (widgets.RHTipoFieldCaudal.text())
        
        um = widgets.RHTipoComboBoxPendientaLateral.currentText()
        um = cambioUnidadesAngulo[um]

        uy = widgets.RHTipoComboBoxProfundidad.currentText()
        uy = cambioUnidadesLongitud[uy]

        uyn = widgets.RHTipoComboBoxNormal.currentText()
        uyn = cambioUnidadesLongitud[uyn]

        ub = widgets.RHTipoComboBoxBase.currentText()
        ub = cambioUnidadesLongitud[ub]

        uQ = widgets.RHTipoComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else "Metros cúbicos/segundos"

        ui = widgets.RHTipoComboBoxInclinacion.currentText()
        ui = cambioUnidadesAngulo[ui]

        opcionales, resultados = tipoResalto(Q,b,y,m1,m2,yn,s0,uQ,ub,uy,uyn,ui)

        y2, y_a = opcionales

        widgets.RHTipoFieldSubsecuente.setText(str(round(y2, 3)) + " m")
        widgets.RHTipoFieldAsterisco.setText(str(round(y_a, 3)) + " m")

        widgets.RHTipoFieldTipo.setText(resultados[0])

    def RHCompuertas(self):
        b =  float (widgets.RHCompuertasFieldAncho.text())
        y1 =  float (widgets.RHCompuertasFieldProfundidad.text())       
        m1 =  float (widgets.RHCompuertasFieldPendienteLateral.text())
        m2 =  float (widgets.RHCompuertasFieldPendienteLateral2.text())
        Q =  float (widgets.RHCompuertasFieldCaudal.text())
        d =  float (widgets.RHCompuertasFieldDiametro.text())

        y2 =  widgets.RHCompuertasFieldProfundidad2.text()
        y2 = float(y2) if y2 else 0

        rho =  widgets.RHCompuertasFieldDensidad.text()
        rho = float(rho) if rho else 0

        um = widgets.RHCompuertasComboBoxPendienteLateral.currentText()
        um = cambioUnidadesAngulo[um]

        uy1 = widgets.RHCompuertasComboBoxProfundidad.currentText()
        uy1 = cambioUnidadesLongitud[uy1]

        ud = widgets.RHCompuertasComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        ub = widgets.RHCompuertasComboBoxAncho.currentText()
        ub = cambioUnidadesLongitud[ub]

        uQ = widgets.RHCompuertasComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else "Metros cúbicos/segundos"
        
        uy2 = widgets.RHCompuertasComboBoxProfundidad2.currentText()
        uy2 = cambioUnidadesLongitud[uy2]

        M1 = momentum(Q,b,m1,m2,um,y1,d,uQ,ub,uy1,ud)
        M2 = "No aplica."
        F_a = "No aplica."
        f = "No aplica."

        if d == 0 and y2 and rho:
            M1,M2,F_a,f = fuerzaCompuerta(y1,y2,b,Q,m1,m2,um,rho,uy1,uy2,ub,uQ)
            M2 = str(round(M2, 3)) + " m²"
            F_a = str(round(F_a, 3)) + " m²"
            f = str(round(f, 3)) + " N"


        widgets.RHCompuertasFieldMomentum.setText(str(round(M1, 3)) + "m²")
        widgets.RHCompuertasFieldMomentum2.setText(M2)
        widgets.RHCompuertasFieldFuerza.setText(F_a)
        widgets.RHCompuertasFieldFuerzaCompuerta.setText(f)

    # ///////////////////////////////////////////////////////////////
    # FLUJO GRADUALMENTE VARIADO (FGV)
    def FGVIntegracion (self):
        
        b =  float (widgets.FGVFieldAncho.text())
        d =  float (widgets.FGVFieldDiametro.text())
        S0 =  float (widgets.FGVPasoDFieldInclinacion.text())       
        n =  float (widgets.FGVFieldInclinacion.text())       
        m1 =  float (widgets.FGVFieldPendienteLateral.text())
        m2 =  float (widgets.FGVFieldPendienteLateral2.text())
        y1 =  float (widgets.FGVFieldProfundidad1.text())       
        y2 =  float (widgets.FGVFieldProfundidad2.text())       
        Q =  float (widgets.FGVFieldCaudal.text())

        um = widgets.FGVComboBoxPendienteLateral.currentText()
        um = cambioUnidadesAngulo[um]

        uS0 = widgets.FGVComboBoxInclinacion.currentText()
        uS0 = cambioUnidadesAngulo[uS0]

        uy1 = widgets.FGVComboBoxProfundidad1.currentText()
        uy1 = cambioUnidadesLongitud[uy1]

        uy2 = widgets.FGVComboBoxProfundidad2.currentText()
        uy2 = cambioUnidadesLongitud[uy2]
        
        ub = widgets.FGVComboBoxAncho.currentText()
        ub = cambioUnidadesLongitud[ub]

        ud = widgets.FGVComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        uQ = widgets.FGVComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else "Metros cúbicos/segundos"
        

        x = fgv_int(Q,n,S0,b,m1,m2,um,d,y1,y2,uQ,uS0,ub,ud,uy1,uy2)

        widgets.FGVFieldDistanciaX.setText(str(round(x, 3)) + "m")

    def FGVPasoDirecto (self):
        
        b =  float (widgets.FGVPasoDFieldAncho.text())
        d =  float (widgets.FGVPasoDFieldDiametro.text())
        S0 =  float (widgets.FGVPasoDFieldInclinacion.text())       
        n =  float (widgets.FGVPasoDFieldNumManning.text())       
        m1 =  float (widgets.FGVPasoDFieldPendienteLateral.text())
        m2 =  float (widgets.FGVPasoDFieldPendienteLateral2.text())
        y1 =  float (widgets.FGVPasoDFieldProfundidadControl.text())       
        y2 =  float (widgets.FGVPasoDFieldProfundidadObjetivo.text())       
        Q =  float (widgets.FGVPasoDFieldCaudal.text())
        pasos =  int (widgets.FGVPasoDFieldPasos.text())
        datum =  float (widgets.FGVPasoDFieldDatum.text())

        um = widgets.FGVPasoDComboBoxPendienteLateral.currentText()
        um = cambioUnidadesAngulo[um]

        uS0 = widgets.FGVPasoDComboBoxInclinacion.currentText()
        uS0 = cambioUnidadesAngulo[uS0]

        uy1 = widgets.FGVPasoDComboBoxPendienteControl.currentText()
        uy1 = cambioUnidadesLongitud[uy1]

        uy2 = widgets.FGVPasoDComboBoxPendienteObjetivo.currentText()
        uy2 = cambioUnidadesLongitud[uy2]
        
        ub = widgets.FGVPasoDComboBoxAncho.currentText()
        ub = cambioUnidadesLongitud[ub]

        ud = widgets.FGVPasoDComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        uQ = widgets.FGVPasoDComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else "Metros cúbicos/segundos"
        
        ruta = self.FGVSolicitarRutaCSV ()

        parametrosGrafica = pasoDirecto(Q,n,S0,b,m1,m2,um,d,y1,y2,pasos,datum,uQ,uS0,ub,ud,uy1,uy2, ruta)

        return parametrosGrafica 

    def RGVTxt_pasoDirecto (self):
        ruta = askdirectory(title='Seleccionar carpeta')
        txt_pasoDirecto(parametrosGrafica, ruta)

    def RGVGrafica_pasoDirecto (self):
        ruta = askdirectory(title='Seleccionar carpeta')
        grafica_pasoDirecto(parametrosGrafica, ruta)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())