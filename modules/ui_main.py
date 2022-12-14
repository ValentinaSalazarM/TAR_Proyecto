# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainVLbnuM.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1244, 813)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setEnabled(True)
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"border-image: url(:/images/images/images/wave.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_new)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setFont(font)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setMaximumSize(QSize(1350, 610))
        self.stackedWidget.setBaseSize(QSize(50, 50))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setLineWidth(-2)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/LogoHome.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.menu_principal = QWidget()
        self.menu_principal.setObjectName(u"menu_principal")
        self.menu_principal.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.menu_principal)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame = QFrame(self.menu_principal)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.botonGeneralidades = QPushButton(self.frame)
        self.botonGeneralidades.setObjectName(u"botonGeneralidades")
        self.botonGeneralidades.setGeometry(QRect(460, 40, 241, 61))
        self.botonGeneralidades.setStyleSheet(u"font: 500 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(105, 183, 255);\n"
"background-color: rgb(105, 183, 255);")
        self.botonGeneralidades_2 = QPushButton(self.frame)
        self.botonGeneralidades_2.setObjectName(u"botonGeneralidades_2")
        self.botonGeneralidades_2.setGeometry(QRect(10, 260, 1111, 311))
        self.botonGeneralidades_2.setStyleSheet(u"background-image: url(:/images/images/images/Wastewater treatment.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"border-color: transparent")
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 120, 967, 111))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.botonMenuPrimario = QPushButton(self.layoutWidget)
        self.botonMenuPrimario.setObjectName(u"botonMenuPrimario")
        self.botonMenuPrimario.setMinimumSize(QSize(230, 50))
        self.botonMenuPrimario.setMaximumSize(QSize(230, 100))
        self.botonMenuPrimario.setStyleSheet(u"font: 500 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(250, 148, 150);\n"
"background-color: rgb(250, 148, 150);")

        self.horizontalLayout_10.addWidget(self.botonMenuPrimario)

        self.botonMenuSecundario = QPushButton(self.layoutWidget)
        self.botonMenuSecundario.setObjectName(u"botonMenuSecundario")
        self.botonMenuSecundario.setMinimumSize(QSize(230, 0))
        self.botonMenuSecundario.setMaximumSize(QSize(230, 100))
        self.botonMenuSecundario.setStyleSheet(u"font: 500 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(250, 190, 167);\n"
"background-color: rgb(250, 190, 167);")

        self.horizontalLayout_10.addWidget(self.botonMenuSecundario)

        self.botonMenuTerciario = QPushButton(self.layoutWidget)
        self.botonMenuTerciario.setObjectName(u"botonMenuTerciario")
        self.botonMenuTerciario.setMinimumSize(QSize(230, 0))
        self.botonMenuTerciario.setMaximumSize(QSize(230, 100))
        self.botonMenuTerciario.setStyleSheet(u"font: 500 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(244, 229, 145);\n"
"background-color: rgb(244, 229, 145);")

        self.horizontalLayout_10.addWidget(self.botonMenuTerciario)

        self.botonMenuOtros = QPushButton(self.layoutWidget)
        self.botonMenuOtros.setObjectName(u"botonMenuOtros")
        self.botonMenuOtros.setMinimumSize(QSize(230, 0))
        self.botonMenuOtros.setMaximumSize(QSize(230, 100))
        self.botonMenuOtros.setStyleSheet(u"font: 500 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(118, 199, 158);\n"
"background-color: rgb(118, 199, 158);")

        self.horizontalLayout_10.addWidget(self.botonMenuOtros)


        self.verticalLayout_20.addWidget(self.frame)

        self.stackedWidget.addWidget(self.menu_principal)
        self.pagina_Primario = QWidget()
        self.pagina_Primario.setObjectName(u"pagina_Primario")
        self.tabPrim = QTabWidget(self.pagina_Primario)
        self.tabPrim.setObjectName(u"tabPrim")
        self.tabPrim.setGeometry(QRect(0, 0, 1131, 613))
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabPrim.sizePolicy().hasHeightForWidth())
        self.tabPrim.setSizePolicy(sizePolicy4)
        self.tabPrim.setStyleSheet(u"font: 500 10pt \"Allerta\";\n"
"color: rgb(79, 79, 79);")
        self.tabPrim.setTabPosition(QTabWidget.West)
        self.primarioEntrada = QWidget()
        self.primarioEntrada.setObjectName(u"primarioEntrada")
        self.primarioEntrada.setStyleSheet(u"\n"
"font: 500 11pt \"Allerta\";")
        self.groupBox_Resultados_19 = QGroupBox(self.primarioEntrada)
        self.groupBox_Resultados_19.setObjectName(u"groupBox_Resultados_19")
        self.groupBox_Resultados_19.setGeometry(QRect(739, 10, 341, 281))
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_Resultados_19.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_19.setSizePolicy(sizePolicy5)
        self.groupBox_Resultados_19.setMinimumSize(QSize(300, 0))
        self.groupBox_Resultados_19.setMaximumSize(QSize(450, 16777215))
        self.groupBox_Resultados_19.setStyleSheet(u"QGroupBox {\n"
"color: rgb(190, 190, 190);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(190, 190, 190);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.gridLayout_83 = QGridLayout(self.groupBox_Resultados_19)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.row_40 = QFrame(self.groupBox_Resultados_19)
        self.row_40.setObjectName(u"row_40")
        self.row_40.setStyleSheet(u"")
        self.row_40.setFrameShape(QFrame.StyledPanel)
        self.row_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.row_40)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_88 = QGridLayout()
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.gridLayout_88.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_88.setHorizontalSpacing(10)
        self.gridLayout_88.setVerticalSpacing(15)
        self.gridLayout_88.setContentsMargins(10, 10, 10, 10)
        self.PrimComboBoxCriterio = QComboBox(self.row_40)
        self.PrimComboBoxCriterio.addItem("")
        self.PrimComboBoxCriterio.addItem("")
        self.PrimComboBoxCriterio.addItem("")
        self.PrimComboBoxCriterio.addItem("")
        self.PrimComboBoxCriterio.addItem("")
        self.PrimComboBoxCriterio.setObjectName(u"PrimComboBoxCriterio")
        self.PrimComboBoxCriterio.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.PrimComboBoxCriterio.sizePolicy().hasHeightForWidth())
        self.PrimComboBoxCriterio.setSizePolicy(sizePolicy4)
        self.PrimComboBoxCriterio.setMinimumSize(QSize(170, 35))
        self.PrimComboBoxCriterio.setMaximumSize(QSize(170, 30))
        self.PrimComboBoxCriterio.setLayoutDirection(Qt.LeftToRight)
        self.PrimComboBoxCriterio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.PrimComboBoxCriterio.setEditable(False)
        self.PrimComboBoxCriterio.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.PrimComboBoxCriterio.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_88.addWidget(self.PrimComboBoxCriterio, 1, 1, 1, 1)

        self.PrimInputMinCriterio = QLineEdit(self.row_40)
        self.PrimInputMinCriterio.setObjectName(u"PrimInputMinCriterio")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.PrimInputMinCriterio.sizePolicy().hasHeightForWidth())
        self.PrimInputMinCriterio.setSizePolicy(sizePolicy6)
        self.PrimInputMinCriterio.setMinimumSize(QSize(170, 35))
        self.PrimInputMinCriterio.setMaximumSize(QSize(100, 16777215))
        self.PrimInputMinCriterio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_88.addWidget(self.PrimInputMinCriterio, 2, 1, 1, 1)

        self.PrimInputMaxCriterio = QLineEdit(self.row_40)
        self.PrimInputMaxCriterio.setObjectName(u"PrimInputMaxCriterio")
        sizePolicy6.setHeightForWidth(self.PrimInputMaxCriterio.sizePolicy().hasHeightForWidth())
        self.PrimInputMaxCriterio.setSizePolicy(sizePolicy6)
        self.PrimInputMaxCriterio.setMinimumSize(QSize(170, 35))
        self.PrimInputMaxCriterio.setMaximumSize(QSize(100, 16777215))
        self.PrimInputMaxCriterio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_88.addWidget(self.PrimInputMaxCriterio, 3, 1, 1, 1)

        self.PrimLabelMinCriteiro = QLabel(self.row_40)
        self.PrimLabelMinCriteiro.setObjectName(u"PrimLabelMinCriteiro")
        sizePolicy6.setHeightForWidth(self.PrimLabelMinCriteiro.sizePolicy().hasHeightForWidth())
        self.PrimLabelMinCriteiro.setSizePolicy(sizePolicy6)
        self.PrimLabelMinCriteiro.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.PrimLabelMinCriteiro.setAlignment(Qt.AlignCenter)

        self.gridLayout_88.addWidget(self.PrimLabelMinCriteiro, 2, 0, 1, 1)

        self.PrimLabelMaxCriterio = QLabel(self.row_40)
        self.PrimLabelMaxCriterio.setObjectName(u"PrimLabelMaxCriterio")
        sizePolicy6.setHeightForWidth(self.PrimLabelMaxCriterio.sizePolicy().hasHeightForWidth())
        self.PrimLabelMaxCriterio.setSizePolicy(sizePolicy6)
        self.PrimLabelMaxCriterio.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.PrimLabelMaxCriterio.setAlignment(Qt.AlignCenter)

        self.gridLayout_88.addWidget(self.PrimLabelMaxCriterio, 3, 0, 1, 1)

        self.PrimLabelCriterio = QLabel(self.row_40)
        self.PrimLabelCriterio.setObjectName(u"PrimLabelCriterio")
        sizePolicy6.setHeightForWidth(self.PrimLabelCriterio.sizePolicy().hasHeightForWidth())
        self.PrimLabelCriterio.setSizePolicy(sizePolicy6)
        self.PrimLabelCriterio.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.PrimLabelCriterio.setAlignment(Qt.AlignCenter)

        self.gridLayout_88.addWidget(self.PrimLabelCriterio, 1, 0, 1, 1)


        self.verticalLayout_60.addLayout(self.gridLayout_88)


        self.gridLayout_83.addWidget(self.row_40, 0, 0, 1, 1)

        self.PrimInputParametro_3 = QLineEdit(self.primarioEntrada)
        self.PrimInputParametro_3.setObjectName(u"PrimInputParametro_3")
        self.PrimInputParametro_3.setGeometry(QRect(780, 350, 265, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_3.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_3.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_3.setMinimumSize(QSize(265, 2))
        self.PrimInputParametro_3.setMaximumSize(QSize(250, 2))
        self.PrimInputParametro_3.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.PrimInputParametro_4 = QLineEdit(self.primarioEntrada)
        self.PrimInputParametro_4.setObjectName(u"PrimInputParametro_4")
        self.PrimInputParametro_4.setGeometry(QRect(780, 460, 265, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_4.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_4.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_4.setMinimumSize(QSize(265, 2))
        self.PrimInputParametro_4.setMaximumSize(QSize(250, 2))
        self.PrimInputParametro_4.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.layoutWidget1 = QWidget(self.primarioEntrada)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 10, 692, 603))
        self.verticalLayout_30 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_30.setSpacing(6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.groupBox_Propiedades_21 = QGroupBox(self.layoutWidget1)
        self.groupBox_Propiedades_21.setObjectName(u"groupBox_Propiedades_21")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_21.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_21.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_21.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_21.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_21.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 148, 150);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(250, 148, 150);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_21.setAlignment(Qt.AlignCenter)
        self.gridLayout_93 = QGridLayout(self.groupBox_Propiedades_21)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.row_45 = QFrame(self.groupBox_Propiedades_21)
        self.row_45.setObjectName(u"row_45")
        self.row_45.setStyleSheet(u"")
        self.row_45.setFrameShape(QFrame.StyledPanel)
        self.row_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.row_45)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_98 = QGridLayout()
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.gridLayout_98.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_98.setHorizontalSpacing(35)
        self.gridLayout_98.setVerticalSpacing(10)
        self.gridLayout_98.setContentsMargins(20, 10, 20, 10)
        self.PrimInputMinCapital = QLineEdit(self.row_45)
        self.PrimInputMinCapital.setObjectName(u"PrimInputMinCapital")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.PrimInputMinCapital.sizePolicy().hasHeightForWidth())
        self.PrimInputMinCapital.setSizePolicy(sizePolicy7)
        self.PrimInputMinCapital.setMinimumSize(QSize(110, 30))
        self.PrimInputMinCapital.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.PrimInputMinCapital.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.PrimInputMinCapital.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_98.addWidget(self.PrimInputMinCapital, 0, 1, 1, 1)

        self.PrimLabelCostoOM = QLabel(self.row_45)
        self.PrimLabelCostoOM.setObjectName(u"PrimLabelCostoOM")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.PrimLabelCostoOM.sizePolicy().hasHeightForWidth())
        self.PrimLabelCostoOM.setSizePolicy(sizePolicy8)
        self.PrimLabelCostoOM.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelCostoOM.setLineWidth(1)
        self.PrimLabelCostoOM.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_98.addWidget(self.PrimLabelCostoOM, 1, 0, 1, 1)

        self.PrimLabelCostoCapital = QLabel(self.row_45)
        self.PrimLabelCostoCapital.setObjectName(u"PrimLabelCostoCapital")
        sizePolicy8.setHeightForWidth(self.PrimLabelCostoCapital.sizePolicy().hasHeightForWidth())
        self.PrimLabelCostoCapital.setSizePolicy(sizePolicy8)
        self.PrimLabelCostoCapital.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelCostoCapital.setLineWidth(1)
        self.PrimLabelCostoCapital.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_98.addWidget(self.PrimLabelCostoCapital, 0, 0, 1, 1)

        self.PrimInputMinOM = QLineEdit(self.row_45)
        self.PrimInputMinOM.setObjectName(u"PrimInputMinOM")
        sizePolicy7.setHeightForWidth(self.PrimInputMinOM.sizePolicy().hasHeightForWidth())
        self.PrimInputMinOM.setSizePolicy(sizePolicy7)
        self.PrimInputMinOM.setMinimumSize(QSize(110, 30))
        self.PrimInputMinOM.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.PrimInputMinOM.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.PrimInputMinOM.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_98.addWidget(self.PrimInputMinOM, 1, 1, 1, 1)

        self.PrimInputMaxCapital = QLineEdit(self.row_45)
        self.PrimInputMaxCapital.setObjectName(u"PrimInputMaxCapital")
        sizePolicy7.setHeightForWidth(self.PrimInputMaxCapital.sizePolicy().hasHeightForWidth())
        self.PrimInputMaxCapital.setSizePolicy(sizePolicy7)
        self.PrimInputMaxCapital.setMinimumSize(QSize(110, 30))
        self.PrimInputMaxCapital.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.PrimInputMaxCapital.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.PrimInputMaxCapital.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_98.addWidget(self.PrimInputMaxCapital, 0, 2, 1, 1)

        self.PrimInputMaxOM = QLineEdit(self.row_45)
        self.PrimInputMaxOM.setObjectName(u"PrimInputMaxOM")
        sizePolicy7.setHeightForWidth(self.PrimInputMaxOM.sizePolicy().hasHeightForWidth())
        self.PrimInputMaxOM.setSizePolicy(sizePolicy7)
        self.PrimInputMaxOM.setMinimumSize(QSize(110, 30))
        self.PrimInputMaxOM.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.PrimInputMaxOM.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.PrimInputMaxOM.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_98.addWidget(self.PrimInputMaxOM, 1, 2, 1, 1)


        self.verticalLayout_65.addLayout(self.gridLayout_98)


        self.gridLayout_93.addWidget(self.row_45, 0, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.groupBox_Propiedades_21)

        self.groupBox_Propiedades_23 = QGroupBox(self.layoutWidget1)
        self.groupBox_Propiedades_23.setObjectName(u"groupBox_Propiedades_23")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_23.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_23.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_23.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_23.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_23.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 148, 150);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(250, 148, 150);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_23.setAlignment(Qt.AlignCenter)
        self.gridLayout_99 = QGridLayout(self.groupBox_Propiedades_23)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.row_48 = QFrame(self.groupBox_Propiedades_23)
        self.row_48.setObjectName(u"row_48")
        self.row_48.setStyleSheet(u"")
        self.row_48.setFrameShape(QFrame.StyledPanel)
        self.row_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.row_48)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_100 = QGridLayout()
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.gridLayout_100.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_100.setHorizontalSpacing(35)
        self.gridLayout_100.setVerticalSpacing(10)
        self.gridLayout_100.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelEnergia = QLabel(self.row_48)
        self.PrimLabelEnergia.setObjectName(u"PrimLabelEnergia")
        sizePolicy8.setHeightForWidth(self.PrimLabelEnergia.sizePolicy().hasHeightForWidth())
        self.PrimLabelEnergia.setSizePolicy(sizePolicy8)
        self.PrimLabelEnergia.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelEnergia.setLineWidth(1)
        self.PrimLabelEnergia.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_100.addWidget(self.PrimLabelEnergia, 1, 0, 1, 1)

        self.PrimLabelRecuperacion = QLabel(self.row_48)
        self.PrimLabelRecuperacion.setObjectName(u"PrimLabelRecuperacion")
        sizePolicy8.setHeightForWidth(self.PrimLabelRecuperacion.sizePolicy().hasHeightForWidth())
        self.PrimLabelRecuperacion.setSizePolicy(sizePolicy8)
        self.PrimLabelRecuperacion.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelRecuperacion.setLineWidth(1)
        self.PrimLabelRecuperacion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_100.addWidget(self.PrimLabelRecuperacion, 0, 0, 1, 1)

        self.PrimComboBoxRecuperacion = QComboBox(self.row_48)
        self.PrimComboBoxRecuperacion.addItem("")
        self.PrimComboBoxRecuperacion.addItem("")
        self.PrimComboBoxRecuperacion.addItem("")
        self.PrimComboBoxRecuperacion.addItem("")
        self.PrimComboBoxRecuperacion.addItem("")
        self.PrimComboBoxRecuperacion.setObjectName(u"PrimComboBoxRecuperacion")
        self.PrimComboBoxRecuperacion.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.PrimComboBoxRecuperacion.sizePolicy().hasHeightForWidth())
        self.PrimComboBoxRecuperacion.setSizePolicy(sizePolicy4)
        self.PrimComboBoxRecuperacion.setMinimumSize(QSize(200, 35))
        self.PrimComboBoxRecuperacion.setMaximumSize(QSize(150, 30))
        self.PrimComboBoxRecuperacion.setLayoutDirection(Qt.LeftToRight)
        self.PrimComboBoxRecuperacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.PrimComboBoxRecuperacion.setEditable(False)
        self.PrimComboBoxRecuperacion.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.PrimComboBoxRecuperacion.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_100.addWidget(self.PrimComboBoxRecuperacion, 0, 1, 1, 1)

        self.PrimComboBoxEnergia = QComboBox(self.row_48)
        self.PrimComboBoxEnergia.addItem("")
        self.PrimComboBoxEnergia.addItem("")
        self.PrimComboBoxEnergia.addItem("")
        self.PrimComboBoxEnergia.addItem("")
        self.PrimComboBoxEnergia.addItem("")
        self.PrimComboBoxEnergia.setObjectName(u"PrimComboBoxEnergia")
        self.PrimComboBoxEnergia.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.PrimComboBoxEnergia.sizePolicy().hasHeightForWidth())
        self.PrimComboBoxEnergia.setSizePolicy(sizePolicy4)
        self.PrimComboBoxEnergia.setMinimumSize(QSize(200, 35))
        self.PrimComboBoxEnergia.setMaximumSize(QSize(150, 30))
        self.PrimComboBoxEnergia.setLayoutDirection(Qt.LeftToRight)
        self.PrimComboBoxEnergia.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.PrimComboBoxEnergia.setEditable(False)
        self.PrimComboBoxEnergia.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.PrimComboBoxEnergia.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_100.addWidget(self.PrimComboBoxEnergia, 1, 1, 1, 1)


        self.verticalLayout_68.addLayout(self.gridLayout_100)


        self.gridLayout_99.addWidget(self.row_48, 0, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.groupBox_Propiedades_23)

        self.groupBox_Propiedades_24 = QGroupBox(self.layoutWidget1)
        self.groupBox_Propiedades_24.setObjectName(u"groupBox_Propiedades_24")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_24.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_24.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_24.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_24.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_24.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 148, 150);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(250, 148, 150);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_24.setAlignment(Qt.AlignCenter)
        self.gridLayout_101 = QGridLayout(self.groupBox_Propiedades_24)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.row_49 = QFrame(self.groupBox_Propiedades_24)
        self.row_49.setObjectName(u"row_49")
        self.row_49.setStyleSheet(u"")
        self.row_49.setFrameShape(QFrame.StyledPanel)
        self.row_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.row_49)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_102 = QGridLayout()
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.gridLayout_102.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_102.setHorizontalSpacing(35)
        self.gridLayout_102.setVerticalSpacing(10)
        self.gridLayout_102.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelRobustez = QLabel(self.row_49)
        self.PrimLabelRobustez.setObjectName(u"PrimLabelRobustez")
        sizePolicy8.setHeightForWidth(self.PrimLabelRobustez.sizePolicy().hasHeightForWidth())
        self.PrimLabelRobustez.setSizePolicy(sizePolicy8)
        self.PrimLabelRobustez.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelRobustez.setLineWidth(1)
        self.PrimLabelRobustez.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_102.addWidget(self.PrimLabelRobustez, 1, 0, 1, 1)

        self.PrimLabelSimplicidad = QLabel(self.row_49)
        self.PrimLabelSimplicidad.setObjectName(u"PrimLabelSimplicidad")
        sizePolicy8.setHeightForWidth(self.PrimLabelSimplicidad.sizePolicy().hasHeightForWidth())
        self.PrimLabelSimplicidad.setSizePolicy(sizePolicy8)
        self.PrimLabelSimplicidad.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelSimplicidad.setLineWidth(1)
        self.PrimLabelSimplicidad.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_102.addWidget(self.PrimLabelSimplicidad, 0, 0, 1, 1)

        self.PrimComboBoxSimplicidad = QComboBox(self.row_49)
        self.PrimComboBoxSimplicidad.addItem("")
        self.PrimComboBoxSimplicidad.addItem("")
        self.PrimComboBoxSimplicidad.addItem("")
        self.PrimComboBoxSimplicidad.addItem("")
        self.PrimComboBoxSimplicidad.addItem("")
        self.PrimComboBoxSimplicidad.setObjectName(u"PrimComboBoxSimplicidad")
        self.PrimComboBoxSimplicidad.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.PrimComboBoxSimplicidad.sizePolicy().hasHeightForWidth())
        self.PrimComboBoxSimplicidad.setSizePolicy(sizePolicy4)
        self.PrimComboBoxSimplicidad.setMinimumSize(QSize(200, 35))
        self.PrimComboBoxSimplicidad.setMaximumSize(QSize(150, 30))
        self.PrimComboBoxSimplicidad.setLayoutDirection(Qt.LeftToRight)
        self.PrimComboBoxSimplicidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.PrimComboBoxSimplicidad.setEditable(False)
        self.PrimComboBoxSimplicidad.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.PrimComboBoxSimplicidad.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_102.addWidget(self.PrimComboBoxSimplicidad, 0, 1, 1, 1)

        self.PrimComboBoxRobustez = QComboBox(self.row_49)
        self.PrimComboBoxRobustez.addItem("")
        self.PrimComboBoxRobustez.addItem("")
        self.PrimComboBoxRobustez.addItem("")
        self.PrimComboBoxRobustez.addItem("")
        self.PrimComboBoxRobustez.addItem("")
        self.PrimComboBoxRobustez.setObjectName(u"PrimComboBoxRobustez")
        self.PrimComboBoxRobustez.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.PrimComboBoxRobustez.sizePolicy().hasHeightForWidth())
        self.PrimComboBoxRobustez.setSizePolicy(sizePolicy4)
        self.PrimComboBoxRobustez.setMinimumSize(QSize(200, 35))
        self.PrimComboBoxRobustez.setMaximumSize(QSize(150, 30))
        self.PrimComboBoxRobustez.setLayoutDirection(Qt.LeftToRight)
        self.PrimComboBoxRobustez.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.PrimComboBoxRobustez.setEditable(False)
        self.PrimComboBoxRobustez.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.PrimComboBoxRobustez.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_102.addWidget(self.PrimComboBoxRobustez, 1, 1, 1, 1)

        self.PrimLabelArea = QLabel(self.row_49)
        self.PrimLabelArea.setObjectName(u"PrimLabelArea")
        sizePolicy8.setHeightForWidth(self.PrimLabelArea.sizePolicy().hasHeightForWidth())
        self.PrimLabelArea.setSizePolicy(sizePolicy8)
        self.PrimLabelArea.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelArea.setLineWidth(1)
        self.PrimLabelArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_102.addWidget(self.PrimLabelArea, 2, 0, 1, 1)

        self.PrimComboBoxArea = QComboBox(self.row_49)
        self.PrimComboBoxArea.addItem("")
        self.PrimComboBoxArea.addItem("")
        self.PrimComboBoxArea.addItem("")
        self.PrimComboBoxArea.addItem("")
        self.PrimComboBoxArea.addItem("")
        self.PrimComboBoxArea.setObjectName(u"PrimComboBoxArea")
        self.PrimComboBoxArea.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.PrimComboBoxArea.sizePolicy().hasHeightForWidth())
        self.PrimComboBoxArea.setSizePolicy(sizePolicy4)
        self.PrimComboBoxArea.setMinimumSize(QSize(200, 35))
        self.PrimComboBoxArea.setMaximumSize(QSize(150, 30))
        self.PrimComboBoxArea.setLayoutDirection(Qt.LeftToRight)
        self.PrimComboBoxArea.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.PrimComboBoxArea.setEditable(False)
        self.PrimComboBoxArea.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.PrimComboBoxArea.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_102.addWidget(self.PrimComboBoxArea, 2, 1, 1, 1)


        self.verticalLayout_69.addLayout(self.gridLayout_102)


        self.gridLayout_101.addWidget(self.row_49, 0, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.groupBox_Propiedades_24)

        self.groupBox_Propiedades_25 = QGroupBox(self.layoutWidget1)
        self.groupBox_Propiedades_25.setObjectName(u"groupBox_Propiedades_25")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_25.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_25.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_25.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_25.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_25.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 148, 150);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(250, 148, 150);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_25.setAlignment(Qt.AlignCenter)
        self.gridLayout_103 = QGridLayout(self.groupBox_Propiedades_25)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.row_50 = QFrame(self.groupBox_Propiedades_25)
        self.row_50.setObjectName(u"row_50")
        self.row_50.setStyleSheet(u"")
        self.row_50.setFrameShape(QFrame.StyledPanel)
        self.row_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.row_50)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_104 = QGridLayout()
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.gridLayout_104.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_104.setHorizontalSpacing(35)
        self.gridLayout_104.setVerticalSpacing(10)
        self.gridLayout_104.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelSocial = QLabel(self.row_50)
        self.PrimLabelSocial.setObjectName(u"PrimLabelSocial")
        sizePolicy8.setHeightForWidth(self.PrimLabelSocial.sizePolicy().hasHeightForWidth())
        self.PrimLabelSocial.setSizePolicy(sizePolicy8)
        self.PrimLabelSocial.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelSocial.setLineWidth(1)
        self.PrimLabelSocial.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_104.addWidget(self.PrimLabelSocial, 0, 0, 1, 1)

        self.PrimComboBoxSocial = QComboBox(self.row_50)
        self.PrimComboBoxSocial.addItem("")
        self.PrimComboBoxSocial.addItem("")
        self.PrimComboBoxSocial.addItem("")
        self.PrimComboBoxSocial.addItem("")
        self.PrimComboBoxSocial.addItem("")
        self.PrimComboBoxSocial.setObjectName(u"PrimComboBoxSocial")
        self.PrimComboBoxSocial.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.PrimComboBoxSocial.sizePolicy().hasHeightForWidth())
        self.PrimComboBoxSocial.setSizePolicy(sizePolicy4)
        self.PrimComboBoxSocial.setMinimumSize(QSize(200, 35))
        self.PrimComboBoxSocial.setMaximumSize(QSize(150, 30))
        self.PrimComboBoxSocial.setLayoutDirection(Qt.LeftToRight)
        self.PrimComboBoxSocial.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.PrimComboBoxSocial.setEditable(False)
        self.PrimComboBoxSocial.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.PrimComboBoxSocial.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_104.addWidget(self.PrimComboBoxSocial, 0, 1, 1, 1)


        self.verticalLayout_70.addLayout(self.gridLayout_104)


        self.gridLayout_103.addWidget(self.row_50, 0, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.groupBox_Propiedades_25)

        self.PrimLabelMaxCriterio_2 = QLabel(self.primarioEntrada)
        self.PrimLabelMaxCriterio_2.setObjectName(u"PrimLabelMaxCriterio_2")
        self.PrimLabelMaxCriterio_2.setGeometry(QRect(780, 360, 265, 21))
        sizePolicy6.setHeightForWidth(self.PrimLabelMaxCriterio_2.sizePolicy().hasHeightForWidth())
        self.PrimLabelMaxCriterio_2.setSizePolicy(sizePolicy6)
        self.PrimLabelMaxCriterio_2.setMinimumSize(QSize(265, 0))
        self.PrimLabelMaxCriterio_2.setMaximumSize(QSize(265, 16777215))
        self.PrimLabelMaxCriterio_2.setStyleSheet(u"font: 600 12pt \"Allerta\";\n"
"background-color: rgb(250, 148, 150);\n"
"color: rgb(255, 255, 255);")
        self.PrimLabelMaxCriterio_2.setTextFormat(Qt.AutoText)
        self.PrimLabelMaxCriterio_2.setAlignment(Qt.AlignCenter)
        self.PrimComboBoxPeso = QComboBox(self.primarioEntrada)
        self.PrimComboBoxPeso.addItem("")
        self.PrimComboBoxPeso.addItem("")
        self.PrimComboBoxPeso.addItem("")
        self.PrimComboBoxPeso.addItem("")
        self.PrimComboBoxPeso.addItem("")
        self.PrimComboBoxPeso.setObjectName(u"PrimComboBoxPeso")
        self.PrimComboBoxPeso.setEnabled(True)
        self.PrimComboBoxPeso.setGeometry(QRect(810, 400, 200, 35))
        sizePolicy4.setHeightForWidth(self.PrimComboBoxPeso.sizePolicy().hasHeightForWidth())
        self.PrimComboBoxPeso.setSizePolicy(sizePolicy4)
        self.PrimComboBoxPeso.setMinimumSize(QSize(200, 35))
        self.PrimComboBoxPeso.setMaximumSize(QSize(150, 30))
        self.PrimComboBoxPeso.setLayoutDirection(Qt.LeftToRight)
        self.PrimComboBoxPeso.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.PrimComboBoxPeso.setEditable(False)
        self.PrimComboBoxPeso.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.PrimComboBoxPeso.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.tabPrim.addTab(self.primarioEntrada, "")
        self.primarioSalida = QWidget()
        self.primarioSalida.setObjectName(u"primarioSalida")
        self.primarioSalida.setStyleSheet(u"font: 500 11pt \"Allerta\";")
        self.groupBox_Propiedades_22 = QGroupBox(self.primarioSalida)
        self.groupBox_Propiedades_22.setObjectName(u"groupBox_Propiedades_22")
        self.groupBox_Propiedades_22.setGeometry(QRect(20, 150, 770, 201))
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_22.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_22.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_22.setMinimumSize(QSize(770, 0))
        self.groupBox_Propiedades_22.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_22.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 148, 150);\n"
"font: bold; \n"
"border: 2px solid;\n"
"font: 700 11pt \"Allerta\";\n"
"border-color: rgb(250, 148, 150);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_22.setAlignment(Qt.AlignCenter)
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_Propiedades_22)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.row_51 = QFrame(self.groupBox_Propiedades_22)
        self.row_51.setObjectName(u"row_51")
        self.row_51.setStyleSheet(u"")
        self.row_51.setFrameShape(QFrame.StyledPanel)
        self.row_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.row_51)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_106 = QGridLayout()
        self.gridLayout_106.setObjectName(u"gridLayout_106")
        self.gridLayout_106.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_106.setHorizontalSpacing(35)
        self.gridLayout_106.setVerticalSpacing(30)
        self.gridLayout_106.setContentsMargins(20, 5, 20, 5)
        self.PrimFieldResultadoConvencional = QLineEdit(self.row_51)
        self.PrimFieldResultadoConvencional.setObjectName(u"PrimFieldResultadoConvencional")
        self.PrimFieldResultadoConvencional.setEnabled(False)
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.PrimFieldResultadoConvencional.sizePolicy().hasHeightForWidth())
        self.PrimFieldResultadoConvencional.setSizePolicy(sizePolicy9)
        self.PrimFieldResultadoConvencional.setMinimumSize(QSize(110, 35))
        self.PrimFieldResultadoConvencional.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.PrimFieldResultadoConvencional.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.PrimFieldResultadoConvencional.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.PrimFieldResultadoConvencional.setAlignment(Qt.AlignCenter)

        self.gridLayout_106.addWidget(self.PrimFieldResultadoConvencional, 0, 1, 1, 1)

        self.PrimLabelConvencional = QLabel(self.row_51)
        self.PrimLabelConvencional.setObjectName(u"PrimLabelConvencional")
        sizePolicy8.setHeightForWidth(self.PrimLabelConvencional.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional.setSizePolicy(sizePolicy8)
        self.PrimLabelConvencional.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelConvencional.setLineWidth(1)
        self.PrimLabelConvencional.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_106.addWidget(self.PrimLabelConvencional, 0, 0, 1, 1)

        self.PrimFieldResultadoTQA = QLineEdit(self.row_51)
        self.PrimFieldResultadoTQA.setObjectName(u"PrimFieldResultadoTQA")
        self.PrimFieldResultadoTQA.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.PrimFieldResultadoTQA.sizePolicy().hasHeightForWidth())
        self.PrimFieldResultadoTQA.setSizePolicy(sizePolicy9)
        self.PrimFieldResultadoTQA.setMinimumSize(QSize(110, 35))
        self.PrimFieldResultadoTQA.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.PrimFieldResultadoTQA.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.PrimFieldResultadoTQA.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.PrimFieldResultadoTQA.setAlignment(Qt.AlignCenter)

        self.gridLayout_106.addWidget(self.PrimFieldResultadoTQA, 1, 1, 1, 1)

        self.PrimLabelTQA = QLabel(self.row_51)
        self.PrimLabelTQA.setObjectName(u"PrimLabelTQA")
        sizePolicy8.setHeightForWidth(self.PrimLabelTQA.sizePolicy().hasHeightForWidth())
        self.PrimLabelTQA.setSizePolicy(sizePolicy8)
        self.PrimLabelTQA.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelTQA.setLineWidth(1)
        self.PrimLabelTQA.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_106.addWidget(self.PrimLabelTQA, 1, 0, 1, 1)


        self.verticalLayout_71.addLayout(self.gridLayout_106)


        self.verticalLayout_22.addWidget(self.row_51)

        self.PrimBtnCalcular = QPushButton(self.primarioSalida)
        self.PrimBtnCalcular.setObjectName(u"PrimBtnCalcular")
        self.PrimBtnCalcular.setEnabled(True)
        self.PrimBtnCalcular.setGeometry(QRect(810, 160, 250, 50))
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.PrimBtnCalcular.sizePolicy().hasHeightForWidth())
        self.PrimBtnCalcular.setSizePolicy(sizePolicy10)
        self.PrimBtnCalcular.setMinimumSize(QSize(250, 50))
        self.PrimBtnCalcular.setMaximumSize(QSize(40, 40))
        self.PrimBtnCalcular.setStyleSheet(u"background-color: rgb(163, 160, 159);\n"
"border-width: 5px;\n"
"border-color: rgb(163, 160, 159);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Allerta\";\n"
"\n"
"")
        self.PrimBtnCalcular.setCheckable(False)
        self.PrimBtnCalcular.setChecked(False)
        self.PrimBtnCalcular.setAutoDefault(False)
        self.PrimBtnReiniciar = QPushButton(self.primarioSalida)
        self.PrimBtnReiniciar.setObjectName(u"PrimBtnReiniciar")
        self.PrimBtnReiniciar.setEnabled(True)
        self.PrimBtnReiniciar.setGeometry(QRect(810, 220, 250, 50))
        sizePolicy10.setHeightForWidth(self.PrimBtnReiniciar.sizePolicy().hasHeightForWidth())
        self.PrimBtnReiniciar.setSizePolicy(sizePolicy10)
        self.PrimBtnReiniciar.setMinimumSize(QSize(250, 50))
        self.PrimBtnReiniciar.setMaximumSize(QSize(40, 40))
        self.PrimBtnReiniciar.setStyleSheet(u"background-color: rgb(163, 160, 159);\n"
"border-width: 5px;\n"
"border-color: rgb(163, 160, 159);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Allerta\";\n"
"\n"
"")
        self.PrimLabelConvencional_2 = QLabel(self.primarioSalida)
        self.PrimLabelConvencional_2.setObjectName(u"PrimLabelConvencional_2")
        self.PrimLabelConvencional_2.setGeometry(QRect(10, 50, 1061, 35))
        sizePolicy9.setHeightForWidth(self.PrimLabelConvencional_2.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_2.setSizePolicy(sizePolicy9)
        self.PrimLabelConvencional_2.setStyleSheet(u"font: 650 25pt \"Allerta\";\n"
"")
        self.PrimLabelConvencional_2.setLineWidth(1)
        self.PrimLabelConvencional_2.setAlignment(Qt.AlignCenter)
        self.PrimInputParametro_6 = QLineEdit(self.primarioSalida)
        self.PrimInputParametro_6.setObjectName(u"PrimInputParametro_6")
        self.PrimInputParametro_6.setGeometry(QRect(320, 40, 445, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_6.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_6.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_6.setMinimumSize(QSize(445, 2))
        self.PrimInputParametro_6.setMaximumSize(QSize(445, 2))
        self.PrimInputParametro_6.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.PrimInputParametro_7 = QLineEdit(self.primarioSalida)
        self.PrimInputParametro_7.setObjectName(u"PrimInputParametro_7")
        self.PrimInputParametro_7.setGeometry(QRect(320, 100, 445, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_7.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_7.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_7.setMinimumSize(QSize(445, 2))
        self.PrimInputParametro_7.setMaximumSize(QSize(445, 2))
        self.PrimInputParametro_7.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.groupBox_Propiedades_46 = QGroupBox(self.primarioSalida)
        self.groupBox_Propiedades_46.setObjectName(u"groupBox_Propiedades_46")
        self.groupBox_Propiedades_46.setGeometry(QRect(20, 400, 770, 131))
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_46.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_46.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_46.setMinimumSize(QSize(770, 0))
        self.groupBox_Propiedades_46.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_46.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 148, 150);\n"
"font: bold; \n"
"border: 2px solid;\n"
"font: 700 11pt \"Allerta\";\n"
"border-color: rgb(250, 148, 150);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_46.setAlignment(Qt.AlignCenter)
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_Propiedades_46)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.row_74 = QFrame(self.groupBox_Propiedades_46)
        self.row_74.setObjectName(u"row_74")
        self.row_74.setStyleSheet(u"")
        self.row_74.setFrameShape(QFrame.StyledPanel)
        self.row_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.row_74)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_144 = QGridLayout()
        self.gridLayout_144.setObjectName(u"gridLayout_144")
        self.gridLayout_144.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_144.setHorizontalSpacing(35)
        self.gridLayout_144.setVerticalSpacing(10)
        self.gridLayout_144.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelConvencional_15 = QLabel(self.row_74)
        self.PrimLabelConvencional_15.setObjectName(u"PrimLabelConvencional_15")
        sizePolicy8.setHeightForWidth(self.PrimLabelConvencional_15.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_15.setSizePolicy(sizePolicy8)
        self.PrimLabelConvencional_15.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelConvencional_15.setLineWidth(1)
        self.PrimLabelConvencional_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_144.addWidget(self.PrimLabelConvencional_15, 0, 0, 1, 1)

        self.PrimFieldResultadoMejor = QLineEdit(self.row_74)
        self.PrimFieldResultadoMejor.setObjectName(u"PrimFieldResultadoMejor")
        self.PrimFieldResultadoMejor.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.PrimFieldResultadoMejor.sizePolicy().hasHeightForWidth())
        self.PrimFieldResultadoMejor.setSizePolicy(sizePolicy9)
        self.PrimFieldResultadoMejor.setMinimumSize(QSize(110, 35))
        self.PrimFieldResultadoMejor.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.PrimFieldResultadoMejor.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.PrimFieldResultadoMejor.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.PrimFieldResultadoMejor.setAlignment(Qt.AlignCenter)

        self.gridLayout_144.addWidget(self.PrimFieldResultadoMejor, 0, 1, 1, 1)


        self.verticalLayout_94.addLayout(self.gridLayout_144)


        self.verticalLayout_23.addWidget(self.row_74)

        self.tabPrim.addTab(self.primarioSalida, "")
        self.stackedWidget.addWidget(self.pagina_Primario)
        self.pagina_Secundario = QWidget()
        self.pagina_Secundario.setObjectName(u"pagina_Secundario")
        self.tabSec = QTabWidget(self.pagina_Secundario)
        self.tabSec.setObjectName(u"tabSec")
        self.tabSec.setGeometry(QRect(0, 0, 1131, 621))
        sizePolicy4.setHeightForWidth(self.tabSec.sizePolicy().hasHeightForWidth())
        self.tabSec.setSizePolicy(sizePolicy4)
        self.tabSec.setStyleSheet(u"font: 500 10pt \"Allerta\";\n"
"color: rgb(79, 79, 79);")
        self.tabSec.setTabPosition(QTabWidget.West)
        self.tabSec.setTabsClosable(False)
        self.secundarioEntrada = QWidget()
        self.secundarioEntrada.setObjectName(u"secundarioEntrada")
        self.secundarioEntrada.setStyleSheet(u"font: 500 11pt \"Allerta\";")
        self.SecuComboBoxPeso = QComboBox(self.secundarioEntrada)
        self.SecuComboBoxPeso.addItem("")
        self.SecuComboBoxPeso.addItem("")
        self.SecuComboBoxPeso.addItem("")
        self.SecuComboBoxPeso.addItem("")
        self.SecuComboBoxPeso.addItem("")
        self.SecuComboBoxPeso.setObjectName(u"SecuComboBoxPeso")
        self.SecuComboBoxPeso.setEnabled(True)
        self.SecuComboBoxPeso.setGeometry(QRect(810, 400, 200, 35))
        sizePolicy4.setHeightForWidth(self.SecuComboBoxPeso.sizePolicy().hasHeightForWidth())
        self.SecuComboBoxPeso.setSizePolicy(sizePolicy4)
        self.SecuComboBoxPeso.setMinimumSize(QSize(200, 35))
        self.SecuComboBoxPeso.setMaximumSize(QSize(150, 30))
        self.SecuComboBoxPeso.setLayoutDirection(Qt.LeftToRight)
        self.SecuComboBoxPeso.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.SecuComboBoxPeso.setEditable(False)
        self.SecuComboBoxPeso.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.SecuComboBoxPeso.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.PrimInputParametro_5 = QLineEdit(self.secundarioEntrada)
        self.PrimInputParametro_5.setObjectName(u"PrimInputParametro_5")
        self.PrimInputParametro_5.setGeometry(QRect(780, 350, 265, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_5.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_5.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_5.setMinimumSize(QSize(265, 2))
        self.PrimInputParametro_5.setMaximumSize(QSize(250, 2))
        self.PrimInputParametro_5.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.groupBox_Resultados_20 = QGroupBox(self.secundarioEntrada)
        self.groupBox_Resultados_20.setObjectName(u"groupBox_Resultados_20")
        self.groupBox_Resultados_20.setGeometry(QRect(739, 10, 341, 281))
        sizePolicy5.setHeightForWidth(self.groupBox_Resultados_20.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_20.setSizePolicy(sizePolicy5)
        self.groupBox_Resultados_20.setMinimumSize(QSize(300, 0))
        self.groupBox_Resultados_20.setMaximumSize(QSize(450, 16777215))
        self.groupBox_Resultados_20.setStyleSheet(u"QGroupBox {\n"
"color: rgb(190, 190, 190);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(190, 190, 190);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.gridLayout_84 = QGridLayout(self.groupBox_Resultados_20)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.row_41 = QFrame(self.groupBox_Resultados_20)
        self.row_41.setObjectName(u"row_41")
        self.row_41.setStyleSheet(u"")
        self.row_41.setFrameShape(QFrame.StyledPanel)
        self.row_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.row_41)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_89 = QGridLayout()
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.gridLayout_89.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_89.setHorizontalSpacing(10)
        self.gridLayout_89.setVerticalSpacing(15)
        self.gridLayout_89.setContentsMargins(10, 10, 10, 10)
        self.SecuComboBoxCriterio = QComboBox(self.row_41)
        self.SecuComboBoxCriterio.addItem("")
        self.SecuComboBoxCriterio.addItem("")
        self.SecuComboBoxCriterio.addItem("")
        self.SecuComboBoxCriterio.addItem("")
        self.SecuComboBoxCriterio.addItem("")
        self.SecuComboBoxCriterio.setObjectName(u"SecuComboBoxCriterio")
        self.SecuComboBoxCriterio.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.SecuComboBoxCriterio.sizePolicy().hasHeightForWidth())
        self.SecuComboBoxCriterio.setSizePolicy(sizePolicy4)
        self.SecuComboBoxCriterio.setMinimumSize(QSize(170, 35))
        self.SecuComboBoxCriterio.setMaximumSize(QSize(170, 30))
        self.SecuComboBoxCriterio.setLayoutDirection(Qt.LeftToRight)
        self.SecuComboBoxCriterio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.SecuComboBoxCriterio.setEditable(False)
        self.SecuComboBoxCriterio.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.SecuComboBoxCriterio.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_89.addWidget(self.SecuComboBoxCriterio, 1, 1, 1, 1)

        self.SecuInputMinCriterio = QLineEdit(self.row_41)
        self.SecuInputMinCriterio.setObjectName(u"SecuInputMinCriterio")
        sizePolicy6.setHeightForWidth(self.SecuInputMinCriterio.sizePolicy().hasHeightForWidth())
        self.SecuInputMinCriterio.setSizePolicy(sizePolicy6)
        self.SecuInputMinCriterio.setMinimumSize(QSize(170, 35))
        self.SecuInputMinCriterio.setMaximumSize(QSize(100, 16777215))
        self.SecuInputMinCriterio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_89.addWidget(self.SecuInputMinCriterio, 2, 1, 1, 1)

        self.SecuInputMaxCriterio = QLineEdit(self.row_41)
        self.SecuInputMaxCriterio.setObjectName(u"SecuInputMaxCriterio")
        sizePolicy6.setHeightForWidth(self.SecuInputMaxCriterio.sizePolicy().hasHeightForWidth())
        self.SecuInputMaxCriterio.setSizePolicy(sizePolicy6)
        self.SecuInputMaxCriterio.setMinimumSize(QSize(170, 35))
        self.SecuInputMaxCriterio.setMaximumSize(QSize(100, 16777215))
        self.SecuInputMaxCriterio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_89.addWidget(self.SecuInputMaxCriterio, 3, 1, 1, 1)

        self.PrimLabelMinCriteiro_2 = QLabel(self.row_41)
        self.PrimLabelMinCriteiro_2.setObjectName(u"PrimLabelMinCriteiro_2")
        sizePolicy6.setHeightForWidth(self.PrimLabelMinCriteiro_2.sizePolicy().hasHeightForWidth())
        self.PrimLabelMinCriteiro_2.setSizePolicy(sizePolicy6)
        self.PrimLabelMinCriteiro_2.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.PrimLabelMinCriteiro_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_89.addWidget(self.PrimLabelMinCriteiro_2, 2, 0, 1, 1)

        self.PrimLabelMaxCriterio_3 = QLabel(self.row_41)
        self.PrimLabelMaxCriterio_3.setObjectName(u"PrimLabelMaxCriterio_3")
        sizePolicy6.setHeightForWidth(self.PrimLabelMaxCriterio_3.sizePolicy().hasHeightForWidth())
        self.PrimLabelMaxCriterio_3.setSizePolicy(sizePolicy6)
        self.PrimLabelMaxCriterio_3.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.PrimLabelMaxCriterio_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_89.addWidget(self.PrimLabelMaxCriterio_3, 3, 0, 1, 1)

        self.PrimLabelCriterio_2 = QLabel(self.row_41)
        self.PrimLabelCriterio_2.setObjectName(u"PrimLabelCriterio_2")
        sizePolicy6.setHeightForWidth(self.PrimLabelCriterio_2.sizePolicy().hasHeightForWidth())
        self.PrimLabelCriterio_2.setSizePolicy(sizePolicy6)
        self.PrimLabelCriterio_2.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.PrimLabelCriterio_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_89.addWidget(self.PrimLabelCriterio_2, 1, 0, 1, 1)


        self.verticalLayout_61.addLayout(self.gridLayout_89)


        self.gridLayout_84.addWidget(self.row_41, 0, 0, 1, 1)

        self.layoutWidget2 = QWidget(self.secundarioEntrada)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 10, 692, 603))
        self.verticalLayout_31 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_31.setSpacing(6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.groupBox_Propiedades_26 = QGroupBox(self.layoutWidget2)
        self.groupBox_Propiedades_26.setObjectName(u"groupBox_Propiedades_26")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_26.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_26.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_26.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_26.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_26.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 190, 167);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(250, 190, 167);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_26.setAlignment(Qt.AlignCenter)
        self.gridLayout_105 = QGridLayout(self.groupBox_Propiedades_26)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.row_52 = QFrame(self.groupBox_Propiedades_26)
        self.row_52.setObjectName(u"row_52")
        self.row_52.setStyleSheet(u"")
        self.row_52.setFrameShape(QFrame.StyledPanel)
        self.row_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.row_52)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_107 = QGridLayout()
        self.gridLayout_107.setObjectName(u"gridLayout_107")
        self.gridLayout_107.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_107.setHorizontalSpacing(35)
        self.gridLayout_107.setVerticalSpacing(10)
        self.gridLayout_107.setContentsMargins(20, 10, 20, 10)
        self.SecuInputMinCapital = QLineEdit(self.row_52)
        self.SecuInputMinCapital.setObjectName(u"SecuInputMinCapital")
        sizePolicy7.setHeightForWidth(self.SecuInputMinCapital.sizePolicy().hasHeightForWidth())
        self.SecuInputMinCapital.setSizePolicy(sizePolicy7)
        self.SecuInputMinCapital.setMinimumSize(QSize(110, 30))
        self.SecuInputMinCapital.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.SecuInputMinCapital.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.SecuInputMinCapital.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_107.addWidget(self.SecuInputMinCapital, 0, 1, 1, 1)

        self.SecuLabelCostoOM = QLabel(self.row_52)
        self.SecuLabelCostoOM.setObjectName(u"SecuLabelCostoOM")
        sizePolicy8.setHeightForWidth(self.SecuLabelCostoOM.sizePolicy().hasHeightForWidth())
        self.SecuLabelCostoOM.setSizePolicy(sizePolicy8)
        self.SecuLabelCostoOM.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.SecuLabelCostoOM.setLineWidth(1)
        self.SecuLabelCostoOM.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_107.addWidget(self.SecuLabelCostoOM, 1, 0, 1, 1)

        self.SecuLabelCostoCapital = QLabel(self.row_52)
        self.SecuLabelCostoCapital.setObjectName(u"SecuLabelCostoCapital")
        sizePolicy8.setHeightForWidth(self.SecuLabelCostoCapital.sizePolicy().hasHeightForWidth())
        self.SecuLabelCostoCapital.setSizePolicy(sizePolicy8)
        self.SecuLabelCostoCapital.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.SecuLabelCostoCapital.setLineWidth(1)
        self.SecuLabelCostoCapital.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_107.addWidget(self.SecuLabelCostoCapital, 0, 0, 1, 1)

        self.SecuInputMinOM = QLineEdit(self.row_52)
        self.SecuInputMinOM.setObjectName(u"SecuInputMinOM")
        sizePolicy7.setHeightForWidth(self.SecuInputMinOM.sizePolicy().hasHeightForWidth())
        self.SecuInputMinOM.setSizePolicy(sizePolicy7)
        self.SecuInputMinOM.setMinimumSize(QSize(110, 30))
        self.SecuInputMinOM.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.SecuInputMinOM.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.SecuInputMinOM.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_107.addWidget(self.SecuInputMinOM, 1, 1, 1, 1)

        self.SecuInputMaxCapital = QLineEdit(self.row_52)
        self.SecuInputMaxCapital.setObjectName(u"SecuInputMaxCapital")
        sizePolicy7.setHeightForWidth(self.SecuInputMaxCapital.sizePolicy().hasHeightForWidth())
        self.SecuInputMaxCapital.setSizePolicy(sizePolicy7)
        self.SecuInputMaxCapital.setMinimumSize(QSize(110, 30))
        self.SecuInputMaxCapital.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.SecuInputMaxCapital.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.SecuInputMaxCapital.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_107.addWidget(self.SecuInputMaxCapital, 0, 2, 1, 1)

        self.SecuInputMaxOM = QLineEdit(self.row_52)
        self.SecuInputMaxOM.setObjectName(u"SecuInputMaxOM")
        sizePolicy7.setHeightForWidth(self.SecuInputMaxOM.sizePolicy().hasHeightForWidth())
        self.SecuInputMaxOM.setSizePolicy(sizePolicy7)
        self.SecuInputMaxOM.setMinimumSize(QSize(110, 30))
        self.SecuInputMaxOM.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.SecuInputMaxOM.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.SecuInputMaxOM.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_107.addWidget(self.SecuInputMaxOM, 1, 2, 1, 1)


        self.verticalLayout_72.addLayout(self.gridLayout_107)


        self.gridLayout_105.addWidget(self.row_52, 0, 1, 1, 1)


        self.verticalLayout_31.addWidget(self.groupBox_Propiedades_26)

        self.groupBox_Propiedades_27 = QGroupBox(self.layoutWidget2)
        self.groupBox_Propiedades_27.setObjectName(u"groupBox_Propiedades_27")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_27.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_27.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_27.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_27.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_27.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 190, 167);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(250, 190, 167);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_27.setAlignment(Qt.AlignCenter)
        self.gridLayout_108 = QGridLayout(self.groupBox_Propiedades_27)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.row_53 = QFrame(self.groupBox_Propiedades_27)
        self.row_53.setObjectName(u"row_53")
        self.row_53.setStyleSheet(u"")
        self.row_53.setFrameShape(QFrame.StyledPanel)
        self.row_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.row_53)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_109 = QGridLayout()
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.gridLayout_109.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_109.setHorizontalSpacing(35)
        self.gridLayout_109.setVerticalSpacing(10)
        self.gridLayout_109.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelEnergia_2 = QLabel(self.row_53)
        self.PrimLabelEnergia_2.setObjectName(u"PrimLabelEnergia_2")
        sizePolicy8.setHeightForWidth(self.PrimLabelEnergia_2.sizePolicy().hasHeightForWidth())
        self.PrimLabelEnergia_2.setSizePolicy(sizePolicy8)
        self.PrimLabelEnergia_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelEnergia_2.setLineWidth(1)
        self.PrimLabelEnergia_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_109.addWidget(self.PrimLabelEnergia_2, 1, 0, 1, 1)

        self.PrimLabelRecuperacion_2 = QLabel(self.row_53)
        self.PrimLabelRecuperacion_2.setObjectName(u"PrimLabelRecuperacion_2")
        sizePolicy8.setHeightForWidth(self.PrimLabelRecuperacion_2.sizePolicy().hasHeightForWidth())
        self.PrimLabelRecuperacion_2.setSizePolicy(sizePolicy8)
        self.PrimLabelRecuperacion_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelRecuperacion_2.setLineWidth(1)
        self.PrimLabelRecuperacion_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_109.addWidget(self.PrimLabelRecuperacion_2, 0, 0, 1, 1)

        self.SecuComboBoxRecuperacion = QComboBox(self.row_53)
        self.SecuComboBoxRecuperacion.addItem("")
        self.SecuComboBoxRecuperacion.addItem("")
        self.SecuComboBoxRecuperacion.addItem("")
        self.SecuComboBoxRecuperacion.addItem("")
        self.SecuComboBoxRecuperacion.addItem("")
        self.SecuComboBoxRecuperacion.setObjectName(u"SecuComboBoxRecuperacion")
        self.SecuComboBoxRecuperacion.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.SecuComboBoxRecuperacion.sizePolicy().hasHeightForWidth())
        self.SecuComboBoxRecuperacion.setSizePolicy(sizePolicy4)
        self.SecuComboBoxRecuperacion.setMinimumSize(QSize(200, 35))
        self.SecuComboBoxRecuperacion.setMaximumSize(QSize(150, 30))
        self.SecuComboBoxRecuperacion.setLayoutDirection(Qt.LeftToRight)
        self.SecuComboBoxRecuperacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.SecuComboBoxRecuperacion.setEditable(False)
        self.SecuComboBoxRecuperacion.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.SecuComboBoxRecuperacion.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_109.addWidget(self.SecuComboBoxRecuperacion, 0, 1, 1, 1)

        self.SecuComboBoxEnergia = QComboBox(self.row_53)
        self.SecuComboBoxEnergia.addItem("")
        self.SecuComboBoxEnergia.addItem("")
        self.SecuComboBoxEnergia.addItem("")
        self.SecuComboBoxEnergia.addItem("")
        self.SecuComboBoxEnergia.addItem("")
        self.SecuComboBoxEnergia.setObjectName(u"SecuComboBoxEnergia")
        self.SecuComboBoxEnergia.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.SecuComboBoxEnergia.sizePolicy().hasHeightForWidth())
        self.SecuComboBoxEnergia.setSizePolicy(sizePolicy4)
        self.SecuComboBoxEnergia.setMinimumSize(QSize(200, 35))
        self.SecuComboBoxEnergia.setMaximumSize(QSize(150, 30))
        self.SecuComboBoxEnergia.setLayoutDirection(Qt.LeftToRight)
        self.SecuComboBoxEnergia.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.SecuComboBoxEnergia.setEditable(False)
        self.SecuComboBoxEnergia.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.SecuComboBoxEnergia.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_109.addWidget(self.SecuComboBoxEnergia, 1, 1, 1, 1)


        self.verticalLayout_73.addLayout(self.gridLayout_109)


        self.gridLayout_108.addWidget(self.row_53, 0, 1, 1, 1)


        self.verticalLayout_31.addWidget(self.groupBox_Propiedades_27)

        self.groupBox_Propiedades_28 = QGroupBox(self.layoutWidget2)
        self.groupBox_Propiedades_28.setObjectName(u"groupBox_Propiedades_28")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_28.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_28.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_28.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_28.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_28.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 190, 167);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(250, 190, 167);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_28.setAlignment(Qt.AlignCenter)
        self.gridLayout_110 = QGridLayout(self.groupBox_Propiedades_28)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.row_54 = QFrame(self.groupBox_Propiedades_28)
        self.row_54.setObjectName(u"row_54")
        self.row_54.setStyleSheet(u"")
        self.row_54.setFrameShape(QFrame.StyledPanel)
        self.row_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.row_54)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_111 = QGridLayout()
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.gridLayout_111.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_111.setHorizontalSpacing(35)
        self.gridLayout_111.setVerticalSpacing(10)
        self.gridLayout_111.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelRobustez_2 = QLabel(self.row_54)
        self.PrimLabelRobustez_2.setObjectName(u"PrimLabelRobustez_2")
        sizePolicy8.setHeightForWidth(self.PrimLabelRobustez_2.sizePolicy().hasHeightForWidth())
        self.PrimLabelRobustez_2.setSizePolicy(sizePolicy8)
        self.PrimLabelRobustez_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelRobustez_2.setLineWidth(1)
        self.PrimLabelRobustez_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_111.addWidget(self.PrimLabelRobustez_2, 1, 0, 1, 1)

        self.PrimLabelSimplicidad_2 = QLabel(self.row_54)
        self.PrimLabelSimplicidad_2.setObjectName(u"PrimLabelSimplicidad_2")
        sizePolicy8.setHeightForWidth(self.PrimLabelSimplicidad_2.sizePolicy().hasHeightForWidth())
        self.PrimLabelSimplicidad_2.setSizePolicy(sizePolicy8)
        self.PrimLabelSimplicidad_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelSimplicidad_2.setLineWidth(1)
        self.PrimLabelSimplicidad_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_111.addWidget(self.PrimLabelSimplicidad_2, 0, 0, 1, 1)

        self.SecuComboBoxSimplicidad = QComboBox(self.row_54)
        self.SecuComboBoxSimplicidad.addItem("")
        self.SecuComboBoxSimplicidad.addItem("")
        self.SecuComboBoxSimplicidad.addItem("")
        self.SecuComboBoxSimplicidad.addItem("")
        self.SecuComboBoxSimplicidad.addItem("")
        self.SecuComboBoxSimplicidad.setObjectName(u"SecuComboBoxSimplicidad")
        self.SecuComboBoxSimplicidad.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.SecuComboBoxSimplicidad.sizePolicy().hasHeightForWidth())
        self.SecuComboBoxSimplicidad.setSizePolicy(sizePolicy4)
        self.SecuComboBoxSimplicidad.setMinimumSize(QSize(200, 35))
        self.SecuComboBoxSimplicidad.setMaximumSize(QSize(150, 30))
        self.SecuComboBoxSimplicidad.setLayoutDirection(Qt.LeftToRight)
        self.SecuComboBoxSimplicidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.SecuComboBoxSimplicidad.setEditable(False)
        self.SecuComboBoxSimplicidad.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.SecuComboBoxSimplicidad.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_111.addWidget(self.SecuComboBoxSimplicidad, 0, 1, 1, 1)

        self.SecuComboBoxRobustez = QComboBox(self.row_54)
        self.SecuComboBoxRobustez.addItem("")
        self.SecuComboBoxRobustez.addItem("")
        self.SecuComboBoxRobustez.addItem("")
        self.SecuComboBoxRobustez.addItem("")
        self.SecuComboBoxRobustez.addItem("")
        self.SecuComboBoxRobustez.setObjectName(u"SecuComboBoxRobustez")
        self.SecuComboBoxRobustez.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.SecuComboBoxRobustez.sizePolicy().hasHeightForWidth())
        self.SecuComboBoxRobustez.setSizePolicy(sizePolicy4)
        self.SecuComboBoxRobustez.setMinimumSize(QSize(200, 35))
        self.SecuComboBoxRobustez.setMaximumSize(QSize(150, 30))
        self.SecuComboBoxRobustez.setLayoutDirection(Qt.LeftToRight)
        self.SecuComboBoxRobustez.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.SecuComboBoxRobustez.setEditable(False)
        self.SecuComboBoxRobustez.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.SecuComboBoxRobustez.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_111.addWidget(self.SecuComboBoxRobustez, 1, 1, 1, 1)

        self.PrimLabelArea_2 = QLabel(self.row_54)
        self.PrimLabelArea_2.setObjectName(u"PrimLabelArea_2")
        sizePolicy8.setHeightForWidth(self.PrimLabelArea_2.sizePolicy().hasHeightForWidth())
        self.PrimLabelArea_2.setSizePolicy(sizePolicy8)
        self.PrimLabelArea_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelArea_2.setLineWidth(1)
        self.PrimLabelArea_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_111.addWidget(self.PrimLabelArea_2, 2, 0, 1, 1)

        self.SecuComboBoxArea = QComboBox(self.row_54)
        self.SecuComboBoxArea.addItem("")
        self.SecuComboBoxArea.addItem("")
        self.SecuComboBoxArea.addItem("")
        self.SecuComboBoxArea.addItem("")
        self.SecuComboBoxArea.addItem("")
        self.SecuComboBoxArea.setObjectName(u"SecuComboBoxArea")
        self.SecuComboBoxArea.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.SecuComboBoxArea.sizePolicy().hasHeightForWidth())
        self.SecuComboBoxArea.setSizePolicy(sizePolicy4)
        self.SecuComboBoxArea.setMinimumSize(QSize(200, 35))
        self.SecuComboBoxArea.setMaximumSize(QSize(150, 30))
        self.SecuComboBoxArea.setLayoutDirection(Qt.LeftToRight)
        self.SecuComboBoxArea.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.SecuComboBoxArea.setEditable(False)
        self.SecuComboBoxArea.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.SecuComboBoxArea.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_111.addWidget(self.SecuComboBoxArea, 2, 1, 1, 1)


        self.verticalLayout_74.addLayout(self.gridLayout_111)


        self.gridLayout_110.addWidget(self.row_54, 0, 1, 1, 1)


        self.verticalLayout_31.addWidget(self.groupBox_Propiedades_28)

        self.groupBox_Propiedades_29 = QGroupBox(self.layoutWidget2)
        self.groupBox_Propiedades_29.setObjectName(u"groupBox_Propiedades_29")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_29.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_29.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_29.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_29.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_29.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 190, 167);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(250, 190, 167);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_29.setAlignment(Qt.AlignCenter)
        self.gridLayout_112 = QGridLayout(self.groupBox_Propiedades_29)
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.row_55 = QFrame(self.groupBox_Propiedades_29)
        self.row_55.setObjectName(u"row_55")
        self.row_55.setStyleSheet(u"")
        self.row_55.setFrameShape(QFrame.StyledPanel)
        self.row_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.row_55)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_113 = QGridLayout()
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.gridLayout_113.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_113.setHorizontalSpacing(35)
        self.gridLayout_113.setVerticalSpacing(10)
        self.gridLayout_113.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelSocial_2 = QLabel(self.row_55)
        self.PrimLabelSocial_2.setObjectName(u"PrimLabelSocial_2")
        sizePolicy8.setHeightForWidth(self.PrimLabelSocial_2.sizePolicy().hasHeightForWidth())
        self.PrimLabelSocial_2.setSizePolicy(sizePolicy8)
        self.PrimLabelSocial_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelSocial_2.setLineWidth(1)
        self.PrimLabelSocial_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_113.addWidget(self.PrimLabelSocial_2, 0, 0, 1, 1)

        self.SecuComboBoxSocial = QComboBox(self.row_55)
        self.SecuComboBoxSocial.addItem("")
        self.SecuComboBoxSocial.addItem("")
        self.SecuComboBoxSocial.addItem("")
        self.SecuComboBoxSocial.addItem("")
        self.SecuComboBoxSocial.addItem("")
        self.SecuComboBoxSocial.setObjectName(u"SecuComboBoxSocial")
        self.SecuComboBoxSocial.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.SecuComboBoxSocial.sizePolicy().hasHeightForWidth())
        self.SecuComboBoxSocial.setSizePolicy(sizePolicy4)
        self.SecuComboBoxSocial.setMinimumSize(QSize(200, 35))
        self.SecuComboBoxSocial.setMaximumSize(QSize(150, 30))
        self.SecuComboBoxSocial.setLayoutDirection(Qt.LeftToRight)
        self.SecuComboBoxSocial.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.SecuComboBoxSocial.setEditable(False)
        self.SecuComboBoxSocial.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.SecuComboBoxSocial.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_113.addWidget(self.SecuComboBoxSocial, 0, 1, 1, 1)


        self.verticalLayout_75.addLayout(self.gridLayout_113)


        self.gridLayout_112.addWidget(self.row_55, 0, 1, 1, 1)


        self.verticalLayout_31.addWidget(self.groupBox_Propiedades_29)

        self.PrimInputParametro_9 = QLineEdit(self.secundarioEntrada)
        self.PrimInputParametro_9.setObjectName(u"PrimInputParametro_9")
        self.PrimInputParametro_9.setGeometry(QRect(780, 460, 265, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_9.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_9.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_9.setMinimumSize(QSize(265, 2))
        self.PrimInputParametro_9.setMaximumSize(QSize(250, 2))
        self.PrimInputParametro_9.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.PrimLabelMaxCriterio_4 = QLabel(self.secundarioEntrada)
        self.PrimLabelMaxCriterio_4.setObjectName(u"PrimLabelMaxCriterio_4")
        self.PrimLabelMaxCriterio_4.setGeometry(QRect(780, 360, 265, 21))
        sizePolicy6.setHeightForWidth(self.PrimLabelMaxCriterio_4.sizePolicy().hasHeightForWidth())
        self.PrimLabelMaxCriterio_4.setSizePolicy(sizePolicy6)
        self.PrimLabelMaxCriterio_4.setMinimumSize(QSize(265, 0))
        self.PrimLabelMaxCriterio_4.setMaximumSize(QSize(265, 16777215))
        self.PrimLabelMaxCriterio_4.setStyleSheet(u"font: 600 12pt \"Allerta\";\n"
"background-color: rgb(250, 190, 167);\n"
"color: rgb(255, 255, 255);")
        self.PrimLabelMaxCriterio_4.setTextFormat(Qt.AutoText)
        self.PrimLabelMaxCriterio_4.setAlignment(Qt.AlignCenter)
        self.tabSec.addTab(self.secundarioEntrada, "")
        self.secundarioResultados = QWidget()
        self.secundarioResultados.setObjectName(u"secundarioResultados")
        self.SecuBtnReiniciar = QPushButton(self.secundarioResultados)
        self.SecuBtnReiniciar.setObjectName(u"SecuBtnReiniciar")
        self.SecuBtnReiniciar.setEnabled(True)
        self.SecuBtnReiniciar.setGeometry(QRect(810, 210, 250, 50))
        sizePolicy10.setHeightForWidth(self.SecuBtnReiniciar.sizePolicy().hasHeightForWidth())
        self.SecuBtnReiniciar.setSizePolicy(sizePolicy10)
        self.SecuBtnReiniciar.setMinimumSize(QSize(250, 50))
        self.SecuBtnReiniciar.setMaximumSize(QSize(40, 40))
        self.SecuBtnReiniciar.setStyleSheet(u"background-color: rgb(163, 160, 159);\n"
"border-width: 5px;\n"
"border-color: rgb(163, 160, 159);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Allerta\";\n"
"\n"
"")
        self.PrimInputParametro_8 = QLineEdit(self.secundarioResultados)
        self.PrimInputParametro_8.setObjectName(u"PrimInputParametro_8")
        self.PrimInputParametro_8.setGeometry(QRect(300, 100, 475, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_8.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_8.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_8.setMinimumSize(QSize(475, 2))
        self.PrimInputParametro_8.setMaximumSize(QSize(475, 2))
        self.PrimInputParametro_8.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.PrimLabelConvencional_3 = QLabel(self.secundarioResultados)
        self.PrimLabelConvencional_3.setObjectName(u"PrimLabelConvencional_3")
        self.PrimLabelConvencional_3.setGeometry(QRect(10, 50, 1061, 35))
        sizePolicy9.setHeightForWidth(self.PrimLabelConvencional_3.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_3.setSizePolicy(sizePolicy9)
        self.PrimLabelConvencional_3.setStyleSheet(u"font: 650 25pt \"Allerta\";\n"
"")
        self.PrimLabelConvencional_3.setLineWidth(1)
        self.PrimLabelConvencional_3.setAlignment(Qt.AlignCenter)
        self.PrimInputParametro_10 = QLineEdit(self.secundarioResultados)
        self.PrimInputParametro_10.setObjectName(u"PrimInputParametro_10")
        self.PrimInputParametro_10.setGeometry(QRect(300, 40, 475, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_10.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_10.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_10.setMinimumSize(QSize(475, 2))
        self.PrimInputParametro_10.setMaximumSize(QSize(475, 2))
        self.PrimInputParametro_10.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.groupBox_Propiedades_30 = QGroupBox(self.secundarioResultados)
        self.groupBox_Propiedades_30.setObjectName(u"groupBox_Propiedades_30")
        self.groupBox_Propiedades_30.setGeometry(QRect(20, 130, 770, 291))
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_30.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_30.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_30.setMinimumSize(QSize(770, 0))
        self.groupBox_Propiedades_30.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_30.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 190, 167);\n"
"font: bold; \n"
"border: 2px solid;\n"
"font: 700 11pt \"Allerta\";\n"
"border-color: rgb(250, 190, 167);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_30.setAlignment(Qt.AlignCenter)
        self.verticalLayout_32 = QVBoxLayout(self.groupBox_Propiedades_30)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.row_58 = QFrame(self.groupBox_Propiedades_30)
        self.row_58.setObjectName(u"row_58")
        self.row_58.setStyleSheet(u"")
        self.row_58.setFrameShape(QFrame.StyledPanel)
        self.row_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.row_58)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_116 = QGridLayout()
        self.gridLayout_116.setObjectName(u"gridLayout_116")
        self.gridLayout_116.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_116.setHorizontalSpacing(35)
        self.gridLayout_116.setVerticalSpacing(10)
        self.gridLayout_116.setContentsMargins(20, 10, 20, 10)
        self.SecuFieldResultadoCAS = QLineEdit(self.row_58)
        self.SecuFieldResultadoCAS.setObjectName(u"SecuFieldResultadoCAS")
        self.SecuFieldResultadoCAS.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.SecuFieldResultadoCAS.sizePolicy().hasHeightForWidth())
        self.SecuFieldResultadoCAS.setSizePolicy(sizePolicy9)
        self.SecuFieldResultadoCAS.setMinimumSize(QSize(110, 35))
        self.SecuFieldResultadoCAS.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.SecuFieldResultadoCAS.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.SecuFieldResultadoCAS.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.SecuFieldResultadoCAS.setAlignment(Qt.AlignCenter)

        self.gridLayout_116.addWidget(self.SecuFieldResultadoCAS, 0, 1, 1, 1)

        self.PrimLabelConvencional_6 = QLabel(self.row_58)
        self.PrimLabelConvencional_6.setObjectName(u"PrimLabelConvencional_6")
        sizePolicy8.setHeightForWidth(self.PrimLabelConvencional_6.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_6.setSizePolicy(sizePolicy8)
        self.PrimLabelConvencional_6.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelConvencional_6.setLineWidth(1)
        self.PrimLabelConvencional_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_116.addWidget(self.PrimLabelConvencional_6, 0, 0, 1, 1)

        self.SecuFieldResultadoSBR = QLineEdit(self.row_58)
        self.SecuFieldResultadoSBR.setObjectName(u"SecuFieldResultadoSBR")
        self.SecuFieldResultadoSBR.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.SecuFieldResultadoSBR.sizePolicy().hasHeightForWidth())
        self.SecuFieldResultadoSBR.setSizePolicy(sizePolicy9)
        self.SecuFieldResultadoSBR.setMinimumSize(QSize(110, 35))
        self.SecuFieldResultadoSBR.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.SecuFieldResultadoSBR.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.SecuFieldResultadoSBR.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.SecuFieldResultadoSBR.setAlignment(Qt.AlignCenter)

        self.gridLayout_116.addWidget(self.SecuFieldResultadoSBR, 1, 1, 1, 1)

        self.PrimLabelTQA_4 = QLabel(self.row_58)
        self.PrimLabelTQA_4.setObjectName(u"PrimLabelTQA_4")
        sizePolicy8.setHeightForWidth(self.PrimLabelTQA_4.sizePolicy().hasHeightForWidth())
        self.PrimLabelTQA_4.setSizePolicy(sizePolicy8)
        self.PrimLabelTQA_4.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelTQA_4.setLineWidth(1)
        self.PrimLabelTQA_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_116.addWidget(self.PrimLabelTQA_4, 1, 0, 1, 1)

        self.PrimLabelTQA_5 = QLabel(self.row_58)
        self.PrimLabelTQA_5.setObjectName(u"PrimLabelTQA_5")
        sizePolicy8.setHeightForWidth(self.PrimLabelTQA_5.sizePolicy().hasHeightForWidth())
        self.PrimLabelTQA_5.setSizePolicy(sizePolicy8)
        self.PrimLabelTQA_5.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelTQA_5.setLineWidth(1)
        self.PrimLabelTQA_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_116.addWidget(self.PrimLabelTQA_5, 2, 0, 1, 1)

        self.PrimLabelTQA_6 = QLabel(self.row_58)
        self.PrimLabelTQA_6.setObjectName(u"PrimLabelTQA_6")
        sizePolicy8.setHeightForWidth(self.PrimLabelTQA_6.sizePolicy().hasHeightForWidth())
        self.PrimLabelTQA_6.setSizePolicy(sizePolicy8)
        self.PrimLabelTQA_6.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelTQA_6.setLineWidth(1)
        self.PrimLabelTQA_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_116.addWidget(self.PrimLabelTQA_6, 3, 0, 1, 1)

        self.SecuFieldResultadoTF = QLineEdit(self.row_58)
        self.SecuFieldResultadoTF.setObjectName(u"SecuFieldResultadoTF")
        self.SecuFieldResultadoTF.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.SecuFieldResultadoTF.sizePolicy().hasHeightForWidth())
        self.SecuFieldResultadoTF.setSizePolicy(sizePolicy9)
        self.SecuFieldResultadoTF.setMinimumSize(QSize(110, 35))
        self.SecuFieldResultadoTF.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.SecuFieldResultadoTF.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.SecuFieldResultadoTF.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.SecuFieldResultadoTF.setAlignment(Qt.AlignCenter)

        self.gridLayout_116.addWidget(self.SecuFieldResultadoTF, 2, 1, 1, 1)

        self.SecuFieldResultadoRBC = QLineEdit(self.row_58)
        self.SecuFieldResultadoRBC.setObjectName(u"SecuFieldResultadoRBC")
        self.SecuFieldResultadoRBC.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.SecuFieldResultadoRBC.sizePolicy().hasHeightForWidth())
        self.SecuFieldResultadoRBC.setSizePolicy(sizePolicy9)
        self.SecuFieldResultadoRBC.setMinimumSize(QSize(110, 35))
        self.SecuFieldResultadoRBC.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.SecuFieldResultadoRBC.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.SecuFieldResultadoRBC.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.SecuFieldResultadoRBC.setAlignment(Qt.AlignCenter)

        self.gridLayout_116.addWidget(self.SecuFieldResultadoRBC, 3, 1, 1, 1)


        self.verticalLayout_78.addLayout(self.gridLayout_116)


        self.verticalLayout_32.addWidget(self.row_58)

        self.SecuBtnCalcular = QPushButton(self.secundarioResultados)
        self.SecuBtnCalcular.setObjectName(u"SecuBtnCalcular")
        self.SecuBtnCalcular.setEnabled(True)
        self.SecuBtnCalcular.setGeometry(QRect(810, 140, 250, 50))
        sizePolicy10.setHeightForWidth(self.SecuBtnCalcular.sizePolicy().hasHeightForWidth())
        self.SecuBtnCalcular.setSizePolicy(sizePolicy10)
        self.SecuBtnCalcular.setMinimumSize(QSize(250, 50))
        self.SecuBtnCalcular.setMaximumSize(QSize(40, 40))
        self.SecuBtnCalcular.setStyleSheet(u"background-color: rgb(163, 160, 159);\n"
"border-width: 5px;\n"
"border-color: rgb(163, 160, 159);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Allerta\";\n"
"\n"
"")
        self.SecuBtnCalcular.setCheckable(False)
        self.SecuBtnCalcular.setChecked(False)
        self.SecuBtnCalcular.setAutoDefault(False)
        self.groupBox_Propiedades_47 = QGroupBox(self.secundarioResultados)
        self.groupBox_Propiedades_47.setObjectName(u"groupBox_Propiedades_47")
        self.groupBox_Propiedades_47.setGeometry(QRect(20, 440, 770, 131))
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_47.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_47.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_47.setMinimumSize(QSize(770, 0))
        self.groupBox_Propiedades_47.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_47.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 190, 167);\n"
"font: bold; \n"
"border: 2px solid;\n"
"font: 700 11pt \"Allerta\";\n"
"border-color: rgb(250, 190, 167);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_47.setAlignment(Qt.AlignCenter)
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_Propiedades_47)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.row_75 = QFrame(self.groupBox_Propiedades_47)
        self.row_75.setObjectName(u"row_75")
        self.row_75.setStyleSheet(u"")
        self.row_75.setFrameShape(QFrame.StyledPanel)
        self.row_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.row_75)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_145 = QGridLayout()
        self.gridLayout_145.setObjectName(u"gridLayout_145")
        self.gridLayout_145.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_145.setHorizontalSpacing(35)
        self.gridLayout_145.setVerticalSpacing(10)
        self.gridLayout_145.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelConvencional_16 = QLabel(self.row_75)
        self.PrimLabelConvencional_16.setObjectName(u"PrimLabelConvencional_16")
        sizePolicy8.setHeightForWidth(self.PrimLabelConvencional_16.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_16.setSizePolicy(sizePolicy8)
        self.PrimLabelConvencional_16.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelConvencional_16.setLineWidth(1)
        self.PrimLabelConvencional_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_145.addWidget(self.PrimLabelConvencional_16, 0, 0, 1, 1)

        self.SecuFieldResultadoMejor = QLineEdit(self.row_75)
        self.SecuFieldResultadoMejor.setObjectName(u"SecuFieldResultadoMejor")
        self.SecuFieldResultadoMejor.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.SecuFieldResultadoMejor.sizePolicy().hasHeightForWidth())
        self.SecuFieldResultadoMejor.setSizePolicy(sizePolicy9)
        self.SecuFieldResultadoMejor.setMinimumSize(QSize(110, 35))
        self.SecuFieldResultadoMejor.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.SecuFieldResultadoMejor.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.SecuFieldResultadoMejor.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.SecuFieldResultadoMejor.setAlignment(Qt.AlignCenter)

        self.gridLayout_145.addWidget(self.SecuFieldResultadoMejor, 0, 1, 1, 1)


        self.verticalLayout_95.addLayout(self.gridLayout_145)


        self.verticalLayout_24.addWidget(self.row_75)

        self.tabSec.addTab(self.secundarioResultados, "")
        self.stackedWidget.addWidget(self.pagina_Secundario)
        self.pagina_Terciario = QWidget()
        self.pagina_Terciario.setObjectName(u"pagina_Terciario")
        self.tabTerc = QTabWidget(self.pagina_Terciario)
        self.tabTerc.setObjectName(u"tabTerc")
        self.tabTerc.setGeometry(QRect(0, 0, 1131, 621))
        sizePolicy4.setHeightForWidth(self.tabTerc.sizePolicy().hasHeightForWidth())
        self.tabTerc.setSizePolicy(sizePolicy4)
        self.tabTerc.setStyleSheet(u"font: 500 10pt \"Allerta\";\n"
"color: rgb(79, 79, 79);")
        self.tabTerc.setTabPosition(QTabWidget.West)
        self.tabTerc.setTabsClosable(False)
        self.terciarioEntrada = QWidget()
        self.terciarioEntrada.setObjectName(u"terciarioEntrada")
        self.terciarioEntrada.setStyleSheet(u"font: 500 11pt \"Allerta\";")
        self.TercComboBoxPeso = QComboBox(self.terciarioEntrada)
        self.TercComboBoxPeso.addItem("")
        self.TercComboBoxPeso.addItem("")
        self.TercComboBoxPeso.addItem("")
        self.TercComboBoxPeso.addItem("")
        self.TercComboBoxPeso.addItem("")
        self.TercComboBoxPeso.setObjectName(u"TercComboBoxPeso")
        self.TercComboBoxPeso.setEnabled(True)
        self.TercComboBoxPeso.setGeometry(QRect(810, 400, 200, 35))
        sizePolicy4.setHeightForWidth(self.TercComboBoxPeso.sizePolicy().hasHeightForWidth())
        self.TercComboBoxPeso.setSizePolicy(sizePolicy4)
        self.TercComboBoxPeso.setMinimumSize(QSize(200, 35))
        self.TercComboBoxPeso.setMaximumSize(QSize(150, 30))
        self.TercComboBoxPeso.setLayoutDirection(Qt.LeftToRight)
        self.TercComboBoxPeso.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.TercComboBoxPeso.setEditable(False)
        self.TercComboBoxPeso.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.TercComboBoxPeso.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.PrimInputParametro_15 = QLineEdit(self.terciarioEntrada)
        self.PrimInputParametro_15.setObjectName(u"PrimInputParametro_15")
        self.PrimInputParametro_15.setGeometry(QRect(780, 350, 265, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_15.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_15.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_15.setMinimumSize(QSize(265, 2))
        self.PrimInputParametro_15.setMaximumSize(QSize(250, 2))
        self.PrimInputParametro_15.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.groupBox_Resultados_22 = QGroupBox(self.terciarioEntrada)
        self.groupBox_Resultados_22.setObjectName(u"groupBox_Resultados_22")
        self.groupBox_Resultados_22.setGeometry(QRect(739, 10, 341, 281))
        sizePolicy5.setHeightForWidth(self.groupBox_Resultados_22.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_22.setSizePolicy(sizePolicy5)
        self.groupBox_Resultados_22.setMinimumSize(QSize(300, 0))
        self.groupBox_Resultados_22.setMaximumSize(QSize(450, 16777215))
        self.groupBox_Resultados_22.setStyleSheet(u"QGroupBox {\n"
"color: rgb(190, 190, 190);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(190, 190, 190);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.gridLayout_86 = QGridLayout(self.groupBox_Resultados_22)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.row_43 = QFrame(self.groupBox_Resultados_22)
        self.row_43.setObjectName(u"row_43")
        self.row_43.setStyleSheet(u"")
        self.row_43.setFrameShape(QFrame.StyledPanel)
        self.row_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.row_43)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_91 = QGridLayout()
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.gridLayout_91.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_91.setHorizontalSpacing(10)
        self.gridLayout_91.setVerticalSpacing(15)
        self.gridLayout_91.setContentsMargins(10, 10, 10, 10)
        self.TercComboBoxCriterio = QComboBox(self.row_43)
        self.TercComboBoxCriterio.addItem("")
        self.TercComboBoxCriterio.addItem("")
        self.TercComboBoxCriterio.addItem("")
        self.TercComboBoxCriterio.addItem("")
        self.TercComboBoxCriterio.addItem("")
        self.TercComboBoxCriterio.setObjectName(u"TercComboBoxCriterio")
        self.TercComboBoxCriterio.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.TercComboBoxCriterio.sizePolicy().hasHeightForWidth())
        self.TercComboBoxCriterio.setSizePolicy(sizePolicy4)
        self.TercComboBoxCriterio.setMinimumSize(QSize(170, 35))
        self.TercComboBoxCriterio.setMaximumSize(QSize(170, 30))
        self.TercComboBoxCriterio.setLayoutDirection(Qt.LeftToRight)
        self.TercComboBoxCriterio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.TercComboBoxCriterio.setEditable(False)
        self.TercComboBoxCriterio.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.TercComboBoxCriterio.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_91.addWidget(self.TercComboBoxCriterio, 1, 1, 1, 1)

        self.TercInputMinCriterio = QLineEdit(self.row_43)
        self.TercInputMinCriterio.setObjectName(u"TercInputMinCriterio")
        sizePolicy6.setHeightForWidth(self.TercInputMinCriterio.sizePolicy().hasHeightForWidth())
        self.TercInputMinCriterio.setSizePolicy(sizePolicy6)
        self.TercInputMinCriterio.setMinimumSize(QSize(170, 35))
        self.TercInputMinCriterio.setMaximumSize(QSize(100, 16777215))
        self.TercInputMinCriterio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_91.addWidget(self.TercInputMinCriterio, 2, 1, 1, 1)

        self.TercInputMaxCriterio = QLineEdit(self.row_43)
        self.TercInputMaxCriterio.setObjectName(u"TercInputMaxCriterio")
        sizePolicy6.setHeightForWidth(self.TercInputMaxCriterio.sizePolicy().hasHeightForWidth())
        self.TercInputMaxCriterio.setSizePolicy(sizePolicy6)
        self.TercInputMaxCriterio.setMinimumSize(QSize(170, 35))
        self.TercInputMaxCriterio.setMaximumSize(QSize(100, 16777215))
        self.TercInputMaxCriterio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_91.addWidget(self.TercInputMaxCriterio, 3, 1, 1, 1)

        self.PrimLabelMinCriteiro_4 = QLabel(self.row_43)
        self.PrimLabelMinCriteiro_4.setObjectName(u"PrimLabelMinCriteiro_4")
        sizePolicy6.setHeightForWidth(self.PrimLabelMinCriteiro_4.sizePolicy().hasHeightForWidth())
        self.PrimLabelMinCriteiro_4.setSizePolicy(sizePolicy6)
        self.PrimLabelMinCriteiro_4.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.PrimLabelMinCriteiro_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_91.addWidget(self.PrimLabelMinCriteiro_4, 2, 0, 1, 1)

        self.PrimLabelMaxCriterio_7 = QLabel(self.row_43)
        self.PrimLabelMaxCriterio_7.setObjectName(u"PrimLabelMaxCriterio_7")
        sizePolicy6.setHeightForWidth(self.PrimLabelMaxCriterio_7.sizePolicy().hasHeightForWidth())
        self.PrimLabelMaxCriterio_7.setSizePolicy(sizePolicy6)
        self.PrimLabelMaxCriterio_7.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.PrimLabelMaxCriterio_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_91.addWidget(self.PrimLabelMaxCriterio_7, 3, 0, 1, 1)

        self.PrimLabelCriterio_4 = QLabel(self.row_43)
        self.PrimLabelCriterio_4.setObjectName(u"PrimLabelCriterio_4")
        sizePolicy6.setHeightForWidth(self.PrimLabelCriterio_4.sizePolicy().hasHeightForWidth())
        self.PrimLabelCriterio_4.setSizePolicy(sizePolicy6)
        self.PrimLabelCriterio_4.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.PrimLabelCriterio_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_91.addWidget(self.PrimLabelCriterio_4, 1, 0, 1, 1)


        self.verticalLayout_63.addLayout(self.gridLayout_91)


        self.gridLayout_86.addWidget(self.row_43, 0, 0, 1, 1)

        self.layoutWidget_3 = QWidget(self.terciarioEntrada)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 10, 692, 603))
        self.verticalLayout_35 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_35.setSpacing(6)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.groupBox_Propiedades_36 = QGroupBox(self.layoutWidget_3)
        self.groupBox_Propiedades_36.setObjectName(u"groupBox_Propiedades_36")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_36.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_36.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_36.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_36.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_36.setStyleSheet(u"QGroupBox {\n"
"color:rgb(255, 244, 119);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(255, 244, 119);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_36.setAlignment(Qt.AlignCenter)
        self.gridLayout_126 = QGridLayout(self.groupBox_Propiedades_36)
        self.gridLayout_126.setObjectName(u"gridLayout_126")
        self.row_64 = QFrame(self.groupBox_Propiedades_36)
        self.row_64.setObjectName(u"row_64")
        self.row_64.setStyleSheet(u"")
        self.row_64.setFrameShape(QFrame.StyledPanel)
        self.row_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.row_64)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_127 = QGridLayout()
        self.gridLayout_127.setObjectName(u"gridLayout_127")
        self.gridLayout_127.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_127.setHorizontalSpacing(35)
        self.gridLayout_127.setVerticalSpacing(10)
        self.gridLayout_127.setContentsMargins(20, 10, 20, 10)
        self.TercInputMinCapital = QLineEdit(self.row_64)
        self.TercInputMinCapital.setObjectName(u"TercInputMinCapital")
        sizePolicy7.setHeightForWidth(self.TercInputMinCapital.sizePolicy().hasHeightForWidth())
        self.TercInputMinCapital.setSizePolicy(sizePolicy7)
        self.TercInputMinCapital.setMinimumSize(QSize(110, 30))
        self.TercInputMinCapital.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.TercInputMinCapital.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.TercInputMinCapital.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_127.addWidget(self.TercInputMinCapital, 0, 1, 1, 1)

        self.SecuLabelCostoOM_3 = QLabel(self.row_64)
        self.SecuLabelCostoOM_3.setObjectName(u"SecuLabelCostoOM_3")
        sizePolicy8.setHeightForWidth(self.SecuLabelCostoOM_3.sizePolicy().hasHeightForWidth())
        self.SecuLabelCostoOM_3.setSizePolicy(sizePolicy8)
        self.SecuLabelCostoOM_3.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.SecuLabelCostoOM_3.setLineWidth(1)
        self.SecuLabelCostoOM_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_127.addWidget(self.SecuLabelCostoOM_3, 1, 0, 1, 1)

        self.TercLabelCostoCapital = QLabel(self.row_64)
        self.TercLabelCostoCapital.setObjectName(u"TercLabelCostoCapital")
        sizePolicy8.setHeightForWidth(self.TercLabelCostoCapital.sizePolicy().hasHeightForWidth())
        self.TercLabelCostoCapital.setSizePolicy(sizePolicy8)
        self.TercLabelCostoCapital.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.TercLabelCostoCapital.setLineWidth(1)
        self.TercLabelCostoCapital.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_127.addWidget(self.TercLabelCostoCapital, 0, 0, 1, 1)

        self.TercInputMinOM = QLineEdit(self.row_64)
        self.TercInputMinOM.setObjectName(u"TercInputMinOM")
        sizePolicy7.setHeightForWidth(self.TercInputMinOM.sizePolicy().hasHeightForWidth())
        self.TercInputMinOM.setSizePolicy(sizePolicy7)
        self.TercInputMinOM.setMinimumSize(QSize(110, 30))
        self.TercInputMinOM.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.TercInputMinOM.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.TercInputMinOM.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_127.addWidget(self.TercInputMinOM, 1, 1, 1, 1)

        self.TercInputMaxCapital = QLineEdit(self.row_64)
        self.TercInputMaxCapital.setObjectName(u"TercInputMaxCapital")
        sizePolicy7.setHeightForWidth(self.TercInputMaxCapital.sizePolicy().hasHeightForWidth())
        self.TercInputMaxCapital.setSizePolicy(sizePolicy7)
        self.TercInputMaxCapital.setMinimumSize(QSize(110, 30))
        self.TercInputMaxCapital.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.TercInputMaxCapital.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.TercInputMaxCapital.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_127.addWidget(self.TercInputMaxCapital, 0, 2, 1, 1)

        self.TercInputMaxOM = QLineEdit(self.row_64)
        self.TercInputMaxOM.setObjectName(u"TercInputMaxOM")
        sizePolicy7.setHeightForWidth(self.TercInputMaxOM.sizePolicy().hasHeightForWidth())
        self.TercInputMaxOM.setSizePolicy(sizePolicy7)
        self.TercInputMaxOM.setMinimumSize(QSize(110, 30))
        self.TercInputMaxOM.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.TercInputMaxOM.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.TercInputMaxOM.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_127.addWidget(self.TercInputMaxOM, 1, 2, 1, 1)


        self.verticalLayout_84.addLayout(self.gridLayout_127)


        self.gridLayout_126.addWidget(self.row_64, 0, 1, 1, 1)


        self.verticalLayout_35.addWidget(self.groupBox_Propiedades_36)

        self.groupBox_Propiedades_37 = QGroupBox(self.layoutWidget_3)
        self.groupBox_Propiedades_37.setObjectName(u"groupBox_Propiedades_37")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_37.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_37.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_37.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_37.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_37.setStyleSheet(u"QGroupBox {\n"
"color: rgb(255, 244, 119);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(255, 244, 119);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_37.setAlignment(Qt.AlignCenter)
        self.gridLayout_128 = QGridLayout(self.groupBox_Propiedades_37)
        self.gridLayout_128.setObjectName(u"gridLayout_128")
        self.row_65 = QFrame(self.groupBox_Propiedades_37)
        self.row_65.setObjectName(u"row_65")
        self.row_65.setStyleSheet(u"")
        self.row_65.setFrameShape(QFrame.StyledPanel)
        self.row_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.row_65)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_129 = QGridLayout()
        self.gridLayout_129.setObjectName(u"gridLayout_129")
        self.gridLayout_129.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_129.setHorizontalSpacing(35)
        self.gridLayout_129.setVerticalSpacing(10)
        self.gridLayout_129.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelEnergia_4 = QLabel(self.row_65)
        self.PrimLabelEnergia_4.setObjectName(u"PrimLabelEnergia_4")
        sizePolicy8.setHeightForWidth(self.PrimLabelEnergia_4.sizePolicy().hasHeightForWidth())
        self.PrimLabelEnergia_4.setSizePolicy(sizePolicy8)
        self.PrimLabelEnergia_4.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelEnergia_4.setLineWidth(1)
        self.PrimLabelEnergia_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_129.addWidget(self.PrimLabelEnergia_4, 1, 0, 1, 1)

        self.PrimLabelRecuperacion_4 = QLabel(self.row_65)
        self.PrimLabelRecuperacion_4.setObjectName(u"PrimLabelRecuperacion_4")
        sizePolicy8.setHeightForWidth(self.PrimLabelRecuperacion_4.sizePolicy().hasHeightForWidth())
        self.PrimLabelRecuperacion_4.setSizePolicy(sizePolicy8)
        self.PrimLabelRecuperacion_4.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelRecuperacion_4.setLineWidth(1)
        self.PrimLabelRecuperacion_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_129.addWidget(self.PrimLabelRecuperacion_4, 0, 0, 1, 1)

        self.TercComboBoxRecuperacion = QComboBox(self.row_65)
        self.TercComboBoxRecuperacion.addItem("")
        self.TercComboBoxRecuperacion.addItem("")
        self.TercComboBoxRecuperacion.addItem("")
        self.TercComboBoxRecuperacion.addItem("")
        self.TercComboBoxRecuperacion.addItem("")
        self.TercComboBoxRecuperacion.setObjectName(u"TercComboBoxRecuperacion")
        self.TercComboBoxRecuperacion.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.TercComboBoxRecuperacion.sizePolicy().hasHeightForWidth())
        self.TercComboBoxRecuperacion.setSizePolicy(sizePolicy4)
        self.TercComboBoxRecuperacion.setMinimumSize(QSize(200, 35))
        self.TercComboBoxRecuperacion.setMaximumSize(QSize(150, 30))
        self.TercComboBoxRecuperacion.setLayoutDirection(Qt.LeftToRight)
        self.TercComboBoxRecuperacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.TercComboBoxRecuperacion.setEditable(False)
        self.TercComboBoxRecuperacion.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.TercComboBoxRecuperacion.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_129.addWidget(self.TercComboBoxRecuperacion, 0, 1, 1, 1)

        self.TercComboBoxEnergia = QComboBox(self.row_65)
        self.TercComboBoxEnergia.addItem("")
        self.TercComboBoxEnergia.addItem("")
        self.TercComboBoxEnergia.addItem("")
        self.TercComboBoxEnergia.addItem("")
        self.TercComboBoxEnergia.addItem("")
        self.TercComboBoxEnergia.setObjectName(u"TercComboBoxEnergia")
        self.TercComboBoxEnergia.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.TercComboBoxEnergia.sizePolicy().hasHeightForWidth())
        self.TercComboBoxEnergia.setSizePolicy(sizePolicy4)
        self.TercComboBoxEnergia.setMinimumSize(QSize(200, 35))
        self.TercComboBoxEnergia.setMaximumSize(QSize(150, 30))
        self.TercComboBoxEnergia.setLayoutDirection(Qt.LeftToRight)
        self.TercComboBoxEnergia.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.TercComboBoxEnergia.setEditable(False)
        self.TercComboBoxEnergia.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.TercComboBoxEnergia.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_129.addWidget(self.TercComboBoxEnergia, 1, 1, 1, 1)


        self.verticalLayout_85.addLayout(self.gridLayout_129)


        self.gridLayout_128.addWidget(self.row_65, 0, 1, 1, 1)


        self.verticalLayout_35.addWidget(self.groupBox_Propiedades_37)

        self.groupBox_Propiedades_38 = QGroupBox(self.layoutWidget_3)
        self.groupBox_Propiedades_38.setObjectName(u"groupBox_Propiedades_38")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_38.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_38.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_38.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_38.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_38.setStyleSheet(u"QGroupBox {\n"
"color: rgb(255, 244, 119);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(255, 244, 119);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_38.setAlignment(Qt.AlignCenter)
        self.gridLayout_130 = QGridLayout(self.groupBox_Propiedades_38)
        self.gridLayout_130.setObjectName(u"gridLayout_130")
        self.row_66 = QFrame(self.groupBox_Propiedades_38)
        self.row_66.setObjectName(u"row_66")
        self.row_66.setStyleSheet(u"")
        self.row_66.setFrameShape(QFrame.StyledPanel)
        self.row_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.row_66)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_131 = QGridLayout()
        self.gridLayout_131.setObjectName(u"gridLayout_131")
        self.gridLayout_131.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_131.setHorizontalSpacing(35)
        self.gridLayout_131.setVerticalSpacing(10)
        self.gridLayout_131.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelRobustez_4 = QLabel(self.row_66)
        self.PrimLabelRobustez_4.setObjectName(u"PrimLabelRobustez_4")
        sizePolicy8.setHeightForWidth(self.PrimLabelRobustez_4.sizePolicy().hasHeightForWidth())
        self.PrimLabelRobustez_4.setSizePolicy(sizePolicy8)
        self.PrimLabelRobustez_4.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelRobustez_4.setLineWidth(1)
        self.PrimLabelRobustez_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_131.addWidget(self.PrimLabelRobustez_4, 1, 0, 1, 1)

        self.PrimLabelSimplicidad_4 = QLabel(self.row_66)
        self.PrimLabelSimplicidad_4.setObjectName(u"PrimLabelSimplicidad_4")
        sizePolicy8.setHeightForWidth(self.PrimLabelSimplicidad_4.sizePolicy().hasHeightForWidth())
        self.PrimLabelSimplicidad_4.setSizePolicy(sizePolicy8)
        self.PrimLabelSimplicidad_4.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelSimplicidad_4.setLineWidth(1)
        self.PrimLabelSimplicidad_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_131.addWidget(self.PrimLabelSimplicidad_4, 0, 0, 1, 1)

        self.TercComboBoxSimplicidad = QComboBox(self.row_66)
        self.TercComboBoxSimplicidad.addItem("")
        self.TercComboBoxSimplicidad.addItem("")
        self.TercComboBoxSimplicidad.addItem("")
        self.TercComboBoxSimplicidad.addItem("")
        self.TercComboBoxSimplicidad.addItem("")
        self.TercComboBoxSimplicidad.setObjectName(u"TercComboBoxSimplicidad")
        self.TercComboBoxSimplicidad.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.TercComboBoxSimplicidad.sizePolicy().hasHeightForWidth())
        self.TercComboBoxSimplicidad.setSizePolicy(sizePolicy4)
        self.TercComboBoxSimplicidad.setMinimumSize(QSize(200, 35))
        self.TercComboBoxSimplicidad.setMaximumSize(QSize(150, 30))
        self.TercComboBoxSimplicidad.setLayoutDirection(Qt.LeftToRight)
        self.TercComboBoxSimplicidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.TercComboBoxSimplicidad.setEditable(False)
        self.TercComboBoxSimplicidad.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.TercComboBoxSimplicidad.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_131.addWidget(self.TercComboBoxSimplicidad, 0, 1, 1, 1)

        self.TercComboBoxRobustez = QComboBox(self.row_66)
        self.TercComboBoxRobustez.addItem("")
        self.TercComboBoxRobustez.addItem("")
        self.TercComboBoxRobustez.addItem("")
        self.TercComboBoxRobustez.addItem("")
        self.TercComboBoxRobustez.addItem("")
        self.TercComboBoxRobustez.setObjectName(u"TercComboBoxRobustez")
        self.TercComboBoxRobustez.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.TercComboBoxRobustez.sizePolicy().hasHeightForWidth())
        self.TercComboBoxRobustez.setSizePolicy(sizePolicy4)
        self.TercComboBoxRobustez.setMinimumSize(QSize(200, 35))
        self.TercComboBoxRobustez.setMaximumSize(QSize(150, 30))
        self.TercComboBoxRobustez.setLayoutDirection(Qt.LeftToRight)
        self.TercComboBoxRobustez.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.TercComboBoxRobustez.setEditable(False)
        self.TercComboBoxRobustez.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.TercComboBoxRobustez.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_131.addWidget(self.TercComboBoxRobustez, 1, 1, 1, 1)

        self.PrimLabelArea_4 = QLabel(self.row_66)
        self.PrimLabelArea_4.setObjectName(u"PrimLabelArea_4")
        sizePolicy8.setHeightForWidth(self.PrimLabelArea_4.sizePolicy().hasHeightForWidth())
        self.PrimLabelArea_4.setSizePolicy(sizePolicy8)
        self.PrimLabelArea_4.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelArea_4.setLineWidth(1)
        self.PrimLabelArea_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_131.addWidget(self.PrimLabelArea_4, 2, 0, 1, 1)

        self.TercComboBoxArea = QComboBox(self.row_66)
        self.TercComboBoxArea.addItem("")
        self.TercComboBoxArea.addItem("")
        self.TercComboBoxArea.addItem("")
        self.TercComboBoxArea.addItem("")
        self.TercComboBoxArea.addItem("")
        self.TercComboBoxArea.setObjectName(u"TercComboBoxArea")
        self.TercComboBoxArea.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.TercComboBoxArea.sizePolicy().hasHeightForWidth())
        self.TercComboBoxArea.setSizePolicy(sizePolicy4)
        self.TercComboBoxArea.setMinimumSize(QSize(200, 35))
        self.TercComboBoxArea.setMaximumSize(QSize(150, 30))
        self.TercComboBoxArea.setLayoutDirection(Qt.LeftToRight)
        self.TercComboBoxArea.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.TercComboBoxArea.setEditable(False)
        self.TercComboBoxArea.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.TercComboBoxArea.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_131.addWidget(self.TercComboBoxArea, 2, 1, 1, 1)


        self.verticalLayout_86.addLayout(self.gridLayout_131)


        self.gridLayout_130.addWidget(self.row_66, 0, 1, 1, 1)


        self.verticalLayout_35.addWidget(self.groupBox_Propiedades_38)

        self.groupBox_Propiedades_39 = QGroupBox(self.layoutWidget_3)
        self.groupBox_Propiedades_39.setObjectName(u"groupBox_Propiedades_39")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_39.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_39.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_39.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_39.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_39.setStyleSheet(u"QGroupBox {\n"
"color: rgb(255, 244, 119);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(255, 244, 119);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_39.setAlignment(Qt.AlignCenter)
        self.gridLayout_132 = QGridLayout(self.groupBox_Propiedades_39)
        self.gridLayout_132.setObjectName(u"gridLayout_132")
        self.row_67 = QFrame(self.groupBox_Propiedades_39)
        self.row_67.setObjectName(u"row_67")
        self.row_67.setStyleSheet(u"")
        self.row_67.setFrameShape(QFrame.StyledPanel)
        self.row_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.row_67)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_133 = QGridLayout()
        self.gridLayout_133.setObjectName(u"gridLayout_133")
        self.gridLayout_133.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_133.setHorizontalSpacing(35)
        self.gridLayout_133.setVerticalSpacing(10)
        self.gridLayout_133.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelSocial_4 = QLabel(self.row_67)
        self.PrimLabelSocial_4.setObjectName(u"PrimLabelSocial_4")
        sizePolicy8.setHeightForWidth(self.PrimLabelSocial_4.sizePolicy().hasHeightForWidth())
        self.PrimLabelSocial_4.setSizePolicy(sizePolicy8)
        self.PrimLabelSocial_4.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelSocial_4.setLineWidth(1)
        self.PrimLabelSocial_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_133.addWidget(self.PrimLabelSocial_4, 0, 0, 1, 1)

        self.TercComboBoxSocial = QComboBox(self.row_67)
        self.TercComboBoxSocial.addItem("")
        self.TercComboBoxSocial.addItem("")
        self.TercComboBoxSocial.addItem("")
        self.TercComboBoxSocial.addItem("")
        self.TercComboBoxSocial.addItem("")
        self.TercComboBoxSocial.setObjectName(u"TercComboBoxSocial")
        self.TercComboBoxSocial.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.TercComboBoxSocial.sizePolicy().hasHeightForWidth())
        self.TercComboBoxSocial.setSizePolicy(sizePolicy4)
        self.TercComboBoxSocial.setMinimumSize(QSize(200, 35))
        self.TercComboBoxSocial.setMaximumSize(QSize(150, 30))
        self.TercComboBoxSocial.setLayoutDirection(Qt.LeftToRight)
        self.TercComboBoxSocial.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.TercComboBoxSocial.setEditable(False)
        self.TercComboBoxSocial.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.TercComboBoxSocial.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_133.addWidget(self.TercComboBoxSocial, 0, 1, 1, 1)


        self.verticalLayout_87.addLayout(self.gridLayout_133)


        self.gridLayout_132.addWidget(self.row_67, 0, 1, 1, 1)


        self.verticalLayout_35.addWidget(self.groupBox_Propiedades_39)

        self.PrimInputParametro_16 = QLineEdit(self.terciarioEntrada)
        self.PrimInputParametro_16.setObjectName(u"PrimInputParametro_16")
        self.PrimInputParametro_16.setGeometry(QRect(780, 460, 265, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_16.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_16.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_16.setMinimumSize(QSize(265, 2))
        self.PrimInputParametro_16.setMaximumSize(QSize(250, 2))
        self.PrimInputParametro_16.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.PrimLabelMaxCriterio_8 = QLabel(self.terciarioEntrada)
        self.PrimLabelMaxCriterio_8.setObjectName(u"PrimLabelMaxCriterio_8")
        self.PrimLabelMaxCriterio_8.setGeometry(QRect(780, 360, 265, 21))
        sizePolicy6.setHeightForWidth(self.PrimLabelMaxCriterio_8.sizePolicy().hasHeightForWidth())
        self.PrimLabelMaxCriterio_8.setSizePolicy(sizePolicy6)
        self.PrimLabelMaxCriterio_8.setMinimumSize(QSize(265, 0))
        self.PrimLabelMaxCriterio_8.setMaximumSize(QSize(265, 16777215))
        self.PrimLabelMaxCriterio_8.setStyleSheet(u"font: 600 12pt \"Allerta\";\n"
"background-color: rgb(244, 229, 145);\n"
"color: rgb(255, 255, 255);")
        self.PrimLabelMaxCriterio_8.setTextFormat(Qt.AutoText)
        self.PrimLabelMaxCriterio_8.setAlignment(Qt.AlignCenter)
        self.tabTerc.addTab(self.terciarioEntrada, "")
        self.terciarioResultado = QWidget()
        self.terciarioResultado.setObjectName(u"terciarioResultado")
        self.TercBtnReiniciar = QPushButton(self.terciarioResultado)
        self.TercBtnReiniciar.setObjectName(u"TercBtnReiniciar")
        self.TercBtnReiniciar.setEnabled(True)
        self.TercBtnReiniciar.setGeometry(QRect(810, 210, 250, 50))
        sizePolicy10.setHeightForWidth(self.TercBtnReiniciar.sizePolicy().hasHeightForWidth())
        self.TercBtnReiniciar.setSizePolicy(sizePolicy10)
        self.TercBtnReiniciar.setMinimumSize(QSize(250, 50))
        self.TercBtnReiniciar.setMaximumSize(QSize(40, 40))
        self.TercBtnReiniciar.setStyleSheet(u"background-color: rgb(163, 160, 159);\n"
"border-width: 5px;\n"
"border-color: rgb(163, 160, 159);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Allerta\";\n"
"\n"
"")
        self.PrimInputParametro_17 = QLineEdit(self.terciarioResultado)
        self.PrimInputParametro_17.setObjectName(u"PrimInputParametro_17")
        self.PrimInputParametro_17.setGeometry(QRect(300, 100, 475, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_17.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_17.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_17.setMinimumSize(QSize(475, 2))
        self.PrimInputParametro_17.setMaximumSize(QSize(475, 2))
        self.PrimInputParametro_17.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.PrimLabelConvencional_9 = QLabel(self.terciarioResultado)
        self.PrimLabelConvencional_9.setObjectName(u"PrimLabelConvencional_9")
        self.PrimLabelConvencional_9.setGeometry(QRect(10, 50, 1061, 35))
        sizePolicy9.setHeightForWidth(self.PrimLabelConvencional_9.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_9.setSizePolicy(sizePolicy9)
        self.PrimLabelConvencional_9.setStyleSheet(u"font: 650 25pt \"Allerta\";\n"
"")
        self.PrimLabelConvencional_9.setLineWidth(1)
        self.PrimLabelConvencional_9.setAlignment(Qt.AlignCenter)
        self.PrimInputParametro_18 = QLineEdit(self.terciarioResultado)
        self.PrimInputParametro_18.setObjectName(u"PrimInputParametro_18")
        self.PrimInputParametro_18.setGeometry(QRect(300, 40, 475, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_18.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_18.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_18.setMinimumSize(QSize(475, 2))
        self.PrimInputParametro_18.setMaximumSize(QSize(475, 2))
        self.PrimInputParametro_18.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.groupBox_Propiedades_40 = QGroupBox(self.terciarioResultado)
        self.groupBox_Propiedades_40.setObjectName(u"groupBox_Propiedades_40")
        self.groupBox_Propiedades_40.setGeometry(QRect(20, 130, 770, 291))
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_40.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_40.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_40.setMinimumSize(QSize(770, 0))
        self.groupBox_Propiedades_40.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_40.setStyleSheet(u"QGroupBox {\n"
"color: rgb(244, 229, 145);\n"
"font: bold; \n"
"border: 2px solid;\n"
"font: 700 11pt \"Allerta\";\n"
"border-color: rgb(244, 229, 145);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_40.setAlignment(Qt.AlignCenter)
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_Propiedades_40)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.row_68 = QFrame(self.groupBox_Propiedades_40)
        self.row_68.setObjectName(u"row_68")
        self.row_68.setStyleSheet(u"")
        self.row_68.setFrameShape(QFrame.StyledPanel)
        self.row_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.row_68)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_134 = QGridLayout()
        self.gridLayout_134.setObjectName(u"gridLayout_134")
        self.gridLayout_134.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_134.setHorizontalSpacing(35)
        self.gridLayout_134.setVerticalSpacing(10)
        self.gridLayout_134.setContentsMargins(20, 10, 20, 10)
        self.TercFieldResultadoAO = QLineEdit(self.row_68)
        self.TercFieldResultadoAO.setObjectName(u"TercFieldResultadoAO")
        sizePolicy9.setHeightForWidth(self.TercFieldResultadoAO.sizePolicy().hasHeightForWidth())
        self.TercFieldResultadoAO.setSizePolicy(sizePolicy9)
        self.TercFieldResultadoAO.setMinimumSize(QSize(110, 35))
        self.TercFieldResultadoAO.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.TercFieldResultadoAO.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.TercFieldResultadoAO.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.TercFieldResultadoAO.setAlignment(Qt.AlignCenter)

        self.gridLayout_134.addWidget(self.TercFieldResultadoAO, 0, 1, 1, 1)

        self.PrimLabelConvencional_10 = QLabel(self.row_68)
        self.PrimLabelConvencional_10.setObjectName(u"PrimLabelConvencional_10")
        sizePolicy8.setHeightForWidth(self.PrimLabelConvencional_10.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_10.setSizePolicy(sizePolicy8)
        self.PrimLabelConvencional_10.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelConvencional_10.setLineWidth(1)
        self.PrimLabelConvencional_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_134.addWidget(self.PrimLabelConvencional_10, 0, 0, 1, 1)

        self.PrimLabelTQA_10 = QLabel(self.row_68)
        self.PrimLabelTQA_10.setObjectName(u"PrimLabelTQA_10")
        sizePolicy8.setHeightForWidth(self.PrimLabelTQA_10.sizePolicy().hasHeightForWidth())
        self.PrimLabelTQA_10.setSizePolicy(sizePolicy8)
        self.PrimLabelTQA_10.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelTQA_10.setLineWidth(1)
        self.PrimLabelTQA_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_134.addWidget(self.PrimLabelTQA_10, 1, 0, 1, 1)

        self.PrimLabelTQA_11 = QLabel(self.row_68)
        self.PrimLabelTQA_11.setObjectName(u"PrimLabelTQA_11")
        sizePolicy8.setHeightForWidth(self.PrimLabelTQA_11.sizePolicy().hasHeightForWidth())
        self.PrimLabelTQA_11.setSizePolicy(sizePolicy8)
        self.PrimLabelTQA_11.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelTQA_11.setLineWidth(1)
        self.PrimLabelTQA_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_134.addWidget(self.PrimLabelTQA_11, 2, 0, 1, 1)

        self.TercFieldResultadoPhoStrip = QLineEdit(self.row_68)
        self.TercFieldResultadoPhoStrip.setObjectName(u"TercFieldResultadoPhoStrip")
        sizePolicy9.setHeightForWidth(self.TercFieldResultadoPhoStrip.sizePolicy().hasHeightForWidth())
        self.TercFieldResultadoPhoStrip.setSizePolicy(sizePolicy9)
        self.TercFieldResultadoPhoStrip.setMinimumSize(QSize(110, 35))
        self.TercFieldResultadoPhoStrip.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.TercFieldResultadoPhoStrip.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.TercFieldResultadoPhoStrip.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.TercFieldResultadoPhoStrip.setAlignment(Qt.AlignCenter)

        self.gridLayout_134.addWidget(self.TercFieldResultadoPhoStrip, 1, 1, 1, 1)

        self.TercFieldResultadoBardenpho = QLineEdit(self.row_68)
        self.TercFieldResultadoBardenpho.setObjectName(u"TercFieldResultadoBardenpho")
        sizePolicy9.setHeightForWidth(self.TercFieldResultadoBardenpho.sizePolicy().hasHeightForWidth())
        self.TercFieldResultadoBardenpho.setSizePolicy(sizePolicy9)
        self.TercFieldResultadoBardenpho.setMinimumSize(QSize(110, 35))
        self.TercFieldResultadoBardenpho.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.TercFieldResultadoBardenpho.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.TercFieldResultadoBardenpho.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.TercFieldResultadoBardenpho.setAlignment(Qt.AlignCenter)

        self.gridLayout_134.addWidget(self.TercFieldResultadoBardenpho, 2, 1, 1, 1)


        self.verticalLayout_88.addLayout(self.gridLayout_134)


        self.verticalLayout_36.addWidget(self.row_68)

        self.TercBtnCalcular = QPushButton(self.terciarioResultado)
        self.TercBtnCalcular.setObjectName(u"TercBtnCalcular")
        self.TercBtnCalcular.setEnabled(True)
        self.TercBtnCalcular.setGeometry(QRect(810, 140, 250, 50))
        sizePolicy10.setHeightForWidth(self.TercBtnCalcular.sizePolicy().hasHeightForWidth())
        self.TercBtnCalcular.setSizePolicy(sizePolicy10)
        self.TercBtnCalcular.setMinimumSize(QSize(250, 50))
        self.TercBtnCalcular.setMaximumSize(QSize(40, 40))
        self.TercBtnCalcular.setStyleSheet(u"background-color: rgb(163, 160, 159);\n"
"border-width: 5px;\n"
"border-color: rgb(163, 160, 159);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Allerta\";\n"
"\n"
"")
        self.TercBtnCalcular.setCheckable(False)
        self.TercBtnCalcular.setChecked(False)
        self.TercBtnCalcular.setAutoDefault(False)
        self.groupBox_Propiedades_48 = QGroupBox(self.terciarioResultado)
        self.groupBox_Propiedades_48.setObjectName(u"groupBox_Propiedades_48")
        self.groupBox_Propiedades_48.setGeometry(QRect(20, 440, 770, 131))
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_48.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_48.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_48.setMinimumSize(QSize(770, 0))
        self.groupBox_Propiedades_48.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_48.setStyleSheet(u"QGroupBox {\n"
"color: rgb(244, 229, 145);\n"
"font: bold; \n"
"border: 2px solid;\n"
"font: 700 11pt \"Allerta\";\n"
"border-color: rgb(244, 229, 145);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_48.setAlignment(Qt.AlignCenter)
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_Propiedades_48)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.row_76 = QFrame(self.groupBox_Propiedades_48)
        self.row_76.setObjectName(u"row_76")
        self.row_76.setStyleSheet(u"")
        self.row_76.setFrameShape(QFrame.StyledPanel)
        self.row_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.row_76)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_146 = QGridLayout()
        self.gridLayout_146.setObjectName(u"gridLayout_146")
        self.gridLayout_146.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_146.setHorizontalSpacing(35)
        self.gridLayout_146.setVerticalSpacing(10)
        self.gridLayout_146.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelConvencional_17 = QLabel(self.row_76)
        self.PrimLabelConvencional_17.setObjectName(u"PrimLabelConvencional_17")
        sizePolicy8.setHeightForWidth(self.PrimLabelConvencional_17.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_17.setSizePolicy(sizePolicy8)
        self.PrimLabelConvencional_17.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelConvencional_17.setLineWidth(1)
        self.PrimLabelConvencional_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_146.addWidget(self.PrimLabelConvencional_17, 0, 0, 1, 1)

        self.TercFieldResultadoMejor = QLineEdit(self.row_76)
        self.TercFieldResultadoMejor.setObjectName(u"TercFieldResultadoMejor")
        self.TercFieldResultadoMejor.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.TercFieldResultadoMejor.sizePolicy().hasHeightForWidth())
        self.TercFieldResultadoMejor.setSizePolicy(sizePolicy9)
        self.TercFieldResultadoMejor.setMinimumSize(QSize(110, 35))
        self.TercFieldResultadoMejor.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.TercFieldResultadoMejor.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.TercFieldResultadoMejor.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.TercFieldResultadoMejor.setAlignment(Qt.AlignCenter)

        self.gridLayout_146.addWidget(self.TercFieldResultadoMejor, 0, 1, 1, 1)


        self.verticalLayout_96.addLayout(self.gridLayout_146)


        self.verticalLayout_26.addWidget(self.row_76)

        self.tabTerc.addTab(self.terciarioResultado, "")
        self.stackedWidget.addWidget(self.pagina_Terciario)
        self.pagina_NoC = QWidget()
        self.pagina_NoC.setObjectName(u"pagina_NoC")
        self.tabNoC = QTabWidget(self.pagina_NoC)
        self.tabNoC.setObjectName(u"tabNoC")
        self.tabNoC.setGeometry(QRect(0, 0, 1131, 621))
        sizePolicy4.setHeightForWidth(self.tabNoC.sizePolicy().hasHeightForWidth())
        self.tabNoC.setSizePolicy(sizePolicy4)
        self.tabNoC.setStyleSheet(u"font: 500 10pt \"Allerta\";\n"
"color: rgb(79, 79, 79);")
        self.tabNoC.setTabPosition(QTabWidget.West)
        self.tabNoC.setTabsClosable(False)
        self.NoConvEntrada = QWidget()
        self.NoConvEntrada.setObjectName(u"NoConvEntrada")
        self.NoConvEntrada.setStyleSheet(u"font: 500 11pt \"Allerta\";")
        self.NoCComboBoxPeso = QComboBox(self.NoConvEntrada)
        self.NoCComboBoxPeso.addItem("")
        self.NoCComboBoxPeso.addItem("")
        self.NoCComboBoxPeso.addItem("")
        self.NoCComboBoxPeso.addItem("")
        self.NoCComboBoxPeso.addItem("")
        self.NoCComboBoxPeso.setObjectName(u"NoCComboBoxPeso")
        self.NoCComboBoxPeso.setEnabled(True)
        self.NoCComboBoxPeso.setGeometry(QRect(810, 400, 200, 35))
        sizePolicy4.setHeightForWidth(self.NoCComboBoxPeso.sizePolicy().hasHeightForWidth())
        self.NoCComboBoxPeso.setSizePolicy(sizePolicy4)
        self.NoCComboBoxPeso.setMinimumSize(QSize(200, 35))
        self.NoCComboBoxPeso.setMaximumSize(QSize(150, 30))
        self.NoCComboBoxPeso.setLayoutDirection(Qt.LeftToRight)
        self.NoCComboBoxPeso.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.NoCComboBoxPeso.setEditable(False)
        self.NoCComboBoxPeso.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.NoCComboBoxPeso.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.PrimInputParametro_19 = QLineEdit(self.NoConvEntrada)
        self.PrimInputParametro_19.setObjectName(u"PrimInputParametro_19")
        self.PrimInputParametro_19.setGeometry(QRect(780, 350, 265, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_19.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_19.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_19.setMinimumSize(QSize(265, 2))
        self.PrimInputParametro_19.setMaximumSize(QSize(250, 2))
        self.PrimInputParametro_19.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.groupBox_Resultados_23 = QGroupBox(self.NoConvEntrada)
        self.groupBox_Resultados_23.setObjectName(u"groupBox_Resultados_23")
        self.groupBox_Resultados_23.setGeometry(QRect(739, 10, 341, 281))
        sizePolicy5.setHeightForWidth(self.groupBox_Resultados_23.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_23.setSizePolicy(sizePolicy5)
        self.groupBox_Resultados_23.setMinimumSize(QSize(300, 0))
        self.groupBox_Resultados_23.setMaximumSize(QSize(450, 16777215))
        self.groupBox_Resultados_23.setStyleSheet(u"QGroupBox {\n"
"color: rgb(190, 190, 190);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(190, 190, 190);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.gridLayout_87 = QGridLayout(self.groupBox_Resultados_23)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.row_44 = QFrame(self.groupBox_Resultados_23)
        self.row_44.setObjectName(u"row_44")
        self.row_44.setStyleSheet(u"")
        self.row_44.setFrameShape(QFrame.StyledPanel)
        self.row_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.row_44)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_92 = QGridLayout()
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.gridLayout_92.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_92.setHorizontalSpacing(10)
        self.gridLayout_92.setVerticalSpacing(15)
        self.gridLayout_92.setContentsMargins(10, 10, 10, 10)
        self.NoCComboBoxCriterio = QComboBox(self.row_44)
        self.NoCComboBoxCriterio.addItem("")
        self.NoCComboBoxCriterio.addItem("")
        self.NoCComboBoxCriterio.addItem("")
        self.NoCComboBoxCriterio.addItem("")
        self.NoCComboBoxCriterio.addItem("")
        self.NoCComboBoxCriterio.setObjectName(u"NoCComboBoxCriterio")
        self.NoCComboBoxCriterio.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.NoCComboBoxCriterio.sizePolicy().hasHeightForWidth())
        self.NoCComboBoxCriterio.setSizePolicy(sizePolicy4)
        self.NoCComboBoxCriterio.setMinimumSize(QSize(170, 35))
        self.NoCComboBoxCriterio.setMaximumSize(QSize(170, 30))
        self.NoCComboBoxCriterio.setLayoutDirection(Qt.LeftToRight)
        self.NoCComboBoxCriterio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.NoCComboBoxCriterio.setEditable(False)
        self.NoCComboBoxCriterio.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.NoCComboBoxCriterio.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_92.addWidget(self.NoCComboBoxCriterio, 1, 1, 1, 1)

        self.NoCInputMinCriterio = QLineEdit(self.row_44)
        self.NoCInputMinCriterio.setObjectName(u"NoCInputMinCriterio")
        sizePolicy6.setHeightForWidth(self.NoCInputMinCriterio.sizePolicy().hasHeightForWidth())
        self.NoCInputMinCriterio.setSizePolicy(sizePolicy6)
        self.NoCInputMinCriterio.setMinimumSize(QSize(170, 35))
        self.NoCInputMinCriterio.setMaximumSize(QSize(100, 16777215))
        self.NoCInputMinCriterio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_92.addWidget(self.NoCInputMinCriterio, 2, 1, 1, 1)

        self.NoCInputMaxCriterio = QLineEdit(self.row_44)
        self.NoCInputMaxCriterio.setObjectName(u"NoCInputMaxCriterio")
        sizePolicy6.setHeightForWidth(self.NoCInputMaxCriterio.sizePolicy().hasHeightForWidth())
        self.NoCInputMaxCriterio.setSizePolicy(sizePolicy6)
        self.NoCInputMaxCriterio.setMinimumSize(QSize(170, 35))
        self.NoCInputMaxCriterio.setMaximumSize(QSize(100, 16777215))
        self.NoCInputMaxCriterio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_92.addWidget(self.NoCInputMaxCriterio, 3, 1, 1, 1)

        self.PrimLabelMinCriteiro_5 = QLabel(self.row_44)
        self.PrimLabelMinCriteiro_5.setObjectName(u"PrimLabelMinCriteiro_5")
        sizePolicy6.setHeightForWidth(self.PrimLabelMinCriteiro_5.sizePolicy().hasHeightForWidth())
        self.PrimLabelMinCriteiro_5.setSizePolicy(sizePolicy6)
        self.PrimLabelMinCriteiro_5.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.PrimLabelMinCriteiro_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_92.addWidget(self.PrimLabelMinCriteiro_5, 2, 0, 1, 1)

        self.PrimLabelMaxCriterio_9 = QLabel(self.row_44)
        self.PrimLabelMaxCriterio_9.setObjectName(u"PrimLabelMaxCriterio_9")
        sizePolicy6.setHeightForWidth(self.PrimLabelMaxCriterio_9.sizePolicy().hasHeightForWidth())
        self.PrimLabelMaxCriterio_9.setSizePolicy(sizePolicy6)
        self.PrimLabelMaxCriterio_9.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.PrimLabelMaxCriterio_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_92.addWidget(self.PrimLabelMaxCriterio_9, 3, 0, 1, 1)

        self.PrimLabelCriterio_5 = QLabel(self.row_44)
        self.PrimLabelCriterio_5.setObjectName(u"PrimLabelCriterio_5")
        sizePolicy6.setHeightForWidth(self.PrimLabelCriterio_5.sizePolicy().hasHeightForWidth())
        self.PrimLabelCriterio_5.setSizePolicy(sizePolicy6)
        self.PrimLabelCriterio_5.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.PrimLabelCriterio_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_92.addWidget(self.PrimLabelCriterio_5, 1, 0, 1, 1)


        self.verticalLayout_64.addLayout(self.gridLayout_92)


        self.gridLayout_87.addWidget(self.row_44, 0, 0, 1, 1)

        self.layoutWidget_4 = QWidget(self.NoConvEntrada)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(20, 10, 692, 603))
        self.verticalLayout_43 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_43.setSpacing(6)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.groupBox_Propiedades_41 = QGroupBox(self.layoutWidget_4)
        self.groupBox_Propiedades_41.setObjectName(u"groupBox_Propiedades_41")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_41.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_41.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_41.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_41.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_41.setStyleSheet(u"QGroupBox {\n"
"color:rgb(118, 199, 158);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(118, 199, 158);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_41.setAlignment(Qt.AlignCenter)
        self.gridLayout_135 = QGridLayout(self.groupBox_Propiedades_41)
        self.gridLayout_135.setObjectName(u"gridLayout_135")
        self.row_69 = QFrame(self.groupBox_Propiedades_41)
        self.row_69.setObjectName(u"row_69")
        self.row_69.setStyleSheet(u"")
        self.row_69.setFrameShape(QFrame.StyledPanel)
        self.row_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.row_69)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_136 = QGridLayout()
        self.gridLayout_136.setObjectName(u"gridLayout_136")
        self.gridLayout_136.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_136.setHorizontalSpacing(35)
        self.gridLayout_136.setVerticalSpacing(10)
        self.gridLayout_136.setContentsMargins(20, 10, 20, 10)
        self.NoCInputMinCapital = QLineEdit(self.row_69)
        self.NoCInputMinCapital.setObjectName(u"NoCInputMinCapital")
        sizePolicy7.setHeightForWidth(self.NoCInputMinCapital.sizePolicy().hasHeightForWidth())
        self.NoCInputMinCapital.setSizePolicy(sizePolicy7)
        self.NoCInputMinCapital.setMinimumSize(QSize(110, 30))
        self.NoCInputMinCapital.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.NoCInputMinCapital.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.NoCInputMinCapital.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_136.addWidget(self.NoCInputMinCapital, 0, 1, 1, 1)

        self.SecuLabelCostoOM_4 = QLabel(self.row_69)
        self.SecuLabelCostoOM_4.setObjectName(u"SecuLabelCostoOM_4")
        sizePolicy8.setHeightForWidth(self.SecuLabelCostoOM_4.sizePolicy().hasHeightForWidth())
        self.SecuLabelCostoOM_4.setSizePolicy(sizePolicy8)
        self.SecuLabelCostoOM_4.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.SecuLabelCostoOM_4.setLineWidth(1)
        self.SecuLabelCostoOM_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_136.addWidget(self.SecuLabelCostoOM_4, 1, 0, 1, 1)

        self.TercLabelCostoCapital_2 = QLabel(self.row_69)
        self.TercLabelCostoCapital_2.setObjectName(u"TercLabelCostoCapital_2")
        sizePolicy8.setHeightForWidth(self.TercLabelCostoCapital_2.sizePolicy().hasHeightForWidth())
        self.TercLabelCostoCapital_2.setSizePolicy(sizePolicy8)
        self.TercLabelCostoCapital_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.TercLabelCostoCapital_2.setLineWidth(1)
        self.TercLabelCostoCapital_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_136.addWidget(self.TercLabelCostoCapital_2, 0, 0, 1, 1)

        self.NoCInputMinOM = QLineEdit(self.row_69)
        self.NoCInputMinOM.setObjectName(u"NoCInputMinOM")
        sizePolicy7.setHeightForWidth(self.NoCInputMinOM.sizePolicy().hasHeightForWidth())
        self.NoCInputMinOM.setSizePolicy(sizePolicy7)
        self.NoCInputMinOM.setMinimumSize(QSize(110, 30))
        self.NoCInputMinOM.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.NoCInputMinOM.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.NoCInputMinOM.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_136.addWidget(self.NoCInputMinOM, 1, 1, 1, 1)

        self.NoCInputMaxCapital = QLineEdit(self.row_69)
        self.NoCInputMaxCapital.setObjectName(u"NoCInputMaxCapital")
        sizePolicy7.setHeightForWidth(self.NoCInputMaxCapital.sizePolicy().hasHeightForWidth())
        self.NoCInputMaxCapital.setSizePolicy(sizePolicy7)
        self.NoCInputMaxCapital.setMinimumSize(QSize(110, 30))
        self.NoCInputMaxCapital.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.NoCInputMaxCapital.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.NoCInputMaxCapital.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_136.addWidget(self.NoCInputMaxCapital, 0, 2, 1, 1)

        self.NoCInputMaxOM = QLineEdit(self.row_69)
        self.NoCInputMaxOM.setObjectName(u"NoCInputMaxOM")
        sizePolicy7.setHeightForWidth(self.NoCInputMaxOM.sizePolicy().hasHeightForWidth())
        self.NoCInputMaxOM.setSizePolicy(sizePolicy7)
        self.NoCInputMaxOM.setMinimumSize(QSize(110, 30))
        self.NoCInputMaxOM.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.NoCInputMaxOM.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.NoCInputMaxOM.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";\n"
"")

        self.gridLayout_136.addWidget(self.NoCInputMaxOM, 1, 2, 1, 1)


        self.verticalLayout_89.addLayout(self.gridLayout_136)


        self.gridLayout_135.addWidget(self.row_69, 0, 1, 1, 1)


        self.verticalLayout_43.addWidget(self.groupBox_Propiedades_41)

        self.groupBox_Propiedades_42 = QGroupBox(self.layoutWidget_4)
        self.groupBox_Propiedades_42.setObjectName(u"groupBox_Propiedades_42")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_42.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_42.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_42.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_42.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_42.setStyleSheet(u"QGroupBox {\n"
"color: rgb(118, 199, 158);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(118, 199, 158);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_42.setAlignment(Qt.AlignCenter)
        self.gridLayout_137 = QGridLayout(self.groupBox_Propiedades_42)
        self.gridLayout_137.setObjectName(u"gridLayout_137")
        self.row_70 = QFrame(self.groupBox_Propiedades_42)
        self.row_70.setObjectName(u"row_70")
        self.row_70.setStyleSheet(u"")
        self.row_70.setFrameShape(QFrame.StyledPanel)
        self.row_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.row_70)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_138 = QGridLayout()
        self.gridLayout_138.setObjectName(u"gridLayout_138")
        self.gridLayout_138.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_138.setHorizontalSpacing(35)
        self.gridLayout_138.setVerticalSpacing(10)
        self.gridLayout_138.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelEnergia_5 = QLabel(self.row_70)
        self.PrimLabelEnergia_5.setObjectName(u"PrimLabelEnergia_5")
        sizePolicy8.setHeightForWidth(self.PrimLabelEnergia_5.sizePolicy().hasHeightForWidth())
        self.PrimLabelEnergia_5.setSizePolicy(sizePolicy8)
        self.PrimLabelEnergia_5.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelEnergia_5.setLineWidth(1)
        self.PrimLabelEnergia_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_138.addWidget(self.PrimLabelEnergia_5, 1, 0, 1, 1)

        self.PrimLabelRecuperacion_5 = QLabel(self.row_70)
        self.PrimLabelRecuperacion_5.setObjectName(u"PrimLabelRecuperacion_5")
        sizePolicy8.setHeightForWidth(self.PrimLabelRecuperacion_5.sizePolicy().hasHeightForWidth())
        self.PrimLabelRecuperacion_5.setSizePolicy(sizePolicy8)
        self.PrimLabelRecuperacion_5.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelRecuperacion_5.setLineWidth(1)
        self.PrimLabelRecuperacion_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_138.addWidget(self.PrimLabelRecuperacion_5, 0, 0, 1, 1)

        self.NoCComboBoxRecuperacion = QComboBox(self.row_70)
        self.NoCComboBoxRecuperacion.addItem("")
        self.NoCComboBoxRecuperacion.addItem("")
        self.NoCComboBoxRecuperacion.addItem("")
        self.NoCComboBoxRecuperacion.addItem("")
        self.NoCComboBoxRecuperacion.addItem("")
        self.NoCComboBoxRecuperacion.setObjectName(u"NoCComboBoxRecuperacion")
        self.NoCComboBoxRecuperacion.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.NoCComboBoxRecuperacion.sizePolicy().hasHeightForWidth())
        self.NoCComboBoxRecuperacion.setSizePolicy(sizePolicy4)
        self.NoCComboBoxRecuperacion.setMinimumSize(QSize(200, 35))
        self.NoCComboBoxRecuperacion.setMaximumSize(QSize(150, 30))
        self.NoCComboBoxRecuperacion.setLayoutDirection(Qt.LeftToRight)
        self.NoCComboBoxRecuperacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.NoCComboBoxRecuperacion.setEditable(False)
        self.NoCComboBoxRecuperacion.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.NoCComboBoxRecuperacion.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_138.addWidget(self.NoCComboBoxRecuperacion, 0, 1, 1, 1)

        self.NoCComboBoxEnergia = QComboBox(self.row_70)
        self.NoCComboBoxEnergia.addItem("")
        self.NoCComboBoxEnergia.addItem("")
        self.NoCComboBoxEnergia.addItem("")
        self.NoCComboBoxEnergia.addItem("")
        self.NoCComboBoxEnergia.addItem("")
        self.NoCComboBoxEnergia.setObjectName(u"NoCComboBoxEnergia")
        self.NoCComboBoxEnergia.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.NoCComboBoxEnergia.sizePolicy().hasHeightForWidth())
        self.NoCComboBoxEnergia.setSizePolicy(sizePolicy4)
        self.NoCComboBoxEnergia.setMinimumSize(QSize(200, 35))
        self.NoCComboBoxEnergia.setMaximumSize(QSize(150, 30))
        self.NoCComboBoxEnergia.setLayoutDirection(Qt.LeftToRight)
        self.NoCComboBoxEnergia.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.NoCComboBoxEnergia.setEditable(False)
        self.NoCComboBoxEnergia.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.NoCComboBoxEnergia.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_138.addWidget(self.NoCComboBoxEnergia, 1, 1, 1, 1)


        self.verticalLayout_90.addLayout(self.gridLayout_138)


        self.gridLayout_137.addWidget(self.row_70, 0, 1, 1, 1)


        self.verticalLayout_43.addWidget(self.groupBox_Propiedades_42)

        self.groupBox_Propiedades_43 = QGroupBox(self.layoutWidget_4)
        self.groupBox_Propiedades_43.setObjectName(u"groupBox_Propiedades_43")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_43.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_43.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_43.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_43.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_43.setStyleSheet(u"QGroupBox {\n"
"color: rgb(118, 199, 158);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(118, 199, 158);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_43.setAlignment(Qt.AlignCenter)
        self.gridLayout_139 = QGridLayout(self.groupBox_Propiedades_43)
        self.gridLayout_139.setObjectName(u"gridLayout_139")
        self.row_71 = QFrame(self.groupBox_Propiedades_43)
        self.row_71.setObjectName(u"row_71")
        self.row_71.setStyleSheet(u"")
        self.row_71.setFrameShape(QFrame.StyledPanel)
        self.row_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.row_71)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_140 = QGridLayout()
        self.gridLayout_140.setObjectName(u"gridLayout_140")
        self.gridLayout_140.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_140.setHorizontalSpacing(35)
        self.gridLayout_140.setVerticalSpacing(10)
        self.gridLayout_140.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelRobustez_5 = QLabel(self.row_71)
        self.PrimLabelRobustez_5.setObjectName(u"PrimLabelRobustez_5")
        sizePolicy8.setHeightForWidth(self.PrimLabelRobustez_5.sizePolicy().hasHeightForWidth())
        self.PrimLabelRobustez_5.setSizePolicy(sizePolicy8)
        self.PrimLabelRobustez_5.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelRobustez_5.setLineWidth(1)
        self.PrimLabelRobustez_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_140.addWidget(self.PrimLabelRobustez_5, 1, 0, 1, 1)

        self.PrimLabelSimplicidad_5 = QLabel(self.row_71)
        self.PrimLabelSimplicidad_5.setObjectName(u"PrimLabelSimplicidad_5")
        sizePolicy8.setHeightForWidth(self.PrimLabelSimplicidad_5.sizePolicy().hasHeightForWidth())
        self.PrimLabelSimplicidad_5.setSizePolicy(sizePolicy8)
        self.PrimLabelSimplicidad_5.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelSimplicidad_5.setLineWidth(1)
        self.PrimLabelSimplicidad_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_140.addWidget(self.PrimLabelSimplicidad_5, 0, 0, 1, 1)

        self.NoCComboBoxSimplicidad = QComboBox(self.row_71)
        self.NoCComboBoxSimplicidad.addItem("")
        self.NoCComboBoxSimplicidad.addItem("")
        self.NoCComboBoxSimplicidad.addItem("")
        self.NoCComboBoxSimplicidad.addItem("")
        self.NoCComboBoxSimplicidad.addItem("")
        self.NoCComboBoxSimplicidad.setObjectName(u"NoCComboBoxSimplicidad")
        self.NoCComboBoxSimplicidad.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.NoCComboBoxSimplicidad.sizePolicy().hasHeightForWidth())
        self.NoCComboBoxSimplicidad.setSizePolicy(sizePolicy4)
        self.NoCComboBoxSimplicidad.setMinimumSize(QSize(200, 35))
        self.NoCComboBoxSimplicidad.setMaximumSize(QSize(150, 30))
        self.NoCComboBoxSimplicidad.setLayoutDirection(Qt.LeftToRight)
        self.NoCComboBoxSimplicidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.NoCComboBoxSimplicidad.setEditable(False)
        self.NoCComboBoxSimplicidad.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.NoCComboBoxSimplicidad.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_140.addWidget(self.NoCComboBoxSimplicidad, 0, 1, 1, 1)

        self.NoCComboBoxRobustez = QComboBox(self.row_71)
        self.NoCComboBoxRobustez.addItem("")
        self.NoCComboBoxRobustez.addItem("")
        self.NoCComboBoxRobustez.addItem("")
        self.NoCComboBoxRobustez.addItem("")
        self.NoCComboBoxRobustez.addItem("")
        self.NoCComboBoxRobustez.setObjectName(u"NoCComboBoxRobustez")
        self.NoCComboBoxRobustez.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.NoCComboBoxRobustez.sizePolicy().hasHeightForWidth())
        self.NoCComboBoxRobustez.setSizePolicy(sizePolicy4)
        self.NoCComboBoxRobustez.setMinimumSize(QSize(200, 35))
        self.NoCComboBoxRobustez.setMaximumSize(QSize(150, 30))
        self.NoCComboBoxRobustez.setLayoutDirection(Qt.LeftToRight)
        self.NoCComboBoxRobustez.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.NoCComboBoxRobustez.setEditable(False)
        self.NoCComboBoxRobustez.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.NoCComboBoxRobustez.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_140.addWidget(self.NoCComboBoxRobustez, 1, 1, 1, 1)

        self.PrimLabelArea_5 = QLabel(self.row_71)
        self.PrimLabelArea_5.setObjectName(u"PrimLabelArea_5")
        sizePolicy8.setHeightForWidth(self.PrimLabelArea_5.sizePolicy().hasHeightForWidth())
        self.PrimLabelArea_5.setSizePolicy(sizePolicy8)
        self.PrimLabelArea_5.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelArea_5.setLineWidth(1)
        self.PrimLabelArea_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_140.addWidget(self.PrimLabelArea_5, 2, 0, 1, 1)

        self.NoCComboBoxArea = QComboBox(self.row_71)
        self.NoCComboBoxArea.addItem("")
        self.NoCComboBoxArea.addItem("")
        self.NoCComboBoxArea.addItem("")
        self.NoCComboBoxArea.addItem("")
        self.NoCComboBoxArea.addItem("")
        self.NoCComboBoxArea.setObjectName(u"NoCComboBoxArea")
        self.NoCComboBoxArea.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.NoCComboBoxArea.sizePolicy().hasHeightForWidth())
        self.NoCComboBoxArea.setSizePolicy(sizePolicy4)
        self.NoCComboBoxArea.setMinimumSize(QSize(200, 35))
        self.NoCComboBoxArea.setMaximumSize(QSize(150, 30))
        self.NoCComboBoxArea.setLayoutDirection(Qt.LeftToRight)
        self.NoCComboBoxArea.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.NoCComboBoxArea.setEditable(False)
        self.NoCComboBoxArea.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.NoCComboBoxArea.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_140.addWidget(self.NoCComboBoxArea, 2, 1, 1, 1)


        self.verticalLayout_91.addLayout(self.gridLayout_140)


        self.gridLayout_139.addWidget(self.row_71, 0, 1, 1, 1)


        self.verticalLayout_43.addWidget(self.groupBox_Propiedades_43)

        self.groupBox_Propiedades_44 = QGroupBox(self.layoutWidget_4)
        self.groupBox_Propiedades_44.setObjectName(u"groupBox_Propiedades_44")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_44.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_44.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_44.setMinimumSize(QSize(690, 0))
        self.groupBox_Propiedades_44.setMaximumSize(QSize(680, 16777215))
        self.groupBox_Propiedades_44.setStyleSheet(u"QGroupBox {\n"
"color: rgb(118, 199, 158);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(118, 199, 158);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_44.setAlignment(Qt.AlignCenter)
        self.gridLayout_141 = QGridLayout(self.groupBox_Propiedades_44)
        self.gridLayout_141.setObjectName(u"gridLayout_141")
        self.row_72 = QFrame(self.groupBox_Propiedades_44)
        self.row_72.setObjectName(u"row_72")
        self.row_72.setStyleSheet(u"")
        self.row_72.setFrameShape(QFrame.StyledPanel)
        self.row_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.row_72)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_142 = QGridLayout()
        self.gridLayout_142.setObjectName(u"gridLayout_142")
        self.gridLayout_142.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_142.setHorizontalSpacing(35)
        self.gridLayout_142.setVerticalSpacing(10)
        self.gridLayout_142.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelSocial_5 = QLabel(self.row_72)
        self.PrimLabelSocial_5.setObjectName(u"PrimLabelSocial_5")
        sizePolicy8.setHeightForWidth(self.PrimLabelSocial_5.sizePolicy().hasHeightForWidth())
        self.PrimLabelSocial_5.setSizePolicy(sizePolicy8)
        self.PrimLabelSocial_5.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.PrimLabelSocial_5.setLineWidth(1)
        self.PrimLabelSocial_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_142.addWidget(self.PrimLabelSocial_5, 0, 0, 1, 1)

        self.NoCComboBoxSocial = QComboBox(self.row_72)
        self.NoCComboBoxSocial.addItem("")
        self.NoCComboBoxSocial.addItem("")
        self.NoCComboBoxSocial.addItem("")
        self.NoCComboBoxSocial.addItem("")
        self.NoCComboBoxSocial.addItem("")
        self.NoCComboBoxSocial.setObjectName(u"NoCComboBoxSocial")
        self.NoCComboBoxSocial.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.NoCComboBoxSocial.sizePolicy().hasHeightForWidth())
        self.NoCComboBoxSocial.setSizePolicy(sizePolicy4)
        self.NoCComboBoxSocial.setMinimumSize(QSize(200, 35))
        self.NoCComboBoxSocial.setMaximumSize(QSize(150, 30))
        self.NoCComboBoxSocial.setLayoutDirection(Qt.LeftToRight)
        self.NoCComboBoxSocial.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.NoCComboBoxSocial.setEditable(False)
        self.NoCComboBoxSocial.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.NoCComboBoxSocial.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_142.addWidget(self.NoCComboBoxSocial, 0, 1, 1, 1)


        self.verticalLayout_92.addLayout(self.gridLayout_142)


        self.gridLayout_141.addWidget(self.row_72, 0, 1, 1, 1)


        self.verticalLayout_43.addWidget(self.groupBox_Propiedades_44)

        self.PrimInputParametro_20 = QLineEdit(self.NoConvEntrada)
        self.PrimInputParametro_20.setObjectName(u"PrimInputParametro_20")
        self.PrimInputParametro_20.setGeometry(QRect(780, 460, 265, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_20.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_20.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_20.setMinimumSize(QSize(265, 2))
        self.PrimInputParametro_20.setMaximumSize(QSize(250, 2))
        self.PrimInputParametro_20.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.PrimLabelMaxCriterio_10 = QLabel(self.NoConvEntrada)
        self.PrimLabelMaxCriterio_10.setObjectName(u"PrimLabelMaxCriterio_10")
        self.PrimLabelMaxCriterio_10.setGeometry(QRect(780, 360, 265, 21))
        sizePolicy6.setHeightForWidth(self.PrimLabelMaxCriterio_10.sizePolicy().hasHeightForWidth())
        self.PrimLabelMaxCriterio_10.setSizePolicy(sizePolicy6)
        self.PrimLabelMaxCriterio_10.setMinimumSize(QSize(265, 0))
        self.PrimLabelMaxCriterio_10.setMaximumSize(QSize(265, 16777215))
        self.PrimLabelMaxCriterio_10.setStyleSheet(u"font: 600 12pt \"Allerta\";\n"
"background-color: rgb(118, 199, 158);\n"
"color: rgb(255, 255, 255);")
        self.PrimLabelMaxCriterio_10.setTextFormat(Qt.AutoText)
        self.PrimLabelMaxCriterio_10.setAlignment(Qt.AlignCenter)
        self.tabNoC.addTab(self.NoConvEntrada, "")
        self.NoConvResultados = QWidget()
        self.NoConvResultados.setObjectName(u"NoConvResultados")
        self.NoCBtnReiniciar = QPushButton(self.NoConvResultados)
        self.NoCBtnReiniciar.setObjectName(u"NoCBtnReiniciar")
        self.NoCBtnReiniciar.setEnabled(True)
        self.NoCBtnReiniciar.setGeometry(QRect(810, 210, 250, 50))
        sizePolicy10.setHeightForWidth(self.NoCBtnReiniciar.sizePolicy().hasHeightForWidth())
        self.NoCBtnReiniciar.setSizePolicy(sizePolicy10)
        self.NoCBtnReiniciar.setMinimumSize(QSize(250, 50))
        self.NoCBtnReiniciar.setMaximumSize(QSize(40, 40))
        self.NoCBtnReiniciar.setStyleSheet(u"background-color: rgb(163, 160, 159);\n"
"border-width: 5px;\n"
"border-color: rgb(163, 160, 159);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Allerta\";\n"
"\n"
"")
        self.PrimInputParametro_21 = QLineEdit(self.NoConvResultados)
        self.PrimInputParametro_21.setObjectName(u"PrimInputParametro_21")
        self.PrimInputParametro_21.setGeometry(QRect(130, 100, 830, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_21.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_21.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_21.setMinimumSize(QSize(830, 2))
        self.PrimInputParametro_21.setMaximumSize(QSize(830, 2))
        self.PrimInputParametro_21.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.PrimLabelConvencional_11 = QLabel(self.NoConvResultados)
        self.PrimLabelConvencional_11.setObjectName(u"PrimLabelConvencional_11")
        self.PrimLabelConvencional_11.setGeometry(QRect(10, 50, 1061, 35))
        sizePolicy9.setHeightForWidth(self.PrimLabelConvencional_11.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_11.setSizePolicy(sizePolicy9)
        self.PrimLabelConvencional_11.setStyleSheet(u"font: 650 25pt \"Allerta\";\n"
"")
        self.PrimLabelConvencional_11.setLineWidth(1)
        self.PrimLabelConvencional_11.setAlignment(Qt.AlignCenter)
        self.PrimInputParametro_22 = QLineEdit(self.NoConvResultados)
        self.PrimInputParametro_22.setObjectName(u"PrimInputParametro_22")
        self.PrimInputParametro_22.setGeometry(QRect(130, 40, 830, 2))
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_22.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_22.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_22.setMinimumSize(QSize(830, 2))
        self.PrimInputParametro_22.setMaximumSize(QSize(830, 2))
        self.PrimInputParametro_22.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.groupBox_Propiedades_45 = QGroupBox(self.NoConvResultados)
        self.groupBox_Propiedades_45.setObjectName(u"groupBox_Propiedades_45")
        self.groupBox_Propiedades_45.setGeometry(QRect(20, 130, 770, 291))
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_45.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_45.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_45.setMinimumSize(QSize(770, 0))
        self.groupBox_Propiedades_45.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_45.setStyleSheet(u"QGroupBox {\n"
"color: rgb(118, 199, 158);\n"
"font: bold; \n"
"border: 2px solid;\n"
"font: 700 11pt \"Allerta\";\n"
"border-color: rgb(118, 199, 158);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_45.setAlignment(Qt.AlignCenter)
        self.verticalLayout_44 = QVBoxLayout(self.groupBox_Propiedades_45)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.row_73 = QFrame(self.groupBox_Propiedades_45)
        self.row_73.setObjectName(u"row_73")
        self.row_73.setStyleSheet(u"")
        self.row_73.setFrameShape(QFrame.StyledPanel)
        self.row_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.row_73)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_143 = QGridLayout()
        self.gridLayout_143.setObjectName(u"gridLayout_143")
        self.gridLayout_143.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_143.setHorizontalSpacing(35)
        self.gridLayout_143.setVerticalSpacing(10)
        self.gridLayout_143.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelConvencional_12 = QLabel(self.row_73)
        self.PrimLabelConvencional_12.setObjectName(u"PrimLabelConvencional_12")
        sizePolicy8.setHeightForWidth(self.PrimLabelConvencional_12.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_12.setSizePolicy(sizePolicy8)
        self.PrimLabelConvencional_12.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelConvencional_12.setLineWidth(1)
        self.PrimLabelConvencional_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_143.addWidget(self.PrimLabelConvencional_12, 0, 0, 1, 1)

        self.NoCFieldResultadoLaguna = QLineEdit(self.row_73)
        self.NoCFieldResultadoLaguna.setObjectName(u"NoCFieldResultadoLaguna")
        sizePolicy9.setHeightForWidth(self.NoCFieldResultadoLaguna.sizePolicy().hasHeightForWidth())
        self.NoCFieldResultadoLaguna.setSizePolicy(sizePolicy9)
        self.NoCFieldResultadoLaguna.setMinimumSize(QSize(110, 35))
        self.NoCFieldResultadoLaguna.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.NoCFieldResultadoLaguna.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.NoCFieldResultadoLaguna.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.NoCFieldResultadoLaguna.setAlignment(Qt.AlignCenter)

        self.gridLayout_143.addWidget(self.NoCFieldResultadoLaguna, 0, 1, 1, 1)

        self.PrimLabelTQA_12 = QLabel(self.row_73)
        self.PrimLabelTQA_12.setObjectName(u"PrimLabelTQA_12")
        sizePolicy8.setHeightForWidth(self.PrimLabelTQA_12.sizePolicy().hasHeightForWidth())
        self.PrimLabelTQA_12.setSizePolicy(sizePolicy8)
        self.PrimLabelTQA_12.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelTQA_12.setLineWidth(1)
        self.PrimLabelTQA_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_143.addWidget(self.PrimLabelTQA_12, 1, 0, 1, 1)

        self.PrimLabelTQA_13 = QLabel(self.row_73)
        self.PrimLabelTQA_13.setObjectName(u"PrimLabelTQA_13")
        sizePolicy8.setHeightForWidth(self.PrimLabelTQA_13.sizePolicy().hasHeightForWidth())
        self.PrimLabelTQA_13.setSizePolicy(sizePolicy8)
        self.PrimLabelTQA_13.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelTQA_13.setLineWidth(1)
        self.PrimLabelTQA_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_143.addWidget(self.PrimLabelTQA_13, 2, 0, 1, 1)

        self.NoCFieldResultadoUASB = QLineEdit(self.row_73)
        self.NoCFieldResultadoUASB.setObjectName(u"NoCFieldResultadoUASB")
        sizePolicy9.setHeightForWidth(self.NoCFieldResultadoUASB.sizePolicy().hasHeightForWidth())
        self.NoCFieldResultadoUASB.setSizePolicy(sizePolicy9)
        self.NoCFieldResultadoUASB.setMinimumSize(QSize(110, 35))
        self.NoCFieldResultadoUASB.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.NoCFieldResultadoUASB.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.NoCFieldResultadoUASB.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.NoCFieldResultadoUASB.setAlignment(Qt.AlignCenter)

        self.gridLayout_143.addWidget(self.NoCFieldResultadoUASB, 1, 1, 1, 1)

        self.NoCFieldResultadoHumedal = QLineEdit(self.row_73)
        self.NoCFieldResultadoHumedal.setObjectName(u"NoCFieldResultadoHumedal")
        sizePolicy9.setHeightForWidth(self.NoCFieldResultadoHumedal.sizePolicy().hasHeightForWidth())
        self.NoCFieldResultadoHumedal.setSizePolicy(sizePolicy9)
        self.NoCFieldResultadoHumedal.setMinimumSize(QSize(110, 35))
        self.NoCFieldResultadoHumedal.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.NoCFieldResultadoHumedal.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.NoCFieldResultadoHumedal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.NoCFieldResultadoHumedal.setAlignment(Qt.AlignCenter)

        self.gridLayout_143.addWidget(self.NoCFieldResultadoHumedal, 2, 1, 1, 1)

        self.PrimLabelTQA_14 = QLabel(self.row_73)
        self.PrimLabelTQA_14.setObjectName(u"PrimLabelTQA_14")
        sizePolicy8.setHeightForWidth(self.PrimLabelTQA_14.sizePolicy().hasHeightForWidth())
        self.PrimLabelTQA_14.setSizePolicy(sizePolicy8)
        self.PrimLabelTQA_14.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelTQA_14.setLineWidth(1)
        self.PrimLabelTQA_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_143.addWidget(self.PrimLabelTQA_14, 3, 0, 1, 1)

        self.NoCFieldResultadoMBR = QLineEdit(self.row_73)
        self.NoCFieldResultadoMBR.setObjectName(u"NoCFieldResultadoMBR")
        sizePolicy9.setHeightForWidth(self.NoCFieldResultadoMBR.sizePolicy().hasHeightForWidth())
        self.NoCFieldResultadoMBR.setSizePolicy(sizePolicy9)
        self.NoCFieldResultadoMBR.setMinimumSize(QSize(110, 35))
        self.NoCFieldResultadoMBR.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.NoCFieldResultadoMBR.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.NoCFieldResultadoMBR.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.NoCFieldResultadoMBR.setAlignment(Qt.AlignCenter)

        self.gridLayout_143.addWidget(self.NoCFieldResultadoMBR, 3, 1, 1, 1)


        self.verticalLayout_93.addLayout(self.gridLayout_143)


        self.verticalLayout_44.addWidget(self.row_73)

        self.NoCBtnCalcular = QPushButton(self.NoConvResultados)
        self.NoCBtnCalcular.setObjectName(u"NoCBtnCalcular")
        self.NoCBtnCalcular.setEnabled(True)
        self.NoCBtnCalcular.setGeometry(QRect(810, 140, 250, 50))
        sizePolicy10.setHeightForWidth(self.NoCBtnCalcular.sizePolicy().hasHeightForWidth())
        self.NoCBtnCalcular.setSizePolicy(sizePolicy10)
        self.NoCBtnCalcular.setMinimumSize(QSize(250, 50))
        self.NoCBtnCalcular.setMaximumSize(QSize(40, 40))
        self.NoCBtnCalcular.setStyleSheet(u"background-color: rgb(163, 160, 159);\n"
"border-width: 5px;\n"
"border-color: rgb(163, 160, 159);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Allerta\";\n"
"\n"
"")
        self.NoCBtnCalcular.setCheckable(False)
        self.NoCBtnCalcular.setChecked(False)
        self.NoCBtnCalcular.setAutoDefault(False)
        self.groupBox_Propiedades_49 = QGroupBox(self.NoConvResultados)
        self.groupBox_Propiedades_49.setObjectName(u"groupBox_Propiedades_49")
        self.groupBox_Propiedades_49.setGeometry(QRect(20, 440, 770, 131))
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_49.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_49.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_49.setMinimumSize(QSize(770, 0))
        self.groupBox_Propiedades_49.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_49.setStyleSheet(u"QGroupBox {\n"
"color: rgb(118, 199, 158);\n"
"font: bold; \n"
"border: 2px solid;\n"
"font: 700 11pt \"Allerta\";\n"
"border-color: rgb(118, 199, 158);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_49.setAlignment(Qt.AlignCenter)
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_Propiedades_49)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.row_77 = QFrame(self.groupBox_Propiedades_49)
        self.row_77.setObjectName(u"row_77")
        self.row_77.setStyleSheet(u"")
        self.row_77.setFrameShape(QFrame.StyledPanel)
        self.row_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.row_77)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_147 = QGridLayout()
        self.gridLayout_147.setObjectName(u"gridLayout_147")
        self.gridLayout_147.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_147.setHorizontalSpacing(35)
        self.gridLayout_147.setVerticalSpacing(10)
        self.gridLayout_147.setContentsMargins(20, 10, 20, 10)
        self.PrimLabelConvencional_18 = QLabel(self.row_77)
        self.PrimLabelConvencional_18.setObjectName(u"PrimLabelConvencional_18")
        sizePolicy8.setHeightForWidth(self.PrimLabelConvencional_18.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_18.setSizePolicy(sizePolicy8)
        self.PrimLabelConvencional_18.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.PrimLabelConvencional_18.setLineWidth(1)
        self.PrimLabelConvencional_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_147.addWidget(self.PrimLabelConvencional_18, 0, 0, 1, 1)

        self.NoCFieldResultadoMejor = QLineEdit(self.row_77)
        self.NoCFieldResultadoMejor.setObjectName(u"NoCFieldResultadoMejor")
        self.NoCFieldResultadoMejor.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.NoCFieldResultadoMejor.sizePolicy().hasHeightForWidth())
        self.NoCFieldResultadoMejor.setSizePolicy(sizePolicy9)
        self.NoCFieldResultadoMejor.setMinimumSize(QSize(110, 35))
        self.NoCFieldResultadoMejor.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.NoCFieldResultadoMejor.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.NoCFieldResultadoMejor.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.NoCFieldResultadoMejor.setAlignment(Qt.AlignCenter)

        self.gridLayout_147.addWidget(self.NoCFieldResultadoMejor, 0, 1, 1, 1)


        self.verticalLayout_97.addLayout(self.gridLayout_147)


        self.verticalLayout_27.addWidget(self.row_77)

        self.tabNoC.addTab(self.NoConvResultados, "")
        self.stackedWidget.addWidget(self.pagina_NoC)
        self.pagina_generalidades = QWidget()
        self.pagina_generalidades.setObjectName(u"pagina_generalidades")
        self.tabManning = QTabWidget(self.pagina_generalidades)
        self.tabManning.setObjectName(u"tabManning")
        self.tabManning.setGeometry(QRect(0, 0, 1131, 610))
        sizePolicy6.setHeightForWidth(self.tabManning.sizePolicy().hasHeightForWidth())
        self.tabManning.setSizePolicy(sizePolicy6)
        self.tabManning.setStyleSheet(u"font: 500 10pt \"Allerta\";\n"
"color: rgb(79, 79, 79);")
        self.tabManning.setTabPosition(QTabWidget.West)
        self.Matriz = QWidget()
        self.Matriz.setObjectName(u"Matriz")
        font3 = QFont()
        font3.setFamilies([u"Allerta"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.Matriz.setFont(font3)
        self.Matriz.setStyleSheet(u"color: rgb(48, 48, 48);\n"
"\n"
"")
        self.gridLayout_38 = QGridLayout(self.Matriz)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.groupBox_Propiedades_7 = QGroupBox(self.Matriz)
        self.groupBox_Propiedades_7.setObjectName(u"groupBox_Propiedades_7")
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_7.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_7.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_7.setMinimumSize(QSize(750, 500))
        self.groupBox_Propiedades_7.setMaximumSize(QSize(16777215, 500))
        self.groupBox_Propiedades_7.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_Propiedades_7.setStyleSheet(u"QGroupBox {\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(114, 161, 228);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"color: rgb(114, 161, 228);\n"
"\n"
"}\n"
"")
        self.groupBox_Propiedades_7.setAlignment(Qt.AlignCenter)
        self.gridLayout_42 = QGridLayout(self.groupBox_Propiedades_7)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_43.setHorizontalSpacing(40)
        self.gridLayout_43.setVerticalSpacing(10)
        self.gridLayout_43.setContentsMargins(0, 20, 5, 10)
        self.GeneralidadesLabel_22 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_22.setObjectName(u"GeneralidadesLabel_22")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_22.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_22.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_22.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_22.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_22.setLineWidth(1)
        self.GeneralidadesLabel_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_22, 4, 6, 1, 1)

        self.GeneralidadesLabel_39 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_39.setObjectName(u"GeneralidadesLabel_39")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_39.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_39.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_39.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_39.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_39.setLineWidth(1)
        self.GeneralidadesLabel_39.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_39, 10, 4, 1, 1)

        self.GeneralidadesLabel_12 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_12.setObjectName(u"GeneralidadesLabel_12")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_12.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_12.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_12.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_12.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_12.setLineWidth(1)
        self.GeneralidadesLabel_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_12, 1, 4, 1, 1)

        self.GeneralidadesLabel_26 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_26.setObjectName(u"GeneralidadesLabel_26")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_26.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_26.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_26.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_26.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_26.setLineWidth(1)
        self.GeneralidadesLabel_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_26, 4, 4, 1, 1)

        self.GeneralidadesLabel_21 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_21.setObjectName(u"GeneralidadesLabel_21")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_21.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_21.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_21.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_21.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_21.setLineWidth(1)
        self.GeneralidadesLabel_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_21, 4, 8, 1, 1)

        self.GeneralidadesLabel_37 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_37.setObjectName(u"GeneralidadesLabel_37")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_37.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_37.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_37.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_37.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_37.setLineWidth(1)
        self.GeneralidadesLabel_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_37, 11, 4, 1, 1)

        self.GeneralidadesLabel_40 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_40.setObjectName(u"GeneralidadesLabel_40")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_40.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_40.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_40.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_40.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_40.setLineWidth(1)
        self.GeneralidadesLabel_40.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_40, 10, 6, 1, 1)

        self.GeneralidadesLabel_33 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_33.setObjectName(u"GeneralidadesLabel_33")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_33.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_33.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_33.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_33.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_33.setLineWidth(1)
        self.GeneralidadesLabel_33.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_33, 11, 10, 1, 1)

        self.GeneralidadesLabel_116 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_116.setObjectName(u"GeneralidadesLabel_116")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_116.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_116.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_116.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_116.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_116.setLineWidth(1)
        self.GeneralidadesLabel_116.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_116, 7, 2, 1, 1)

        self.GeneralidadesLabel_28 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_28.setObjectName(u"GeneralidadesLabel_28")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_28.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_28.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_28.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_28.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_28.setLineWidth(1)
        self.GeneralidadesLabel_28.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_28, 11, 6, 1, 1)

        self.GeneralidadesLabel_31 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_31.setObjectName(u"GeneralidadesLabel_31")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_31.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_31.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_31.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_31.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_31.setLineWidth(1)
        self.GeneralidadesLabel_31.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_31, 10, 8, 1, 1)

        self.GeneralidadesLabel_19 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_19.setObjectName(u"GeneralidadesLabel_19")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_19.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_19.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_19.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_19.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_19.setLineWidth(1)
        self.GeneralidadesLabel_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_19, 3, 6, 1, 1)

        self.GeneralidadesLabel_16 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_16.setObjectName(u"GeneralidadesLabel_16")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_16.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_16.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_16.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_16.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_16.setLineWidth(1)
        self.GeneralidadesLabel_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_16, 3, 10, 1, 1)

        self.GeneralidadesLabel_17 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_17.setObjectName(u"GeneralidadesLabel_17")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_17.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_17.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_17.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_17.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_17.setLineWidth(1)
        self.GeneralidadesLabel_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_17, 3, 8, 1, 1)

        self.GeneralidadesLabel_38 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_38.setObjectName(u"GeneralidadesLabel_38")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_38.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_38.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_38.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_38.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_38.setLineWidth(1)
        self.GeneralidadesLabel_38.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_38, 9, 10, 1, 1)

        self.GeneralidadesLabel_29 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_29.setObjectName(u"GeneralidadesLabel_29")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_29.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_29.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_29.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_29.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_29.setLineWidth(1)
        self.GeneralidadesLabel_29.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_29, 8, 6, 1, 1)

        self.GeneralidadesLabel_43 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_43.setObjectName(u"GeneralidadesLabel_43")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_43.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_43.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_43.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_43.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_43.setLineWidth(1)
        self.GeneralidadesLabel_43.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_43, 9, 8, 1, 1)

        self.GeneralidadesLabel_13 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_13.setObjectName(u"GeneralidadesLabel_13")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_13.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_13.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_13.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_13.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_13.setLineWidth(1)
        self.GeneralidadesLabel_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_13, 1, 6, 1, 1)

        self.GeneralidadesLabel_41 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_41.setObjectName(u"GeneralidadesLabel_41")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_41.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_41.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_41.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_41.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_41.setLineWidth(1)
        self.GeneralidadesLabel_41.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_41, 9, 6, 1, 1)

        self.GeneralidadesLabel_18 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_18.setObjectName(u"GeneralidadesLabel_18")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_18.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_18.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_18.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_18.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_18.setLineWidth(1)
        self.GeneralidadesLabel_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_18, 3, 4, 1, 1)

        self.GeneralidadesLabel_32 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_32.setObjectName(u"GeneralidadesLabel_32")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_32.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_32.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_32.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_32.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_32.setLineWidth(1)
        self.GeneralidadesLabel_32.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_32, 11, 8, 1, 1)

        self.GeneralidadesLabel_10 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_10.setObjectName(u"GeneralidadesLabel_10")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_10.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_10.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_10.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_10.setStyleSheet(u"font: 650 11pt \"Allerta\";\n"
"background-color: rgb(114, 161, 228);\n"
"color: rgb(255, 255, 255);")
        self.GeneralidadesLabel_10.setLineWidth(1)
        self.GeneralidadesLabel_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_10, 5, 0, 1, 1)

        self.GeneralidadesLabel_8 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_8.setObjectName(u"GeneralidadesLabel_8")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_8.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_8.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_8.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_8.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_8.setLineWidth(1)
        self.GeneralidadesLabel_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_8, 3, 0, 1, 1)

        self.GeneralidadesLabel_9 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_9.setObjectName(u"GeneralidadesLabel_9")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_9.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_9.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_9.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_9.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_9.setLineWidth(1)
        self.GeneralidadesLabel_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_9, 4, 0, 1, 1)

        self.GeneralidadesLabel_47 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_47.setObjectName(u"GeneralidadesLabel_47")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_47.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_47.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_47.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_47.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_47.setLineWidth(1)
        self.GeneralidadesLabel_47.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_47, 7, 0, 1, 1)

        self.GeneralidadesLabel_68 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_68.setObjectName(u"GeneralidadesLabel_68")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_68.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_68.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_68.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_68.setStyleSheet(u"font: 650 11pt \"Allerta\";\n"
"background-color: rgb(114, 161, 228);\n"
"color: rgb(255, 255, 255);")
        self.GeneralidadesLabel_68.setLineWidth(1)
        self.GeneralidadesLabel_68.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_68, 12, 0, 1, 1)

        self.GeneralidadesLabel_11 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_11.setObjectName(u"GeneralidadesLabel_11")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_11.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_11.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_11.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_11.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_11.setLineWidth(1)
        self.GeneralidadesLabel_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_11, 6, 0, 1, 1)

        self.GeneralidadesLabel_52 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_52.setObjectName(u"GeneralidadesLabel_52")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_52.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_52.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_52.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_52.setStyleSheet(u"font: 650 11pt \"Allerta\";\n"
"background-color: rgb(114, 161, 228);\n"
"color: rgb(255, 255, 255);")
        self.GeneralidadesLabel_52.setLineWidth(1)
        self.GeneralidadesLabel_52.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_52, 8, 0, 1, 1)

        self.GeneralidadesLabel_71 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_71.setObjectName(u"GeneralidadesLabel_71")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_71.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_71.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_71.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_71.setStyleSheet(u"font: 650 11pt \"Allerta\";\n"
"background-color: rgb(114, 161, 228);\n"
"color: rgb(255, 255, 255);")
        self.GeneralidadesLabel_71.setLineWidth(1)
        self.GeneralidadesLabel_71.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_71, 13, 0, 1, 1)

        self.GeneralidadesLabel_63 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_63.setObjectName(u"GeneralidadesLabel_63")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_63.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_63.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_63.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_63.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_63.setLineWidth(1)
        self.GeneralidadesLabel_63.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_63, 11, 0, 1, 1)

        self.GeneralidadesLabel_92 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_92.setObjectName(u"GeneralidadesLabel_92")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_92.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_92.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_92.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_92.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_92.setLineWidth(1)
        self.GeneralidadesLabel_92.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_92, 14, 0, 1, 1)

        self.GeneralidadesLabel_55 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_55.setObjectName(u"GeneralidadesLabel_55")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_55.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_55.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_55.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_55.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_55.setLineWidth(1)
        self.GeneralidadesLabel_55.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_55, 9, 0, 1, 1)

        self.GeneralidadesLabel_58 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_58.setObjectName(u"GeneralidadesLabel_58")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_58.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_58.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_58.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_58.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_58.setLineWidth(1)
        self.GeneralidadesLabel_58.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_58, 10, 0, 1, 1)

        self.PrimInputParametro_27 = QLineEdit(self.groupBox_Propiedades_7)
        self.PrimInputParametro_27.setObjectName(u"PrimInputParametro_27")
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_27.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_27.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_27.setMinimumSize(QSize(2, 355))
        self.PrimInputParametro_27.setMaximumSize(QSize(2, 350))
        self.PrimInputParametro_27.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_43.addWidget(self.PrimInputParametro_27, 1, 1, 1, 1)

        self.GeneralidadesLabel_20 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_20.setObjectName(u"GeneralidadesLabel_20")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_20.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_20.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_20.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_20.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_20.setLineWidth(1)
        self.GeneralidadesLabel_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_20, 4, 10, 1, 1)

        self.GeneralidadesLabel_24 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_24.setObjectName(u"GeneralidadesLabel_24")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_24.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_24.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_24.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_24.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_24.setLineWidth(1)
        self.GeneralidadesLabel_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_24, 7, 8, 1, 1)

        self.GeneralidadesLabel_23 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_23.setObjectName(u"GeneralidadesLabel_23")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_23.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_23.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_23.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_23.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_23.setLineWidth(1)
        self.GeneralidadesLabel_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_23, 7, 6, 1, 1)

        self.GeneralidadesLabel_27 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_27.setObjectName(u"GeneralidadesLabel_27")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_27.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_27.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_27.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_27.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_27.setLineWidth(1)
        self.GeneralidadesLabel_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_27, 7, 4, 1, 1)

        self.GeneralidadesLabel_25 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_25.setObjectName(u"GeneralidadesLabel_25")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_25.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_25.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_25.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_25.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_25.setLineWidth(1)
        self.GeneralidadesLabel_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_25, 7, 10, 1, 1)

        self.GeneralidadesLabel_82 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_82.setObjectName(u"GeneralidadesLabel_82")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_82.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_82.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_82.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_82.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_82.setLineWidth(1)
        self.GeneralidadesLabel_82.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_82, 14, 4, 1, 1)

        self.GeneralidadesLabel_80 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_80.setObjectName(u"GeneralidadesLabel_80")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_80.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_80.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_80.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_80.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_80.setLineWidth(1)
        self.GeneralidadesLabel_80.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_80, 14, 8, 1, 1)

        self.PrimInputParametro_25 = QLineEdit(self.groupBox_Propiedades_7)
        self.PrimInputParametro_25.setObjectName(u"PrimInputParametro_25")
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_25.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_25.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_25.setMinimumSize(QSize(2, 355))
        self.PrimInputParametro_25.setMaximumSize(QSize(2, 350))
        self.PrimInputParametro_25.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_43.addWidget(self.PrimInputParametro_25, 1, 7, 1, 1)

        self.GeneralidadesLabel_87 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_87.setObjectName(u"GeneralidadesLabel_87")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_87.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_87.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_87.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_87.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_87.setLineWidth(1)
        self.GeneralidadesLabel_87.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_87, 14, 6, 1, 1)

        self.GeneralidadesLabel_109 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_109.setObjectName(u"GeneralidadesLabel_109")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_109.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_109.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_109.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_109.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_109.setLineWidth(1)
        self.GeneralidadesLabel_109.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_109, 4, 2, 1, 1)

        self.GeneralidadesLabel_110 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_110.setObjectName(u"GeneralidadesLabel_110")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_110.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_110.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_110.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_110.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_110.setLineWidth(1)
        self.GeneralidadesLabel_110.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_110, 6, 4, 1, 1)

        self.GeneralidadesLabel_104 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_104.setObjectName(u"GeneralidadesLabel_104")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_104.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_104.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_104.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_104.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_104.setLineWidth(1)
        self.GeneralidadesLabel_104.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_104, 6, 8, 1, 1)

        self.GeneralidadesLabel_114 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_114.setObjectName(u"GeneralidadesLabel_114")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_114.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_114.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_114.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_114.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_114.setLineWidth(1)
        self.GeneralidadesLabel_114.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_114, 6, 6, 1, 1)

        self.GeneralidadesLabel_106 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_106.setObjectName(u"GeneralidadesLabel_106")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_106.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_106.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_106.setMinimumSize(QSize(100, 0))
        font4 = QFont()
        font4.setFamilies([u"Allerta"])
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(False)
        self.GeneralidadesLabel_106.setFont(font4)
        self.GeneralidadesLabel_106.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_106.setLineWidth(1)
        self.GeneralidadesLabel_106.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_106, 5, 2, 1, 1)

        self.GeneralidadesLabel_115 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_115.setObjectName(u"GeneralidadesLabel_115")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_115.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_115.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_115.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_115.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_115.setLineWidth(1)
        self.GeneralidadesLabel_115.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_115, 6, 2, 1, 1)

        self.GeneralidadesLabel_112 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_112.setObjectName(u"GeneralidadesLabel_112")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_112.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_112.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_112.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_112.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_112.setLineWidth(1)
        self.GeneralidadesLabel_112.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_112, 6, 10, 1, 1)

        self.GeneralidadesLabel_113 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_113.setObjectName(u"GeneralidadesLabel_113")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_113.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_113.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_113.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_113.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_113.setLineWidth(1)
        self.GeneralidadesLabel_113.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_113, 1, 2, 1, 1)

        self.GeneralidadesLabel_105 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_105.setObjectName(u"GeneralidadesLabel_105")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_105.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_105.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_105.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_105.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_105.setLineWidth(1)
        self.GeneralidadesLabel_105.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_105, 3, 2, 1, 1)

        self.GeneralidadesLabel_42 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_42.setObjectName(u"GeneralidadesLabel_42")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_42.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_42.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_42.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_42.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_42.setLineWidth(1)
        self.GeneralidadesLabel_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_42, 9, 4, 1, 1)

        self.GeneralidadesLabel_36 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_36.setObjectName(u"GeneralidadesLabel_36")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_36.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_36.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_36.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_36.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_36.setLineWidth(1)
        self.GeneralidadesLabel_36.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_36, 10, 10, 1, 1)

        self.GeneralidadesLabel_78 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_78.setObjectName(u"GeneralidadesLabel_78")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_78.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_78.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_78.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_78.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_78.setLineWidth(1)
        self.GeneralidadesLabel_78.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_78, 12, 4, 1, 1)

        self.GeneralidadesLabel_81 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_81.setObjectName(u"GeneralidadesLabel_81")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_81.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_81.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_81.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_81.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_81.setLineWidth(1)
        self.GeneralidadesLabel_81.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_81, 12, 6, 1, 1)

        self.GeneralidadesLabel_85 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_85.setObjectName(u"GeneralidadesLabel_85")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_85.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_85.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_85.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_85.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_85.setLineWidth(1)
        self.GeneralidadesLabel_85.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_85, 12, 10, 1, 1)

        self.GeneralidadesLabel_89 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_89.setObjectName(u"GeneralidadesLabel_89")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_89.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_89.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_89.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_89.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_89.setLineWidth(1)
        self.GeneralidadesLabel_89.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_89, 13, 2, 1, 1)

        self.GeneralidadesLabel_93 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_93.setObjectName(u"GeneralidadesLabel_93")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_93.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_93.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_93.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_93.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_93.setLineWidth(1)
        self.GeneralidadesLabel_93.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_93, 13, 10, 1, 1)

        self.GeneralidadesLabel_84 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_84.setObjectName(u"GeneralidadesLabel_84")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_84.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_84.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_84.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_84.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_84.setLineWidth(1)
        self.GeneralidadesLabel_84.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_84, 12, 8, 1, 1)

        self.GeneralidadesLabel_86 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_86.setObjectName(u"GeneralidadesLabel_86")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_86.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_86.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_86.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_86.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_86.setLineWidth(1)
        self.GeneralidadesLabel_86.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_86, 13, 6, 1, 1)

        self.GeneralidadesLabel_83 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_83.setObjectName(u"GeneralidadesLabel_83")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_83.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_83.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_83.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_83.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_83.setLineWidth(1)
        self.GeneralidadesLabel_83.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_83, 13, 4, 1, 1)

        self.GeneralidadesLabel_97 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_97.setObjectName(u"GeneralidadesLabel_97")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_97.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_97.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_97.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_97.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_97.setLineWidth(1)
        self.GeneralidadesLabel_97.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_97, 13, 8, 1, 1)

        self.GeneralidadesLabel_120 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_120.setObjectName(u"GeneralidadesLabel_120")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_120.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_120.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_120.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_120.setFont(font4)
        self.GeneralidadesLabel_120.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_120.setLineWidth(1)
        self.GeneralidadesLabel_120.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_120, 12, 2, 1, 1)

        self.GeneralidadesLabel_111 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_111.setObjectName(u"GeneralidadesLabel_111")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_111.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_111.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_111.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_111.setFont(font4)
        self.GeneralidadesLabel_111.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_111.setLineWidth(1)
        self.GeneralidadesLabel_111.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_111, 5, 8, 1, 1)

        self.GeneralidadesLabel_30 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_30.setObjectName(u"GeneralidadesLabel_30")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_30.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_30.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_30.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_30.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_30.setLineWidth(1)
        self.GeneralidadesLabel_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_30, 8, 8, 1, 1)

        self.GeneralidadesLabel_35 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_35.setObjectName(u"GeneralidadesLabel_35")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_35.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_35.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_35.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_35.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_35.setLineWidth(1)
        self.GeneralidadesLabel_35.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_35, 8, 10, 1, 1)

        self.GeneralidadesLabel_77 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_77.setObjectName(u"GeneralidadesLabel_77")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_77.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_77.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_77.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_77.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_77.setLineWidth(1)
        self.GeneralidadesLabel_77.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_77, 5, 10, 1, 1)

        self.GeneralidadesLabel_107 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_107.setObjectName(u"GeneralidadesLabel_107")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_107.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_107.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_107.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_107.setFont(font4)
        self.GeneralidadesLabel_107.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_107.setLineWidth(1)
        self.GeneralidadesLabel_107.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_107, 5, 4, 1, 1)

        self.GeneralidadesLabel_108 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_108.setObjectName(u"GeneralidadesLabel_108")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_108.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_108.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_108.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_108.setFont(font4)
        self.GeneralidadesLabel_108.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_108.setLineWidth(1)
        self.GeneralidadesLabel_108.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_108, 5, 6, 1, 1)

        self.GeneralidadesLabel_14 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_14.setObjectName(u"GeneralidadesLabel_14")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_14.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_14.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_14.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_14.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_14.setLineWidth(1)
        self.GeneralidadesLabel_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_14, 1, 8, 1, 1)

        self.GeneralidadesLabel_34 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_34.setObjectName(u"GeneralidadesLabel_34")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_34.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_34.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_34.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_34.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_34.setLineWidth(1)
        self.GeneralidadesLabel_34.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_34, 8, 4, 1, 1)

        self.GeneralidadesLabel_121 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_121.setObjectName(u"GeneralidadesLabel_121")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_121.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_121.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_121.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_121.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_121.setLineWidth(1)
        self.GeneralidadesLabel_121.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_121, 9, 2, 1, 1)

        self.PrimInputParametro_24 = QLineEdit(self.groupBox_Propiedades_7)
        self.PrimInputParametro_24.setObjectName(u"PrimInputParametro_24")
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_24.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_24.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_24.setMinimumSize(QSize(2, 355))
        self.PrimInputParametro_24.setMaximumSize(QSize(2, 350))
        self.PrimInputParametro_24.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_43.addWidget(self.PrimInputParametro_24, 1, 5, 1, 1)

        self.GeneralidadesLabel_117 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_117.setObjectName(u"GeneralidadesLabel_117")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_117.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_117.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_117.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_117.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_117.setLineWidth(1)
        self.GeneralidadesLabel_117.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_117, 10, 2, 1, 1)

        self.GeneralidadesLabel_118 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_118.setObjectName(u"GeneralidadesLabel_118")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_118.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_118.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_118.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_118.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_118.setLineWidth(1)
        self.GeneralidadesLabel_118.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_118, 11, 2, 1, 1)

        self.GeneralidadesLabel_129 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_129.setObjectName(u"GeneralidadesLabel_129")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_129.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_129.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_129.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_129.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_129.setLineWidth(1)
        self.GeneralidadesLabel_129.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_129, 14, 2, 1, 1)

        self.GeneralidadesLabel_15 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_15.setObjectName(u"GeneralidadesLabel_15")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_15.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_15.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_15.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_15.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_15.setLineWidth(1)
        self.GeneralidadesLabel_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_15, 1, 10, 1, 1)

        self.GeneralidadesLabel_119 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_119.setObjectName(u"GeneralidadesLabel_119")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_119.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_119.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_119.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_119.setStyleSheet(u"font: 600 11pt \"Allerta\";\n"
"color: rgb(40, 106, 176);")
        self.GeneralidadesLabel_119.setLineWidth(1)
        self.GeneralidadesLabel_119.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_119, 8, 2, 1, 1)

        self.GeneralidadesLabel_76 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_76.setObjectName(u"GeneralidadesLabel_76")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_76.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_76.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_76.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_76.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_76.setLineWidth(1)
        self.GeneralidadesLabel_76.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_76, 14, 10, 1, 1)

        self.PrimInputParametro_23 = QLineEdit(self.groupBox_Propiedades_7)
        self.PrimInputParametro_23.setObjectName(u"PrimInputParametro_23")
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_23.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_23.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_23.setMinimumSize(QSize(2, 355))
        self.PrimInputParametro_23.setMaximumSize(QSize(2, 350))
        self.PrimInputParametro_23.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_43.addWidget(self.PrimInputParametro_23, 1, 3, 1, 1)

        self.PrimInputParametro_26 = QLineEdit(self.groupBox_Propiedades_7)
        self.PrimInputParametro_26.setObjectName(u"PrimInputParametro_26")
        sizePolicy6.setHeightForWidth(self.PrimInputParametro_26.sizePolicy().hasHeightForWidth())
        self.PrimInputParametro_26.setSizePolicy(sizePolicy6)
        self.PrimInputParametro_26.setMinimumSize(QSize(2, 355))
        self.PrimInputParametro_26.setMaximumSize(QSize(2, 350))
        self.PrimInputParametro_26.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")

        self.gridLayout_43.addWidget(self.PrimInputParametro_26, 1, 9, 1, 1)

        self.GeneralidadesLabel_7 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_7.setObjectName(u"GeneralidadesLabel_7")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_7.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_7.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_7.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_7.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_7.setLineWidth(1)
        self.GeneralidadesLabel_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_7, 1, 0, 1, 1)

        self.GeneralidadesLabel_90 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_90.setObjectName(u"GeneralidadesLabel_90")
        self.GeneralidadesLabel_90.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_90.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_90.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_90.setMinimumSize(QSize(100, 35))
        self.GeneralidadesLabel_90.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_90.setLineWidth(1)
        self.GeneralidadesLabel_90.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_90, 0, 6, 1, 1)

        self.GeneralidadesLabel_79 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_79.setObjectName(u"GeneralidadesLabel_79")
        self.GeneralidadesLabel_79.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_79.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_79.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_79.setMinimumSize(QSize(100, 35))
        self.GeneralidadesLabel_79.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_79.setLineWidth(1)
        self.GeneralidadesLabel_79.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_79, 0, 8, 1, 1)

        self.GeneralidadesLabel_94 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_94.setObjectName(u"GeneralidadesLabel_94")
        self.GeneralidadesLabel_94.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_94.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_94.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_94.setMinimumSize(QSize(100, 35))
        self.GeneralidadesLabel_94.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_94.setLineWidth(1)
        self.GeneralidadesLabel_94.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_94, 0, 2, 1, 1)

        self.GeneralidadesLabel_88 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_88.setObjectName(u"GeneralidadesLabel_88")
        self.GeneralidadesLabel_88.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_88.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_88.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_88.setMinimumSize(QSize(100, 35))
        self.GeneralidadesLabel_88.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_88.setLineWidth(1)
        self.GeneralidadesLabel_88.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_88, 0, 10, 1, 1)

        self.GeneralidadesLabel_91 = QLabel(self.groupBox_Propiedades_7)
        self.GeneralidadesLabel_91.setObjectName(u"GeneralidadesLabel_91")
        self.GeneralidadesLabel_91.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_91.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_91.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_91.setMinimumSize(QSize(100, 35))
        self.GeneralidadesLabel_91.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_91.setLineWidth(1)
        self.GeneralidadesLabel_91.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_43.addWidget(self.GeneralidadesLabel_91, 0, 4, 1, 1)


        self.gridLayout_42.addLayout(self.gridLayout_43, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.groupBox_Propiedades_7, 3, 0, 1, 1)

        self.PrimLabelConvencional_13 = QLabel(self.Matriz)
        self.PrimLabelConvencional_13.setObjectName(u"PrimLabelConvencional_13")
        sizePolicy9.setHeightForWidth(self.PrimLabelConvencional_13.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_13.setSizePolicy(sizePolicy9)
        self.PrimLabelConvencional_13.setStyleSheet(u"font: 650 25pt \"Allerta\";\n"
"")
        self.PrimLabelConvencional_13.setLineWidth(1)
        self.PrimLabelConvencional_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_38.addWidget(self.PrimLabelConvencional_13, 0, 0, 1, 1)

        self.tabManning.addTab(self.Matriz, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_Propiedades_8 = QGroupBox(self.tab)
        self.groupBox_Propiedades_8.setObjectName(u"groupBox_Propiedades_8")
        self.groupBox_Propiedades_8.setGeometry(QRect(30, 90, 600, 500))
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_8.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_8.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_8.setMinimumSize(QSize(600, 500))
        self.groupBox_Propiedades_8.setMaximumSize(QSize(590, 500))
        self.groupBox_Propiedades_8.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_Propiedades_8.setStyleSheet(u"QGroupBox {\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(114, 161, 228);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"color: rgb(114, 161, 228);\n"
"\n"
"}\n"
"")
        self.groupBox_Propiedades_8.setAlignment(Qt.AlignCenter)
        self.gridLayout_44 = QGridLayout(self.groupBox_Propiedades_8)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(20)
        self.gridLayout_8.setVerticalSpacing(10)
        self.GeneralidadesLabel_204 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_204.setObjectName(u"GeneralidadesLabel_204")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_204.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_204.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_204.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_204.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_204.setLineWidth(1)
        self.GeneralidadesLabel_204.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_204, 1, 2, 1, 1)

        self.GeneralidadesLabel_205 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_205.setObjectName(u"GeneralidadesLabel_205")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_205.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_205.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_205.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_205.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_205.setLineWidth(1)
        self.GeneralidadesLabel_205.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_205, 3, 2, 1, 1)

        self.GeneralidadesLabel_206 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_206.setObjectName(u"GeneralidadesLabel_206")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_206.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_206.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_206.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_206.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_206.setLineWidth(1)
        self.GeneralidadesLabel_206.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_206, 8, 2, 1, 1)

        self.GeneralidadesLabel_211 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_211.setObjectName(u"GeneralidadesLabel_211")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_211.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_211.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_211.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_211.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_211.setLineWidth(1)
        self.GeneralidadesLabel_211.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_211, 4, 2, 1, 1)

        self.GeneralidadesLabel_210 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_210.setObjectName(u"GeneralidadesLabel_210")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_210.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_210.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_210.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_210.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_210.setLineWidth(1)
        self.GeneralidadesLabel_210.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_210, 6, 2, 1, 1)

        self.GeneralidadesLabel_208 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_208.setObjectName(u"GeneralidadesLabel_208")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_208.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_208.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_208.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_208.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_208.setLineWidth(1)
        self.GeneralidadesLabel_208.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_208, 5, 2, 1, 1)

        self.GeneralidadesLabel_212 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_212.setObjectName(u"GeneralidadesLabel_212")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_212.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_212.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_212.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_212.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_212.setLineWidth(1)
        self.GeneralidadesLabel_212.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_212, 9, 2, 1, 1)

        self.GeneralidadesLabel_209 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_209.setObjectName(u"GeneralidadesLabel_209")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_209.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_209.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_209.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_209.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_209.setLineWidth(1)
        self.GeneralidadesLabel_209.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_209, 7, 2, 1, 1)

        self.GeneralidadesLabel_207 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_207.setObjectName(u"GeneralidadesLabel_207")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_207.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_207.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_207.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_207.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_207.setLineWidth(1)
        self.GeneralidadesLabel_207.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_207, 2, 2, 1, 1)

        self.GeneralidadesLabel_213 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_213.setObjectName(u"GeneralidadesLabel_213")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_213.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_213.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_213.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_213.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_213.setLineWidth(1)
        self.GeneralidadesLabel_213.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_213, 1, 1, 1, 1)

        self.GeneralidadesLabel_214 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_214.setObjectName(u"GeneralidadesLabel_214")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_214.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_214.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_214.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_214.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_214.setLineWidth(1)
        self.GeneralidadesLabel_214.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_214, 2, 1, 1, 1)

        self.GeneralidadesLabel_217 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_217.setObjectName(u"GeneralidadesLabel_217")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_217.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_217.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_217.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_217.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_217.setLineWidth(1)
        self.GeneralidadesLabel_217.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_217, 5, 1, 1, 1)

        self.GeneralidadesLabel_219 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_219.setObjectName(u"GeneralidadesLabel_219")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_219.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_219.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_219.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_219.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_219.setLineWidth(1)
        self.GeneralidadesLabel_219.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_219, 7, 1, 1, 1)

        self.GeneralidadesLabel_216 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_216.setObjectName(u"GeneralidadesLabel_216")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_216.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_216.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_216.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_216.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_216.setLineWidth(1)
        self.GeneralidadesLabel_216.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_216, 4, 1, 1, 1)

        self.GeneralidadesLabel_221 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_221.setObjectName(u"GeneralidadesLabel_221")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_221.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_221.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_221.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_221.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_221.setLineWidth(1)
        self.GeneralidadesLabel_221.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_221, 9, 1, 1, 1)

        self.GeneralidadesLabel_218 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_218.setObjectName(u"GeneralidadesLabel_218")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_218.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_218.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_218.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_218.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_218.setLineWidth(1)
        self.GeneralidadesLabel_218.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_218, 6, 1, 1, 1)

        self.GeneralidadesLabel_220 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_220.setObjectName(u"GeneralidadesLabel_220")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_220.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_220.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_220.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_220.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_220.setLineWidth(1)
        self.GeneralidadesLabel_220.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_220, 8, 1, 1, 1)

        self.GeneralidadesLabel_215 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_215.setObjectName(u"GeneralidadesLabel_215")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_215.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_215.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_215.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_215.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_215.setLineWidth(1)
        self.GeneralidadesLabel_215.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_215, 3, 1, 1, 1)

        self.GeneralidadesLabel_222 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_222.setObjectName(u"GeneralidadesLabel_222")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_222.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_222.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_222.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_222.setStyleSheet(u"font: 550 11pt \"Allerta\";\n"
"background-color: rgb(222, 222, 222);")
        self.GeneralidadesLabel_222.setLineWidth(1)
        self.GeneralidadesLabel_222.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_222, 1, 0, 1, 1)

        self.GeneralidadesLabel_224 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_224.setObjectName(u"GeneralidadesLabel_224")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_224.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_224.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_224.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_224.setStyleSheet(u"font: 550 11pt \"Allerta\";\n"
"background-color: rgb(222, 222, 222);")
        self.GeneralidadesLabel_224.setLineWidth(1)
        self.GeneralidadesLabel_224.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_224, 6, 0, 1, 1)

        self.GeneralidadesLabel_223 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_223.setObjectName(u"GeneralidadesLabel_223")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_223.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_223.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_223.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_223.setStyleSheet(u"font: 550 11pt \"Allerta\";\n"
"background-color: rgb(222, 222, 222);")
        self.GeneralidadesLabel_223.setLineWidth(1)
        self.GeneralidadesLabel_223.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_223, 3, 0, 1, 1)

        self.GeneralidadesLabel_225 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_225.setObjectName(u"GeneralidadesLabel_225")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_225.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_225.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_225.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_225.setStyleSheet(u"font: 550 11pt \"Allerta\";\n"
"background-color: rgb(222, 222, 222);")
        self.GeneralidadesLabel_225.setLineWidth(1)
        self.GeneralidadesLabel_225.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_225, 9, 0, 1, 1)

        self.GeneralidadesLabel_226 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_226.setObjectName(u"GeneralidadesLabel_226")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_226.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_226.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_226.setMinimumSize(QSize(120, 0))
        self.GeneralidadesLabel_226.setFont(font4)
        self.GeneralidadesLabel_226.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_226.setLineWidth(1)
        self.GeneralidadesLabel_226.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_226, 0, 1, 1, 1)

        self.GeneralidadesLabel_227 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_227.setObjectName(u"GeneralidadesLabel_227")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_227.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_227.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_227.setMinimumSize(QSize(270, 0))
        self.GeneralidadesLabel_227.setFont(font4)
        self.GeneralidadesLabel_227.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_227.setLineWidth(1)
        self.GeneralidadesLabel_227.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_227, 0, 2, 1, 1)

        self.GeneralidadesLabel_228 = QLabel(self.groupBox_Propiedades_8)
        self.GeneralidadesLabel_228.setObjectName(u"GeneralidadesLabel_228")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_228.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_228.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_228.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_228.setFont(font4)
        self.GeneralidadesLabel_228.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.GeneralidadesLabel_228.setLineWidth(1)
        self.GeneralidadesLabel_228.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.GeneralidadesLabel_228, 0, 0, 1, 1)


        self.gridLayout_44.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.groupBox_Propiedades_9 = QGroupBox(self.tab)
        self.groupBox_Propiedades_9.setObjectName(u"groupBox_Propiedades_9")
        self.groupBox_Propiedades_9.setGeometry(QRect(670, 90, 400, 500))
        sizePolicy4.setHeightForWidth(self.groupBox_Propiedades_9.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_9.setSizePolicy(sizePolicy4)
        self.groupBox_Propiedades_9.setMinimumSize(QSize(400, 500))
        self.groupBox_Propiedades_9.setMaximumSize(QSize(400, 500))
        self.groupBox_Propiedades_9.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_Propiedades_9.setStyleSheet(u"QGroupBox {\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(114, 161, 228);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"color: rgb(114, 161, 228);\n"
"\n"
"}\n"
"")
        self.groupBox_Propiedades_9.setAlignment(Qt.AlignCenter)
        self.gridLayout_45 = QGridLayout(self.groupBox_Propiedades_9)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(20)
        self.gridLayout_9.setVerticalSpacing(10)
        self.GeneralidadesLabel_231 = QLabel(self.groupBox_Propiedades_9)
        self.GeneralidadesLabel_231.setObjectName(u"GeneralidadesLabel_231")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_231.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_231.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_231.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_231.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_231.setLineWidth(1)
        self.GeneralidadesLabel_231.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.GeneralidadesLabel_231, 7, 0, 1, 1)

        self.GeneralidadesLabel_235 = QLabel(self.groupBox_Propiedades_9)
        self.GeneralidadesLabel_235.setObjectName(u"GeneralidadesLabel_235")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_235.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_235.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_235.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_235.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_235.setLineWidth(1)
        self.GeneralidadesLabel_235.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.GeneralidadesLabel_235, 8, 0, 1, 1)

        self.GeneralidadesLabel_252 = QLabel(self.groupBox_Propiedades_9)
        self.GeneralidadesLabel_252.setObjectName(u"GeneralidadesLabel_252")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_252.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_252.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_252.setMinimumSize(QSize(330, 0))
        self.GeneralidadesLabel_252.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.GeneralidadesLabel_252.setLineWidth(1)
        self.GeneralidadesLabel_252.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.GeneralidadesLabel_252, 0, 0, 1, 1)

        self.GeneralidadesLabel_229 = QLabel(self.groupBox_Propiedades_9)
        self.GeneralidadesLabel_229.setObjectName(u"GeneralidadesLabel_229")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_229.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_229.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_229.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_229.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_229.setLineWidth(1)
        self.GeneralidadesLabel_229.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.GeneralidadesLabel_229, 1, 0, 1, 1)

        self.GeneralidadesLabel_230 = QLabel(self.groupBox_Propiedades_9)
        self.GeneralidadesLabel_230.setObjectName(u"GeneralidadesLabel_230")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_230.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_230.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_230.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_230.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_230.setLineWidth(1)
        self.GeneralidadesLabel_230.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.GeneralidadesLabel_230, 3, 0, 1, 1)

        self.GeneralidadesLabel_232 = QLabel(self.groupBox_Propiedades_9)
        self.GeneralidadesLabel_232.setObjectName(u"GeneralidadesLabel_232")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_232.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_232.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_232.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_232.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_232.setLineWidth(1)
        self.GeneralidadesLabel_232.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.GeneralidadesLabel_232, 4, 0, 1, 1)

        self.GeneralidadesLabel_234 = QLabel(self.groupBox_Propiedades_9)
        self.GeneralidadesLabel_234.setObjectName(u"GeneralidadesLabel_234")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_234.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_234.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_234.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_234.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_234.setLineWidth(1)
        self.GeneralidadesLabel_234.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.GeneralidadesLabel_234, 5, 0, 1, 1)

        self.GeneralidadesLabel_236 = QLabel(self.groupBox_Propiedades_9)
        self.GeneralidadesLabel_236.setObjectName(u"GeneralidadesLabel_236")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_236.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_236.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_236.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_236.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_236.setLineWidth(1)
        self.GeneralidadesLabel_236.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.GeneralidadesLabel_236, 9, 0, 1, 1)

        self.GeneralidadesLabel_237 = QLabel(self.groupBox_Propiedades_9)
        self.GeneralidadesLabel_237.setObjectName(u"GeneralidadesLabel_237")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_237.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_237.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_237.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_237.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_237.setLineWidth(1)
        self.GeneralidadesLabel_237.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.GeneralidadesLabel_237, 2, 0, 1, 1)

        self.GeneralidadesLabel_233 = QLabel(self.groupBox_Propiedades_9)
        self.GeneralidadesLabel_233.setObjectName(u"GeneralidadesLabel_233")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_233.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_233.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_233.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_233.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_233.setLineWidth(1)
        self.GeneralidadesLabel_233.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.GeneralidadesLabel_233, 6, 0, 1, 1)

        self.GeneralidadesLabel_238 = QLabel(self.groupBox_Propiedades_9)
        self.GeneralidadesLabel_238.setObjectName(u"GeneralidadesLabel_238")
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_238.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_238.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_238.setMinimumSize(QSize(100, 0))
        self.GeneralidadesLabel_238.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_238.setLineWidth(1)
        self.GeneralidadesLabel_238.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.GeneralidadesLabel_238, 10, 0, 1, 1)


        self.gridLayout_45.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.PrimLabelConvencional_14 = QLabel(self.tab)
        self.PrimLabelConvencional_14.setObjectName(u"PrimLabelConvencional_14")
        self.PrimLabelConvencional_14.setGeometry(QRect(10, 10, 1084, 80))
        sizePolicy9.setHeightForWidth(self.PrimLabelConvencional_14.sizePolicy().hasHeightForWidth())
        self.PrimLabelConvencional_14.setSizePolicy(sizePolicy9)
        self.PrimLabelConvencional_14.setStyleSheet(u"font: 650 25pt \"Allerta\";\n"
"")
        self.PrimLabelConvencional_14.setLineWidth(1)
        self.PrimLabelConvencional_14.setAlignment(Qt.AlignCenter)
        self.tabManning.addTab(self.tab, "")
        self.GeneralidadesLabel_44 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_44.setObjectName(u"GeneralidadesLabel_44")
        self.GeneralidadesLabel_44.setGeometry(QRect(1352, 479, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_44.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_44.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_44.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_44.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_44.setLineWidth(1)
        self.GeneralidadesLabel_44.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_45 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_45.setObjectName(u"GeneralidadesLabel_45")
        self.GeneralidadesLabel_45.setGeometry(QRect(1805, 518, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_45.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_45.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_45.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_45.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_45.setLineWidth(1)
        self.GeneralidadesLabel_45.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_46 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_46.setObjectName(u"GeneralidadesLabel_46")
        self.GeneralidadesLabel_46.setGeometry(QRect(1805, 479, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_46.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_46.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_46.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_46.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_46.setLineWidth(1)
        self.GeneralidadesLabel_46.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_48 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_48.setObjectName(u"GeneralidadesLabel_48")
        self.GeneralidadesLabel_48.setGeometry(QRect(1805, 440, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_48.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_48.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_48.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_48.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_48.setLineWidth(1)
        self.GeneralidadesLabel_48.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_49 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_49.setObjectName(u"GeneralidadesLabel_49")
        self.GeneralidadesLabel_49.setGeometry(QRect(1583, 557, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_49.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_49.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_49.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_49.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_49.setLineWidth(1)
        self.GeneralidadesLabel_49.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_50 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_50.setObjectName(u"GeneralidadesLabel_50")
        self.GeneralidadesLabel_50.setGeometry(QRect(1352, 518, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_50.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_50.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_50.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_50.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_50.setLineWidth(1)
        self.GeneralidadesLabel_50.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_51 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_51.setObjectName(u"GeneralidadesLabel_51")
        self.GeneralidadesLabel_51.setGeometry(QRect(1583, 518, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_51.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_51.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_51.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_51.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_51.setLineWidth(1)
        self.GeneralidadesLabel_51.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_53 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_53.setObjectName(u"GeneralidadesLabel_53")
        self.GeneralidadesLabel_53.setGeometry(QRect(1583, 440, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_53.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_53.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_53.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_53.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_53.setLineWidth(1)
        self.GeneralidadesLabel_53.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_54 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_54.setObjectName(u"GeneralidadesLabel_54")
        self.GeneralidadesLabel_54.setGeometry(QRect(1352, 557, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_54.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_54.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_54.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_54.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_54.setLineWidth(1)
        self.GeneralidadesLabel_54.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_56 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_56.setObjectName(u"GeneralidadesLabel_56")
        self.GeneralidadesLabel_56.setGeometry(QRect(1352, 440, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_56.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_56.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_56.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_56.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_56.setLineWidth(1)
        self.GeneralidadesLabel_56.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_57 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_57.setObjectName(u"GeneralidadesLabel_57")
        self.GeneralidadesLabel_57.setGeometry(QRect(1583, 479, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_57.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_57.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_57.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_57.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_57.setLineWidth(1)
        self.GeneralidadesLabel_57.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_59 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_59.setObjectName(u"GeneralidadesLabel_59")
        self.GeneralidadesLabel_59.setGeometry(QRect(1805, 557, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_59.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_59.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_59.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_59.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_59.setLineWidth(1)
        self.GeneralidadesLabel_59.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_60 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_60.setObjectName(u"GeneralidadesLabel_60")
        self.GeneralidadesLabel_60.setGeometry(QRect(1352, 529, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_60.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_60.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_60.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_60.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_60.setLineWidth(1)
        self.GeneralidadesLabel_60.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_61 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_61.setObjectName(u"GeneralidadesLabel_61")
        self.GeneralidadesLabel_61.setGeometry(QRect(1805, 568, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_61.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_61.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_61.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_61.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_61.setLineWidth(1)
        self.GeneralidadesLabel_61.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_62 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_62.setObjectName(u"GeneralidadesLabel_62")
        self.GeneralidadesLabel_62.setGeometry(QRect(1805, 529, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_62.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_62.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_62.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_62.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_62.setLineWidth(1)
        self.GeneralidadesLabel_62.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_64 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_64.setObjectName(u"GeneralidadesLabel_64")
        self.GeneralidadesLabel_64.setGeometry(QRect(1805, 490, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_64.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_64.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_64.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_64.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_64.setLineWidth(1)
        self.GeneralidadesLabel_64.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_65 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_65.setObjectName(u"GeneralidadesLabel_65")
        self.GeneralidadesLabel_65.setGeometry(QRect(1583, 607, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_65.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_65.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_65.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_65.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_65.setLineWidth(1)
        self.GeneralidadesLabel_65.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_66 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_66.setObjectName(u"GeneralidadesLabel_66")
        self.GeneralidadesLabel_66.setGeometry(QRect(1352, 568, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_66.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_66.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_66.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_66.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_66.setLineWidth(1)
        self.GeneralidadesLabel_66.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_67 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_67.setObjectName(u"GeneralidadesLabel_67")
        self.GeneralidadesLabel_67.setGeometry(QRect(1583, 568, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_67.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_67.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_67.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_67.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_67.setLineWidth(1)
        self.GeneralidadesLabel_67.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_69 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_69.setObjectName(u"GeneralidadesLabel_69")
        self.GeneralidadesLabel_69.setGeometry(QRect(1583, 490, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_69.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_69.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_69.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_69.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_69.setLineWidth(1)
        self.GeneralidadesLabel_69.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_70 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_70.setObjectName(u"GeneralidadesLabel_70")
        self.GeneralidadesLabel_70.setGeometry(QRect(1352, 607, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_70.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_70.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_70.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_70.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_70.setLineWidth(1)
        self.GeneralidadesLabel_70.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_72 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_72.setObjectName(u"GeneralidadesLabel_72")
        self.GeneralidadesLabel_72.setGeometry(QRect(1352, 490, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_72.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_72.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_72.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_72.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_72.setLineWidth(1)
        self.GeneralidadesLabel_72.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_73 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_73.setObjectName(u"GeneralidadesLabel_73")
        self.GeneralidadesLabel_73.setGeometry(QRect(1583, 529, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_73.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_73.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_73.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_73.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_73.setLineWidth(1)
        self.GeneralidadesLabel_73.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_74 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_74.setObjectName(u"GeneralidadesLabel_74")
        self.GeneralidadesLabel_74.setGeometry(QRect(1130, 607, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_74.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_74.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_74.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_74.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_74.setLineWidth(1)
        self.GeneralidadesLabel_74.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_75 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_75.setObjectName(u"GeneralidadesLabel_75")
        self.GeneralidadesLabel_75.setGeometry(QRect(1805, 607, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_75.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_75.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_75.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_75.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_75.setLineWidth(1)
        self.GeneralidadesLabel_75.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_95 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_95.setObjectName(u"GeneralidadesLabel_95")
        self.GeneralidadesLabel_95.setGeometry(QRect(1120, 644, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_95.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_95.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_95.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_95.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_95.setLineWidth(1)
        self.GeneralidadesLabel_95.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_96 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_96.setObjectName(u"GeneralidadesLabel_96")
        self.GeneralidadesLabel_96.setGeometry(QRect(1120, 839, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_96.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_96.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_96.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_96.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_96.setLineWidth(1)
        self.GeneralidadesLabel_96.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_98 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_98.setObjectName(u"GeneralidadesLabel_98")
        self.GeneralidadesLabel_98.setGeometry(QRect(1120, 800, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_98.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_98.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_98.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_98.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_98.setLineWidth(1)
        self.GeneralidadesLabel_98.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_100 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_100.setObjectName(u"GeneralidadesLabel_100")
        self.GeneralidadesLabel_100.setGeometry(QRect(1120, 761, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_100.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_100.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_100.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_100.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_100.setLineWidth(1)
        self.GeneralidadesLabel_100.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_101 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_101.setObjectName(u"GeneralidadesLabel_101")
        self.GeneralidadesLabel_101.setGeometry(QRect(1120, 683, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_101.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_101.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_101.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_101.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_101.setLineWidth(1)
        self.GeneralidadesLabel_101.setAlignment(Qt.AlignCenter)
        self.GeneralidadesLabel_102 = QLabel(self.pagina_generalidades)
        self.GeneralidadesLabel_102.setObjectName(u"GeneralidadesLabel_102")
        self.GeneralidadesLabel_102.setGeometry(QRect(1120, 722, 158, 19))
        sizePolicy8.setHeightForWidth(self.GeneralidadesLabel_102.sizePolicy().hasHeightForWidth())
        self.GeneralidadesLabel_102.setSizePolicy(sizePolicy8)
        self.GeneralidadesLabel_102.setMinimumSize(QSize(158, 0))
        self.GeneralidadesLabel_102.setStyleSheet(u"font: 550 11pt \"Allerta\";")
        self.GeneralidadesLabel_102.setLineWidth(1)
        self.GeneralidadesLabel_102.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.pagina_generalidades)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_6.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabPrim.setCurrentIndex(0)
        self.tabSec.setCurrentIndex(0)
        self.tabTerc.setCurrentIndex(0)
        self.tabNoC.setCurrentIndex(0)
        self.tabManning.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.topLogo.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"HidrApp Uniandes", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Hidr\u00e1ulica de canales abiertos", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Selecci\u00f3n de tecnolog\u00edas de tratamiento de aguas residuales</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.botonGeneralidades.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.botonGeneralidades_2.setText("")
        self.botonMenuPrimario.setText(QCoreApplication.translate("MainWindow", u"Tratamiento \n"
" primario", None))
        self.botonMenuSecundario.setText(QCoreApplication.translate("MainWindow", u"Tratamiento \n"
" secundario", None))
        self.botonMenuTerciario.setText(QCoreApplication.translate("MainWindow", u"Tratamiento \n"
" terciario", None))
        self.botonMenuOtros.setText(QCoreApplication.translate("MainWindow", u"Tratamiento \n"
" avanzado", None))
        self.groupBox_Resultados_19.setTitle(QCoreApplication.translate("MainWindow", u"Eficiencia de remoci\u00f3n", None))
        self.PrimComboBoxCriterio.setItemText(0, QCoreApplication.translate("MainWindow", u"DQO", None))
        self.PrimComboBoxCriterio.setItemText(1, QCoreApplication.translate("MainWindow", u"DBO", None))
        self.PrimComboBoxCriterio.setItemText(2, QCoreApplication.translate("MainWindow", u"SST", None))
        self.PrimComboBoxCriterio.setItemText(3, QCoreApplication.translate("MainWindow", u"Nitr\u00f3geno Total", None))
        self.PrimComboBoxCriterio.setItemText(4, QCoreApplication.translate("MainWindow", u"F\u00f3sforo Total", None))

        self.PrimComboBoxCriterio.setCurrentText(QCoreApplication.translate("MainWindow", u"DQO", None))
#if QT_CONFIG(tooltip)
        self.PrimInputMinCriterio.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputMinCriterio.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputMinCriterio.setText("")
        self.PrimInputMinCriterio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(tooltip)
        self.PrimInputMaxCriterio.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputMaxCriterio.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputMaxCriterio.setText("")
        self.PrimInputMaxCriterio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%", None))
        self.PrimLabelMinCriteiro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>M\u00ednimo</p></body></html>", None))
        self.PrimLabelMaxCriterio.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>M\u00e1ximo</p></body></html>", None))
        self.PrimLabelCriterio.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Criterio</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_3.setText("")
        self.PrimInputParametro_3.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_4.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_4.setText("")
        self.PrimInputParametro_4.setPlaceholderText("")
        self.groupBox_Propiedades_21.setTitle(QCoreApplication.translate("MainWindow", u"Criterios econ\u00f3micos", None))
#if QT_CONFIG(whatsthis)
        self.PrimInputMinCapital.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.PrimInputMinCapital.setText("")
        self.PrimInputMinCapital.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00ednimo", None))
        self.PrimLabelCostoOM.setText(QCoreApplication.translate("MainWindow", u"Costos operaci\u00f3n/mantenimiento [$]", None))
        self.PrimLabelCostoCapital.setText(QCoreApplication.translate("MainWindow", u"Costos de capital [$]", None))
#if QT_CONFIG(whatsthis)
        self.PrimInputMinOM.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.PrimInputMinOM.setText("")
        self.PrimInputMinOM.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00ednimo", None))
#if QT_CONFIG(whatsthis)
        self.PrimInputMaxCapital.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.PrimInputMaxCapital.setText("")
        self.PrimInputMaxCapital.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo", None))
#if QT_CONFIG(whatsthis)
        self.PrimInputMaxOM.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.PrimInputMaxOM.setText("")
        self.PrimInputMaxOM.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo", None))
        self.groupBox_Propiedades_23.setTitle(QCoreApplication.translate("MainWindow", u"Criterios ambientales", None))
        self.PrimLabelEnergia.setText(QCoreApplication.translate("MainWindow", u"Requerimientos de energ\u00eda ", None))
        self.PrimLabelRecuperacion.setText(QCoreApplication.translate("MainWindow", u"Recuperaci\u00f3n de productos", None))
        self.PrimComboBoxRecuperacion.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimComboBoxRecuperacion.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.PrimComboBoxRecuperacion.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.PrimComboBoxRecuperacion.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.PrimComboBoxRecuperacion.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.PrimComboBoxRecuperacion.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimComboBoxEnergia.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimComboBoxEnergia.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.PrimComboBoxEnergia.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.PrimComboBoxEnergia.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.PrimComboBoxEnergia.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.PrimComboBoxEnergia.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.groupBox_Propiedades_24.setTitle(QCoreApplication.translate("MainWindow", u"Criterios t\u00e9cnicos", None))
        self.PrimLabelRobustez.setText(QCoreApplication.translate("MainWindow", u"Robustez", None))
        self.PrimLabelSimplicidad.setText(QCoreApplication.translate("MainWindow", u"Simplicidad operacional", None))
        self.PrimComboBoxSimplicidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimComboBoxSimplicidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.PrimComboBoxSimplicidad.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.PrimComboBoxSimplicidad.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.PrimComboBoxSimplicidad.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.PrimComboBoxSimplicidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimComboBoxRobustez.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimComboBoxRobustez.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.PrimComboBoxRobustez.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.PrimComboBoxRobustez.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.PrimComboBoxRobustez.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.PrimComboBoxRobustez.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimLabelArea.setText(QCoreApplication.translate("MainWindow", u"Requerimientos de \u00e1rea", None))
        self.PrimComboBoxArea.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimComboBoxArea.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.PrimComboBoxArea.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.PrimComboBoxArea.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.PrimComboBoxArea.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.PrimComboBoxArea.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.groupBox_Propiedades_25.setTitle(QCoreApplication.translate("MainWindow", u"Criterios sociales", None))
        self.PrimLabelSocial.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Efectos negativos (olor, ruido, </p><p>impacto visual)</p></body></html>", None))
        self.PrimComboBoxSocial.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimComboBoxSocial.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.PrimComboBoxSocial.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.PrimComboBoxSocial.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.PrimComboBoxSocial.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.PrimComboBoxSocial.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimLabelMaxCriterio_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Aspecto a priorizar</p></body></html>", None))
        self.PrimComboBoxPeso.setItemText(0, QCoreApplication.translate("MainWindow", u"Equilibrado", None))
        self.PrimComboBoxPeso.setItemText(1, QCoreApplication.translate("MainWindow", u"Econ\u00f3mico", None))
        self.PrimComboBoxPeso.setItemText(2, QCoreApplication.translate("MainWindow", u"Ambiental", None))
        self.PrimComboBoxPeso.setItemText(3, QCoreApplication.translate("MainWindow", u"T\u00e9cnico", None))
        self.PrimComboBoxPeso.setItemText(4, QCoreApplication.translate("MainWindow", u"Social", None))

        self.PrimComboBoxPeso.setCurrentText(QCoreApplication.translate("MainWindow", u"Equilibrado", None))
        self.tabPrim.setTabText(self.tabPrim.indexOf(self.primarioEntrada), QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.groupBox_Propiedades_22.setTitle(QCoreApplication.translate("MainWindow", u"Tecnolog\u00edas", None))
#if QT_CONFIG(whatsthis)
        self.PrimFieldResultadoConvencional.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.PrimFieldResultadoConvencional.setText("")
        self.PrimFieldResultadoConvencional.setPlaceholderText("")
        self.PrimLabelConvencional.setText(QCoreApplication.translate("MainWindow", u"Tratamiento primario convencional", None))
#if QT_CONFIG(whatsthis)
        self.PrimFieldResultadoTQA.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.PrimFieldResultadoTQA.setText("")
        self.PrimFieldResultadoTQA.setPlaceholderText("")
        self.PrimLabelTQA.setText(QCoreApplication.translate("MainWindow", u"Tratamiento asistido qu\u00edmicamente", None))
        self.PrimBtnCalcular.setText(QCoreApplication.translate("MainWindow", u"Calcular resultados", None))
        self.PrimBtnReiniciar.setText(QCoreApplication.translate("MainWindow", u"Reiniciar campos", None))
        self.PrimLabelConvencional_2.setText(QCoreApplication.translate("MainWindow", u"TRATAMIENTO PRIMARIO", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_6.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_6.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_6.setText("")
        self.PrimInputParametro_6.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_7.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_7.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_7.setText("")
        self.PrimInputParametro_7.setPlaceholderText("")
        self.groupBox_Propiedades_46.setTitle(QCoreApplication.translate("MainWindow", u"Selecci\u00f3n", None))
        self.PrimLabelConvencional_15.setText(QCoreApplication.translate("MainWindow", u"Mejor tecnolog\u00eda de acuerdo a los requerimientos", None))
#if QT_CONFIG(whatsthis)
        self.PrimFieldResultadoMejor.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.PrimFieldResultadoMejor.setText("")
        self.PrimFieldResultadoMejor.setPlaceholderText("")
        self.tabPrim.setTabText(self.tabPrim.indexOf(self.primarioSalida), QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.SecuComboBoxPeso.setItemText(0, QCoreApplication.translate("MainWindow", u"Equilibrado", None))
        self.SecuComboBoxPeso.setItemText(1, QCoreApplication.translate("MainWindow", u"Econ\u00f3mico", None))
        self.SecuComboBoxPeso.setItemText(2, QCoreApplication.translate("MainWindow", u"Ambiental", None))
        self.SecuComboBoxPeso.setItemText(3, QCoreApplication.translate("MainWindow", u"T\u00e9cnico", None))
        self.SecuComboBoxPeso.setItemText(4, QCoreApplication.translate("MainWindow", u"Social", None))

        self.SecuComboBoxPeso.setCurrentText(QCoreApplication.translate("MainWindow", u"Equilibrado", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_5.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_5.setText("")
        self.PrimInputParametro_5.setPlaceholderText("")
        self.groupBox_Resultados_20.setTitle(QCoreApplication.translate("MainWindow", u"Eficiencia de remoci\u00f3n", None))
        self.SecuComboBoxCriterio.setItemText(0, QCoreApplication.translate("MainWindow", u"DQO", None))
        self.SecuComboBoxCriterio.setItemText(1, QCoreApplication.translate("MainWindow", u"DBO", None))
        self.SecuComboBoxCriterio.setItemText(2, QCoreApplication.translate("MainWindow", u"SST", None))
        self.SecuComboBoxCriterio.setItemText(3, QCoreApplication.translate("MainWindow", u"Nitr\u00f3geno Total", None))
        self.SecuComboBoxCriterio.setItemText(4, QCoreApplication.translate("MainWindow", u"F\u00f3sforo Total", None))

        self.SecuComboBoxCriterio.setCurrentText(QCoreApplication.translate("MainWindow", u"DQO", None))
#if QT_CONFIG(tooltip)
        self.SecuInputMinCriterio.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.SecuInputMinCriterio.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.SecuInputMinCriterio.setText("")
        self.SecuInputMinCriterio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(tooltip)
        self.SecuInputMaxCriterio.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.SecuInputMaxCriterio.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.SecuInputMaxCriterio.setText("")
        self.SecuInputMaxCriterio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%", None))
        self.PrimLabelMinCriteiro_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>M\u00ednimo</p></body></html>", None))
        self.PrimLabelMaxCriterio_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>M\u00e1ximo</p></body></html>", None))
        self.PrimLabelCriterio_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Criterio</p></body></html>", None))
        self.groupBox_Propiedades_26.setTitle(QCoreApplication.translate("MainWindow", u"Criterios econ\u00f3micos", None))
#if QT_CONFIG(whatsthis)
        self.SecuInputMinCapital.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.SecuInputMinCapital.setText("")
        self.SecuInputMinCapital.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00ednimo", None))
        self.SecuLabelCostoOM.setText(QCoreApplication.translate("MainWindow", u"Costos operaci\u00f3n/mantenimiento [$]", None))
        self.SecuLabelCostoCapital.setText(QCoreApplication.translate("MainWindow", u"Costos de capital [$]", None))
#if QT_CONFIG(whatsthis)
        self.SecuInputMinOM.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.SecuInputMinOM.setText("")
        self.SecuInputMinOM.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00ednimo", None))
#if QT_CONFIG(whatsthis)
        self.SecuInputMaxCapital.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.SecuInputMaxCapital.setText("")
        self.SecuInputMaxCapital.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo", None))
#if QT_CONFIG(whatsthis)
        self.SecuInputMaxOM.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.SecuInputMaxOM.setText("")
        self.SecuInputMaxOM.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo", None))
        self.groupBox_Propiedades_27.setTitle(QCoreApplication.translate("MainWindow", u"Criterios ambientales", None))
        self.PrimLabelEnergia_2.setText(QCoreApplication.translate("MainWindow", u"Requerimientos de energ\u00eda ", None))
        self.PrimLabelRecuperacion_2.setText(QCoreApplication.translate("MainWindow", u"Recuperaci\u00f3n de productos", None))
        self.SecuComboBoxRecuperacion.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.SecuComboBoxRecuperacion.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.SecuComboBoxRecuperacion.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.SecuComboBoxRecuperacion.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.SecuComboBoxRecuperacion.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.SecuComboBoxRecuperacion.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.SecuComboBoxEnergia.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.SecuComboBoxEnergia.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.SecuComboBoxEnergia.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.SecuComboBoxEnergia.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.SecuComboBoxEnergia.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.SecuComboBoxEnergia.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.groupBox_Propiedades_28.setTitle(QCoreApplication.translate("MainWindow", u"Criterios t\u00e9cnicos", None))
        self.PrimLabelRobustez_2.setText(QCoreApplication.translate("MainWindow", u"Robustez", None))
        self.PrimLabelSimplicidad_2.setText(QCoreApplication.translate("MainWindow", u"Simplicidad operacional", None))
        self.SecuComboBoxSimplicidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.SecuComboBoxSimplicidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.SecuComboBoxSimplicidad.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.SecuComboBoxSimplicidad.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.SecuComboBoxSimplicidad.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.SecuComboBoxSimplicidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.SecuComboBoxRobustez.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.SecuComboBoxRobustez.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.SecuComboBoxRobustez.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.SecuComboBoxRobustez.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.SecuComboBoxRobustez.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.SecuComboBoxRobustez.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimLabelArea_2.setText(QCoreApplication.translate("MainWindow", u"Requerimientos de \u00e1rea", None))
        self.SecuComboBoxArea.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.SecuComboBoxArea.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.SecuComboBoxArea.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.SecuComboBoxArea.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.SecuComboBoxArea.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.SecuComboBoxArea.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.groupBox_Propiedades_29.setTitle(QCoreApplication.translate("MainWindow", u"Criterios sociales", None))
        self.PrimLabelSocial_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Efectos negativos (olor, ruido, </p><p>impacto visual)</p></body></html>", None))
        self.SecuComboBoxSocial.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.SecuComboBoxSocial.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.SecuComboBoxSocial.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.SecuComboBoxSocial.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.SecuComboBoxSocial.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.SecuComboBoxSocial.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_9.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_9.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_9.setText("")
        self.PrimInputParametro_9.setPlaceholderText("")
        self.PrimLabelMaxCriterio_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Aspecto a priorizar</p></body></html>", None))
        self.tabSec.setTabText(self.tabSec.indexOf(self.secundarioEntrada), QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.SecuBtnReiniciar.setText(QCoreApplication.translate("MainWindow", u"Reiniciar campos", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_8.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_8.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_8.setText("")
        self.PrimInputParametro_8.setPlaceholderText("")
        self.PrimLabelConvencional_3.setText(QCoreApplication.translate("MainWindow", u"TRATAMIENTO SECUNDARIO", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_10.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_10.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_10.setText("")
        self.PrimInputParametro_10.setPlaceholderText("")
        self.groupBox_Propiedades_30.setTitle(QCoreApplication.translate("MainWindow", u"Puntajes", None))
#if QT_CONFIG(whatsthis)
        self.SecuFieldResultadoCAS.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.SecuFieldResultadoCAS.setText("")
        self.SecuFieldResultadoCAS.setPlaceholderText("")
        self.PrimLabelConvencional_6.setText(QCoreApplication.translate("MainWindow", u"Proceso convencional de lodos activados", None))
#if QT_CONFIG(whatsthis)
        self.SecuFieldResultadoSBR.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.SecuFieldResultadoSBR.setText("")
        self.SecuFieldResultadoSBR.setPlaceholderText("")
        self.PrimLabelTQA_4.setText(QCoreApplication.translate("MainWindow", u"Reactor batch en secuencia", None))
        self.PrimLabelTQA_5.setText(QCoreApplication.translate("MainWindow", u"Filtros percoladores", None))
        self.PrimLabelTQA_6.setText(QCoreApplication.translate("MainWindow", u"Reactor biol\u00f3gico de biodiscos", None))
#if QT_CONFIG(whatsthis)
        self.SecuFieldResultadoTF.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.SecuFieldResultadoTF.setText("")
        self.SecuFieldResultadoTF.setPlaceholderText("")
#if QT_CONFIG(whatsthis)
        self.SecuFieldResultadoRBC.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.SecuFieldResultadoRBC.setText("")
        self.SecuFieldResultadoRBC.setPlaceholderText("")
        self.SecuBtnCalcular.setText(QCoreApplication.translate("MainWindow", u"Calcular resultados", None))
        self.groupBox_Propiedades_47.setTitle(QCoreApplication.translate("MainWindow", u"Selecci\u00f3n", None))
        self.PrimLabelConvencional_16.setText(QCoreApplication.translate("MainWindow", u"Mejor tecnolog\u00eda de acuerdo a los requerimientos", None))
#if QT_CONFIG(whatsthis)
        self.SecuFieldResultadoMejor.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.SecuFieldResultadoMejor.setText("")
        self.SecuFieldResultadoMejor.setPlaceholderText("")
        self.tabSec.setTabText(self.tabSec.indexOf(self.secundarioResultados), QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.TercComboBoxPeso.setItemText(0, QCoreApplication.translate("MainWindow", u"Equilibrado", None))
        self.TercComboBoxPeso.setItemText(1, QCoreApplication.translate("MainWindow", u"Econ\u00f3mico", None))
        self.TercComboBoxPeso.setItemText(2, QCoreApplication.translate("MainWindow", u"Ambiental", None))
        self.TercComboBoxPeso.setItemText(3, QCoreApplication.translate("MainWindow", u"T\u00e9cnico", None))
        self.TercComboBoxPeso.setItemText(4, QCoreApplication.translate("MainWindow", u"Social", None))

        self.TercComboBoxPeso.setCurrentText(QCoreApplication.translate("MainWindow", u"Equilibrado", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_15.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_15.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_15.setText("")
        self.PrimInputParametro_15.setPlaceholderText("")
        self.groupBox_Resultados_22.setTitle(QCoreApplication.translate("MainWindow", u"Eficiencia de remoci\u00f3n", None))
        self.TercComboBoxCriterio.setItemText(0, QCoreApplication.translate("MainWindow", u"DQO", None))
        self.TercComboBoxCriterio.setItemText(1, QCoreApplication.translate("MainWindow", u"DBO", None))
        self.TercComboBoxCriterio.setItemText(2, QCoreApplication.translate("MainWindow", u"SST", None))
        self.TercComboBoxCriterio.setItemText(3, QCoreApplication.translate("MainWindow", u"Nitr\u00f3geno Total", None))
        self.TercComboBoxCriterio.setItemText(4, QCoreApplication.translate("MainWindow", u"F\u00f3sforo Total", None))

        self.TercComboBoxCriterio.setCurrentText(QCoreApplication.translate("MainWindow", u"DQO", None))
#if QT_CONFIG(tooltip)
        self.TercInputMinCriterio.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.TercInputMinCriterio.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.TercInputMinCriterio.setText("")
        self.TercInputMinCriterio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(tooltip)
        self.TercInputMaxCriterio.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.TercInputMaxCriterio.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.TercInputMaxCriterio.setText("")
        self.TercInputMaxCriterio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%", None))
        self.PrimLabelMinCriteiro_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>M\u00ednimo</p></body></html>", None))
        self.PrimLabelMaxCriterio_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>M\u00e1ximo</p></body></html>", None))
        self.PrimLabelCriterio_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Criterio</p></body></html>", None))
        self.groupBox_Propiedades_36.setTitle(QCoreApplication.translate("MainWindow", u"Criterios econ\u00f3micos", None))
#if QT_CONFIG(whatsthis)
        self.TercInputMinCapital.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.TercInputMinCapital.setText("")
        self.TercInputMinCapital.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00ednimo", None))
        self.SecuLabelCostoOM_3.setText(QCoreApplication.translate("MainWindow", u"Costos operaci\u00f3n/mantenimiento [$]", None))
        self.TercLabelCostoCapital.setText(QCoreApplication.translate("MainWindow", u"Costos de capital [$]", None))
#if QT_CONFIG(whatsthis)
        self.TercInputMinOM.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.TercInputMinOM.setText("")
        self.TercInputMinOM.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00ednimo", None))
#if QT_CONFIG(whatsthis)
        self.TercInputMaxCapital.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.TercInputMaxCapital.setText("")
        self.TercInputMaxCapital.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo", None))
#if QT_CONFIG(whatsthis)
        self.TercInputMaxOM.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.TercInputMaxOM.setText("")
        self.TercInputMaxOM.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo", None))
        self.groupBox_Propiedades_37.setTitle(QCoreApplication.translate("MainWindow", u"Criterios ambientales", None))
        self.PrimLabelEnergia_4.setText(QCoreApplication.translate("MainWindow", u"Requerimientos de energ\u00eda ", None))
        self.PrimLabelRecuperacion_4.setText(QCoreApplication.translate("MainWindow", u"Recuperaci\u00f3n de productos", None))
        self.TercComboBoxRecuperacion.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.TercComboBoxRecuperacion.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.TercComboBoxRecuperacion.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.TercComboBoxRecuperacion.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.TercComboBoxRecuperacion.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.TercComboBoxRecuperacion.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.TercComboBoxEnergia.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.TercComboBoxEnergia.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.TercComboBoxEnergia.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.TercComboBoxEnergia.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.TercComboBoxEnergia.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.TercComboBoxEnergia.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.groupBox_Propiedades_38.setTitle(QCoreApplication.translate("MainWindow", u"Criterios t\u00e9cnicos", None))
        self.PrimLabelRobustez_4.setText(QCoreApplication.translate("MainWindow", u"Robustez", None))
        self.PrimLabelSimplicidad_4.setText(QCoreApplication.translate("MainWindow", u"Simplicidad operacional", None))
        self.TercComboBoxSimplicidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.TercComboBoxSimplicidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.TercComboBoxSimplicidad.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.TercComboBoxSimplicidad.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.TercComboBoxSimplicidad.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.TercComboBoxSimplicidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.TercComboBoxRobustez.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.TercComboBoxRobustez.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.TercComboBoxRobustez.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.TercComboBoxRobustez.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.TercComboBoxRobustez.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.TercComboBoxRobustez.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimLabelArea_4.setText(QCoreApplication.translate("MainWindow", u"Requerimientos de \u00e1rea", None))
        self.TercComboBoxArea.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.TercComboBoxArea.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.TercComboBoxArea.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.TercComboBoxArea.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.TercComboBoxArea.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.TercComboBoxArea.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.groupBox_Propiedades_39.setTitle(QCoreApplication.translate("MainWindow", u"Criterios sociales", None))
        self.PrimLabelSocial_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Efectos negativos (olor, ruido, </p><p>impacto visual)</p></body></html>", None))
        self.TercComboBoxSocial.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.TercComboBoxSocial.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.TercComboBoxSocial.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.TercComboBoxSocial.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.TercComboBoxSocial.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.TercComboBoxSocial.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_16.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_16.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_16.setText("")
        self.PrimInputParametro_16.setPlaceholderText("")
        self.PrimLabelMaxCriterio_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Aspecto a priorizar</p></body></html>", None))
        self.tabTerc.setTabText(self.tabTerc.indexOf(self.terciarioEntrada), QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.TercBtnReiniciar.setText(QCoreApplication.translate("MainWindow", u"Reiniciar campos", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_17.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_17.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_17.setText("")
        self.PrimInputParametro_17.setPlaceholderText("")
        self.PrimLabelConvencional_9.setText(QCoreApplication.translate("MainWindow", u"TRATAMIENTO TERCIARIO", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_18.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_18.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_18.setText("")
        self.PrimInputParametro_18.setPlaceholderText("")
        self.groupBox_Propiedades_40.setTitle(QCoreApplication.translate("MainWindow", u"Puntajes", None))
#if QT_CONFIG(whatsthis)
        self.TercFieldResultadoAO.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.TercFieldResultadoAO.setText("")
        self.TercFieldResultadoAO.setPlaceholderText("")
        self.PrimLabelConvencional_10.setText(QCoreApplication.translate("MainWindow", u"Sistema A/O (eliminaci\u00f3n biol\u00f3gica de f\u00f3sforo)", None))
        self.PrimLabelTQA_10.setText(QCoreApplication.translate("MainWindow", u"PhoStrip (eliminaci\u00f3n biol\u00f3gica de f\u00f3sforo)", None))
        self.PrimLabelTQA_11.setText(QCoreApplication.translate("MainWindow", u"Bardenpho (eliminaci\u00f3n biol\u00f3gica de f\u00f3sforo\n"
"y nitr\u00f3geno)", None))
#if QT_CONFIG(whatsthis)
        self.TercFieldResultadoPhoStrip.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.TercFieldResultadoPhoStrip.setText("")
        self.TercFieldResultadoPhoStrip.setPlaceholderText("")
#if QT_CONFIG(whatsthis)
        self.TercFieldResultadoBardenpho.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.TercFieldResultadoBardenpho.setText("")
        self.TercFieldResultadoBardenpho.setPlaceholderText("")
        self.TercBtnCalcular.setText(QCoreApplication.translate("MainWindow", u"Calcular resultados", None))
        self.groupBox_Propiedades_48.setTitle(QCoreApplication.translate("MainWindow", u"Selecci\u00f3n", None))
        self.PrimLabelConvencional_17.setText(QCoreApplication.translate("MainWindow", u"Mejor tecnolog\u00eda de acuerdo a los requerimientos", None))
#if QT_CONFIG(whatsthis)
        self.TercFieldResultadoMejor.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.TercFieldResultadoMejor.setText("")
        self.TercFieldResultadoMejor.setPlaceholderText("")
        self.tabTerc.setTabText(self.tabTerc.indexOf(self.terciarioResultado), QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.NoCComboBoxPeso.setItemText(0, QCoreApplication.translate("MainWindow", u"Equilibrado", None))
        self.NoCComboBoxPeso.setItemText(1, QCoreApplication.translate("MainWindow", u"Econ\u00f3mico", None))
        self.NoCComboBoxPeso.setItemText(2, QCoreApplication.translate("MainWindow", u"Ambiental", None))
        self.NoCComboBoxPeso.setItemText(3, QCoreApplication.translate("MainWindow", u"T\u00e9cnico", None))
        self.NoCComboBoxPeso.setItemText(4, QCoreApplication.translate("MainWindow", u"Social", None))

        self.NoCComboBoxPeso.setCurrentText(QCoreApplication.translate("MainWindow", u"Equilibrado", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_19.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_19.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_19.setText("")
        self.PrimInputParametro_19.setPlaceholderText("")
        self.groupBox_Resultados_23.setTitle(QCoreApplication.translate("MainWindow", u"Eficiencia de remoci\u00f3n", None))
        self.NoCComboBoxCriterio.setItemText(0, QCoreApplication.translate("MainWindow", u"DQO", None))
        self.NoCComboBoxCriterio.setItemText(1, QCoreApplication.translate("MainWindow", u"DBO", None))
        self.NoCComboBoxCriterio.setItemText(2, QCoreApplication.translate("MainWindow", u"SST", None))
        self.NoCComboBoxCriterio.setItemText(3, QCoreApplication.translate("MainWindow", u"Nitr\u00f3geno Total", None))
        self.NoCComboBoxCriterio.setItemText(4, QCoreApplication.translate("MainWindow", u"F\u00f3sforo Total", None))

        self.NoCComboBoxCriterio.setCurrentText(QCoreApplication.translate("MainWindow", u"DQO", None))
#if QT_CONFIG(tooltip)
        self.NoCInputMinCriterio.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.NoCInputMinCriterio.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.NoCInputMinCriterio.setText("")
        self.NoCInputMinCriterio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(tooltip)
        self.NoCInputMaxCriterio.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.NoCInputMaxCriterio.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.NoCInputMaxCriterio.setText("")
        self.NoCInputMaxCriterio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%", None))
        self.PrimLabelMinCriteiro_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>M\u00ednimo</p></body></html>", None))
        self.PrimLabelMaxCriterio_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>M\u00e1ximo</p></body></html>", None))
        self.PrimLabelCriterio_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Criterio</p></body></html>", None))
        self.groupBox_Propiedades_41.setTitle(QCoreApplication.translate("MainWindow", u"Criterios econ\u00f3micos", None))
#if QT_CONFIG(whatsthis)
        self.NoCInputMinCapital.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.NoCInputMinCapital.setText("")
        self.NoCInputMinCapital.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00ednimo", None))
        self.SecuLabelCostoOM_4.setText(QCoreApplication.translate("MainWindow", u"Costos operaci\u00f3n/mantenimiento [$]", None))
        self.TercLabelCostoCapital_2.setText(QCoreApplication.translate("MainWindow", u"Costos de capital [$]", None))
#if QT_CONFIG(whatsthis)
        self.NoCInputMinOM.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.NoCInputMinOM.setText("")
        self.NoCInputMinOM.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00ednimo", None))
#if QT_CONFIG(whatsthis)
        self.NoCInputMaxCapital.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.NoCInputMaxCapital.setText("")
        self.NoCInputMaxCapital.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo", None))
#if QT_CONFIG(whatsthis)
        self.NoCInputMaxOM.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.NoCInputMaxOM.setText("")
        self.NoCInputMaxOM.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo", None))
        self.groupBox_Propiedades_42.setTitle(QCoreApplication.translate("MainWindow", u"Criterios ambientales", None))
        self.PrimLabelEnergia_5.setText(QCoreApplication.translate("MainWindow", u"Requerimientos de energ\u00eda ", None))
        self.PrimLabelRecuperacion_5.setText(QCoreApplication.translate("MainWindow", u"Recuperaci\u00f3n de productos", None))
        self.NoCComboBoxRecuperacion.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.NoCComboBoxRecuperacion.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.NoCComboBoxRecuperacion.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.NoCComboBoxRecuperacion.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.NoCComboBoxRecuperacion.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.NoCComboBoxRecuperacion.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.NoCComboBoxEnergia.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.NoCComboBoxEnergia.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.NoCComboBoxEnergia.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.NoCComboBoxEnergia.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.NoCComboBoxEnergia.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.NoCComboBoxEnergia.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.groupBox_Propiedades_43.setTitle(QCoreApplication.translate("MainWindow", u"Criterios t\u00e9cnicos", None))
        self.PrimLabelRobustez_5.setText(QCoreApplication.translate("MainWindow", u"Robustez", None))
        self.PrimLabelSimplicidad_5.setText(QCoreApplication.translate("MainWindow", u"Simplicidad operacional", None))
        self.NoCComboBoxSimplicidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.NoCComboBoxSimplicidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.NoCComboBoxSimplicidad.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.NoCComboBoxSimplicidad.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.NoCComboBoxSimplicidad.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.NoCComboBoxSimplicidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.NoCComboBoxRobustez.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.NoCComboBoxRobustez.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.NoCComboBoxRobustez.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.NoCComboBoxRobustez.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.NoCComboBoxRobustez.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.NoCComboBoxRobustez.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.PrimLabelArea_5.setText(QCoreApplication.translate("MainWindow", u"Requerimientos de \u00e1rea", None))
        self.NoCComboBoxArea.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.NoCComboBoxArea.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.NoCComboBoxArea.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.NoCComboBoxArea.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.NoCComboBoxArea.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.NoCComboBoxArea.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.groupBox_Propiedades_44.setTitle(QCoreApplication.translate("MainWindow", u"Criterios sociales", None))
        self.PrimLabelSocial_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Efectos negativos (olor, ruido, </p><p>impacto visual)</p></body></html>", None))
        self.NoCComboBoxSocial.setItemText(0, QCoreApplication.translate("MainWindow", u"Muy alto", None))
        self.NoCComboBoxSocial.setItemText(1, QCoreApplication.translate("MainWindow", u"Alto", None))
        self.NoCComboBoxSocial.setItemText(2, QCoreApplication.translate("MainWindow", u"Moderado", None))
        self.NoCComboBoxSocial.setItemText(3, QCoreApplication.translate("MainWindow", u"Bajo", None))
        self.NoCComboBoxSocial.setItemText(4, QCoreApplication.translate("MainWindow", u"Muy bajo", None))

        self.NoCComboBoxSocial.setCurrentText(QCoreApplication.translate("MainWindow", u"Muy alto", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_20.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_20.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_20.setText("")
        self.PrimInputParametro_20.setPlaceholderText("")
        self.PrimLabelMaxCriterio_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Aspecto a priorizar</p></body></html>", None))
        self.tabNoC.setTabText(self.tabNoC.indexOf(self.NoConvEntrada), QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.NoCBtnReiniciar.setText(QCoreApplication.translate("MainWindow", u"Reiniciar campos", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_21.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_21.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_21.setText("")
        self.PrimInputParametro_21.setPlaceholderText("")
        self.PrimLabelConvencional_11.setText(QCoreApplication.translate("MainWindow", u"TRATAMIENTO NO CONVENCIONAL Y AVANZADO", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_22.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_22.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_22.setText("")
        self.PrimInputParametro_22.setPlaceholderText("")
        self.groupBox_Propiedades_45.setTitle(QCoreApplication.translate("MainWindow", u"Puntajes", None))
        self.PrimLabelConvencional_12.setText(QCoreApplication.translate("MainWindow", u"Tren de lagunas de estabilizaci\u00f3n", None))
#if QT_CONFIG(whatsthis)
        self.NoCFieldResultadoLaguna.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.NoCFieldResultadoLaguna.setText("")
        self.NoCFieldResultadoLaguna.setPlaceholderText("")
        self.PrimLabelTQA_12.setText(QCoreApplication.translate("MainWindow", u"Reactor Anaerobio de Flujo Ascendente (UASB)", None))
        self.PrimLabelTQA_13.setText(QCoreApplication.translate("MainWindow", u"Humedal construido", None))
#if QT_CONFIG(whatsthis)
        self.NoCFieldResultadoUASB.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.NoCFieldResultadoUASB.setText("")
        self.NoCFieldResultadoUASB.setPlaceholderText("")
#if QT_CONFIG(whatsthis)
        self.NoCFieldResultadoHumedal.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.NoCFieldResultadoHumedal.setText("")
        self.NoCFieldResultadoHumedal.setPlaceholderText("")
        self.PrimLabelTQA_14.setText(QCoreApplication.translate("MainWindow", u"Reactor Biol\u00f3gico de Membrana (MBR)", None))
#if QT_CONFIG(whatsthis)
        self.NoCFieldResultadoMBR.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.NoCFieldResultadoMBR.setText("")
        self.NoCFieldResultadoMBR.setPlaceholderText("")
        self.NoCBtnCalcular.setText(QCoreApplication.translate("MainWindow", u"Calcular resultados", None))
        self.groupBox_Propiedades_49.setTitle(QCoreApplication.translate("MainWindow", u"Selecci\u00f3n", None))
        self.PrimLabelConvencional_18.setText(QCoreApplication.translate("MainWindow", u"Mejor tecnolog\u00eda de acuerdo a los requerimientos", None))
#if QT_CONFIG(whatsthis)
        self.NoCFieldResultadoMejor.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.NoCFieldResultadoMejor.setText("")
        self.NoCFieldResultadoMejor.setPlaceholderText("")
        self.tabNoC.setTabText(self.tabNoC.indexOf(self.NoConvResultados), QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.groupBox_Propiedades_7.setTitle("")
        self.GeneralidadesLabel_22.setText(QCoreApplication.translate("MainWindow", u"5.56%", None))
        self.GeneralidadesLabel_39.setText(QCoreApplication.translate("MainWindow", u"5.56%", None))
        self.GeneralidadesLabel_12.setText(QCoreApplication.translate("MainWindow", u"16.67%", None))
        self.GeneralidadesLabel_26.setText(QCoreApplication.translate("MainWindow", u"16.67%", None))
        self.GeneralidadesLabel_21.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_37.setText(QCoreApplication.translate("MainWindow", u"5.56%", None))
        self.GeneralidadesLabel_40.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_33.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_116.setText(QCoreApplication.translate("MainWindow", u"8.33 %", None))
        self.GeneralidadesLabel_28.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_31.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_19.setText(QCoreApplication.translate("MainWindow", u"5.56%", None))
        self.GeneralidadesLabel_16.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_17.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_38.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_29.setText(QCoreApplication.translate("MainWindow", u"50 %", None))
        self.GeneralidadesLabel_43.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_13.setText(QCoreApplication.translate("MainWindow", u"5.56%", None))
        self.GeneralidadesLabel_41.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_18.setText(QCoreApplication.translate("MainWindow", u"16.67%", None))
        self.GeneralidadesLabel_32.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_10.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.GeneralidadesLabel_8.setText(QCoreApplication.translate("MainWindow", u"A2", None))
        self.GeneralidadesLabel_9.setText(QCoreApplication.translate("MainWindow", u"A3", None))
        self.GeneralidadesLabel_47.setText(QCoreApplication.translate("MainWindow", u"E2", None))
        self.GeneralidadesLabel_68.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.GeneralidadesLabel_11.setText(QCoreApplication.translate("MainWindow", u"E1", None))
        self.GeneralidadesLabel_52.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.GeneralidadesLabel_71.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.GeneralidadesLabel_63.setText(QCoreApplication.translate("MainWindow", u"T3", None))
        self.GeneralidadesLabel_92.setText(QCoreApplication.translate("MainWindow", u"\u03a3C", None))
        self.GeneralidadesLabel_55.setText(QCoreApplication.translate("MainWindow", u"T1", None))
        self.GeneralidadesLabel_58.setText(QCoreApplication.translate("MainWindow", u"T2", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_27.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_27.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_27.setText("")
        self.PrimInputParametro_27.setPlaceholderText("")
        self.GeneralidadesLabel_20.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_24.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_23.setText(QCoreApplication.translate("MainWindow", u"25 %", None))
        self.GeneralidadesLabel_27.setText(QCoreApplication.translate("MainWindow", u"8.33 %", None))
        self.GeneralidadesLabel_25.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_82.setText(QCoreApplication.translate("MainWindow", u"100 %", None))
        self.GeneralidadesLabel_80.setText(QCoreApplication.translate("MainWindow", u"100 %", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_25.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_25.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_25.setText("")
        self.PrimInputParametro_25.setPlaceholderText("")
        self.GeneralidadesLabel_87.setText(QCoreApplication.translate("MainWindow", u"100 %", None))
        self.GeneralidadesLabel_109.setText(QCoreApplication.translate("MainWindow", u"8.33 %", None))
        self.GeneralidadesLabel_110.setText(QCoreApplication.translate("MainWindow", u"8.33 %", None))
        self.GeneralidadesLabel_104.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_114.setText(QCoreApplication.translate("MainWindow", u"25 %", None))
        self.GeneralidadesLabel_106.setText(QCoreApplication.translate("MainWindow", u"25 %", None))
        self.GeneralidadesLabel_115.setText(QCoreApplication.translate("MainWindow", u"8.33 %", None))
        self.GeneralidadesLabel_112.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_113.setText(QCoreApplication.translate("MainWindow", u"8.33 %", None))
        self.GeneralidadesLabel_105.setText(QCoreApplication.translate("MainWindow", u"8.33 %", None))
        self.GeneralidadesLabel_42.setText(QCoreApplication.translate("MainWindow", u"5.56%", None))
        self.GeneralidadesLabel_36.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_78.setText(QCoreApplication.translate("MainWindow", u"16.67 %", None))
        self.GeneralidadesLabel_81.setText(QCoreApplication.translate("MainWindow", u"16.67 %", None))
        self.GeneralidadesLabel_85.setText(QCoreApplication.translate("MainWindow", u"16.67 %", None))
        self.GeneralidadesLabel_89.setText(QCoreApplication.translate("MainWindow", u"25 %", None))
        self.GeneralidadesLabel_93.setText(QCoreApplication.translate("MainWindow", u"50 %", None))
        self.GeneralidadesLabel_84.setText(QCoreApplication.translate("MainWindow", u"50 %", None))
        self.GeneralidadesLabel_86.setText(QCoreApplication.translate("MainWindow", u"16.67 %", None))
        self.GeneralidadesLabel_83.setText(QCoreApplication.translate("MainWindow", u"16.67 %", None))
        self.GeneralidadesLabel_97.setText(QCoreApplication.translate("MainWindow", u"16.67 %", None))
        self.GeneralidadesLabel_120.setText(QCoreApplication.translate("MainWindow", u"25 %", None))
        self.GeneralidadesLabel_111.setText(QCoreApplication.translate("MainWindow", u"16.67 %", None))
        self.GeneralidadesLabel_30.setText(QCoreApplication.translate("MainWindow", u"16.67 %", None))
        self.GeneralidadesLabel_35.setText(QCoreApplication.translate("MainWindow", u"16.67 %", None))
        self.GeneralidadesLabel_77.setText(QCoreApplication.translate("MainWindow", u"16.67 %", None))
        self.GeneralidadesLabel_107.setText(QCoreApplication.translate("MainWindow", u"50 %", None))
        self.GeneralidadesLabel_108.setText(QCoreApplication.translate("MainWindow", u"16.67 %", None))
        self.GeneralidadesLabel_14.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_34.setText(QCoreApplication.translate("MainWindow", u"16.67%", None))
        self.GeneralidadesLabel_121.setText(QCoreApplication.translate("MainWindow", u"8.33 %", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_24.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_24.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_24.setText("")
        self.PrimInputParametro_24.setPlaceholderText("")
        self.GeneralidadesLabel_117.setText(QCoreApplication.translate("MainWindow", u"8.33 %", None))
        self.GeneralidadesLabel_118.setText(QCoreApplication.translate("MainWindow", u"8.33 %", None))
        self.GeneralidadesLabel_129.setText(QCoreApplication.translate("MainWindow", u"100 %", None))
        self.GeneralidadesLabel_15.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_119.setText(QCoreApplication.translate("MainWindow", u"25 %", None))
        self.GeneralidadesLabel_76.setText(QCoreApplication.translate("MainWindow", u"100 %", None))
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_23.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_23.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_23.setText("")
        self.PrimInputParametro_23.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.PrimInputParametro_26.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.PrimInputParametro_26.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PrimInputParametro_26.setText("")
        self.PrimInputParametro_26.setPlaceholderText("")
        self.GeneralidadesLabel_7.setText(QCoreApplication.translate("MainWindow", u"A1", None))
        self.GeneralidadesLabel_90.setText(QCoreApplication.translate("MainWindow", u"Econ\u00f3mico", None))
        self.GeneralidadesLabel_79.setText(QCoreApplication.translate("MainWindow", u"T\u00e9cnico", None))
        self.GeneralidadesLabel_94.setText(QCoreApplication.translate("MainWindow", u"Equilibrado", None))
        self.GeneralidadesLabel_88.setText(QCoreApplication.translate("MainWindow", u"Social", None))
        self.GeneralidadesLabel_91.setText(QCoreApplication.translate("MainWindow", u"Ambiental", None))
        self.PrimLabelConvencional_13.setText(QCoreApplication.translate("MainWindow", u"Enfoques de an\u00e1lisis", None))
        self.tabManning.setTabText(self.tabManning.indexOf(self.Matriz), QCoreApplication.translate("MainWindow", u"Pesos", None))
        self.groupBox_Propiedades_8.setTitle("")
        self.GeneralidadesLabel_204.setText(QCoreApplication.translate("MainWindow", u"Costos de inversi\u00f3n", None))
        self.GeneralidadesLabel_205.setText(QCoreApplication.translate("MainWindow", u"Potencial recuperaci\u00f3n de productos", None))
        self.GeneralidadesLabel_206.setText(QCoreApplication.translate("MainWindow", u"Requerimientos de \u00e1rea", None))
        self.GeneralidadesLabel_211.setText(QCoreApplication.translate("MainWindow", u"Requerimientos de energ\u00eda", None))
        self.GeneralidadesLabel_210.setText(QCoreApplication.translate("MainWindow", u"Simplicidad operacional ", None))
        self.GeneralidadesLabel_208.setText(QCoreApplication.translate("MainWindow", u"Eficiencia de remoci\u00f3n ", None))
        self.GeneralidadesLabel_212.setText(QCoreApplication.translate("MainWindow", u"Problemas potenciales", None))
        self.GeneralidadesLabel_209.setText(QCoreApplication.translate("MainWindow", u"Robustez", None))
        self.GeneralidadesLabel_207.setText(QCoreApplication.translate("MainWindow", u"Costos de operaci\u00f3n y mantenimiento", None))
        self.GeneralidadesLabel_213.setText(QCoreApplication.translate("MainWindow", u"E1", None))
        self.GeneralidadesLabel_214.setText(QCoreApplication.translate("MainWindow", u"E2", None))
        self.GeneralidadesLabel_217.setText(QCoreApplication.translate("MainWindow", u"A3", None))
        self.GeneralidadesLabel_219.setText(QCoreApplication.translate("MainWindow", u"T2", None))
        self.GeneralidadesLabel_216.setText(QCoreApplication.translate("MainWindow", u"A2", None))
        self.GeneralidadesLabel_221.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.GeneralidadesLabel_218.setText(QCoreApplication.translate("MainWindow", u"T1", None))
        self.GeneralidadesLabel_220.setText(QCoreApplication.translate("MainWindow", u"T3", None))
        self.GeneralidadesLabel_215.setText(QCoreApplication.translate("MainWindow", u"A1", None))
        self.GeneralidadesLabel_222.setText(QCoreApplication.translate("MainWindow", u"Econ\u00f3mico", None))
        self.GeneralidadesLabel_224.setText(QCoreApplication.translate("MainWindow", u"T\u00e9cnico", None))
        self.GeneralidadesLabel_223.setText(QCoreApplication.translate("MainWindow", u"Ambiental", None))
        self.GeneralidadesLabel_225.setText(QCoreApplication.translate("MainWindow", u"Social", None))
        self.GeneralidadesLabel_226.setText(QCoreApplication.translate("MainWindow", u"Identificador", None))
        self.GeneralidadesLabel_227.setText(QCoreApplication.translate("MainWindow", u"Criterio", None))
        self.GeneralidadesLabel_228.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda", None))
        self.groupBox_Propiedades_9.setTitle("")
        self.GeneralidadesLabel_231.setText(QCoreApplication.translate("MainWindow", u"Tren de lagunas", None))
        self.GeneralidadesLabel_235.setText(QCoreApplication.translate("MainWindow", u"Humedales construidos", None))
        self.GeneralidadesLabel_252.setText(QCoreApplication.translate("MainWindow", u"Tecnolog\u00edas", None))
        self.GeneralidadesLabel_229.setText(QCoreApplication.translate("MainWindow", u"Tratamiento primario", None))
        self.GeneralidadesLabel_230.setText(QCoreApplication.translate("MainWindow", u"Proceso convencional de lodos activados", None))
        self.GeneralidadesLabel_232.setText(QCoreApplication.translate("MainWindow", u"Reactor batch en secuencia", None))
        self.GeneralidadesLabel_234.setText(QCoreApplication.translate("MainWindow", u"Filtros percoladores", None))
        self.GeneralidadesLabel_236.setText(QCoreApplication.translate("MainWindow", u"Reactor anaerobio de flujo ascendente", None))
        self.GeneralidadesLabel_237.setText(QCoreApplication.translate("MainWindow", u"Tratamiento primario qu\u00edmicamente asistido", None))
        self.GeneralidadesLabel_233.setText(QCoreApplication.translate("MainWindow", u"Reactor biol\u00f3gico de biodiscos", None))
        self.GeneralidadesLabel_238.setText(QCoreApplication.translate("MainWindow", u"Reactor biol\u00f3gico de membrana", None))
        self.PrimLabelConvencional_14.setText(QCoreApplication.translate("MainWindow", u"Criterios y tecnolog\u00edas", None))
        self.tabManning.setTabText(self.tabManning.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Criterios", None))
        self.GeneralidadesLabel_44.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_45.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_46.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_48.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_49.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_50.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_51.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_53.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_54.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_56.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_57.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_59.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_60.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_61.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_62.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_64.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_65.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_66.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_67.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_69.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_70.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_72.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_73.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_74.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_75.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_95.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_96.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_98.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_100.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_101.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.GeneralidadesLabel_102.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Universidad de los Andes - 2022", None))
    # retranslateUi

