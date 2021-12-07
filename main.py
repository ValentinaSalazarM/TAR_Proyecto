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

from aplicaciones.Geometria.geometria import *
from aplicaciones.ConservacionEnergia.conservacionEnergia import *
from aplicaciones.ConservacionMomentum.conservacionMomentum import *
from aplicaciones.EcuacionManning.ecuacionManning import *
from aplicaciones.EcuacionManning.flujoCritico import *
from aplicaciones.ComprobaciondeDiseno.comprobacion import *
from aplicaciones.ComprobaciondeDiseno.pendientePropia import *
from aplicaciones.FlujoGradualmenteVariado.analisisCualitativo import *
from aplicaciones.FlujoGradualmenteVariado.integral import *
from aplicaciones.FlujoGradualmenteVariado.pasoDirecto import *
from aplicaciones.FlujoGradualmenteVariado.pasoEstandar import *
from aplicaciones.FlujoRapidamenteVariado.piscinas import *
from aplicaciones.FlujoRapidamenteVariado.rebosaderos import *
from macros_graficas.ejecutarMacro import *

from PySide6.QtWidgets import QFileDialog

from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

widgets = None

cambioUnidadesLongitud = {"Milímetros": "mm" , "Centímetros": "cm", "Metros": "m", "Pulgadas": "in"}
cambioUnidadesAngulo = {"Adimensional":"m/m", "Grados": "grados", "Radianes": "radianes"}

parametrosGrafica = ''

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

        title = "HidrApp Uniandes"
        description = "La forma más fácil de diseñar canales y estructuras hidráulicas"

        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

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
        # CONSERVACIÓN DE ENERGÍA

        # Menú principal
        widgets.botonMenuConservacionE.clicked.connect(self.pagConservacionESeleccionada)
        
        # Sección Caudal
        widgets.CECaudalBotonCalcular.clicked.connect(self.conservacionEnergiaCaudal)
        #widgets.CECaudalBotonReiniciar.clicked.connect(self.reiniciarCamposConservacionEnergiaCaudal)

        # Sección Profundidad y2
        widgets.CEnergiaY2BotonCalcular.clicked.connect(self.conservacionEnergiaY2)
        #widgets.CEnergiaY2BotonReiniciar.clicked.connect(self.reiniciarCamposConservacionEnergiaY2)

        # Sección Máximo Z
        widgets.CEnergiaZBotonCalcular.clicked.connect(self.conservacionEnergiaMaxZ)
        #widgets.CEnergiaZBotonReiniciar.clicked.connect(self.reiniciarCamposConservacionEnergiaMaxZ)

        # Sección Mínimo B
        widgets.CEnergiaBBotonCalcular.clicked.connect(self.conservacionEnergiaMinB)
        #widgets.CEnergiaBBotonReiniciar.clicked.connect(self.reiniciarCamposConservacionEnergiaMinB)



        # ///////////////////////////////////////////////////////////////
        # CONSERVACION MOMENTUM
        
        # Menú principal
        widgets.botonMenuConservacionM.clicked.connect(self.pagConservacionMSeleccionada)
        
        # Sección Análisis RH
        widgets.RHAnalisisBotonCalcular.clicked.connect(self.RHAnalisis)
        widgets.RHAnalisisBotonReiniciar.clicked.connect(self.reiniciarCamposRHAnalisis)

        # Sección Propiedades RH
        widgets.RHPropiedadesBotonCalcular.clicked.connect(self.RHPropiedades)
        widgets.RHPropiedadesBotonReiniciar.clicked.connect(self.reiniciarCamposRHPropiedades)

        # Sección Tipo resalto
        widgets.RHTipoBotonCalcular.clicked.connect(self.RHTipo)
        widgets.RHTipoBotonReiniciar.clicked.connect(self.reiniciarCamposRHTipo)

        # Sección Compuertas
        widgets.RHCompuertasBotonCalcular.clicked.connect(self.RHCompuertas)
        widgets.RHCompuertasBotonReiniciar.clicked.connect(self.reiniciarCamposRHCompuertas)



        # ///////////////////////////////////////////////////////////////
        # COMPROBACIÓN DE DISEÑO

        # Menú principal
        widgets.botonMenuComprobacion.clicked.connect(self.pagComprobacionSeleccionada)
        
        # Sección Comprobacion
        widgets.ComprobacionBotonCalcular.clicked.connect(self.comprobacionDiseno)
        widgets.ComprobacionBotonReiniciar.clicked.connect(self.reiniciarCamposComprobacion)



        # ///////////////////////////////////////////////////////////////
        # DISEÑO

        # Menú principal
        widgets.botonMenuDiseno.clicked.connect(self.pagDisenoSeleccionada)
        
        # Sección Tuberias simples
        widgets.DisenoBotonCalcular.clicked.connect(self.disenoTuberiasSimples)
        widgets.DisenoBotonReiniciar.clicked.connect(self.reiniciarCamposDiseno)



        # ///////////////////////////////////////////////////////////////
        # ECUACIÓN DE MANNING

        # Menú principal
        widgets.botonMenuManning.clicked.connect(self.pagManningSeleccionada)

        # Sección Condición crítica
        widgets.ManningCriticaBotonCalcular.clicked.connect(self.ManningCondicionCritica)
        widgets.ManningCriticaBotonReiniciar.clicked.connect(self.reiniciarCamposManningCondicionCritica)

        # Sección Pendiente crítica
        widgets.ManningPendienteBotonCalcular.clicked.connect(self.ManningPendienteCritica)
        widgets.ManningPendienteBotonReiniciar.clicked.connect(self.reiniciarCamposManningPendienteCritica)

        # Sección Flujo Uniforme
        widgets.ManningUniformeBotonCalcular.clicked.connect(self.ManningFlujoUniforme)
        widgets.ManningUniformeBotonReiniciar.clicked.connect(self.reiniciarCamposManningFlujoUniforme)


        # ///////////////////////////////////////////////////////////////
        # FLUJO GRADUALMENTE VARIADO

        # Menú principal
        widgets.botonMenuFGV.clicked.connect(self.pagFGVSeleccionada)

        # Sección Integral
        widgets.FGVBotonCalcular.clicked.connect(self.FGVIntegracion)

        # Sección Método de paso directo
        widgets.FGVPasoDBotonCalcular.clicked.connect(self.FGVPasoDirecto)
        widgets.FGVPasoDBotonDescargarCSV.clicked.connect(self.FGVPasoDirectoCSV)

        # Sección Método de paso estándar
        widgets.FGVPasoEBotonCalcular.clicked.connect(self.FGVPasoEstandar)
        widgets.FGVPasoEBotonDescargarCSV.clicked.connect(self.FGVPasoEstandarCSV)


        # ///////////////////////////////////////////////////////////////
        # FLUJO RAPIDAMENTE VARIADO

        # Menú principal
        widgets.botonMenuFRV.clicked.connect(self.pagFRVSeleccionada)

        # Sección Rebosaderos
        widgets.FRVRebosaderoBotonCalcular.clicked.connect(self.FGVRebosaderos)

        # Sección Piscinas        
        widgets.FRVPiscinaBotonCalcular.clicked.connect(self.FGVPiscinas)


    
    # ///////////////////////////////////////////////////////////////
    # MENÚ PRINCIPAL

    def pagGeometriaSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_geometria)

    def pagConservacionESeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_conservacionE)

    def pagConservacionMSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_conservacionM)

    def pagComprobacionSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_comprobacion)
    
    def pagDisenoSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_diseno)

    def pagManningSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_manning)

    def pagFGVSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_FGV)

    def pagFRVSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_FRV)

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
        widgets.geoCFieldDiametro.setText(0)
        widgets.geoCFieldRelacionLlenado.setText(0)

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

        um1 = widgets.geoRComboBoxPendienteLateral.currentText().split(" - ")[1]
        um1 = cambioUnidadesAngulo[um1]

        um2 = widgets.geoRComboBoxPendienteLateral2.currentText().split(" - ")[1]
        um2 = cambioUnidadesAngulo[um2]

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


        A,P,Rh,T,D = geom_r(y,b,m1,m2,um1,uy,ub)

        widgets.geoRFieldArea.setText(str(round(A, 3)) + " m²")
        widgets.geoRFieldPerimetro.setText(str(round(P, 3)) + " m")
        widgets.geoRFieldRadio.setText(str(round(Rh, 3)) + " m")
        widgets.geoRFieldAnchoSuperficial.setText(str(round(T, 3))+ " m")
        widgets.geoRFieldProfundidadHidraulica.setText(str(round(D, 3)) + " m")
    
    def reiniciarCamposGeoR(self):
        widgets.geoCFieldProfundidadSeccion.setText(0)
        widgets.geoCFieldAncho.setText(0)
        widgets.geoCFieldPendienteLateral.setText(0)
        widgets.geoCFieldPendienteLateral2.setText(0)

        widgets.geoRComboBoxPendienteLateral.setCurrentIndex(0)
        widgets.geoRComboBoxPendienteLateral2.setCurrentIndex(0)
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
        d = float (widgets.geoFroudeFieldDiametro.text())
         
        um1 = widgets.geoFroudeComboBoxPendienteLateral.currentText().split(" - ")[1]
        um1 = cambioUnidadesAngulo[um1]

        um2 = widgets.geoFroudeComboBoxPendienteLateral2.currentText().split(" - ")[1]
        um2 = cambioUnidadesAngulo[um2]       

        uy = widgets.geoFroudeComboBoxProfundidad.currentText()
        uy = cambioUnidadesLongitud[uy]

        ub = widgets.geoFroudeComboBoxAncho.currentText()
        ub = cambioUnidadesLongitud[ub]

        uQ = widgets.geoFroudeComboBoxCaudal.currentText()

        if uQ == "No aplica":
            v = float (widgets.geoFroudeFieldVelocidad.text())
        else:
            Q = float (widgets.geoFroudeFieldCaudal.text())
            uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"

        ud = widgets.geoFroudeComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        Fr = froude(y,b,m1,m2,um1,Q,v,d,uy,ub,ud,uQ)
    
        widgets.geoFroudeFieldFroude.setText(str(round(Fr, 3)))

    def reiniciarCamposGeoFroude(self):
        widgets.geoFroudeFieldProfundidadSeccion.setText(0)
        widgets.geoFroudeFieldAncho.setText(0)
        widgets.geoFroudeFieldPendienteLateral.setText(0)
        widgets.geoFroudeFieldPendienteLateral2.setText(0)
        widgets.geoFroudeFieldCaudal.setText(0)
        widgets.geoFroudeFieldVelocidad.setText(0)
        widgets.geoFroudeFieldDiametro.setText(0)

        widgets.geoFroudeComboBoxPendienteLateral.setCurrentIndex(0)
        widgets.geoFroudeComboBoxPendienteLateral2.setCurrentIndex(0)
        widgets.geoFroudeComboBoxProfundidad.setCurrentIndex(0)
        widgets.geoFroudeComboBoxAncho.setCurrentIndex(0)
        widgets.geoFroudeComboBoxCaudal.setCurrentIndex(0)
        widgets.geoFroudeComboBoxDiametro.setCurrentIndex(0)

        widgets.geoFroudeFieldFroude.setText("")



    # ///////////////////////////////////////////////////////////////
    # CONSERVACIÓN DE ENERGÍA

    def conservacionEnergiaCaudal(self):
        b1 =  float (widgets.CEnergiaCaudalFieldAnchoSec1.text())
        m11 =  float (widgets.CEnergiaCaudalFieldPendienteLateralSec1.text())
        m12 =  float (widgets.CEnergiaCaudalFieldPendienteLateral2Sec1.text())
        y1 =  float (widgets.CEnergiaCaudalFieldProfundidadSec1.text())

        ub1 = widgets.CEnergiaCaudalComboBoxAnchoSec1.currentText()
        ub1 = cambioUnidadesLongitud[ub1]

        um11 = widgets.CEnergiaCaudalComboBoxPendienteLateralSec1.currentText().split(" - ")[1]
        um11 = cambioUnidadesAngulo[um11]

        um12 = widgets.CEnergiaCaudalComboBoxPendienteLateral2Sec1.currentText().split(" - ")[1]
        um12 = cambioUnidadesAngulo[um12]

        uy1 = widgets.CEnergiaCaudalComboBoxProfundidadSec1.currentText()
        uy1 = cambioUnidadesLongitud[uy1]


        b2 =  float (widgets.CEnergiaCaudalFieldAnchoSec2.text())
        m21 =  float (widgets.CEnergiaCaudalFieldPendienteLateralSec2.text())
        m22 =  float (widgets.CEnergiaCaudalFieldPendienteLateral2Sec2.text())
        y2 =  float (widgets.CEnergiaCaudalFieldProfundidadSec2.text())

        ub2 = widgets.CEnergiaCaudalComboBoxAnchoSec2.currentText()
        ub1 = cambioUnidadesLongitud[ub2]

        um21 = widgets.CEnergiaCaudalComboBoxPendienteLateralSec2.currentText().split(" - ")[1]
        um21 = cambioUnidadesAngulo[um21]

        um22 = widgets.CEnergiaCaudalComboBoxPendienteLateral2Sec2.currentText().split(" - ")[1]
        um22 = cambioUnidadesAngulo[um22]

        uy2 = widgets.CEnergiaCaudalComboBoxProfundidadSec2.currentText()
        uy2 = cambioUnidadesLongitud[uy2]

        z =  float (widgets.CEnergiaCaudalFieldEscalon.text())
        
        uz = widgets.CEnergiaCaudalComboBoxEscalon.currentText()
        uz = cambioUnidadesLongitud[uz]

        v, Q = conservacionE(y1,m11,m12,b1,None,y2,m21,m22,b2,uy1,uy2,um11,None,ub1,ub2,None,None,z,"caudal")

        widgets.CEnergiaCaudalFieldVelocidad.setText(str(round(v, 3)) + " m/s")
        widgets.CEEnergiaCaudalFieldCaudal.setText(str(round(Q, 3)) + " m³/s")


    def conservacionEnergiaY2(self):
        b1 =  float (widgets.CEnergiaY2FieldAnchoSec1.text())
        m11 =  float (widgets.CEnergiaY2FieldPendienteLateralSec1.text())
        m12 =  float (widgets.CEnergiaY2FieldPendienteLateral2Sec1.text())
        y1 =  float (widgets.CEnergiaY2FieldProfundidadSec1.text())

        ub1 = widgets.CEnergiaY2ComboBoxAnchoSec1.currentText()
        ub1 = cambioUnidadesLongitud[ub1]

        um11 = widgets.CEnergiaY2ComboBoxPendienteLateralSec1.currentText().split(" - ")[1]
        um11 = cambioUnidadesAngulo[um11]

        um12 = widgets.CEnergiaY2ComboBoxPendienteLateral2Sec1.currentText().split(" - ")[1]
        um12 = cambioUnidadesAngulo[um12]

        uy1 = widgets.CEnergiaY2ComboBoxProfundidadSec1.currentText()
        uy1 = cambioUnidadesLongitud[uy1]


        b2 =  float (widgets.CEnergiaY2FieldAnchoSec2.text())
        m21 =  float (widgets.CEnergiaY2FieldPendienteLateralSec2.text())
        m22 =  float (widgets.CEnergiaY2FieldPendienteLateral2Sec2.text())

        ub2 = widgets.CEnergiaY2ComboBoxAnchoSec2.currentText()
        ub1 = cambioUnidadesLongitud[ub2]

        um21 = widgets.CEnergiaY2ComboBoxPendienteLateralSec2.currentText().split(" - ")[1]
        um21 = cambioUnidadesAngulo[um21]

        um22 = widgets.CEnergiaY2ComboBoxPendienteLateral2Sec2.currentText().split(" - ")[1]
        um22 = cambioUnidadesAngulo[um22]


        z =  float (widgets.CEnergiaY2FieldEscalon.text())
        
        uz = widgets.CEnergiaY2ComboBoxEscalon.currentText()
        uz = cambioUnidadesLongitud[uz]


        uQ = widgets.CEnergiaY2ComboBoxCaudal.currentText()

        if uQ == "No aplica":
            v1 = float (widgets.CEnergiaY2FieldVelocidad.text())
        else:
            Q = float (widgets.CEnergiaY2FieldCaudal.text())
            uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"


        y2_raiz1, y2_raiz2, y2_raiz3, yc, Ec, y1n_raiz1, y1n_raiz2, y1n_raiz3, represamiento = conservacionE(y1,m11,m12,b1,Q,None,m21,m22,b2,uy1,None,um11,uQ,ub1,ub2,v1,None,z,"y")

        widgets.CEnergiaY2LabelProfundidad2Raiz1.setText(str(round(y2_raiz1, 3)) + " m")
        widgets.CEnergiaY2LabelProfundidad2Raiz2.setText(str(round(y2_raiz2, 3)) + " m")
        widgets.CEnergiaY2LabelProfundidad2Raiz3.setText(str(round(y2_raiz3, 3)) + " m")

        if yc:
            widgets.CEnergiaY2FieldYc.setText(str(round(yc, 3)) + " m")
            widgets.CEnergiaY2FieldEc.setText(str(round(Ec, 3)) + " m")

            widgets.CEnergiaY2LabelProfundidad1Raiz1.setText(str(round(y1n_raiz1, 3)) + " m")
            widgets.CEnergiaY2LabelProfundidad1Raiz2.setText(str(round(y1n_raiz2, 3)) + " m")
            widgets.CEnergiaY2LabelProfundidad1Raiz3.setText(str(round(y1n_raiz3, 3)) + " m")           

            widgets.CEnergiaY2FieldRepresamiento.setText(str(round(represamiento, 3)) + " m")  

        else:
            
            widgets.CEnergiaY2FieldYc.setText("")
            widgets.CEnergiaY2FieldEc.setText("")

            widgets.CEnergiaY2LabelProfundidad1Raiz1.setText("")
            widgets.CEnergiaY2LabelProfundidad1Raiz2.setText("")
            widgets.CEnergiaY2LabelProfundidad1Raiz3.setText("")           

            widgets.CEnergiaY2FieldRepresamiento.setText("") 


    def conservacionEnergiaMaxZ (self):
        
        b1 =  float (widgets.CEnergiaZFieldAnchoSec1.text())
        m11 =  float (widgets.CEnergiaZFieldPendienteLateralSec1.text())
        m12 =  float (widgets.CEnergiaZFieldPendienteLateral2Sec1.text())
        y1 =  float (widgets.CEnergiaZFieldProfundidad1Sec1.text())

        ub1 = widgets.CEnergiaZComboBoxAnchoSec1.currentText()
        ub1 = cambioUnidadesLongitud[ub1]

        um11 = widgets.CEnergiaZComboBoxPendienteLateralSec1.currentText().split(" - ")[1]
        um11 = cambioUnidadesAngulo[um11]

        um12 = widgets.CEnergiaZComboBoxPendienteLateral2Sec1.currentText().split(" - ")[1]
        um12 = cambioUnidadesAngulo[um12]

        uy1 = widgets.CEnergiaZComboBoxProfundidad1Sec1.currentText()
        uy1 = cambioUnidadesLongitud[uy1]

        b2 =  float (widgets.CEnergiaZFieldAnchoSec2.text())
        m21 =  float (widgets.CEnergiaZFieldPendienteLateralSec2.text())
        m22 =  float (widgets.CEnergiaZFieldPendienteLateral2Sec2.text())

        ub2 = widgets.CEnergiaZComboBoxAnchoSec2.currentText()
        ub2 = cambioUnidadesLongitud[ub2]

        um21 = widgets.CEnergiaZComboBoxPendienteLateralSec2.currentText().split(" - ")[1]
        um21 = cambioUnidadesAngulo[um21]

        um22 = widgets.CEnergiaZComboBoxPendienteLateral2Sec2.currentText().split(" - ")[1]
        um22 = cambioUnidadesAngulo[um22]

        uQ = widgets.CEnergiaZComboBoxCaudal.currentText()

        if uQ == "No aplica":
            v1 = float (widgets.CEnergiaZFieldVelocidad.text())
        else:
            Q = float (widgets.CEnergiaZFieldCaudal.text())
            uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"

        z, yc = conservacionE(y1,m11,m12,b1,Q,None,m21,m22,b2,uy1,None,um11,uQ,ub1,ub2,v1,None,None,"maximoZ")

        widgets.CEnergiaZFieldZ.setText(str(round(z, 3)) + " m")
        widgets.CEnergiaZFieldYc.setText(str(round(yc, 3)) + " m")


    def conservacionEnergiaMinB (self):

        
        b1 =  float (widgets.CEnergiaBFieldAnchoSec1.text())
        m11 =  float (widgets.CEnergiaBFieldPendienteLateralSec1.text())
        m12 =  float (widgets.CEnergiaBFieldPendienteLateral2Sec1.text())
        y1 =  float (widgets.CEnergiaBFieldProfundidadSec1.text())

        ub1 = widgets.CEnergiaBComboBoxAnchoSec1.currentText()
        ub1 = cambioUnidadesLongitud[ub1]

        um11 = widgets.CEnergiaBComboBoxPendienteLateralSec1.currentText().split(" - ")[1]
        um11 = cambioUnidadesAngulo[um11]

        um12 = widgets.CEnergiaBComboBoxPendienteLateral2Sec1.currentText().split(" - ")[1]
        um12 = cambioUnidadesAngulo[um12]

        uy1 = widgets.CEnergiaBComboBoxProfundidad1Sec1.currentText()
        uy1 = cambioUnidadesLongitud[uy1]

        m21 =  float (widgets.CEnergiaBFieldPendienteLateralSec2.text())
        m22 =  float (widgets.CEnergiaBFieldPendienteLateral2Sec2.text())

        um21 = widgets.CEnergiaBComboBoxPendienteLateralSec2.currentText().split(" - ")[1]
        um21 = cambioUnidadesAngulo[um21]

        um22 = widgets.CEnergiaBComboBoxPendienteLateral2Sec2.currentText().split(" - ")[1]
        um22 = cambioUnidadesAngulo[um22]

        uQ = widgets.CEnergiaBComboBoxCaudal.currentText()

        if uQ == "No aplica":
            v1 = float (widgets.CEnergiaBFieldVelocidad.text())
        else:
            Q = float (widgets.CEnergiaBFieldCaudal.text())
            uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"

        
        z =  float (widgets.CEnergiaBFieldEscalon.text())
        
        uz = widgets.CEnergiaBComboBoxEscalon.currentText()
        uz = cambioUnidadesLongitud[uz]

        E1, b2, yc = conservacionE(y1,m11,m12,b1,Q,None,m21,m22,None,uy1,None,um11,uQ,ub1,None,v1,None,z, "maximoB")

        widgets.CEnergiaBFieldEnergia1.setText(str(round(E1, 3)) + " m")
        widgets.CEnergiaBFieldAncho2.setText(str(round(b2, 3)) + " m")
        widgets.CEnergiaBFieldYc.setText(str(round(yc, 3)) + " m")



    # ///////////////////////////////////////////////////////////////
    # CONSERVACIÓN DE MOMENTUM

    def RHAnalisis (self):
        b =  float (widgets.RHAnalisisFieldAncho.text())
        m1 =  float (widgets.RHAnalisisFieldPendienteLateral.text())
        m2 =  float (widgets.RHAnalisisFieldPendienteLateral2.text())
        y1 =  float (widgets.RHAnalisisFieldProfundidad1.text())
        Q =  float (widgets.RHAnalisisFieldCaudal.text())
        
        l =  float (widgets.RHAnalisisFieldLongitudInclinada.text())
        yn =  float (widgets.RHAnalisisFieldProfundidad.text())
        i =  float (widgets.RHAnalisisFieldInclinacion.text())
        f = float (widgets.RHAnalisisFieldFuerza.text())


        ub = widgets.RHAnalisisComboBoxAncho.currentText()
        ub = cambioUnidadesLongitud[ub]

        um1 = widgets.RHAnalisisComboBoxPendienteLateral.currentText().split(" - ")[1]
        um1 = cambioUnidadesAngulo[um1]

        um2 = widgets.RHAnalisisComboBoxPendienteLateral2.currentText().split(" - ")[1]
        um2 = cambioUnidadesAngulo[um2]

        uy1 = widgets.RHAnalisisComboBoxProfundidad1.currentText()
        uy1 = cambioUnidadesLongitud[uy1]

        uQ = widgets.RHAnalisisComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"


        ul = widgets.RHAnalisisComboBoxLongitudInclinada.currentText()
        ul = cambioUnidadesLongitud[ul]

        uyn = widgets.RHAnalisisComboBoxProfundidad.currentText()
        uyn = cambioUnidadesLongitud[uyn]

        ui = widgets.RHAnalisisComboBoxInclinacion.currentText()
        ui = cambioUnidadesAngulo[ui]

        calculos, resultados = eficienciaRH(Q,b,m1,m2,um1,y1,yn,f,l,i,uQ,ub,uy1,ul,ui)
        E1, E2, z = calculos

        widgets.RHAnalisisFieldAltura.setText(str(round(z, 3)) + " m")
        widgets.RHAnalisisFieldE1.setText(str(round(E1, 3)) + " m")
        widgets.RHAnalisisFieldE2.setText(str(round(E2, 3)) + " m")

        widgets.RHAnalisisFieldEficiencia.setText(str(round(resultados[0], 3)) + " %")

    def reiniciarCamposRHAnalisis(self):

        widgets.RHAnalisisFieldAncho.setText(0)
        widgets.RHAnalisisFieldPendienteLateral.setText(0)
        widgets.RHAnalisisFieldPendienteLateral2.setText(0)
        widgets.RHAnalisisFieldProfundidad1.setText(0)
        widgets.RHAnalisisFieldCaudal.setText(0)
        
        widgets.RHAnalisisFieldLongitudInclinada.setText(0)
        widgets.RHAnalisisFieldProfundidad.setText(0)
        widgets.RHAnalisisFieldInclinacion.setText(0)
        widgets.RHAnalisisFieldFuerza.setText(0)

        widgets.RHAnalisisComboBoxAncho.setCurrentIndex(0)
        widgets.RHAnalisisComboBoxPendienteLateral.setCurrentIndex(0)
        widgets.RHAnalisisComboBoxPendienteLateral2.setCurrentIndex(0)
        widgets.RHAnalisisComboBoxProfundidad1.setCurrentIndex(0)
        widgets.RHAnalisisComboBoxCaudal.setCurrentIndex(0)
        widgets.RHAnalisisComboBoxLongitudInclinada.setCurrentIndex(0)
        widgets.RHAnalisisComboBoxProfundidad.setCurrentIndex(0)
        widgets.RHAnalisisComboBoxInclinacion.setCurrentIndex(0)

        widgets.RHAnalisisFieldAltura.setText("")
        widgets.RHAnalisisFieldE1.setText("")
        widgets.RHAnalisisFieldE2.setText("")
        widgets.RHAnalisisFieldEficiencia.setText("")


    def RHPropiedades(self):
        b =  float (widgets.RHPropiedadesFieldBase.text())
        y =  float (widgets.RHPropiedadesFieldProfundidad.text())       
        m1 =  float (widgets.RHPropiedadesFieldPendienteLateral.text())
        m2 =  float (widgets.RHPropiedadesFieldPendienteLateral2.text())
        y =  float (widgets.RHPropiedadesFieldProfundidad.text())
        Q =  float (widgets.RHPropiedadesFieldCaudal.text())
        d =  float (widgets.RHPropiedadesFieldDiametro.text())
        
        
        ub = widgets.RHPropiedadesComboBoxBase.currentText()
        ub = cambioUnidadesLongitud[ub]

        um1 = widgets.RHPropiedadesComboBoxPendienteLateral.currentText().split(" - ")[1]
        um1 = cambioUnidadesAngulo[um1]

        um2 = widgets.RHPropiedadesComboBoxPendientaLateral2.currentText().split(" - ")[1]
        um2 = cambioUnidadesAngulo[um2]

        uy = widgets.RHPropiedadesComboBoxProfundidad.currentText()
        uy = cambioUnidadesLongitud[uy]

        uQ = widgets.RHPropiedadesComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"
        
        ud = widgets.RHPropiedadesComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]
    
        opcionales, resultados = clasificacionResalto(Q,b,m1,m2,d,ud,um1,y,ub,uy,uQ)
            
        widgets.RHPropiedadesFieldFroude.setText(str(round(opcionales[0], 3)))
        widgets.RHPropiedadesFieldClasificacion.setText(resultados[0])

        Lr = longitudResalto(y,b,m1,m2,Q,d,uy,ub,uQ,ud,um1)
        widgets.RHPropiedadesFieldLongitud.setText(str(round(Lr, 3)) + " m")

    def reiniciarCamposRHPropiedades(self):
        widgets.RHPropiedadesFieldBase.setText(0)
        widgets.RHPropiedadesFieldProfundidad.setText(0) 
        widgets.RHPropiedadesFieldPendienteLateral.setText(0)
        widgets.RHPropiedadesFieldPendienteLateral2.setText(0)
        widgets.RHPropiedadesFieldProfundidad.setText(0)
        widgets.RHPropiedadesFieldCaudal.setText(0)
        widgets.RHPropiedadesFieldDiametro.setText(0)
        
        widgets.RHPropiedadesComboBoxBase.setCurrentIndex(0)
        widgets.RHPropiedadesComboBoxPendienteLateral.setCurrentIndex(0)
        widgets.RHPropiedadesComboBoxPendientaLateral2.setCurrentIndex(0)
        widgets.RHPropiedadesComboBoxProfundidad.setCurrentIndex(0)
        widgets.RHPropiedadesComboBoxCaudal.setCurrentIndex(0)
        widgets.RHPropiedadesComboBoxDiametro.setCurrentIndex(0)


        widgets.RHPropiedadesFieldFroude.setText("")
        widgets.RHPropiedadesFieldClasificacion.setText("")
        widgets.RHPropiedadesFieldLongitud.setText("")


    def RHTipo (self):
        b =  float (widgets.RHTipoFieldBase.text())
        y =  float (widgets.RHTipoFieldProfundidad.text())       
        yn =  float (widgets.RHTipoFieldNormal.text())       
        m1 =  float (widgets.RHTipoFieldPendienteLateral.text())
        m2 =  float (widgets.RHTipoFieldPendienteLateral2.text())
        s0 =  float (widgets.RHTipoFieldInclinacion.text())
        Q =  float (widgets.RHTipoFieldCaudal.text())

        
        ub = widgets.RHTipoComboBoxBase.currentText()
        ub = cambioUnidadesLongitud[ub]

        um1 = widgets.RHTipoComboBoxPendientaLateral.currentText().split(" - ")[1]
        um1 = cambioUnidadesAngulo[um1]

        um2 = widgets.RHTipoComboBoxPendienteLateral2.currentText().split(" - ")[1]
        um2 = cambioUnidadesAngulo[um2]

        uy = widgets.RHTipoComboBoxProfundidad.currentText()
        uy = cambioUnidadesLongitud[uy]

        uyn = widgets.RHTipoComboBoxNormal.currentText()
        uyn = cambioUnidadesLongitud[uyn]

        uQ = widgets.RHTipoComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"

        ui = widgets.RHTipoComboBoxInclinacion.currentText()
        ui = cambioUnidadesAngulo[ui]

        opcionales, resultados = tipoResalto(Q,b,y,m1,m2,yn,s0,uQ,ub,uy,uyn,ui)

        y2, y_a = opcionales

        widgets.RHTipoFieldSubsecuente.setText(str(round(y2, 3)) + " m")
        widgets.RHTipoFieldAsterisco.setText(str(round(y_a, 3)) + " m")

        widgets.RHTipoFieldTipo.setText(resultados[0])

    def reiniciarCamposRHTipo (self):
        widgets.RHTipoFieldBase.setText(0) 
        widgets.RHTipoFieldProfundidad.setText(0)      
        widgets.RHTipoFieldNormal.setText(0)       
        widgets.RHTipoFieldPendienteLateral.setText(0) 
        widgets.RHTipoFieldPendienteLateral2.setText(0) 
        widgets.RHTipoFieldInclinacion.setText(0) 
        widgets.RHTipoFieldCaudal.setText(0) 

        widgets.RHTipoComboBoxBase.setCurrentIndex(0)
        widgets.RHTipoComboBoxPendientaLateral.setCurrentIndex(0)
        widgets.RHTipoComboBoxPendienteLateral2.setCurrentIndex(0)
        widgets.RHTipoComboBoxProfundidad.setCurrentIndex(0)
        widgets.RHTipoComboBoxNormal.setCurrentIndex(0)
        widgets.RHTipoComboBoxCaudal.setCurrentIndex(0)
        widgets.RHTipoComboBoxInclinacion.setCurrentIndex(0)

        widgets.RHTipoFieldSubsecuente.setText("")
        widgets.RHTipoFieldAsterisco.setText("")
        widgets.RHTipoFieldTipo.setText("")


    def RHCompuertas(self):
        b =  float (widgets.RHCompuertasFieldAncho.text())
        y1 =  float (widgets.RHCompuertasFieldProfundidad.text())       
        m1 =  float (widgets.RHCompuertasFieldPendienteLateral.text())
        m2 =  float (widgets.RHCompuertasFieldPendienteLateral2.text())
        Q =  float (widgets.RHCompuertasFieldCaudal.text())
        d =  float (widgets.RHCompuertasFieldDiametro.text())

        y2 =  float(widgets.RHCompuertasFieldProfundidad2.text())
        rho =  float(widgets.RHCompuertasFieldDensidad.text())


        ub = widgets.RHCompuertasComboBoxAncho.currentText()
        ub = cambioUnidadesLongitud[ub]

        uy1 = widgets.RHCompuertasComboBoxProfundidad.currentText()
        uy1 = cambioUnidadesLongitud[uy1]
        
        um1 = widgets.RHCompuertasComboBoxPendienteLateral.currentText().split(" - ")[1]
        um1 = cambioUnidadesAngulo[um1]

        um2 = widgets.RHCompuertasComboBoxPendienteLateral.currentText().split(" - ")[1]
        um2 = cambioUnidadesAngulo[um2]

        ud = widgets.RHCompuertasComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        uQ = widgets.RHCompuertasComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"
        
        uy2 = widgets.RHCompuertasComboBoxProfundidad2.currentText()
        uy2 = cambioUnidadesLongitud[uy2]

        M1 = momentum(Q,b,m1,m2,um1,y1,d,uQ,ub,uy1,ud)
        M2 = "No aplica."
        F_a = "No aplica."
        f = "No aplica."

        if d == 0 and y2 and rho:
            M1,M2,F_a,f = fuerzaCompuerta(y1,y2,b,Q,m1,m2,um1,rho,uy1,uy2,ub,uQ)
            M2 = str(round(M2, 3)) + " m²"
            F_a = str(round(F_a, 3)) + " m²"
            f = str(round(f, 3)) + " N"

        widgets.RHCompuertasFieldMomentum.setText(str(round(M1, 3)) + "m²")
        widgets.RHCompuertasFieldMomentum2.setText(M2)
        widgets.RHCompuertasFieldFuerza.setText(F_a)
        widgets.RHCompuertasFieldFuerzaCompuerta.setText(f)

    def reiniciarCamposRHCompuertas(self):
        widgets.RHCompuertasFieldAncho.setText(0) 
        widgets.RHCompuertasFieldProfundidad.setText(0)      
        widgets.RHCompuertasFieldPendienteLateral.setText(0) 
        widgets.RHCompuertasFieldPendienteLateral2.setText(0) 
        widgets.RHCompuertasFieldCaudal.setText(0) 
        widgets.RHCompuertasFieldDiametro.setText(0) 

        widgets.RHCompuertasFieldProfundidad2.setText(0) 
        widgets.RHCompuertasFieldDensidad.setText(0) 

        widgets.RHCompuertasComboBoxAncho.setCurrentIndex(0)
        widgets.RHCompuertasComboBoxProfundidad.setCurrentIndex(0)       
        widgets.RHCompuertasComboBoxPendienteLateral.setCurrentIndex(0)
        widgets.RHCompuertasComboBoxPendienteLateral.setCurrentIndex(0)
        widgets.RHCompuertasComboBoxDiametro.setCurrentIndex(0)
        widgets.RHCompuertasComboBoxCaudal.setCurrentIndex(0)
        widgets.RHCompuertasComboBoxProfundidad2.setCurrentIndex(0)

        widgets.RHCompuertasFieldMomentum.setText("")
        widgets.RHCompuertasFieldMomentum2.setText("")
        widgets.RHCompuertasFieldFuerza.setText("")
        widgets.RHCompuertasFieldFuerzaCompuerta.setText("")



    # ///////////////////////////////////////////////////////////////
    # COMPROBACIÓN DE DISEÑO
    def comprobacionDiseno(self):
        ynd =  float (widgets.AComprobacionFieldRelacionLlenado.text())
        d =  float (widgets.BComprobacionFieldDiametro.text())
        n = float (widgets.ComprobacionFieldManning.text())
        s0 =  float (widgets.CComprobacionFieldInclinacion.text())       
        ks =  float (widgets.DComprobacionFieldRugosidad.text())
        viscosidad =  float (widgets.EComprobacionFieldViscosidad.text())
        g =  float (widgets.FComprobacionFieldGravedad.text())

        ud = widgets.ComprobacionComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        us0 = widgets.ComprobacionComboBoxInclinacion.currentText()
        us0 = cambioUnidadesAngulo[us0]

        uks = widgets.ComprobacionComboBoxRugosidad.currentText()
        uks = cambioUnidadesLongitud[us0]
        
        ecuacion = widgets.ComprobacionComboBoxEcuacion.currentText()

        Q,Fr,FT,v,Sc = None, None, None, None, None, 
        if ecuacion == 'Manning':
            Q,Fr,FT,v,Sc = comprobacion_manning (d,ynd,s0,g,n,ud,us0)
        else:
            Q,F,v = valores_Darcy(d, ynd,0, ks, viscosidad, g, ud, uks, us0)
            Fr, FT = F

        widgets.ComprobacionFieldCaudal.setText(str(round(Q, 3)) + " m³/s")
        widgets.ComprobacionFieldFroude.setText(str(round(Fr, 3)))
        widgets.ComprobacionFieldVelocidad.setText(str(round(v, 3)) + " m/s")
        widgets.ComprobacionFieldTipoFlujo.setText(FT)

        if Sc:
            widgets.ComprobacionFieldPendienteCritica.setText(str(round(Sc, 3)))
        

    def reiniciarCamposComprobacion (self):
        widgets.AComprobacionFieldRelacionLlenado.setText(0) 
        widgets.BComprobacionFieldDiametro.setText(0) 
        widgets.CComprobacionFieldInclinacion.setText(0)       
        widgets.DComprobacionFieldRugosidad.setText(0) 
        widgets.EComprobacionFieldViscosidad.setText(0) 
        widgets.FComprobacionFieldGravedad.setText(9.81) 

        widgets.ComprobacionComboBoxDiametro.setCurrentIndex(0)

        widgets.ComprobacionComboBoxInclinacion.setCurrentIndex(0)

        widgets.ComprobacionFieldTipoFlujo.setText("")
        widgets.ComprobacionFieldCaudal.setText("")
        widgets.ComprobacionFieldFroude.setText("")
        widgets.ComprobacionFieldVelocidad.setText("")
        widgets.ComprobacionFieldPendienteCritica.setText("")


    # ///////////////////////////////////////////////////////////////
    # DISEÑO
    def disenoTuberiasSimples (self):
        ynd =  float (widgets.ADisenoFieldRelacionLlenado.text())
        d =  float (widgets.BDisenoFieldDiametro.text())
        s0 =  float (widgets.CDisenoFieldInclinacion.text())       
        ks =  float (widgets.DDisenoFieldRugosidad.text())
        viscosidad =  float (widgets.EDisenoFieldViscosidad.text())
        g =  float (widgets.FDisenoFieldGravedad.text())
        diametros = []

        ud = widgets.DisenoComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        us0 = widgets.DisenoComboBoxInclinacion.currentText()
        us0 = cambioUnidadesAngulo[us0]
        
        theta, T, A, Q, Fr, v, P, D, R, tao = None

        widgets.DisenoFieldAngulo.setText(str(round(theta, 3)) + " radianes")
        widgets.DisenoFieldAnchoSuperficial.setText(str(round(T, 3)) + " radianes")
        widgets.DisenoFieldArea.setText(str(round(A, 3)) + " m²")
        widgets.DisenoFieldCaudal.setText(str(round(Q, 3)) + " m³/s")
        widgets.DisenoFieldFroude.setText(str(round(Fr, 3)))
        widgets.DisenoFieldVelocidad.setText(str(round(v, 3)) + " m/s")
        widgets.DisenoFieldPerimetro.setText(str(round(P, 3)) + " m")
        widgets.DisenoFieldProfundidadHidraulica.setText(str(round(D, 3)) + " m")
        widgets.DisenoFieldRadioHidraulico.setText(str(round(R, 3)) + " m")
        widgets.DisenoFieldTao.setText(str(round(tao, 3)) + " Pa")

    def reiniciarCamposDiseno (self):
        widgets.ADisenoFieldRelacionLlenado.setText(0) 
        widgets.BDisenoFieldDiametro.setText(0) 
        widgets.CDisenoFieldInclinacion.setText(0)       
        widgets.DDisenoFieldRugosidad.setText(0) 
        widgets.EDisenoFieldViscosidad.setText(0) 
        widgets.FDisenoFieldGravedad.setText(9.81) 

        widgets.DisenoComboBoxDiametro.setCurrentIndex(0)

        widgets.DisenoComboBoxInclinacion.setCurrentIndex(0)

        widgets.DisenoFieldAngulo.setText("")
        widgets.DisenoFieldAnchoSuperficial.setText("")
        widgets.DisenoFieldArea.setText("")
        widgets.DisenoFieldCaudal.setText("")
        widgets.DisenoFieldFroude.setText("")
        widgets.DisenoFieldVelocidad.setText("")
        widgets.DisenoFieldPerimetro.setText("")
        widgets.DisenoFieldProfundidadHidraulica.setText("")
        widgets.DisenoFieldRadioHidraulico.setText("")
        widgets.DisenoFieldTao.setText("")

 
 
    # ///////////////////////////////////////////////////////////////
    # ECUACIÓN DE MANNING
    
    def ManningCondicionCritica (self):
        b =  float (widgets.ManningCriticaFieldBase.text())
        m1 =  float (widgets.ManningCriticaFieldPendienteLateral.text())       
        m2 =  float (widgets.ManningCriticaFieldPendienteLateral2.text())
        d =  float (widgets.ManningCriticaFieldDiametro.text())
        
        ud = widgets.ManningCriticaComboBoxDiametro.currentText()

        if ud != 'No aplica':
            ud = cambioUnidadesLongitud[ud]
        else:
            ub = widgets.ManningCriticaComboBoxBase.currentText()
            ub = cambioUnidadesLongitud[ub]
            
            um1 = widgets.ManningCriticaComboBoxPendienteLateral.currentText().split(" - ")[1]
            um1 = cambioUnidadesAngulo[um1]

            um2 = widgets.ManningCriticaComboBoxPendienteLateral2.currentText().split(" - ")[1]
            um2 = cambioUnidadesAngulo[um2]

        uQ = widgets.ManningCriticaComboBoxCaudal.currentText()
        if uQ == "No aplica":
            v = float (widgets.ManningCriticaFieldVelocidad.text())
        else:
            Q = float (widgets.ManningCriticaFieldCaudal.text())
            uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"

        profundidad_critica = yc(Q,b,v,m1,m2,um1,d,ub,ud,uQ)
        velocidad_critica = vc(m1,m2,um1,b,yc,d,"m",ub,ud)

        widgets.ManningCriticaLabelFieldProfundidadCritica.setText(str(round(profundidad_critica, 3)) + " m")
        widgets.ManningCriticaLabelFieldVelocidadCritica.setText(str(round(velocidad_critica, 3)) + " m/s")

    def reiniciarCamposManningCondicionCritica (self):
        return 0

    def ManningPendienteCritica (self):
        b =  float (widgets.ManningPendienteFieldAncho.text())
        d =  float (widgets.ManningPendienteFieldDiametro.text())
        n =  float (widgets.ManningPendienteFieldNumeManning.text())       
        m1 =  float (widgets.ManningPendienteFieldPendienteLateral.text())
        m2 =  float (widgets.ManningPendienteFieldPendienteLateral2.text())

        ub = widgets.ManningPendienteComboBoxAncho.currentText()
        ub = cambioUnidadesLongitud[ub]
        
        um1 = widgets.ManningPendienteComboBoxPendienteLateral.currentText().split(" - ")[1]
        um1 = cambioUnidadesAngulo[um1]

        um2 = widgets.ManningPendienteComboBoxPendienteLateral2.currentText().split(" - ")[1]
        um2 = cambioUnidadesAngulo[um2]

        ud = widgets.ManningCriticaComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        uQ = widgets.ManningPendienteComboBoxCaudal.currentText()
        
        if uQ == "No aplica":
            yc = float (widgets.ManningPendienteFieldProfundidadCritica.text())
            y,v,Sc = pendienteC_especifica(n,yc,b,m1,m2,um1,d,ub,ud,"m")
        else:
            Q = float (widgets.ManningPendienteFieldCaudal.text())
            uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"
            Sc = pendienteC_limite(n,Q,b,m1,m2,um1,d,uQ,ub,ud)

        widgets.ManningPendienteFieldPendienteCritica.setText(str(round(Sc, 3)))

    def reiniciarCamposManningPendienteCritica (self):
        return 0

    def ManningFlujoUniforme (self):
        b =  float (widgets.ManningUniformeFieldBase.text())
        d =  float (widgets.ManningUniformeFieldDiametro.text())
        m1 =  float (widgets.ManningUniformeFieldPendienteLateral.text())
        m2 =  float (widgets.ManningUniformeFieldPendienteLateral2.text())
        S0 =  float (widgets.ManningUniformeFieldInclinacion.text())
        Q =  float (widgets.ManningUniformeFieldCaudal.text())
        n =  float (widgets.ManningUniformeFieldNumManning.text())

        ub = widgets.ManningUniformeComboBoxBase.currentText()
        ub = cambioUnidadesLongitud[ub]
        
        ud = widgets.ManningCriticaComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        um1 = widgets.ManningUniformeComboBoxPendienteLateral.currentText().split(" - ")[1]
        um1 = cambioUnidadesAngulo[um1]

        um2 = widgets.ManningUniformeComboBoxPendienteLateral2.currentText().split(" - ")[1]
        um2 = cambioUnidadesAngulo[um2]

        uS0 = widgets.ManningUniformeComboBoxInclinacion.currentText()
        uS0 = cambioUnidadesAngulo[uS0]

        uQ = widgets.ManningUniformeComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"
        
        SI = widgets.ManningCheckBoxSI.isChecked()
        IN = widgets.ManningCheckBoxIngles.isChecked()

        unidades = False
        if SI:
            i = 'si'
            unidades = True
        elif IN:
            i = 'in'
            unidades = True
        else:
            widgets.ManningUniformeFieldNormal.setText("Debe seleccionar unidades")
            
        if unidades:
            yn = yn_manning(Q,n,S0,m1,m2,um1,b,d,i,uQ,ub,ud,uS0)
            widgets.ManningUniformeFieldNormal.setText(str(round(yn, 3) + "m"))



    def reiniciarCamposManningFlujoUniforme (self):
        return 0



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

        um = widgets.FGVComboBoxPendienteLateral.currentText().split(" - ")[1]
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
        uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"
        

        x = fgv_int(Q,n,S0,b,m1,m2,um,d,y1,y2,uQ,uS0,ub,ud,uy1,uy2)

        widgets.FGVFieldDistanciaX.setText(str(round(x, 3)) + "m")

    def FGVPasoDirecto (self):

        global parametrosGrafica

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

        um = widgets.FGVPasoDComboBoxPendienteLateral.currentText().split(" - ")[1]
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
        uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"
        
        parametrosGrafica = pasoDirecto(Q,n,S0,b,m1,m2,um,d,y1,y2,pasos,datum,uQ,uS0,ub,ud,uy1,uy2)

    def FGVPasoDirectoCSV (self):

        global parametrosGrafica
        print ("Entro aquí")
        plot_i, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_Sfi, plot_sfm, plot_So_Sfm, plot_deltaE, plot_deltaX, plot_x, plot_fondo, plot_y, plot_yc, plot_yn = parametrosGrafica
        ruta = self.FGVSolicitarRuta ()
        txt_pasoDirecto(plot_i, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_Sfi, plot_sfm, plot_So_Sfm, plot_deltaE, plot_deltaX, plot_x, plot_fondo, plot_y, plot_yc, plot_yn, ruta)
        self.FGVPasoDirectoGrafica(ruta)

    def FGVPasoDirectoGrafica (self, ruta):
        global parametrosGrafica
        parametrosGrafica = ''
        macroPasoDirecto (ruta)



    def FGVPasoEstandar (self):
        
        global parametrosGrafica

        b1 =  float (widgets.FGVPasoEFieldAnchoSec1.text())
        S01 =  float (widgets.FGVPasoEFieldInclinacionCanalSec1.text())       
        n1 = float (widgets.FGVPasoEFieldManningSec1.text())       
        m11 =  float (widgets.FGVPasoEFieldFieldPendienteLateralSec1.text())
        m12 =  float (widgets.FGVPasoEFieldPendienteLateral2Sec1.text())
        L1 =  float (widgets.FGVPasoEFieldLongitudSec1.text())
        pasos1 = float(widgets.FGVPasoEPasosSec1.value())

        b2 =  float (widgets.FGVPasoEFieldAnchoSec2.text())
        S02 =  float (widgets.FGVPasoEFieldInclinacionCanalSec2.text())       
        n2 = float (widgets.FGVPasoEFieldManningSec2.text())       
        m21 =  float (widgets.FGVPasoEFieldFieldPendienteLateralSec2.text())
        m22 =  float (widgets.FGVPasoEFieldPendienteLateral2Sec2.text())
        L2 =  float (widgets.FGVPasoEFieldLongitudSec2.text())
        pasos2 = float(widgets.FGVPasoEPasosSec2.value())

        Q =  float (widgets.FGVPasoEFieldCaudal.text())
        y_control =  float (widgets.FGVPasoEFieldYc.text())
        datum =  float (widgets.FGVPasoEFieldDatum.text())
        direccion =  widgets.FGVPasoEComboBoxDireccion.currentText()
        secciones =  float(widgets.FGVPasoENumSecciones.value())

        if direccion == "Aguas arriba":
            direccion = "negativo"
        else:
            direccion = "positivo"

        ub1 = widgets.FGVPasoEComboBoxAnchoSec1.currentText()
        ub1 = cambioUnidadesLongitud[ub1]

        um11 = widgets.FGVPasoEComboBoxPendienteLateralSec1.currentText().split(" - ")[1]
        um11 = cambioUnidadesAngulo[um11]

        um12 = widgets.FGVPasoEComboBoxPendienteLateral2Sec1.currentText().split(" - ")[1]
        um12 = cambioUnidadesAngulo[um12]

        uS01 = widgets.FGVPasoEComboBoxInclinacionSec1.currentText()
        uS01 = cambioUnidadesAngulo[uS01]

        uL1 = widgets.FGVPasoEComboBoxLongitudSec1.currentText()
        uL1 = cambioUnidadesLongitud[uL1]


        ub2 = widgets.FGVPasoEComboBoxAnchoSec2.currentText()
        ub2 = cambioUnidadesLongitud[ub2]

        um21 = widgets.FGVPasoEComboBoxPendienteLateralSec2.currentText().split(" - ")[1]
        um21 = cambioUnidadesAngulo[um21]

        um22 = widgets.FGVPasoEComboBoxPendienteLateral2Sec2.currentText().split(" - ")[1]
        um22 = cambioUnidadesAngulo[um22]

        uS02 = widgets.FGVPasoEComboBoxInclinacionSec2.currentText()
        uS02 = cambioUnidadesAngulo[uS02]

        uL2 = widgets.FGVPasoEComboBoxLongitudSec2.currentText()
        uL2 = cambioUnidadesLongitud[uL2]


        uQ = widgets.FGVPasoEComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"
        
        uycontrol = widgets.FGVPasoEComboBoxYc.currentText()
        uycontrol = cambioUnidadesLongitud[uycontrol]

        parametrosGrafica = pasoEstandar(Q,n1,n2,S01,S02,b1,b2,m11,m12,m21,m22,y_control,L1,L2,pasos1,pasos2,datum,direccion,uQ,ub1,ub2,um11,uycontrol,uS01,uS02,uL1,uL2,secciones)
        self.FGVPasoEstandarCSV()

    def FGVPasoEstandarCSV (self):
        global parametrosGrafica
        plot_pasos, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_z,plot_H21, plot_Sfi, plot_Sfm, plot_H22,plot_deltaH, plot_x, plot_y, plot_yc, plot_yn = parametrosGrafica
        ruta = self.FGVSolicitarRuta ()
        txt_pasoEstandar(plot_pasos, plot_yi, plot_A, plot_P, plot_R, plot_v, plot_E, plot_z,plot_H21, plot_Sfi, plot_Sfm, plot_H22,plot_deltaH, plot_x, plot_y, plot_yc, plot_yn,ruta)
        self.FGVPasoEstandarGrafica(ruta)

    def FGVPasoEstandarGrafica (self, ruta):
        global parametrosGrafica
        parametrosGrafica = ''
        macroPasoEstandar (ruta)


    def FGVSolicitarRuta (self):
        
        fname = QFileDialog.getExistingDirectory(self, 'Seleccionar una carpeta', '/')

        if fname:
            # Returns pathName with the '/' separators converted to separators that are appropriate for the underlying operating system.
            # On Windows, toNativeSeparators("c:/winnt/system32") returns
            # "c:\winnt\system32".
            fname = QDir.toNativeSeparators(fname)

        return fname



    # ///////////////////////////////////////////////////////////////
    # FLUJO RAPIDAMENTE VARIADO (FGV)



    def FGVRebosaderos (self):
        
        b =  float (widgets.FRVRebosaderoFieldBase.text())
        Cd =  float (widgets.FRVRebosaderoFieldCoeficienteDescarga.text())
        Qmax =  float (widgets.FRVRebosaderoFieldCoeficienteDescarga.text())
        NME =  float (widgets.FRVRebosaderoFieldNME.text())

        ub = widgets.FRVRebosaderoComboBoxBase.currentText()
        ub = cambioUnidadesLongitud[ub]

        uNME = widgets.FRVRebosaderoComboBoxNME.currentText()
        uNME = cambioUnidadesLongitud[uNME]

        uQ = widgets.FRVRebosaderoComboBoxQmax.currentText()
        uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"

        ccvt,r1,r2,x1,x2,y,r12,r22,x12,x22,y2 = Geo (NME,Cd, Qmax,b,ub,uQ,uNME)
        

        widgets.FRVRebosaderoField1r1.setText(str(round(r1, 3)) + " m")
        widgets.FRVRebosaderoField1r2.setText(str(round(r2, 3)) + " m")
        widgets.FRVRebosaderoField1x1.setText(str(round(x1, 3)) + " m")
        widgets.FRVRebosaderoField1x2.setText(str(round(x2, 3)) + " m")
        widgets.FRVRebosaderoField1y.setText(str(round(y, 3)) + " m")

        widgets.FRVRebosaderoField2r1.setText(str(round(r12, 3)) + " m")
        widgets.FRVRebosaderoField2r2.setText(str(round(r22, 3)) + " m")
        widgets.FRVRebosaderoField2x1.setText(str(round(x12, 3)) + " m")
        widgets.FRVRebosaderoField2x2.setText(str(round(x22, 3)) + " m")
        widgets.FRVRebosaderoField2y.setText(str(round(y2, 3)) + " m")        

        widgets.FRVRebosaderoFieldCota.setText(str(round(ccvt, 3)) + " m")        

    def FGVPiscinas (self):
        g =  float (widgets.FRVPiscinaFieldGravedad.text())
        b =  float (widgets.FRVPiscinaFieldBase.text())
        Q =  float (widgets.FRVPiscinaFieldCaudal.text())
        sigma =  float (widgets.FRVPiscinaFieldFactorSeguridad.text())
        yi =  float (widgets.FRVPiscinaFieldYInicial.text())
        yn =  float (widgets.FRVPiscinaFieldYNormal.text())
        perdidas =  float (widgets.FRVPiscinaFieldPerdidas.text())

        ub = widgets.FRVPiscinaComboBoxBase.currentText()
        ub = cambioUnidadesLongitud[ub]

        uQ = widgets.FRVPiscinaComboBoxCaudal.currentText()
        uQ = "L" if uQ == "Litros/segundos" else uQ == "m3"

        uyi = widgets.FRVPiscinaComboBoxYInicial.currentText()
        uyi = cambioUnidadesLongitud[uyi]

        uyn = widgets.FRVPiscinaComboBoxYNormal.currentText()
        uyn = cambioUnidadesLongitud[uyn]

        delta_y, E, y1_temp, y2_temp, delta_y_i_temp, er, v1, Fr1, msg = ciclo_Fr(sigma, yn, yi, Q, b, g, S,uyi,uyi,uQ,ub)

        widgets.FRVPiscinaFieldY.setText(str(round(delta_y, 3)) + " m")
        widgets.FRVPiscinaFieldE0.setText(str(round(E, 3)) + " m")
        widgets.FRVPiscinaFieldY1.setText(str(round(y1_temp, 3)) + " m")
        widgets.FRVPiscinaFieldV1.setText(str(round(v1, 3)) + " m/s")
        widgets.FRVPiscinaFieldFr1.setText(str(round(Fr1, 3)))
        widgets.FRVPiscinaFieldY2.setText(str(round(y2_temp, 3)) + " m")
        widgets.FRVPiscinaFieldYTemp.setText(str(round(delta_y_i_temp, 3)))
        widgets.FRVPiscinaTipoPiscina.setText(msg)


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

   




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())

