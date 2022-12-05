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

from PySide6.QtWidgets import QFileDialog
from application import seleccion

from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

widgets = None

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

        title = "Tratamiento de Aguas Residuales"
        description = "Selección de tecnologías de tratamiento"

        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        # widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)


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

        # Menú principal - Primario
        widgets.botonMenuPrimario.clicked.connect(self.pagPrimarioSeleccionada)
        
        widgets.PrimBtnCalcular.clicked.connect(self.calcularPrimario)
        widgets.PrimBtnReiniciar.clicked.connect(self.reiniciarPrimario)

        # Menú principal - Secundario
        widgets.botonMenuSecundario.clicked.connect(self.pagSecundarioSeleccionada)
        
        widgets.SecuBtnCalcular.clicked.connect(self.calcularSecundario)
        widgets.SecuBtnReiniciar.clicked.connect(self.reiniciarSecundario)

        # Menú principal - Terciario
        widgets.botonMenuTerciario.clicked.connect(self.pagTerciarioSeleccionada)
        
        widgets.TercBtnCalcular.clicked.connect(self.calcularTerciario)
        widgets.TercBtnReiniciar.clicked.connect(self.reiniciarTerciario)

        # Menú principal - Otros
        widgets.botonMenuOtros.clicked.connect(self.pagNoConvencionalesSeleccionada)
        
        widgets.NoCBtnCalcular.clicked.connect(self.calcularNoConvencional)
        widgets.NoCBtnReiniciar.clicked.connect(self.reiniciarNoConvencional)

        # Menú principal - Generalidades
        widgets.botonGeneralidades.clicked.connect(self.pagGeneralidadesSeleccionada)

    
    # ///////////////////////////////////////////////////////////////
    # MENÚ PRINCIPAL

    def pagPrimarioSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_Primario)

    def pagSecundarioSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_Secundario)

    def pagTerciarioSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_Terciario)

    def pagNoConvencionalesSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_NoC)
    
    def pagGeneralidadesSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_generalidades)


    # ///////////////////////////////////////////////////////////////
    # PRIMARIO

    def calcularPrimario (self):
        minCC =  float (widgets.PrimInputMinCapital.text())
        maxCC =  float (widgets.PrimInputMaxCapital.text())

        minOM =  float (widgets.PrimInputMinOM.text())
        maxOM =  float (widgets.PrimInputMaxOM.text())

        rp = widgets.PrimComboBoxRecuperacion.currentText()
        re = widgets.PrimComboBoxEnergia.currentText()
        so = widgets.PrimComboBoxSimplicidad.currentText()
        ro = widgets.PrimComboBoxRobustez.currentText()
        ra = widgets.PrimComboBoxArea.currentText()
        en = widgets.PrimComboBoxSocial.currentText()

        criterio = widgets.PrimComboBoxCriterio.currentText()
        minCriterio =  float (widgets.PrimInputMinCriterio.text())
        maxCriterio =  float (widgets.PrimInputMaxCriterio.text())

        priorizar = widgets.PrimComboBoxPeso.currentText()

        vector = seleccion (minCC, maxCC, minOM, maxOM, rp, re, so, ro, ra, en, criterio, minCriterio, maxCriterio, priorizar)

        widgets.PrimFieldResultadoConvencional.setText(str(round(vector[0], 3)))
        widgets.PrimFieldResultadoTQA.setText(str(round(vector[1], 3)))

        if (vector[1] > vector[0]):
            widgets.PrimFieldResultadoMejor.setText("CEPT")
        else:
            widgets.PrimFieldResultadoMejor.setText("Convencional")



    def reiniciarPrimario(self):
        widgets.PrimInputMinCapital.setText(0)
        widgets.PrimInputMaxCapital.setText(0)

        widgets.PrimComboBoxRecuperacion.setCurrentIndex(0)
        widgets.PrimComboBoxEnergia.setCurrentIndex(0)
        widgets.PrimComboBoxSimplicidad.setCurrentIndex(0)
        widgets.PrimComboBoxRobustez.setCurrentIndex(0)
        widgets.PrimComboBoxArea.setCurrentIndex(0)
        widgets.PrimComboBoxSocial.setCurrentIndex(0)
        widgets.PrimComboBoxCriterio.setCurrentIndex(0)
        widgets.PrimComboBoxPeso.setCurrentIndex(0)

        widgets.PrimInputMinCriterio.setText(0)
        widgets.PrimInputMaxCriterio.setText(0)


        widgets.PrimFieldResultadoConvencional.setText("")
        widgets.PrimFieldResultadoTQA.setText("")
        widgets.PrimFieldResultadoMejor.setText((""))

    # ///////////////////////////////////////////////////////////////
    # SECUNDARIO

    def calcularSecundario (self):
        minCC =  float (widgets.SecuInputMinCapital.text())
        maxCC =  float (widgets.SecuInputMaxCapital.text())

        minOM =  float (widgets.SecuInputMinOM.text())
        maxOM =  float (widgets.SecuInputMaxOM.text())

        rp = widgets.SecuComboBoxRecuperacion.currentText()
        re = widgets.SecuComboBoxEnergia.currentText()
        so = widgets.SecuComboBoxSimplicidad.currentText()
        ro = widgets.SecuComboBoxRobustez.currentText()
        ra = widgets.SecuComboBoxArea.currentText()
        en = widgets.SecuComboBoxSocial.currentText()

        criterio = widgets.SecuComboBoxCriterio.currentText()
        minCriterio =  float (widgets.SecuInputMinCriterio.text())
        maxCriterio =  float (widgets.SecuInputMaxCriterio.text())

        priorizar = widgets.SecuComboBoxPeso.currentText()

        vector = seleccion (minCC, maxCC, minOM, maxOM, rp, re, so, ro, ra, en, criterio, minCriterio, maxCriterio, priorizar)

        widgets.SecuFieldResultadoCAS.setText(str(round(vector[2], 3)))
        widgets.SecuFieldResultadoSBR.setText(str(round(vector[3], 3)))
        widgets.SecuFieldResultadoTF.setText(str(round(vector[4], 3)))
        widgets.SecuFieldResultadoRBC.setText(str(round(vector[5], 3)))

        if (vector[2] > vector[3] and vector[2] > vector[4] and vector[2] > vector[5] ):
            widgets.SecuFieldResultadoMejor.setText("CAS")
        elif (vector[3] > vector[2] and vector[3] > vector[4] and vector[3] > vector[5] ):
            widgets.SecuFieldResultadoMejor.setText("SBR")
        elif (vector[4] > vector[2] and vector[4] > vector[3] and vector[4] > vector[5] ):
            widgets.SecuFieldResultadoMejor.setText("TF")
        elif (vector[5] > vector[2] and vector[5] > vector[4] and vector[5] > vector[3] ):
            widgets.SecuFieldResultadoMejor.setText("RBC")

    def reiniciarSecundario (self):
        widgets.SecuInputMinCapital.setText(0)
        widgets.SecuInputMaxCapital.setText(0)

        widgets.SecuComboBoxRecuperacion.setCurrentIndex(0)
        widgets.SecuComboBoxEnergia.setCurrentIndex(0)
        widgets.SecuComboBoxSimplicidad.setCurrentIndex(0)
        widgets.SecuComboBoxRobustez.setCurrentIndex(0)
        widgets.SecuComboBoxArea.setCurrentIndex(0)
        widgets.SecuComboBoxSocial.setCurrentIndex(0)
        widgets.SecuComboBoxCriterio.setCurrentIndex(0)
        widgets.SecuComboBoxPeso.setCurrentIndex(0)

        widgets.SecuInputMinCriterio.setText(0)
        widgets.SecuInputMaxCriterio.setText(0)

        widgets.SecuFieldResultadoCAS.setText("")
        widgets.SecuFieldResultadoRBC.setText("")
        widgets.SecuFieldResultadoSBR.setText("")
        widgets.SecuFieldResultadoTF.setText("")
        widgets.SecuFieldResultadoMejor.setText((""))


    # ///////////////////////////////////////////////////////////////
    # TERCIARIO
    
    def calcularTerciario (self):
        minCC =  float (widgets.TercInputMinCapital.text())
        maxCC =  float (widgets.TercInputMaxCapital.text())

        minOM =  float (widgets.TercInputMinOM.text())
        maxOM =  float (widgets.TercInputMaxOM.text())

        rp = widgets.TercComboBoxRecuperacion.currentText()
        re = widgets.TercComboBoxEnergia.currentText()
        so = widgets.TercComboBoxSimplicidad.currentText()
        ro = widgets.TercComboBoxRobustez.currentText()
        ra = widgets.TercComboBoxArea.currentText()
        en = widgets.TercComboBoxSocial.currentText()

        criterio = widgets.TercComboBoxCriterio.currentText()
        minCriterio =  float (widgets.TercInputMinCriterio.text())
        maxCriterio =  float (widgets.TercInputMaxCriterio.text())

        priorizar = widgets.TercComboBoxPeso.currentText()

        vector = seleccion (minCC, maxCC, minOM, maxOM, rp, re, so, ro, ra, en, criterio, minCriterio, maxCriterio, priorizar)

        widgets.TercFieldResultadoAO.setText(str(round(vector[10], 3)))
        widgets.TercFieldResultadoBardenpho.setText(str(round(vector[11], 3)))
        widgets.TercFieldResultadoPhoStrip.setText(str(round(vector[12], 3)))

        if (vector[10] > vector[11] and vector[10] > vector[12]):
            widgets.TercFieldResultadoMejor.setText("A/O")
        elif (vector[11] > vector[10] and vector[11] > vector[12]):
            widgets.TercFieldResultadoMejor.setText("PhoStrip")
        elif (vector[12] > vector[11] and vector[12] > vector[10]):
            widgets.TercFieldResultadoMejor.setText("Bardenpho")


        

    def reiniciarTerciario (self):
        widgets.TercInputMinCapital.setText(0)
        widgets.TercInputMaxCapital.setText(0)

        widgets.TercComboBoxRecuperacion.setCurrentIndex(0)
        widgets.TercComboBoxEnergia.setCurrentIndex(0)
        widgets.TercComboBoxSimplicidad.setCurrentIndex(0)
        widgets.TercComboBoxRobustez.setCurrentIndex(0)
        widgets.TercComboBoxArea.setCurrentIndex(0)
        widgets.TercComboBoxSocial.setCurrentIndex(0)
        widgets.TercComboBoxCriterio.setCurrentIndex(0)
        widgets.TercComboBoxPeso.setCurrentIndex(0)

        widgets.TercInputMinCriterio.setText(0)
        widgets.TercInputMaxCriterio.setText(0)

        widgets.TercFieldResultadoAO.setText("")
        widgets.TercFieldResultadoBardenpho.setText("")
        widgets.TercFieldResultadoPhoStrip.setText("")
        widgets.TercFieldResultadoMejor.setText((""))


    # ///////////////////////////////////////////////////////////////
    # No convencionales
    
    def calcularNoConvencional (self):
        minCC =  float (widgets.NoCInputMinCapital.text())
        maxCC =  float (widgets.NoCInputMaxCapital.text())

        minOM =  float (widgets.NoCInputMinOM.text())
        maxOM =  float (widgets.NoCInputMaxOM.text())

        rp = widgets.NoCComboBoxRecuperacion.currentText()
        re = widgets.NoCComboBoxEnergia.currentText()
        so = widgets.NoCComboBoxSimplicidad.currentText()
        ro = widgets.NoCComboBoxRobustez.currentText()
        ra = widgets.NoCComboBoxArea.currentText()
        en = widgets.NoCComboBoxSocial.currentText()

        criterio = widgets.NoCComboBoxCriterio.currentText()
        minCriterio =  float (widgets.NoCInputMinCriterio.text())
        maxCriterio =  float (widgets.NoCInputMaxCriterio.text())

        priorizar = widgets.NoCComboBoxPeso.currentText()

        vector = seleccion (minCC, maxCC, minOM, maxOM, rp, re, so, ro, ra, en, criterio, minCriterio, maxCriterio, priorizar)

        widgets.NoCFieldResultadoUASB.setText(str(round(vector[6], 3)))
        widgets.NoCFieldResultadoMBR.setText(str(round(vector[7], 3)))
        widgets.NoCFieldResultadoLaguna.setText(str(round(vector[8], 3)))
        widgets.NoCFieldResultadoHumedal.setText(str(round(vector[9], 3)))

        if (vector[6] > vector[7] and vector[6] > vector[8] and vector[6] > vector[9] ):
            widgets.NoCFieldResultadoMejor.setText("UASB")
        elif (vector[7] > vector[6] and vector[7] > vector[8] and vector[7] > vector[9] ):
            widgets.NoCFieldResultadoMejor.setText("MBR")
        elif (vector[8] > vector[7] and vector[8] > vector[6] and vector[8] > vector[9] ):
            widgets.NoCFieldResultadoMejor.setText("Laguna")
        elif (vector[9] > vector[7] and vector[9] > vector[8] and vector[9] > vector[6] ):
            widgets.NoCFieldResultadoMejor.setText("Humedal")


    def reiniciarNoConvencional (self):
        widgets.NoCInputMinCapital.setText(0)
        widgets.NoCInputMaxCapital.setText(0)

        widgets.NoCComboBoxRecuperacion.setCurrentIndex(0)
        widgets.NoCComboBoxEnergia.setCurrentIndex(0)
        widgets.NoCComboBoxSimplicidad.setCurrentIndex(0)
        widgets.NoCComboBoxRobustez.setCurrentIndex(0)
        widgets.NoCComboBoxArea.setCurrentIndex(0)
        widgets.NoCComboBoxSocial.setCurrentIndex(0)
        widgets.NoCComboBoxCriterio.setCurrentIndex(0)
        widgets.NoCComboBoxPeso.setCurrentIndex(0)

        widgets.NoCInputMinCriterio.setText(0)
        widgets.NoCInputMaxCriterio.setText(0)

        widgets.NoCFieldResultadoLaguna.setText("")
        widgets.NoCFieldResultadoMBR.setText("")
        widgets.NoCFieldResultadoUASB.setText("")
        widgets.NoCFieldResultadoHumedal.setText("")
        widgets.NoCFieldResultadoMejor.setText((""))

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

