# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainzxPwtH.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QScrollArea, QScrollBar,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1226, 813)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
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
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
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

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

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

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


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
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
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
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/LogoHome.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 2, 0, 1, 2)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.menu_principal = QWidget()
        self.menu_principal.setObjectName(u"menu_principal")
        self.verticalLayout_20 = QVBoxLayout(self.menu_principal)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame = QFrame(self.menu_principal)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(324, 18, 201, 259))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.imagenFormas_2 = QFrame(self.horizontalLayoutWidget)
        self.imagenFormas_2.setObjectName(u"imagenFormas_2")
        self.imagenFormas_2.setStyleSheet(u"border-image: url(:/menu/images/images/Geometria.png);")
        self.imagenFormas_2.setFrameShape(QFrame.StyledPanel)
        self.imagenFormas_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.imagenFormas_2)

        self.conservacion_de_energia = QPlainTextEdit(self.frame)
        self.conservacion_de_energia.setObjectName(u"conservacion_de_energia")
        self.conservacion_de_energia.setGeometry(QRect(323, 21, 200, 256))
        self.conservacion_de_energia.setMinimumSize(QSize(200, 200))
        font5 = QFont()
        font5.setPointSize(18)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setKerning(True)
        self.conservacion_de_energia.setFont(font5)
        self.conservacion_de_energia.setLayoutDirection(Qt.LeftToRight)
        self.conservacion_de_energia.setAutoFillBackground(False)
        self.conservacion_de_energia.setStyleSheet(u"background-color: rgb(250, 110, 90);\n"
"font: 500 18pt \"Allerta\";\n"
"")
        self.conservacion_de_energia.setReadOnly(False)
        self.conservacion_de_energia.setTabStopDistance(96.000000000000000)
        self.geometria = QPlainTextEdit(self.frame)
        self.geometria.setObjectName(u"geometria")
        self.geometria.setGeometry(QRect(61, 21, 200, 256))
        self.geometria.setMinimumSize(QSize(200, 200))
        self.geometria.setFont(font5)
        self.geometria.setLayoutDirection(Qt.LeftToRight)
        self.geometria.setAutoFillBackground(False)
        self.geometria.setStyleSheet(u"background-color: rgb(128, 138, 255);\n"
"font: 500 18pt \"Allerta\";\n"
"")
        self.geometria.setReadOnly(False)
        self.geometria.setTabStopDistance(96.000000000000000)
        self.resalto_hidraulico = QPlainTextEdit(self.frame)
        self.resalto_hidraulico.setObjectName(u"resalto_hidraulico")
        self.resalto_hidraulico.setGeometry(QRect(585, 21, 200, 256))
        self.resalto_hidraulico.setMinimumSize(QSize(200, 200))
        self.resalto_hidraulico.setFont(font5)
        self.resalto_hidraulico.setLayoutDirection(Qt.LeftToRight)
        self.resalto_hidraulico.setAutoFillBackground(False)
        self.resalto_hidraulico.setStyleSheet(u"font: 500 18pt \"Allerta\";\n"
"background-color: rgb(244, 161, 124);\n"
"")
        self.resalto_hidraulico.setReadOnly(False)
        self.resalto_hidraulico.setTabStopDistance(96.000000000000000)
        self.comprobacion_diseno = QPlainTextEdit(self.frame)
        self.comprobacion_diseno.setObjectName(u"comprobacion_diseno")
        self.comprobacion_diseno.setGeometry(QRect(847, 21, 200, 256))
        self.comprobacion_diseno.setMinimumSize(QSize(200, 200))
        self.comprobacion_diseno.setFont(font5)
        self.comprobacion_diseno.setLayoutDirection(Qt.LeftToRight)
        self.comprobacion_diseno.setAutoFillBackground(False)
        self.comprobacion_diseno.setStyleSheet(u"font: 500 18pt \"Allerta\";\n"
"background-color: rgb(255, 207, 134);\n"
"")
        self.comprobacion_diseno.setReadOnly(False)
        self.comprobacion_diseno.setTabStopDistance(96.000000000000000)
        self.FRV = QPlainTextEdit(self.frame)
        self.FRV.setObjectName(u"FRV")
        self.FRV.setGeometry(QRect(846, 310, 200, 256))
        self.FRV.setMinimumSize(QSize(200, 200))
        self.FRV.setFont(font5)
        self.FRV.setLayoutDirection(Qt.LeftToRight)
        self.FRV.setAutoFillBackground(False)
        self.FRV.setStyleSheet(u"background-color: rgb(217, 165, 181);\n"
"font: 500 18pt \"Allerta\";\n"
"")
        self.FRV.setReadOnly(False)
        self.FRV.setTabStopDistance(96.000000000000000)
        self.manning = QPlainTextEdit(self.frame)
        self.manning.setObjectName(u"manning")
        self.manning.setGeometry(QRect(322, 310, 200, 256))
        self.manning.setMinimumSize(QSize(200, 200))
        self.manning.setFont(font5)
        self.manning.setLayoutDirection(Qt.LeftToRight)
        self.manning.setAutoFillBackground(False)
        self.manning.setStyleSheet(u"font: 500 18pt \"Allerta\";\n"
"background-color: rgb(105, 183, 255);")
        self.manning.setReadOnly(False)
        self.manning.setTabStopDistance(96.000000000000000)
        self.diseno = QPlainTextEdit(self.frame)
        self.diseno.setObjectName(u"diseno")
        self.diseno.setGeometry(QRect(60, 310, 200, 256))
        self.diseno.setMinimumSize(QSize(200, 200))
        self.diseno.setFont(font5)
        self.diseno.setLayoutDirection(Qt.LeftToRight)
        self.diseno.setAutoFillBackground(False)
        self.diseno.setStyleSheet(u"background-color: rgb(118, 199, 158);\n"
"font: 500 18pt \"Allerta\";\n"
"")
        self.diseno.setReadOnly(False)
        self.diseno.setTabStopDistance(96.000000000000000)
        self.FGV = QPlainTextEdit(self.frame)
        self.FGV.setObjectName(u"FGV")
        self.FGV.setGeometry(QRect(584, 310, 200, 256))
        self.FGV.setMinimumSize(QSize(200, 200))
        self.FGV.setFont(font5)
        self.FGV.setLayoutDirection(Qt.LeftToRight)
        self.FGV.setAutoFillBackground(False)
        self.FGV.setStyleSheet(u"background-color: rgb(117, 131, 202);\n"
"font: 500 18pt \"Allerta\";\n"
"")
        self.FGV.setReadOnly(False)
        self.FGV.setTabStopDistance(96.000000000000000)
        self.imagenFormas_3 = QFrame(self.frame)
        self.imagenFormas_3.setObjectName(u"imagenFormas_3")
        self.imagenFormas_3.setGeometry(QRect(846, 312, 196, 253))
        self.imagenFormas_3.setStyleSheet(u"border-image: url(:/menu/images/images/Geometria.png);")
        self.imagenFormas_3.setFrameShape(QFrame.StyledPanel)
        self.imagenFormas_3.setFrameShadow(QFrame.Raised)
        self.imagenFormas_4 = QFrame(self.frame)
        self.imagenFormas_4.setObjectName(u"imagenFormas_4")
        self.imagenFormas_4.setGeometry(QRect(850, 20, 196, 259))
        self.imagenFormas_4.setStyleSheet(u"border-image: url(:/menu/images/images/Geometria.png);")
        self.imagenFormas_4.setFrameShape(QFrame.StyledPanel)
        self.imagenFormas_4.setFrameShadow(QFrame.Raised)
        self.imagenFormas_5 = QFrame(self.frame)
        self.imagenFormas_5.setObjectName(u"imagenFormas_5")
        self.imagenFormas_5.setGeometry(QRect(585, 20, 199, 253))
        self.imagenFormas_5.setStyleSheet(u"border-image: url(:/menu/images/images/Geometria.png);")
        self.imagenFormas_5.setFrameShape(QFrame.StyledPanel)
        self.imagenFormas_5.setFrameShadow(QFrame.Raised)
        self.imagenFormas_6 = QFrame(self.frame)
        self.imagenFormas_6.setObjectName(u"imagenFormas_6")
        self.imagenFormas_6.setGeometry(QRect(65, 310, 191, 253))
        self.imagenFormas_6.setStyleSheet(u"border-image: url(:/menu/images/images/Geometria.png);")
        self.imagenFormas_6.setFrameShape(QFrame.StyledPanel)
        self.imagenFormas_6.setFrameShadow(QFrame.Raised)
        self.imagenFormas_7 = QFrame(self.frame)
        self.imagenFormas_7.setObjectName(u"imagenFormas_7")
        self.imagenFormas_7.setGeometry(QRect(325, 310, 191, 253))
        self.imagenFormas_7.setStyleSheet(u"border-image: url(:/menu/images/images/Geometria.png);")
        self.imagenFormas_7.setFrameShape(QFrame.StyledPanel)
        self.imagenFormas_7.setFrameShadow(QFrame.Raised)
        self.imagenFormas_8 = QFrame(self.frame)
        self.imagenFormas_8.setObjectName(u"imagenFormas_8")
        self.imagenFormas_8.setGeometry(QRect(590, 310, 191, 253))
        self.imagenFormas_8.setStyleSheet(u"border-image: url(:/menu/images/images/Geometria.png);")
        self.imagenFormas_8.setFrameShape(QFrame.StyledPanel)
        self.imagenFormas_8.setFrameShadow(QFrame.Raised)
        self.imagenFormas = QFrame(self.frame)
        self.imagenFormas.setObjectName(u"imagenFormas")
        self.imagenFormas.setGeometry(QRect(72, 18, 181, 259))
        self.imagenFormas.setStyleSheet(u"border-image: url(:/menu/images/images/Geometria.png);")
        self.imagenFormas.setFrameShape(QFrame.StyledPanel)
        self.imagenFormas.setFrameShadow(QFrame.Raised)
        self.botonMenuGeometria = QPushButton(self.frame)
        self.botonMenuGeometria.setObjectName(u"botonMenuGeometria")
        self.botonMenuGeometria.setGeometry(QRect(66, 240, 187, 35))
        self.botonMenuGeometria.setStyleSheet(u"font: 500 18pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(128, 138, 255);")
        self.botonMenuConservacionE = QPushButton(self.frame)
        self.botonMenuConservacionE.setObjectName(u"botonMenuConservacionE")
        self.botonMenuConservacionE.setGeometry(QRect(324, 216, 199, 61))
        self.botonMenuConservacionE.setStyleSheet(u"font: 500 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(250, 110, 90);")
        self.botonMenuConservacionM = QPushButton(self.frame)
        self.botonMenuConservacionM.setObjectName(u"botonMenuConservacionM")
        self.botonMenuConservacionM.setGeometry(QRect(588, 216, 193, 61))
        self.botonMenuConservacionM.setStyleSheet(u"font: 500 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(244, 161, 124);")
        self.botonMenuComprobacion = QPushButton(self.frame)
        self.botonMenuComprobacion.setObjectName(u"botonMenuComprobacion")
        self.botonMenuComprobacion.setGeometry(QRect(852, 216, 193, 61))
        self.botonMenuComprobacion.setStyleSheet(u"font: 500 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 207, 134);")
        self.botonMenuDiseno = QPushButton(self.frame)
        self.botonMenuDiseno.setObjectName(u"botonMenuDiseno")
        self.botonMenuDiseno.setGeometry(QRect(60, 528, 199, 35))
        self.botonMenuDiseno.setStyleSheet(u"font: 500 18pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(118, 199, 158);")
        self.botonMenuManning = QPushButton(self.frame)
        self.botonMenuManning.setObjectName(u"botonMenuManning")
        self.botonMenuManning.setGeometry(QRect(324, 504, 193, 61))
        self.botonMenuManning.setStyleSheet(u"font: 500 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(105, 183, 255);")
        self.botonMenuFGV = QPushButton(self.frame)
        self.botonMenuFGV.setObjectName(u"botonMenuFGV")
        self.botonMenuFGV.setGeometry(QRect(588, 464, 193, 101))
        self.botonMenuFGV.setStyleSheet(u"font: 500 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(117, 131, 202);")
        self.botonMenuManningFRV = QPushButton(self.frame)
        self.botonMenuManningFRV.setObjectName(u"botonMenuManningFRV")
        self.botonMenuManningFRV.setGeometry(QRect(846, 468, 199, 97))
        self.botonMenuManningFRV.setStyleSheet(u"font: 500 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(217, 165, 181);")
        self.resalto_hidraulico.raise_()
        self.geometria.raise_()
        self.FGV.raise_()
        self.FRV.raise_()
        self.conservacion_de_energia.raise_()
        self.comprobacion_diseno.raise_()
        self.diseno.raise_()
        self.manning.raise_()
        self.horizontalLayoutWidget.raise_()
        self.imagenFormas_3.raise_()
        self.imagenFormas_4.raise_()
        self.imagenFormas_5.raise_()
        self.imagenFormas_6.raise_()
        self.imagenFormas_7.raise_()
        self.imagenFormas_8.raise_()
        self.imagenFormas.raise_()
        self.botonMenuGeometria.raise_()
        self.botonMenuConservacionE.raise_()
        self.botonMenuConservacionM.raise_()
        self.botonMenuComprobacion.raise_()
        self.botonMenuDiseno.raise_()
        self.botonMenuManning.raise_()
        self.botonMenuFGV.raise_()
        self.botonMenuManningFRV.raise_()

        self.verticalLayout_20.addWidget(self.frame)

        self.stackedWidget.addWidget(self.menu_principal)
        self.pagina_geometria = QWidget()
        self.pagina_geometria.setObjectName(u"pagina_geometria")
        self.pagina_geometria.setStyleSheet(u"")
        self.tabGeometria = QTabWidget(self.pagina_geometria)
        self.tabGeometria.setObjectName(u"tabGeometria")
        self.tabGeometria.setGeometry(QRect(0, 0, 1117, 610))
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tabGeometria.sizePolicy().hasHeightForWidth())
        self.tabGeometria.setSizePolicy(sizePolicy5)
        self.tabGeometria.setStyleSheet(u"font: 500 10pt \"Allerta\";\n"
"color: rgb(79, 79, 79);")
        self.tabGeometria.setTabPosition(QTabWidget.West)
        self.geometriaCircular = QWidget()
        self.geometriaCircular.setObjectName(u"geometriaCircular")
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setItalic(False)
        self.geometriaCircular.setFont(font6)
        self.geometriaCircular.setStyleSheet(u"border-color: rgb(60, 60, 75);\n"
"background-color: rgb(65, 65, 97);\n"
"font: 500 11pt \"Allerta\";")
        self.gridLayout_11 = QGridLayout(self.geometriaCircular)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.groupBox_Propiedades = QGroupBox(self.geometriaCircular)
        self.groupBox_Propiedades.setObjectName(u"groupBox_Propiedades")
        sizePolicy5.setHeightForWidth(self.groupBox_Propiedades.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades.setSizePolicy(sizePolicy5)
        self.groupBox_Propiedades.setMinimumSize(QSize(870, 0))
        self.groupBox_Propiedades.setStyleSheet(u"QGroupBox {\n"
"color: rgb(203, 208, 253);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(203, 208, 253);\n"
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
        self.gridLayout_4 = QGridLayout(self.groupBox_Propiedades)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, -1)
        self.geoCTextoCalcular = QLabel(self.groupBox_Propiedades)
        self.geoCTextoCalcular.setObjectName(u"geoCTextoCalcular")
        sizePolicy5.setHeightForWidth(self.geoCTextoCalcular.sizePolicy().hasHeightForWidth())
        self.geoCTextoCalcular.setSizePolicy(sizePolicy5)
        self.geoCTextoCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"\n"
"color: rgb(231, 230, 242);")
        self.geoCTextoCalcular.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.geoCTextoCalcular)

        self.geoCTextoReiniciar = QLabel(self.groupBox_Propiedades)
        self.geoCTextoReiniciar.setObjectName(u"geoCTextoReiniciar")
        sizePolicy5.setHeightForWidth(self.geoCTextoReiniciar.sizePolicy().hasHeightForWidth())
        self.geoCTextoReiniciar.setSizePolicy(sizePolicy5)
        self.geoCTextoReiniciar.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(231, 226, 242);")
        self.geoCTextoReiniciar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.geoCTextoReiniciar)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 4, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, -1)
        self.geoCBotonCalcular = QPushButton(self.groupBox_Propiedades)
        self.geoCBotonCalcular.setObjectName(u"geoCBotonCalcular")
        self.geoCBotonCalcular.setMinimumSize(QSize(50, 50))
        self.geoCBotonCalcular.setMaximumSize(QSize(50, 50))
        self.geoCBotonCalcular.setStyleSheet(u"background-color: rgb(142, 151, 253);\n"
"border-color: rgb(142, 151, 253);\n"
"border-width: 2px;\n"
"border-radius: 20px;")

        self.horizontalLayout_7.addWidget(self.geoCBotonCalcular)

        self.geoCBotonReiniciar = QPushButton(self.groupBox_Propiedades)
        self.geoCBotonReiniciar.setObjectName(u"geoCBotonReiniciar")
        self.geoCBotonReiniciar.setMinimumSize(QSize(50, 50))
        self.geoCBotonReiniciar.setMaximumSize(QSize(50, 50))
        self.geoCBotonReiniciar.setStyleSheet(u"background-color: rgb(142, 151, 253);\n"
"border-color: rgb(142, 151, 253);\n"
"border-image: url(:/geometria/images/geometria/reboot.png);\n"
"border-width: 2px;\n"
"border-radius: 20px;")

        self.horizontalLayout_7.addWidget(self.geoCBotonReiniciar)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 1, 0, 2, 1)

        self.row_4 = QFrame(self.groupBox_Propiedades)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setStyleSheet(u"")
        self.row_4.setFrameShape(QFrame.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.row_4)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_5.setHorizontalSpacing(40)
        self.gridLayout_5.setVerticalSpacing(20)
        self.gridLayout_5.setContentsMargins(0, 10, 0, 10)
        self.geoCComboBoxDiametro = QComboBox(self.row_4)
        self.geoCComboBoxDiametro.addItem("")
        self.geoCComboBoxDiametro.addItem("")
        self.geoCComboBoxDiametro.addItem("")
        self.geoCComboBoxDiametro.addItem("")
        self.geoCComboBoxDiametro.setObjectName(u"geoCComboBoxDiametro")
        sizePolicy5.setHeightForWidth(self.geoCComboBoxDiametro.sizePolicy().hasHeightForWidth())
        self.geoCComboBoxDiametro.setSizePolicy(sizePolicy5)
        self.geoCComboBoxDiametro.setMinimumSize(QSize(150, 30))
        self.geoCComboBoxDiametro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoCComboBoxDiametro.setEditable(True)

        self.gridLayout_5.addWidget(self.geoCComboBoxDiametro, 0, 2, 1, 1)

        self.geoLabelRelacionLlenado = QLabel(self.row_4)
        self.geoLabelRelacionLlenado.setObjectName(u"geoLabelRelacionLlenado")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.geoLabelRelacionLlenado.sizePolicy().hasHeightForWidth())
        self.geoLabelRelacionLlenado.setSizePolicy(sizePolicy6)
        self.geoLabelRelacionLlenado.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoLabelRelacionLlenado.setLineWidth(1)
        self.geoLabelRelacionLlenado.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.geoLabelRelacionLlenado, 1, 0, 1, 1)

        self.geoCFieldDiametro = QLineEdit(self.row_4)
        self.geoCFieldDiametro.setObjectName(u"geoCFieldDiametro")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.geoCFieldDiametro.sizePolicy().hasHeightForWidth())
        self.geoCFieldDiametro.setSizePolicy(sizePolicy7)
        self.geoCFieldDiametro.setMinimumSize(QSize(150, 30))
        self.geoCFieldDiametro.setMaximumSize(QSize(16777215, 30))
        self.geoCFieldDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")
        self.geoCFieldDiametro.setInputMethodHints(Qt.ImhNone)
        self.geoCFieldDiametro.setFrame(True)
        self.geoCFieldDiametro.setEchoMode(QLineEdit.Normal)
        self.geoCFieldDiametro.setPlaceholderText(u"")
        self.geoCFieldDiametro.setClearButtonEnabled(False)

        self.gridLayout_5.addWidget(self.geoCFieldDiametro, 0, 1, 1, 1)

        self.geoLabelDiametro = QLabel(self.row_4)
        self.geoLabelDiametro.setObjectName(u"geoLabelDiametro")
        sizePolicy6.setHeightForWidth(self.geoLabelDiametro.sizePolicy().hasHeightForWidth())
        self.geoLabelDiametro.setSizePolicy(sizePolicy6)
        self.geoLabelDiametro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoLabelDiametro.setLineWidth(1)
        self.geoLabelDiametro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.geoLabelDiametro, 0, 0, 1, 1)

        self.geoCFieldRelacionLlenado = QLineEdit(self.row_4)
        self.geoCFieldRelacionLlenado.setObjectName(u"geoCFieldRelacionLlenado")
        sizePolicy5.setHeightForWidth(self.geoCFieldRelacionLlenado.sizePolicy().hasHeightForWidth())
        self.geoCFieldRelacionLlenado.setSizePolicy(sizePolicy5)
        self.geoCFieldRelacionLlenado.setMinimumSize(QSize(150, 30))
        self.geoCFieldRelacionLlenado.setMaximumSize(QSize(16777215, 30))
        self.geoCFieldRelacionLlenado.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.geoCFieldRelacionLlenado, 1, 1, 1, 1)

        self.geoCComboBoxRelacionLlenado = QComboBox(self.row_4)
        self.geoCComboBoxRelacionLlenado.addItem("")
        self.geoCComboBoxRelacionLlenado.setObjectName(u"geoCComboBoxRelacionLlenado")
        sizePolicy5.setHeightForWidth(self.geoCComboBoxRelacionLlenado.sizePolicy().hasHeightForWidth())
        self.geoCComboBoxRelacionLlenado.setSizePolicy(sizePolicy5)
        self.geoCComboBoxRelacionLlenado.setMinimumSize(QSize(150, 30))
        self.geoCComboBoxRelacionLlenado.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoCComboBoxRelacionLlenado.setEditable(True)

        self.gridLayout_5.addWidget(self.geoCComboBoxRelacionLlenado, 1, 2, 1, 1)


        self.verticalLayout_23.addLayout(self.gridLayout_5)


        self.gridLayout_4.addWidget(self.row_4, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_Propiedades, 0, 1, 1, 1)

        self.groupBox_Resultados = QGroupBox(self.geometriaCircular)
        self.groupBox_Resultados.setObjectName(u"groupBox_Resultados")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.groupBox_Resultados.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados.setSizePolicy(sizePolicy8)
        self.groupBox_Resultados.setStyleSheet(u"QGroupBox {\n"
"color: rgb(203, 208, 253);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(203, 208, 253);\n"
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
        self.gridLayout_6 = QGridLayout(self.groupBox_Resultados)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.row_5 = QFrame(self.groupBox_Resultados)
        self.row_5.setObjectName(u"row_5")
        self.row_5.setStyleSheet(u"")
        self.row_5.setFrameShape(QFrame.StyledPanel)
        self.row_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.row_5)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_7.setHorizontalSpacing(25)
        self.gridLayout_7.setVerticalSpacing(15)
        self.gridLayout_7.setContentsMargins(15, 20, 15, 20)
        self.geoCLabelAngulo = QLabel(self.row_5)
        self.geoCLabelAngulo.setObjectName(u"geoCLabelAngulo")
        sizePolicy6.setHeightForWidth(self.geoCLabelAngulo.sizePolicy().hasHeightForWidth())
        self.geoCLabelAngulo.setSizePolicy(sizePolicy6)
        self.geoCLabelAngulo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoCLabelAngulo.setLineWidth(1)
        self.geoCLabelAngulo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.geoCLabelAngulo, 0, 0, 1, 1)

        self.geoCFieldRadio = QLineEdit(self.row_5)
        self.geoCFieldRadio.setObjectName(u"geoCFieldRadio")
        sizePolicy5.setHeightForWidth(self.geoCFieldRadio.sizePolicy().hasHeightForWidth())
        self.geoCFieldRadio.setSizePolicy(sizePolicy5)
        self.geoCFieldRadio.setMinimumSize(QSize(0, 30))
        self.geoCFieldRadio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_7.addWidget(self.geoCFieldRadio, 4, 1, 1, 1)

        self.geoCFieldArea = QLineEdit(self.row_5)
        self.geoCFieldArea.setObjectName(u"geoCFieldArea")
        sizePolicy5.setHeightForWidth(self.geoCFieldArea.sizePolicy().hasHeightForWidth())
        self.geoCFieldArea.setSizePolicy(sizePolicy5)
        self.geoCFieldArea.setMinimumSize(QSize(0, 30))
        self.geoCFieldArea.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.geoCFieldArea, 2, 1, 1, 1)

        self.geoCLabelAnchoSuperficial = QLabel(self.row_5)
        self.geoCLabelAnchoSuperficial.setObjectName(u"geoCLabelAnchoSuperficial")
        sizePolicy6.setHeightForWidth(self.geoCLabelAnchoSuperficial.sizePolicy().hasHeightForWidth())
        self.geoCLabelAnchoSuperficial.setSizePolicy(sizePolicy6)
        self.geoCLabelAnchoSuperficial.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoCLabelAnchoSuperficial.setLineWidth(1)
        self.geoCLabelAnchoSuperficial.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.geoCLabelAnchoSuperficial, 5, 0, 1, 1)

        self.geoCLabelProfundidadHidraulica = QLabel(self.row_5)
        self.geoCLabelProfundidadHidraulica.setObjectName(u"geoCLabelProfundidadHidraulica")
        sizePolicy6.setHeightForWidth(self.geoCLabelProfundidadHidraulica.sizePolicy().hasHeightForWidth())
        self.geoCLabelProfundidadHidraulica.setSizePolicy(sizePolicy6)
        self.geoCLabelProfundidadHidraulica.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoCLabelProfundidadHidraulica.setLineWidth(1)
        self.geoCLabelProfundidadHidraulica.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.geoCLabelProfundidadHidraulica, 6, 0, 1, 1)

        self.geoCLabelPerimetro = QLabel(self.row_5)
        self.geoCLabelPerimetro.setObjectName(u"geoCLabelPerimetro")
        sizePolicy6.setHeightForWidth(self.geoCLabelPerimetro.sizePolicy().hasHeightForWidth())
        self.geoCLabelPerimetro.setSizePolicy(sizePolicy6)
        self.geoCLabelPerimetro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoCLabelPerimetro.setLineWidth(1)
        self.geoCLabelPerimetro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.geoCLabelPerimetro, 3, 0, 1, 1)

        self.geoCLabelArea = QLabel(self.row_5)
        self.geoCLabelArea.setObjectName(u"geoCLabelArea")
        sizePolicy6.setHeightForWidth(self.geoCLabelArea.sizePolicy().hasHeightForWidth())
        self.geoCLabelArea.setSizePolicy(sizePolicy6)
        self.geoCLabelArea.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoCLabelArea.setLineWidth(1)
        self.geoCLabelArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.geoCLabelArea, 2, 0, 1, 1)

        self.geoCFieldAnchoSuperficial = QLineEdit(self.row_5)
        self.geoCFieldAnchoSuperficial.setObjectName(u"geoCFieldAnchoSuperficial")
        sizePolicy5.setHeightForWidth(self.geoCFieldAnchoSuperficial.sizePolicy().hasHeightForWidth())
        self.geoCFieldAnchoSuperficial.setSizePolicy(sizePolicy5)
        self.geoCFieldAnchoSuperficial.setMinimumSize(QSize(0, 30))
        self.geoCFieldAnchoSuperficial.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.geoCFieldAnchoSuperficial, 5, 1, 1, 1)

        self.geoCLabelRadio = QLabel(self.row_5)
        self.geoCLabelRadio.setObjectName(u"geoCLabelRadio")
        sizePolicy6.setHeightForWidth(self.geoCLabelRadio.sizePolicy().hasHeightForWidth())
        self.geoCLabelRadio.setSizePolicy(sizePolicy6)
        self.geoCLabelRadio.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoCLabelRadio.setLineWidth(1)
        self.geoCLabelRadio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.geoCLabelRadio, 4, 0, 1, 1)

        self.geoCFieldPerimetro = QLineEdit(self.row_5)
        self.geoCFieldPerimetro.setObjectName(u"geoCFieldPerimetro")
        sizePolicy5.setHeightForWidth(self.geoCFieldPerimetro.sizePolicy().hasHeightForWidth())
        self.geoCFieldPerimetro.setSizePolicy(sizePolicy5)
        self.geoCFieldPerimetro.setMinimumSize(QSize(0, 30))
        self.geoCFieldPerimetro.setMaximumSize(QSize(16777215, 30))
        self.geoCFieldPerimetro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.geoCFieldPerimetro, 3, 1, 1, 1)

        self.geoCFieldProfundidadHidraulica = QLineEdit(self.row_5)
        self.geoCFieldProfundidadHidraulica.setObjectName(u"geoCFieldProfundidadHidraulica")
        sizePolicy5.setHeightForWidth(self.geoCFieldProfundidadHidraulica.sizePolicy().hasHeightForWidth())
        self.geoCFieldProfundidadHidraulica.setSizePolicy(sizePolicy5)
        self.geoCFieldProfundidadHidraulica.setMinimumSize(QSize(0, 30))
        self.geoCFieldProfundidadHidraulica.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.geoCFieldProfundidadHidraulica, 6, 1, 1, 1)

        self.geoCLabelProfundidadNormal = QLabel(self.row_5)
        self.geoCLabelProfundidadNormal.setObjectName(u"geoCLabelProfundidadNormal")
        sizePolicy6.setHeightForWidth(self.geoCLabelProfundidadNormal.sizePolicy().hasHeightForWidth())
        self.geoCLabelProfundidadNormal.setSizePolicy(sizePolicy6)
        self.geoCLabelProfundidadNormal.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoCLabelProfundidadNormal.setLineWidth(1)
        self.geoCLabelProfundidadNormal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.geoCLabelProfundidadNormal, 1, 0, 1, 1)

        self.geoCFieldAngulo = QLineEdit(self.row_5)
        self.geoCFieldAngulo.setObjectName(u"geoCFieldAngulo")
        sizePolicy5.setHeightForWidth(self.geoCFieldAngulo.sizePolicy().hasHeightForWidth())
        self.geoCFieldAngulo.setSizePolicy(sizePolicy5)
        self.geoCFieldAngulo.setMinimumSize(QSize(0, 30))
        self.geoCFieldAngulo.setMaximumSize(QSize(16777215, 30))
        self.geoCFieldAngulo.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.geoCFieldAngulo, 0, 1, 1, 1)

        self.geoCFieldProfundidadNormal = QLineEdit(self.row_5)
        self.geoCFieldProfundidadNormal.setObjectName(u"geoCFieldProfundidadNormal")
        sizePolicy5.setHeightForWidth(self.geoCFieldProfundidadNormal.sizePolicy().hasHeightForWidth())
        self.geoCFieldProfundidadNormal.setSizePolicy(sizePolicy5)
        self.geoCFieldProfundidadNormal.setMinimumSize(QSize(0, 30))
        self.geoCFieldProfundidadNormal.setMaximumSize(QSize(16777215, 30))
        self.geoCFieldProfundidadNormal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.geoCFieldProfundidadNormal, 1, 1, 1, 1)


        self.verticalLayout_24.addLayout(self.gridLayout_7)


        self.gridLayout_6.addWidget(self.row_5, 0, 0, 1, 1)

        self.geoCImagenCanal = QPushButton(self.groupBox_Resultados)
        self.geoCImagenCanal.setObjectName(u"geoCImagenCanal")
        self.geoCImagenCanal.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.geoCImagenCanal.sizePolicy().hasHeightForWidth())
        self.geoCImagenCanal.setSizePolicy(sizePolicy5)
        self.geoCImagenCanal.setMinimumSize(QSize(260, 213))
        self.geoCImagenCanal.setStyleSheet(u"border-image: url(:/geometria/images/geometria/Geometria-rectangular.PNG);\n"
"background-color: rgb(255,255,255);")
        self.geoCImagenCanal.setFlat(True)

        self.gridLayout_6.addWidget(self.geoCImagenCanal, 0, 1, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_Resultados, 1, 0, 1, 3)

        self.groupBox_Canal = QGroupBox(self.geometriaCircular)
        self.groupBox_Canal.setObjectName(u"groupBox_Canal")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(10)
        sizePolicy9.setVerticalStretch(10)
        sizePolicy9.setHeightForWidth(self.groupBox_Canal.sizePolicy().hasHeightForWidth())
        self.groupBox_Canal.setSizePolicy(sizePolicy9)
        self.groupBox_Canal.setStyleSheet(u"QGroupBox {\n"
"color: rgb(203, 208, 253);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(203, 208, 253);\n"
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
        self.gridLayout_3 = QGridLayout(self.groupBox_Canal)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.geoBotonCircular = QPushButton(self.groupBox_Canal)
        self.geoBotonCircular.setObjectName(u"geoBotonCircular")
        self.geoBotonCircular.setEnabled(False)
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.geoBotonCircular.sizePolicy().hasHeightForWidth())
        self.geoBotonCircular.setSizePolicy(sizePolicy10)
        self.geoBotonCircular.setMinimumSize(QSize(150, 100))
        self.geoBotonCircular.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-image: url(:/geometria/images/geometria/Circulo.png);")
        self.geoBotonCircular.setCheckable(True)
        self.geoBotonCircular.setChecked(False)
        self.geoBotonCircular.setFlat(False)

        self.gridLayout_3.addWidget(self.geoBotonCircular, 2, 1, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_Canal, 0, 0, 1, 1)

        self.tabGeometria.addTab(self.geometriaCircular, "")
        self.geometriaNoCircular = QWidget()
        self.geometriaNoCircular.setObjectName(u"geometriaNoCircular")
        self.geometriaNoCircular.setStyleSheet(u"border-color: rgb(60, 60, 75);\n"
"background-color: rgb(65, 65, 97);\n"
"font: 500 11pt \"Allerta\";")
        self.groupBox_Propiedades_3 = QGroupBox(self.geometriaNoCircular)
        self.groupBox_Propiedades_3.setObjectName(u"groupBox_Propiedades_3")
        self.groupBox_Propiedades_3.setGeometry(QRect(210, 6, 870, 315))
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.groupBox_Propiedades_3.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_3.setSizePolicy(sizePolicy11)
        self.groupBox_Propiedades_3.setMinimumSize(QSize(860, 0))
        self.groupBox_Propiedades_3.setStyleSheet(u"QGroupBox {\n"
"color: rgb(203, 208, 253);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(203, 208, 253);\n"
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
        self.gridLayout_15 = QGridLayout(self.groupBox_Propiedades_3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.row_8 = QFrame(self.groupBox_Propiedades_3)
        self.row_8.setObjectName(u"row_8")
        self.row_8.setStyleSheet(u"")
        self.row_8.setFrameShape(QFrame.StyledPanel)
        self.row_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.row_8)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_16.setHorizontalSpacing(40)
        self.gridLayout_16.setVerticalSpacing(15)
        self.gridLayout_16.setContentsMargins(0, 10, 0, 10)
        self.geoCFieldAncho = QLineEdit(self.row_8)
        self.geoCFieldAncho.setObjectName(u"geoCFieldAncho")
        sizePolicy5.setHeightForWidth(self.geoCFieldAncho.sizePolicy().hasHeightForWidth())
        self.geoCFieldAncho.setSizePolicy(sizePolicy5)
        self.geoCFieldAncho.setMinimumSize(QSize(150, 30))
        self.geoCFieldAncho.setMaximumSize(QSize(16777215, 30))
        self.geoCFieldAncho.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_16.addWidget(self.geoCFieldAncho, 1, 1, 1, 1)

        self.geoRComboBoxPendienteLateral = QComboBox(self.row_8)
        self.geoRComboBoxPendienteLateral.addItem("")
        self.geoRComboBoxPendienteLateral.addItem("")
        self.geoRComboBoxPendienteLateral.addItem("")
        self.geoRComboBoxPendienteLateral.setObjectName(u"geoRComboBoxPendienteLateral")
        sizePolicy5.setHeightForWidth(self.geoRComboBoxPendienteLateral.sizePolicy().hasHeightForWidth())
        self.geoRComboBoxPendienteLateral.setSizePolicy(sizePolicy5)
        self.geoRComboBoxPendienteLateral.setMinimumSize(QSize(190, 30))
        self.geoRComboBoxPendienteLateral.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoRComboBoxPendienteLateral.setEditable(True)

        self.gridLayout_16.addWidget(self.geoRComboBoxPendienteLateral, 2, 2, 1, 1)

        self.geoRLabelAncho = QLabel(self.row_8)
        self.geoRLabelAncho.setObjectName(u"geoRLabelAncho")
        sizePolicy6.setHeightForWidth(self.geoRLabelAncho.sizePolicy().hasHeightForWidth())
        self.geoRLabelAncho.setSizePolicy(sizePolicy6)
        self.geoRLabelAncho.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoRLabelAncho.setLineWidth(1)
        self.geoRLabelAncho.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.geoRLabelAncho, 1, 0, 1, 1)

        self.geoRLabelPendienteLateral = QLabel(self.row_8)
        self.geoRLabelPendienteLateral.setObjectName(u"geoRLabelPendienteLateral")
        sizePolicy6.setHeightForWidth(self.geoRLabelPendienteLateral.sizePolicy().hasHeightForWidth())
        self.geoRLabelPendienteLateral.setSizePolicy(sizePolicy6)
        self.geoRLabelPendienteLateral.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoRLabelPendienteLateral.setLineWidth(1)
        self.geoRLabelPendienteLateral.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.geoRLabelPendienteLateral, 2, 0, 1, 1)

        self.geoCFieldPendienteLateral = QLineEdit(self.row_8)
        self.geoCFieldPendienteLateral.setObjectName(u"geoCFieldPendienteLateral")
        sizePolicy5.setHeightForWidth(self.geoCFieldPendienteLateral.sizePolicy().hasHeightForWidth())
        self.geoCFieldPendienteLateral.setSizePolicy(sizePolicy5)
        self.geoCFieldPendienteLateral.setMinimumSize(QSize(0, 30))
        self.geoCFieldPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_16.addWidget(self.geoCFieldPendienteLateral, 2, 1, 1, 1)

        self.geoCFieldProfundidadSeccion = QLineEdit(self.row_8)
        self.geoCFieldProfundidadSeccion.setObjectName(u"geoCFieldProfundidadSeccion")
        sizePolicy7.setHeightForWidth(self.geoCFieldProfundidadSeccion.sizePolicy().hasHeightForWidth())
        self.geoCFieldProfundidadSeccion.setSizePolicy(sizePolicy7)
        self.geoCFieldProfundidadSeccion.setMinimumSize(QSize(150, 30))
        self.geoCFieldProfundidadSeccion.setMaximumSize(QSize(16777215, 30))
        self.geoCFieldProfundidadSeccion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_16.addWidget(self.geoCFieldProfundidadSeccion, 0, 1, 1, 1)

        self.geoRComboBoxProfundidad = QComboBox(self.row_8)
        self.geoRComboBoxProfundidad.addItem("")
        self.geoRComboBoxProfundidad.addItem("")
        self.geoRComboBoxProfundidad.addItem("")
        self.geoRComboBoxProfundidad.addItem("")
        self.geoRComboBoxProfundidad.setObjectName(u"geoRComboBoxProfundidad")
        sizePolicy5.setHeightForWidth(self.geoRComboBoxProfundidad.sizePolicy().hasHeightForWidth())
        self.geoRComboBoxProfundidad.setSizePolicy(sizePolicy5)
        self.geoRComboBoxProfundidad.setMinimumSize(QSize(190, 30))
        self.geoRComboBoxProfundidad.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoRComboBoxProfundidad.setEditable(True)

        self.gridLayout_16.addWidget(self.geoRComboBoxProfundidad, 0, 2, 1, 1)

        self.geoRLabelProfundidadSeccion = QLabel(self.row_8)
        self.geoRLabelProfundidadSeccion.setObjectName(u"geoRLabelProfundidadSeccion")
        sizePolicy6.setHeightForWidth(self.geoRLabelProfundidadSeccion.sizePolicy().hasHeightForWidth())
        self.geoRLabelProfundidadSeccion.setSizePolicy(sizePolicy6)
        self.geoRLabelProfundidadSeccion.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoRLabelProfundidadSeccion.setLineWidth(1)
        self.geoRLabelProfundidadSeccion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.geoRLabelProfundidadSeccion, 0, 0, 1, 1)

        self.geoRComboBoxAncho = QComboBox(self.row_8)
        self.geoRComboBoxAncho.addItem("")
        self.geoRComboBoxAncho.addItem("")
        self.geoRComboBoxAncho.addItem("")
        self.geoRComboBoxAncho.addItem("")
        self.geoRComboBoxAncho.setObjectName(u"geoRComboBoxAncho")
        sizePolicy5.setHeightForWidth(self.geoRComboBoxAncho.sizePolicy().hasHeightForWidth())
        self.geoRComboBoxAncho.setSizePolicy(sizePolicy5)
        self.geoRComboBoxAncho.setMinimumSize(QSize(190, 30))
        self.geoRComboBoxAncho.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoRComboBoxAncho.setEditable(True)

        self.gridLayout_16.addWidget(self.geoRComboBoxAncho, 1, 2, 1, 1)

        self.geoRLabelPendienteLateral2 = QLabel(self.row_8)
        self.geoRLabelPendienteLateral2.setObjectName(u"geoRLabelPendienteLateral2")
        sizePolicy6.setHeightForWidth(self.geoRLabelPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.geoRLabelPendienteLateral2.setSizePolicy(sizePolicy6)
        self.geoRLabelPendienteLateral2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoRLabelPendienteLateral2.setLineWidth(1)
        self.geoRLabelPendienteLateral2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.geoRLabelPendienteLateral2, 3, 0, 1, 1)

        self.geoCFieldPendienteLateral2 = QLineEdit(self.row_8)
        self.geoCFieldPendienteLateral2.setObjectName(u"geoCFieldPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.geoCFieldPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.geoCFieldPendienteLateral2.setSizePolicy(sizePolicy5)
        self.geoCFieldPendienteLateral2.setMinimumSize(QSize(0, 30))
        self.geoCFieldPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_16.addWidget(self.geoCFieldPendienteLateral2, 3, 1, 1, 1)

        self.geoRComboBoxPendienteLateral2 = QComboBox(self.row_8)
        self.geoRComboBoxPendienteLateral2.addItem("")
        self.geoRComboBoxPendienteLateral2.addItem("")
        self.geoRComboBoxPendienteLateral2.addItem("")
        self.geoRComboBoxPendienteLateral2.setObjectName(u"geoRComboBoxPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.geoRComboBoxPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.geoRComboBoxPendienteLateral2.setSizePolicy(sizePolicy5)
        self.geoRComboBoxPendienteLateral2.setMinimumSize(QSize(190, 30))
        self.geoRComboBoxPendienteLateral2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoRComboBoxPendienteLateral2.setEditable(True)

        self.gridLayout_16.addWidget(self.geoRComboBoxPendienteLateral2, 3, 2, 1, 1)


        self.verticalLayout_27.addLayout(self.gridLayout_16)


        self.gridLayout_15.addWidget(self.row_8, 0, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_14.setContentsMargins(10, 0, 10, -1)
        self.geoRTextoCalcular = QLabel(self.groupBox_Propiedades_3)
        self.geoRTextoCalcular.setObjectName(u"geoRTextoCalcular")
        sizePolicy5.setHeightForWidth(self.geoRTextoCalcular.sizePolicy().hasHeightForWidth())
        self.geoRTextoCalcular.setSizePolicy(sizePolicy5)
        self.geoRTextoCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"\n"
"color: rgb(231, 230, 242);")
        self.geoRTextoCalcular.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.geoRTextoCalcular)

        self.geoRTextoReiniciar = QLabel(self.groupBox_Propiedades_3)
        self.geoRTextoReiniciar.setObjectName(u"geoRTextoReiniciar")
        sizePolicy5.setHeightForWidth(self.geoRTextoReiniciar.sizePolicy().hasHeightForWidth())
        self.geoRTextoReiniciar.setSizePolicy(sizePolicy5)
        self.geoRTextoReiniciar.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(231, 226, 242);")
        self.geoRTextoReiniciar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.geoRTextoReiniciar)


        self.gridLayout_15.addLayout(self.horizontalLayout_14, 4, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_5, 5, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_15.setContentsMargins(10, 0, 10, -1)
        self.geoRBotonCalcular = QPushButton(self.groupBox_Propiedades_3)
        self.geoRBotonCalcular.setObjectName(u"geoRBotonCalcular")
        self.geoRBotonCalcular.setMinimumSize(QSize(50, 50))
        self.geoRBotonCalcular.setMaximumSize(QSize(50, 50))
        self.geoRBotonCalcular.setStyleSheet(u"background-color: rgb(142, 151, 253);\n"
"border-color: rgb(142, 151, 253);\n"
"border-width: 2px;\n"
"border-radius: 20px;")

        self.horizontalLayout_15.addWidget(self.geoRBotonCalcular)

        self.geoRBotonReiniciar = QPushButton(self.groupBox_Propiedades_3)
        self.geoRBotonReiniciar.setObjectName(u"geoRBotonReiniciar")
        self.geoRBotonReiniciar.setMinimumSize(QSize(50, 50))
        self.geoRBotonReiniciar.setMaximumSize(QSize(50, 50))
        self.geoRBotonReiniciar.setStyleSheet(u"background-color: rgb(142, 151, 253);\n"
"border-color: rgb(142, 151, 253);\n"
"border-image: url(:/geometria/images/geometria/reboot.png);\n"
"border-width: 2px;\n"
"border-radius: 20px;")

        self.horizontalLayout_15.addWidget(self.geoRBotonReiniciar)


        self.gridLayout_15.addLayout(self.horizontalLayout_15, 1, 0, 2, 1)

        self.groupBox_Canal_3 = QGroupBox(self.geometriaNoCircular)
        self.groupBox_Canal_3.setObjectName(u"groupBox_Canal_3")
        self.groupBox_Canal_3.setGeometry(QRect(11, 6, 191, 315))
        sizePolicy9.setHeightForWidth(self.groupBox_Canal_3.sizePolicy().hasHeightForWidth())
        self.groupBox_Canal_3.setSizePolicy(sizePolicy9)
        self.groupBox_Canal_3.setStyleSheet(u"QGroupBox {\n"
"color: rgb(203, 208, 253);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(203, 208, 253);\n"
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
        self.gridLayout_17 = QGridLayout(self.groupBox_Canal_3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.geoBotonRectangular = QPushButton(self.groupBox_Canal_3)
        self.geoBotonRectangular.setObjectName(u"geoBotonRectangular")
        self.geoBotonRectangular.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.geoBotonRectangular.sizePolicy().hasHeightForWidth())
        self.geoBotonRectangular.setSizePolicy(sizePolicy10)
        self.geoBotonRectangular.setMinimumSize(QSize(150, 100))
        self.geoBotonRectangular.setStyleSheet(u"border-image: url(:/geometria/images/geometria/FigurasRectangulares.png);\n"
"background-color: rgb(255,255,255);")
        self.geoBotonRectangular.setCheckable(True)
        self.geoBotonRectangular.setChecked(False)
        self.geoBotonRectangular.setFlat(False)

        self.gridLayout_17.addWidget(self.geoBotonRectangular, 1, 1, 1, 1)

        self.groupBox_Resultados_3 = QGroupBox(self.geometriaNoCircular)
        self.groupBox_Resultados_3.setObjectName(u"groupBox_Resultados_3")
        self.groupBox_Resultados_3.setGeometry(QRect(10, 330, 1071, 258))
        sizePolicy8.setHeightForWidth(self.groupBox_Resultados_3.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_3.setSizePolicy(sizePolicy8)
        self.groupBox_Resultados_3.setStyleSheet(u"QGroupBox {\n"
"color: rgb(203, 208, 253);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(203, 208, 253);\n"
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
        self.gridLayout_18 = QGridLayout(self.groupBox_Resultados_3)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_6, 2, 0, 1, 1)

        self.row_9 = QFrame(self.groupBox_Resultados_3)
        self.row_9.setObjectName(u"row_9")
        self.row_9.setStyleSheet(u"")
        self.row_9.setFrameShape(QFrame.StyledPanel)
        self.row_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.row_9)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_19.setHorizontalSpacing(25)
        self.gridLayout_19.setVerticalSpacing(15)
        self.gridLayout_19.setContentsMargins(15, 20, 15, 20)
        self.geoRFieldPerimetro = QLineEdit(self.row_9)
        self.geoRFieldPerimetro.setObjectName(u"geoRFieldPerimetro")
        sizePolicy5.setHeightForWidth(self.geoRFieldPerimetro.sizePolicy().hasHeightForWidth())
        self.geoRFieldPerimetro.setSizePolicy(sizePolicy5)
        self.geoRFieldPerimetro.setMinimumSize(QSize(0, 30))
        self.geoRFieldPerimetro.setMaximumSize(QSize(16777215, 30))
        self.geoRFieldPerimetro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.geoRFieldPerimetro, 1, 1, 1, 1)

        self.geoRFieldRadio = QLineEdit(self.row_9)
        self.geoRFieldRadio.setObjectName(u"geoRFieldRadio")
        sizePolicy5.setHeightForWidth(self.geoRFieldRadio.sizePolicy().hasHeightForWidth())
        self.geoRFieldRadio.setSizePolicy(sizePolicy5)
        self.geoRFieldRadio.setMinimumSize(QSize(0, 30))
        self.geoRFieldRadio.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_19.addWidget(self.geoRFieldRadio, 2, 1, 1, 1)

        self.geoRLabelArea = QLabel(self.row_9)
        self.geoRLabelArea.setObjectName(u"geoRLabelArea")
        sizePolicy6.setHeightForWidth(self.geoRLabelArea.sizePolicy().hasHeightForWidth())
        self.geoRLabelArea.setSizePolicy(sizePolicy6)
        self.geoRLabelArea.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoRLabelArea.setLineWidth(1)
        self.geoRLabelArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.geoRLabelArea, 0, 0, 1, 1)

        self.geoRFieldArea = QLineEdit(self.row_9)
        self.geoRFieldArea.setObjectName(u"geoRFieldArea")
        sizePolicy5.setHeightForWidth(self.geoRFieldArea.sizePolicy().hasHeightForWidth())
        self.geoRFieldArea.setSizePolicy(sizePolicy5)
        self.geoRFieldArea.setMinimumSize(QSize(0, 30))
        self.geoRFieldArea.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.geoRFieldArea, 0, 1, 1, 1)

        self.geoRLabelRadio = QLabel(self.row_9)
        self.geoRLabelRadio.setObjectName(u"geoRLabelRadio")
        sizePolicy6.setHeightForWidth(self.geoRLabelRadio.sizePolicy().hasHeightForWidth())
        self.geoRLabelRadio.setSizePolicy(sizePolicy6)
        self.geoRLabelRadio.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoRLabelRadio.setLineWidth(1)
        self.geoRLabelRadio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.geoRLabelRadio, 2, 0, 1, 1)

        self.geoRLabelAnchoSuperficial = QLabel(self.row_9)
        self.geoRLabelAnchoSuperficial.setObjectName(u"geoRLabelAnchoSuperficial")
        sizePolicy6.setHeightForWidth(self.geoRLabelAnchoSuperficial.sizePolicy().hasHeightForWidth())
        self.geoRLabelAnchoSuperficial.setSizePolicy(sizePolicy6)
        self.geoRLabelAnchoSuperficial.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoRLabelAnchoSuperficial.setLineWidth(1)
        self.geoRLabelAnchoSuperficial.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.geoRLabelAnchoSuperficial, 3, 0, 1, 1)

        self.geoRLabelPerimetro = QLabel(self.row_9)
        self.geoRLabelPerimetro.setObjectName(u"geoRLabelPerimetro")
        sizePolicy6.setHeightForWidth(self.geoRLabelPerimetro.sizePolicy().hasHeightForWidth())
        self.geoRLabelPerimetro.setSizePolicy(sizePolicy6)
        self.geoRLabelPerimetro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoRLabelPerimetro.setLineWidth(1)
        self.geoRLabelPerimetro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.geoRLabelPerimetro, 1, 0, 1, 1)

        self.geoRLabelProfundidadHidraulica = QLabel(self.row_9)
        self.geoRLabelProfundidadHidraulica.setObjectName(u"geoRLabelProfundidadHidraulica")
        sizePolicy6.setHeightForWidth(self.geoRLabelProfundidadHidraulica.sizePolicy().hasHeightForWidth())
        self.geoRLabelProfundidadHidraulica.setSizePolicy(sizePolicy6)
        self.geoRLabelProfundidadHidraulica.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoRLabelProfundidadHidraulica.setLineWidth(1)
        self.geoRLabelProfundidadHidraulica.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.geoRLabelProfundidadHidraulica, 4, 0, 1, 1)

        self.geoRFieldAnchoSuperficial = QLineEdit(self.row_9)
        self.geoRFieldAnchoSuperficial.setObjectName(u"geoRFieldAnchoSuperficial")
        sizePolicy5.setHeightForWidth(self.geoRFieldAnchoSuperficial.sizePolicy().hasHeightForWidth())
        self.geoRFieldAnchoSuperficial.setSizePolicy(sizePolicy5)
        self.geoRFieldAnchoSuperficial.setMinimumSize(QSize(0, 30))
        self.geoRFieldAnchoSuperficial.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.geoRFieldAnchoSuperficial, 3, 1, 1, 1)

        self.geoRFieldProfundidadHidraulica = QLineEdit(self.row_9)
        self.geoRFieldProfundidadHidraulica.setObjectName(u"geoRFieldProfundidadHidraulica")
        sizePolicy5.setHeightForWidth(self.geoRFieldProfundidadHidraulica.sizePolicy().hasHeightForWidth())
        self.geoRFieldProfundidadHidraulica.setSizePolicy(sizePolicy5)
        self.geoRFieldProfundidadHidraulica.setMinimumSize(QSize(0, 30))
        self.geoRFieldProfundidadHidraulica.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.geoRFieldProfundidadHidraulica, 4, 1, 1, 1)


        self.verticalLayout_28.addLayout(self.gridLayout_19)


        self.gridLayout_18.addWidget(self.row_9, 0, 0, 1, 1)

        self.geoRImagenCanal = QPushButton(self.groupBox_Resultados_3)
        self.geoRImagenCanal.setObjectName(u"geoRImagenCanal")
        self.geoRImagenCanal.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.geoRImagenCanal.sizePolicy().hasHeightForWidth())
        self.geoRImagenCanal.setSizePolicy(sizePolicy5)
        self.geoRImagenCanal.setMinimumSize(QSize(260, 213))
        self.geoRImagenCanal.setStyleSheet(u"border-image: url(:/geometria/images/geometria/Geometria-rectangular.PNG);\n"
"background-color: rgb(255,255,255);")
        self.geoRImagenCanal.setFlat(True)

        self.gridLayout_18.addWidget(self.geoRImagenCanal, 0, 1, 1, 1)

        self.tabGeometria.addTab(self.geometriaNoCircular, "")
        self.geometriaFroude = QWidget()
        self.geometriaFroude.setObjectName(u"geometriaFroude")
        self.geometriaFroude.setStyleSheet(u"border-color: rgb(60, 60, 75);\n"
"background-color: rgb(65, 65, 97);\n"
"font: 500 11pt \"Allerta\";")
        self.groupBox_Resultados_6 = QGroupBox(self.geometriaFroude)
        self.groupBox_Resultados_6.setObjectName(u"groupBox_Resultados_6")
        self.groupBox_Resultados_6.setGeometry(QRect(20, 484, 1052, 101))
        sizePolicy8.setHeightForWidth(self.groupBox_Resultados_6.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_6.setSizePolicy(sizePolicy8)
        self.groupBox_Resultados_6.setStyleSheet(u"QGroupBox {\n"
"color: rgb(203, 208, 253);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(203, 208, 253);\n"
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
        self.gridLayout_33 = QGridLayout(self.groupBox_Resultados_6)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.row_17 = QFrame(self.groupBox_Resultados_6)
        self.row_17.setObjectName(u"row_17")
        self.row_17.setStyleSheet(u"")
        self.row_17.setFrameShape(QFrame.StyledPanel)
        self.row_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.row_17)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setSpacing(15)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_34.setContentsMargins(15, 15, 15, 15)
        self.geoFroudeLabelRadio = QLabel(self.row_17)
        self.geoFroudeLabelRadio.setObjectName(u"geoFroudeLabelRadio")
        sizePolicy6.setHeightForWidth(self.geoFroudeLabelRadio.sizePolicy().hasHeightForWidth())
        self.geoFroudeLabelRadio.setSizePolicy(sizePolicy6)
        self.geoFroudeLabelRadio.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoFroudeLabelRadio.setLineWidth(1)
        self.geoFroudeLabelRadio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_34.addWidget(self.geoFroudeLabelRadio, 0, 0, 1, 1)

        self.geoFroudeFieldFroude = QLineEdit(self.row_17)
        self.geoFroudeFieldFroude.setObjectName(u"geoFroudeFieldFroude")
        sizePolicy5.setHeightForWidth(self.geoFroudeFieldFroude.sizePolicy().hasHeightForWidth())
        self.geoFroudeFieldFroude.setSizePolicy(sizePolicy5)
        self.geoFroudeFieldFroude.setMinimumSize(QSize(0, 30))
        self.geoFroudeFieldFroude.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_34.addWidget(self.geoFroudeFieldFroude, 0, 1, 1, 1)


        self.verticalLayout_37.addLayout(self.gridLayout_34)


        self.gridLayout_33.addWidget(self.row_17, 0, 0, 1, 1)

        self.groupBox_Propiedades_6 = QGroupBox(self.geometriaFroude)
        self.groupBox_Propiedades_6.setObjectName(u"groupBox_Propiedades_6")
        self.groupBox_Propiedades_6.setGeometry(QRect(20, 10, 1051, 461))
        sizePolicy11.setHeightForWidth(self.groupBox_Propiedades_6.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_6.setSizePolicy(sizePolicy11)
        self.groupBox_Propiedades_6.setMinimumSize(QSize(850, 0))
        self.groupBox_Propiedades_6.setStyleSheet(u"QGroupBox {\n"
"color: rgb(203, 208, 253);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(203, 208, 253);\n"
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
        self.gridLayout_36 = QGridLayout(self.groupBox_Propiedades_6)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_25.setContentsMargins(10, 0, 10, -1)
        self.geoFroudeBotonCalcular = QPushButton(self.groupBox_Propiedades_6)
        self.geoFroudeBotonCalcular.setObjectName(u"geoFroudeBotonCalcular")
        self.geoFroudeBotonCalcular.setMinimumSize(QSize(50, 50))
        self.geoFroudeBotonCalcular.setMaximumSize(QSize(50, 50))
        self.geoFroudeBotonCalcular.setStyleSheet(u"background-color: rgb(142, 151, 253);\n"
"border-color: rgb(142, 151, 253);\n"
"border-width: 2px;\n"
"border-radius: 20px;")

        self.horizontalLayout_25.addWidget(self.geoFroudeBotonCalcular)

        self.geoFroudeBotonReiniciar = QPushButton(self.groupBox_Propiedades_6)
        self.geoFroudeBotonReiniciar.setObjectName(u"geoFroudeBotonReiniciar")
        self.geoFroudeBotonReiniciar.setMinimumSize(QSize(50, 50))
        self.geoFroudeBotonReiniciar.setMaximumSize(QSize(50, 50))
        self.geoFroudeBotonReiniciar.setStyleSheet(u"background-color: rgb(142, 151, 253);\n"
"border-color: rgb(142, 151, 253);\n"
"border-image: url(:/geometria/images/geometria/reboot.png);\n"
"border-width: 2px;\n"
"border-radius: 20px;")

        self.horizontalLayout_25.addWidget(self.geoFroudeBotonReiniciar)


        self.gridLayout_36.addLayout(self.horizontalLayout_25, 1, 0, 2, 1)

        self.row_18 = QFrame(self.groupBox_Propiedades_6)
        self.row_18.setObjectName(u"row_18")
        self.row_18.setStyleSheet(u"")
        self.row_18.setFrameShape(QFrame.StyledPanel)
        self.row_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.row_18)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_37.setHorizontalSpacing(60)
        self.gridLayout_37.setVerticalSpacing(15)
        self.gridLayout_37.setContentsMargins(0, 10, 0, 10)
        self.geoFroudeComboBoxAncho = QComboBox(self.row_18)
        self.geoFroudeComboBoxAncho.addItem("")
        self.geoFroudeComboBoxAncho.addItem("")
        self.geoFroudeComboBoxAncho.addItem("")
        self.geoFroudeComboBoxAncho.addItem("")
        self.geoFroudeComboBoxAncho.setObjectName(u"geoFroudeComboBoxAncho")
        sizePolicy11.setHeightForWidth(self.geoFroudeComboBoxAncho.sizePolicy().hasHeightForWidth())
        self.geoFroudeComboBoxAncho.setSizePolicy(sizePolicy11)
        self.geoFroudeComboBoxAncho.setMinimumSize(QSize(150, 30))
        self.geoFroudeComboBoxAncho.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoFroudeComboBoxAncho.setEditable(True)

        self.gridLayout_37.addWidget(self.geoFroudeComboBoxAncho, 1, 2, 1, 1)

        self.geoFroudeFieldPendienteLateral = QLineEdit(self.row_18)
        self.geoFroudeFieldPendienteLateral.setObjectName(u"geoFroudeFieldPendienteLateral")
        sizePolicy5.setHeightForWidth(self.geoFroudeFieldPendienteLateral.sizePolicy().hasHeightForWidth())
        self.geoFroudeFieldPendienteLateral.setSizePolicy(sizePolicy5)
        self.geoFroudeFieldPendienteLateral.setMinimumSize(QSize(0, 30))
        self.geoFroudeFieldPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_37.addWidget(self.geoFroudeFieldPendienteLateral, 2, 1, 1, 1)

        self.geoFroudeComboBoxCaudal = QComboBox(self.row_18)
        self.geoFroudeComboBoxCaudal.addItem("")
        self.geoFroudeComboBoxCaudal.addItem("")
        self.geoFroudeComboBoxCaudal.setObjectName(u"geoFroudeComboBoxCaudal")
        sizePolicy10.setHeightForWidth(self.geoFroudeComboBoxCaudal.sizePolicy().hasHeightForWidth())
        self.geoFroudeComboBoxCaudal.setSizePolicy(sizePolicy10)
        self.geoFroudeComboBoxCaudal.setMinimumSize(QSize(260, 32))
        self.geoFroudeComboBoxCaudal.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoFroudeComboBoxCaudal.setEditable(True)

        self.gridLayout_37.addWidget(self.geoFroudeComboBoxCaudal, 4, 2, 1, 1)

        self.geoFroudeFieldPendienteLateral2 = QLineEdit(self.row_18)
        self.geoFroudeFieldPendienteLateral2.setObjectName(u"geoFroudeFieldPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.geoFroudeFieldPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.geoFroudeFieldPendienteLateral2.setSizePolicy(sizePolicy5)
        self.geoFroudeFieldPendienteLateral2.setMinimumSize(QSize(0, 30))
        self.geoFroudeFieldPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_37.addWidget(self.geoFroudeFieldPendienteLateral2, 3, 1, 1, 1)

        self.geoFroudeFieldCaudal = QLineEdit(self.row_18)
        self.geoFroudeFieldCaudal.setObjectName(u"geoFroudeFieldCaudal")
        sizePolicy5.setHeightForWidth(self.geoFroudeFieldCaudal.sizePolicy().hasHeightForWidth())
        self.geoFroudeFieldCaudal.setSizePolicy(sizePolicy5)
        self.geoFroudeFieldCaudal.setMinimumSize(QSize(0, 30))
        self.geoFroudeFieldCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_37.addWidget(self.geoFroudeFieldCaudal, 4, 1, 1, 1)

        self.geoFroudeLabelPendienteLateral2 = QLabel(self.row_18)
        self.geoFroudeLabelPendienteLateral2.setObjectName(u"geoFroudeLabelPendienteLateral2")
        sizePolicy6.setHeightForWidth(self.geoFroudeLabelPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.geoFroudeLabelPendienteLateral2.setSizePolicy(sizePolicy6)
        self.geoFroudeLabelPendienteLateral2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoFroudeLabelPendienteLateral2.setLineWidth(1)
        self.geoFroudeLabelPendienteLateral2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_37.addWidget(self.geoFroudeLabelPendienteLateral2, 3, 0, 1, 1)

        self.geoFroudeLabelPendienteLateral_3 = QLabel(self.row_18)
        self.geoFroudeLabelPendienteLateral_3.setObjectName(u"geoFroudeLabelPendienteLateral_3")
        sizePolicy6.setHeightForWidth(self.geoFroudeLabelPendienteLateral_3.sizePolicy().hasHeightForWidth())
        self.geoFroudeLabelPendienteLateral_3.setSizePolicy(sizePolicy6)
        self.geoFroudeLabelPendienteLateral_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoFroudeLabelPendienteLateral_3.setLineWidth(1)
        self.geoFroudeLabelPendienteLateral_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_37.addWidget(self.geoFroudeLabelPendienteLateral_3, 4, 0, 1, 1)

        self.geoFroudeLabelPendienteLateral_4 = QLabel(self.row_18)
        self.geoFroudeLabelPendienteLateral_4.setObjectName(u"geoFroudeLabelPendienteLateral_4")
        sizePolicy6.setHeightForWidth(self.geoFroudeLabelPendienteLateral_4.sizePolicy().hasHeightForWidth())
        self.geoFroudeLabelPendienteLateral_4.setSizePolicy(sizePolicy6)
        self.geoFroudeLabelPendienteLateral_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoFroudeLabelPendienteLateral_4.setLineWidth(1)
        self.geoFroudeLabelPendienteLateral_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_37.addWidget(self.geoFroudeLabelPendienteLateral_4, 6, 0, 1, 1)

        self.geoFroudeFieldProfundidadSeccion = QLineEdit(self.row_18)
        self.geoFroudeFieldProfundidadSeccion.setObjectName(u"geoFroudeFieldProfundidadSeccion")
        sizePolicy7.setHeightForWidth(self.geoFroudeFieldProfundidadSeccion.sizePolicy().hasHeightForWidth())
        self.geoFroudeFieldProfundidadSeccion.setSizePolicy(sizePolicy7)
        self.geoFroudeFieldProfundidadSeccion.setMinimumSize(QSize(150, 30))
        self.geoFroudeFieldProfundidadSeccion.setMaximumSize(QSize(16777215, 30))
        self.geoFroudeFieldProfundidadSeccion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_37.addWidget(self.geoFroudeFieldProfundidadSeccion, 0, 1, 1, 1)

        self.geoFroudeFieldDiametro = QLineEdit(self.row_18)
        self.geoFroudeFieldDiametro.setObjectName(u"geoFroudeFieldDiametro")
        sizePolicy5.setHeightForWidth(self.geoFroudeFieldDiametro.sizePolicy().hasHeightForWidth())
        self.geoFroudeFieldDiametro.setSizePolicy(sizePolicy5)
        self.geoFroudeFieldDiametro.setMinimumSize(QSize(0, 30))
        self.geoFroudeFieldDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_37.addWidget(self.geoFroudeFieldDiametro, 6, 1, 1, 1)

        self.geoFroudeLabelPendienteLateral_2 = QLabel(self.row_18)
        self.geoFroudeLabelPendienteLateral_2.setObjectName(u"geoFroudeLabelPendienteLateral_2")
        sizePolicy6.setHeightForWidth(self.geoFroudeLabelPendienteLateral_2.sizePolicy().hasHeightForWidth())
        self.geoFroudeLabelPendienteLateral_2.setSizePolicy(sizePolicy6)
        self.geoFroudeLabelPendienteLateral_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoFroudeLabelPendienteLateral_2.setLineWidth(1)
        self.geoFroudeLabelPendienteLateral_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_37.addWidget(self.geoFroudeLabelPendienteLateral_2, 2, 0, 1, 1)

        self.geoFroudeComboBoxProfundidad = QComboBox(self.row_18)
        self.geoFroudeComboBoxProfundidad.addItem("")
        self.geoFroudeComboBoxProfundidad.addItem("")
        self.geoFroudeComboBoxProfundidad.addItem("")
        self.geoFroudeComboBoxProfundidad.addItem("")
        self.geoFroudeComboBoxProfundidad.setObjectName(u"geoFroudeComboBoxProfundidad")
        sizePolicy11.setHeightForWidth(self.geoFroudeComboBoxProfundidad.sizePolicy().hasHeightForWidth())
        self.geoFroudeComboBoxProfundidad.setSizePolicy(sizePolicy11)
        self.geoFroudeComboBoxProfundidad.setMinimumSize(QSize(150, 30))
        self.geoFroudeComboBoxProfundidad.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoFroudeComboBoxProfundidad.setEditable(True)

        self.gridLayout_37.addWidget(self.geoFroudeComboBoxProfundidad, 0, 2, 1, 1)

        self.geoFroudeComboBoxDiametro = QComboBox(self.row_18)
        self.geoFroudeComboBoxDiametro.addItem("")
        self.geoFroudeComboBoxDiametro.addItem("")
        self.geoFroudeComboBoxDiametro.addItem("")
        self.geoFroudeComboBoxDiametro.addItem("")
        self.geoFroudeComboBoxDiametro.setObjectName(u"geoFroudeComboBoxDiametro")
        sizePolicy11.setHeightForWidth(self.geoFroudeComboBoxDiametro.sizePolicy().hasHeightForWidth())
        self.geoFroudeComboBoxDiametro.setSizePolicy(sizePolicy11)
        self.geoFroudeComboBoxDiametro.setMinimumSize(QSize(150, 30))
        self.geoFroudeComboBoxDiametro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoFroudeComboBoxDiametro.setEditable(True)

        self.gridLayout_37.addWidget(self.geoFroudeComboBoxDiametro, 6, 2, 1, 1)

        self.geoFroudeLabelProfundidadSeccion = QLabel(self.row_18)
        self.geoFroudeLabelProfundidadSeccion.setObjectName(u"geoFroudeLabelProfundidadSeccion")
        sizePolicy6.setHeightForWidth(self.geoFroudeLabelProfundidadSeccion.sizePolicy().hasHeightForWidth())
        self.geoFroudeLabelProfundidadSeccion.setSizePolicy(sizePolicy6)
        self.geoFroudeLabelProfundidadSeccion.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoFroudeLabelProfundidadSeccion.setLineWidth(1)
        self.geoFroudeLabelProfundidadSeccion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_37.addWidget(self.geoFroudeLabelProfundidadSeccion, 0, 0, 1, 1)

        self.geoFroudeComboBoxPendienteLateral = QComboBox(self.row_18)
        self.geoFroudeComboBoxPendienteLateral.addItem("")
        self.geoFroudeComboBoxPendienteLateral.addItem("")
        self.geoFroudeComboBoxPendienteLateral.addItem("")
        self.geoFroudeComboBoxPendienteLateral.setObjectName(u"geoFroudeComboBoxPendienteLateral")
        sizePolicy11.setHeightForWidth(self.geoFroudeComboBoxPendienteLateral.sizePolicy().hasHeightForWidth())
        self.geoFroudeComboBoxPendienteLateral.setSizePolicy(sizePolicy11)
        self.geoFroudeComboBoxPendienteLateral.setMinimumSize(QSize(150, 30))
        self.geoFroudeComboBoxPendienteLateral.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoFroudeComboBoxPendienteLateral.setEditable(True)

        self.gridLayout_37.addWidget(self.geoFroudeComboBoxPendienteLateral, 2, 2, 1, 1)

        self.geoFroudeComboBoxPendienteLateral2 = QComboBox(self.row_18)
        self.geoFroudeComboBoxPendienteLateral2.addItem("")
        self.geoFroudeComboBoxPendienteLateral2.addItem("")
        self.geoFroudeComboBoxPendienteLateral2.addItem("")
        self.geoFroudeComboBoxPendienteLateral2.setObjectName(u"geoFroudeComboBoxPendienteLateral2")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.geoFroudeComboBoxPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.geoFroudeComboBoxPendienteLateral2.setSizePolicy(sizePolicy12)
        self.geoFroudeComboBoxPendienteLateral2.setMinimumSize(QSize(150, 30))
        self.geoFroudeComboBoxPendienteLateral2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoFroudeComboBoxPendienteLateral2.setEditable(True)

        self.gridLayout_37.addWidget(self.geoFroudeComboBoxPendienteLateral2, 3, 2, 1, 1)

        self.geoFroudeLabelAncho = QLabel(self.row_18)
        self.geoFroudeLabelAncho.setObjectName(u"geoFroudeLabelAncho")
        sizePolicy6.setHeightForWidth(self.geoFroudeLabelAncho.sizePolicy().hasHeightForWidth())
        self.geoFroudeLabelAncho.setSizePolicy(sizePolicy6)
        self.geoFroudeLabelAncho.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoFroudeLabelAncho.setLineWidth(1)
        self.geoFroudeLabelAncho.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_37.addWidget(self.geoFroudeLabelAncho, 1, 0, 1, 1)

        self.geoFroudeFieldAncho = QLineEdit(self.row_18)
        self.geoFroudeFieldAncho.setObjectName(u"geoFroudeFieldAncho")
        sizePolicy5.setHeightForWidth(self.geoFroudeFieldAncho.sizePolicy().hasHeightForWidth())
        self.geoFroudeFieldAncho.setSizePolicy(sizePolicy5)
        self.geoFroudeFieldAncho.setMinimumSize(QSize(150, 30))
        self.geoFroudeFieldAncho.setMaximumSize(QSize(16777215, 30))
        self.geoFroudeFieldAncho.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_37.addWidget(self.geoFroudeFieldAncho, 1, 1, 1, 1)

        self.geoFroudeLabelVelocidad = QLabel(self.row_18)
        self.geoFroudeLabelVelocidad.setObjectName(u"geoFroudeLabelVelocidad")
        sizePolicy6.setHeightForWidth(self.geoFroudeLabelVelocidad.sizePolicy().hasHeightForWidth())
        self.geoFroudeLabelVelocidad.setSizePolicy(sizePolicy6)
        self.geoFroudeLabelVelocidad.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.geoFroudeLabelVelocidad.setLineWidth(1)
        self.geoFroudeLabelVelocidad.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_37.addWidget(self.geoFroudeLabelVelocidad, 5, 0, 1, 1)

        self.geoFroudeFieldVelocidad = QLineEdit(self.row_18)
        self.geoFroudeFieldVelocidad.setObjectName(u"geoFroudeFieldVelocidad")
        sizePolicy5.setHeightForWidth(self.geoFroudeFieldVelocidad.sizePolicy().hasHeightForWidth())
        self.geoFroudeFieldVelocidad.setSizePolicy(sizePolicy5)
        self.geoFroudeFieldVelocidad.setMinimumSize(QSize(0, 30))
        self.geoFroudeFieldVelocidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_37.addWidget(self.geoFroudeFieldVelocidad, 5, 1, 1, 1)

        self.geoFroudeComboBoxVelocidad = QComboBox(self.row_18)
        self.geoFroudeComboBoxVelocidad.addItem("")
        self.geoFroudeComboBoxVelocidad.setObjectName(u"geoFroudeComboBoxVelocidad")
        sizePolicy11.setHeightForWidth(self.geoFroudeComboBoxVelocidad.sizePolicy().hasHeightForWidth())
        self.geoFroudeComboBoxVelocidad.setSizePolicy(sizePolicy11)
        self.geoFroudeComboBoxVelocidad.setMinimumSize(QSize(150, 30))
        self.geoFroudeComboBoxVelocidad.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.geoFroudeComboBoxVelocidad.setEditable(True)

        self.gridLayout_37.addWidget(self.geoFroudeComboBoxVelocidad, 5, 2, 1, 1)


        self.verticalLayout_38.addLayout(self.gridLayout_37)


        self.gridLayout_36.addWidget(self.row_18, 0, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_24.setContentsMargins(10, 0, 10, -1)
        self.geoFroudeTextoCalcular = QLabel(self.groupBox_Propiedades_6)
        self.geoFroudeTextoCalcular.setObjectName(u"geoFroudeTextoCalcular")
        sizePolicy5.setHeightForWidth(self.geoFroudeTextoCalcular.sizePolicy().hasHeightForWidth())
        self.geoFroudeTextoCalcular.setSizePolicy(sizePolicy5)
        self.geoFroudeTextoCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"\n"
"color: rgb(231, 230, 242);")
        self.geoFroudeTextoCalcular.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.geoFroudeTextoCalcular)

        self.geoFroudeTextoReiniciar = QLabel(self.groupBox_Propiedades_6)
        self.geoFroudeTextoReiniciar.setObjectName(u"geoFroudeTextoReiniciar")
        sizePolicy5.setHeightForWidth(self.geoFroudeTextoReiniciar.sizePolicy().hasHeightForWidth())
        self.geoFroudeTextoReiniciar.setSizePolicy(sizePolicy5)
        self.geoFroudeTextoReiniciar.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(231, 226, 242);")
        self.geoFroudeTextoReiniciar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.geoFroudeTextoReiniciar)


        self.gridLayout_36.addLayout(self.horizontalLayout_24, 4, 0, 1, 1)

        self.tabGeometria.addTab(self.geometriaFroude, "")
        self.stackedWidget.addWidget(self.pagina_geometria)
        self.pagina_conservacionE = QWidget()
        self.pagina_conservacionE.setObjectName(u"pagina_conservacionE")
        self.tabConservacionEnergia = QTabWidget(self.pagina_conservacionE)
        self.tabConservacionEnergia.setObjectName(u"tabConservacionEnergia")
        self.tabConservacionEnergia.setGeometry(QRect(0, 0, 1121, 613))
        sizePolicy13 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.tabConservacionEnergia.sizePolicy().hasHeightForWidth())
        self.tabConservacionEnergia.setSizePolicy(sizePolicy13)
        self.tabConservacionEnergia.setStyleSheet(u"font: 500 10pt \"Allerta\";\n"
"color: rgb(79, 79, 79);")
        self.tabConservacionEnergia.setTabPosition(QTabWidget.West)
        self.tabConservacionEnergia.setTabsClosable(False)
        self.rhCalculoCaudal = QWidget()
        self.rhCalculoCaudal.setObjectName(u"rhCalculoCaudal")
        self.rhCalculoCaudal.setStyleSheet(u"font: 500 11pt \"Allerta\";")
        self.verticalLayoutWidget_4 = QWidget(self.rhCalculoCaudal)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(800, 12, 271, 221))
        self.verticalLayout_29 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setHorizontalSpacing(10)
        self.gridLayout_22.setVerticalSpacing(30)
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setHorizontalSpacing(60)
        self.gridLayout_23.setVerticalSpacing(0)
        self.ManningUniformeTextoReiniciar_2 = QLabel(self.verticalLayoutWidget_4)
        self.ManningUniformeTextoReiniciar_2.setObjectName(u"ManningUniformeTextoReiniciar_2")
        sizePolicy5.setHeightForWidth(self.ManningUniformeTextoReiniciar_2.sizePolicy().hasHeightForWidth())
        self.ManningUniformeTextoReiniciar_2.setSizePolicy(sizePolicy5)
        self.ManningUniformeTextoReiniciar_2.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"")
        self.ManningUniformeTextoReiniciar_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.ManningUniformeTextoReiniciar_2, 2, 1, 1, 1)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(20)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(-1, -1, -1, 20)
        self.ManningUniformeBotonCalcular_2 = QPushButton(self.verticalLayoutWidget_4)
        self.ManningUniformeBotonCalcular_2.setObjectName(u"ManningUniformeBotonCalcular_2")
        self.ManningUniformeBotonCalcular_2.setMinimumSize(QSize(50, 50))
        self.ManningUniformeBotonCalcular_2.setMaximumSize(QSize(40, 40))
        self.ManningUniformeBotonCalcular_2.setStyleSheet(u"background-color: rgb(214, 112, 114);\n"
"border-color: rgb(214, 112, 114);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_35.addWidget(self.ManningUniformeBotonCalcular_2)


        self.gridLayout_23.addLayout(self.horizontalLayout_35, 0, 0, 1, 1)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, -1, -1, 20)
        self.ManningUniformeBotonReiniciar_2 = QPushButton(self.verticalLayoutWidget_4)
        self.ManningUniformeBotonReiniciar_2.setObjectName(u"ManningUniformeBotonReiniciar_2")
        self.ManningUniformeBotonReiniciar_2.setMinimumSize(QSize(50, 50))
        self.ManningUniformeBotonReiniciar_2.setMaximumSize(QSize(40, 40))
        self.ManningUniformeBotonReiniciar_2.setStyleSheet(u"background-color: rgb(214, 112, 114);\n"
"border-color: rgb(214, 112, 114);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_36.addWidget(self.ManningUniformeBotonReiniciar_2)


        self.gridLayout_23.addLayout(self.horizontalLayout_36, 0, 1, 1, 1)

        self.ManningUniformeTextoCalcular_2 = QLabel(self.verticalLayoutWidget_4)
        self.ManningUniformeTextoCalcular_2.setObjectName(u"ManningUniformeTextoCalcular_2")
        sizePolicy5.setHeightForWidth(self.ManningUniformeTextoCalcular_2.sizePolicy().hasHeightForWidth())
        self.ManningUniformeTextoCalcular_2.setSizePolicy(sizePolicy5)
        self.ManningUniformeTextoCalcular_2.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"")
        self.ManningUniformeTextoCalcular_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.ManningUniformeTextoCalcular_2, 2, 0, 1, 1)

        self.gridLayout_23.setColumnStretch(0, 10)

        self.gridLayout_22.addLayout(self.gridLayout_23, 1, 0, 1, 1)


        self.verticalLayout_29.addLayout(self.gridLayout_22)

        self.groupBox_Propiedades_28 = QGroupBox(self.rhCalculoCaudal)
        self.groupBox_Propiedades_28.setObjectName(u"groupBox_Propiedades_28")
        self.groupBox_Propiedades_28.setGeometry(QRect(790, 270, 290, 301))
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_28.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_28.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_28.setMinimumSize(QSize(290, 0))
        self.groupBox_Propiedades_28.setMaximumSize(QSize(290, 16777215))
        self.groupBox_Propiedades_28.setStyleSheet(u"QGroupBox {\n"
"color: rgb(214, 112, 114);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(214, 112, 114);\n"
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
        self.gridLayout_111 = QGridLayout(self.groupBox_Propiedades_28)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.row_54 = QFrame(self.groupBox_Propiedades_28)
        self.row_54.setObjectName(u"row_54")
        self.row_54.setStyleSheet(u"")
        self.row_54.setFrameShape(QFrame.StyledPanel)
        self.row_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.row_54)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_112 = QGridLayout()
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.gridLayout_112.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_112.setHorizontalSpacing(20)
        self.gridLayout_112.setVerticalSpacing(50)
        self.gridLayout_112.setContentsMargins(10, 5, 10, 5)
        self.RHAnalisisFieldCaudal_7 = QLineEdit(self.row_54)
        self.RHAnalisisFieldCaudal_7.setObjectName(u"RHAnalisisFieldCaudal_7")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldCaudal_7.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldCaudal_7.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldCaudal_7.setMinimumSize(QSize(115, 60))
        self.RHAnalisisFieldCaudal_7.setMaximumSize(QSize(160, 16777215))
        self.RHAnalisisFieldCaudal_7.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_112.addWidget(self.RHAnalisisFieldCaudal_7, 1, 1, 1, 1)

        self.RHAnalisisLabelCaudal_7 = QLabel(self.row_54)
        self.RHAnalisisLabelCaudal_7.setObjectName(u"RHAnalisisLabelCaudal_7")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelCaudal_7.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelCaudal_7.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelCaudal_7.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelCaudal_7.setLineWidth(1)
        self.RHAnalisisLabelCaudal_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_112.addWidget(self.RHAnalisisLabelCaudal_7, 1, 0, 1, 1)

        self.RHAnalisisLabelCaudal_8 = QLabel(self.row_54)
        self.RHAnalisisLabelCaudal_8.setObjectName(u"RHAnalisisLabelCaudal_8")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelCaudal_8.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelCaudal_8.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelCaudal_8.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelCaudal_8.setLineWidth(1)
        self.RHAnalisisLabelCaudal_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_112.addWidget(self.RHAnalisisLabelCaudal_8, 0, 0, 1, 1)

        self.RHAnalisisFieldCaudal_8 = QLineEdit(self.row_54)
        self.RHAnalisisFieldCaudal_8.setObjectName(u"RHAnalisisFieldCaudal_8")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldCaudal_8.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldCaudal_8.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldCaudal_8.setMinimumSize(QSize(115, 60))
        self.RHAnalisisFieldCaudal_8.setMaximumSize(QSize(160, 16777215))
        self.RHAnalisisFieldCaudal_8.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_112.addWidget(self.RHAnalisisFieldCaudal_8, 0, 1, 1, 1)


        self.verticalLayout_74.addLayout(self.gridLayout_112)


        self.gridLayout_111.addWidget(self.row_54, 0, 1, 1, 1)

        self.widget = QWidget(self.rhCalculoCaudal)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 752, 581))
        self.verticalLayout_30 = QVBoxLayout(self.widget)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.groupBox_Propiedades_20 = QGroupBox(self.widget)
        self.groupBox_Propiedades_20.setObjectName(u"groupBox_Propiedades_20")
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_20.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_20.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_20.setMinimumSize(QSize(750, 0))
        self.groupBox_Propiedades_20.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_20.setStyleSheet(u"QGroupBox {\n"
"color: rgb(214, 112, 114);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(214, 112, 114);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_20.setAlignment(Qt.AlignCenter)
        self.gridLayout_89 = QGridLayout(self.groupBox_Propiedades_20)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.row_43 = QFrame(self.groupBox_Propiedades_20)
        self.row_43.setObjectName(u"row_43")
        self.row_43.setStyleSheet(u"")
        self.row_43.setFrameShape(QFrame.StyledPanel)
        self.row_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.row_43)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_90 = QGridLayout()
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.gridLayout_90.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_90.setHorizontalSpacing(30)
        self.gridLayout_90.setVerticalSpacing(10)
        self.gridLayout_90.setContentsMargins(10, 5, 20, 5)
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxPendienteLateralSec1 = QComboBox(self.row_43)
        self.CEnergiaComboBoxPendienteLateralSec1.addItem("")
        self.CEnergiaComboBoxPendienteLateralSec1.addItem("")
        self.CEnergiaComboBoxPendienteLateralSec1.addItem("")
        self.CEnergiaComboBoxPendienteLateralSec1.setObjectName(u"CEnergiaComboBoxPendienteLateralSec1")
        sizePolicy14 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.CEnergiaComboBoxPendienteLateralSec1.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxPendienteLateralSec1.setSizePolicy(sizePolicy14)
        self.CEnergiaComboBoxPendienteLateralSec1.setMinimumSize(QSize(226, 30))
        self.CEnergiaComboBoxPendienteLateralSec1.setMaximumSize(QSize(260, 16777215))
        self.CEnergiaComboBoxPendienteLateralSec1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxPendienteLateralSec1.setEditable(True)
        self.CEnergiaComboBoxPendienteLateralSec1.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_64.addWidget(self.CEnergiaComboBoxPendienteLateralSec1)


        self.gridLayout_90.addLayout(self.horizontalLayout_64, 1, 2, 1, 1)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxAnchoSec1 = QComboBox(self.row_43)
        self.CEnergiaComboBoxAnchoSec1.addItem("")
        self.CEnergiaComboBoxAnchoSec1.addItem("")
        self.CEnergiaComboBoxAnchoSec1.addItem("")
        self.CEnergiaComboBoxAnchoSec1.addItem("")
        self.CEnergiaComboBoxAnchoSec1.setObjectName(u"CEnergiaComboBoxAnchoSec1")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxAnchoSec1.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxAnchoSec1.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxAnchoSec1.setMinimumSize(QSize(150, 30))
        self.CEnergiaComboBoxAnchoSec1.setMaximumSize(QSize(260, 30))
        self.CEnergiaComboBoxAnchoSec1.setLayoutDirection(Qt.LeftToRight)
        self.CEnergiaComboBoxAnchoSec1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxAnchoSec1.setEditable(True)
        self.CEnergiaComboBoxAnchoSec1.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.CEnergiaComboBoxAnchoSec1.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_73.addWidget(self.CEnergiaComboBoxAnchoSec1)


        self.gridLayout_90.addLayout(self.horizontalLayout_73, 0, 2, 1, 1)

        self.CEnergiaLabelProfundidadSec1 = QLabel(self.row_43)
        self.CEnergiaLabelProfundidadSec1.setObjectName(u"CEnergiaLabelProfundidadSec1")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelProfundidadSec1.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelProfundidadSec1.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelProfundidadSec1.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelProfundidadSec1.setLineWidth(1)
        self.CEnergiaLabelProfundidadSec1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_90.addWidget(self.CEnergiaLabelProfundidadSec1, 3, 0, 1, 1)

        self.CEnergiaLabelPendienteLateral2Sec1 = QLabel(self.row_43)
        self.CEnergiaLabelPendienteLateral2Sec1.setObjectName(u"CEnergiaLabelPendienteLateral2Sec1")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelPendienteLateral2Sec1.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelPendienteLateral2Sec1.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelPendienteLateral2Sec1.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelPendienteLateral2Sec1.setLineWidth(1)
        self.CEnergiaLabelPendienteLateral2Sec1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_90.addWidget(self.CEnergiaLabelPendienteLateral2Sec1, 2, 0, 1, 1)

        self.CEnergiaFieldPendienteLateralSec1 = QLineEdit(self.row_43)
        self.CEnergiaFieldPendienteLateralSec1.setObjectName(u"CEnergiaFieldPendienteLateralSec1")
        sizePolicy15 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.CEnergiaFieldPendienteLateralSec1.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldPendienteLateralSec1.setSizePolicy(sizePolicy15)
        self.CEnergiaFieldPendienteLateralSec1.setMinimumSize(QSize(110, 30))
        self.CEnergiaFieldPendienteLateralSec1.setMaximumSize(QSize(150, 30))
        self.CEnergiaFieldPendienteLateralSec1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_90.addWidget(self.CEnergiaFieldPendienteLateralSec1, 1, 1, 1, 1)

        self.CEnergiaFieldProfundidad1Sec1 = QLineEdit(self.row_43)
        self.CEnergiaFieldProfundidad1Sec1.setObjectName(u"CEnergiaFieldProfundidad1Sec1")
        sizePolicy5.setHeightForWidth(self.CEnergiaFieldProfundidad1Sec1.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldProfundidad1Sec1.setSizePolicy(sizePolicy5)
        self.CEnergiaFieldProfundidad1Sec1.setMinimumSize(QSize(0, 30))
        self.CEnergiaFieldProfundidad1Sec1.setMaximumSize(QSize(150, 16777215))
        self.CEnergiaFieldProfundidad1Sec1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_90.addWidget(self.CEnergiaFieldProfundidad1Sec1, 3, 1, 1, 1)

        self.CEnergiaLabelBaseSec1 = QLabel(self.row_43)
        self.CEnergiaLabelBaseSec1.setObjectName(u"CEnergiaLabelBaseSec1")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelBaseSec1.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelBaseSec1.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelBaseSec1.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelBaseSec1.setLineWidth(1)
        self.CEnergiaLabelBaseSec1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_90.addWidget(self.CEnergiaLabelBaseSec1, 0, 0, 1, 1)

        self.CEnergiaLabelPendienteLateralSec1 = QLabel(self.row_43)
        self.CEnergiaLabelPendienteLateralSec1.setObjectName(u"CEnergiaLabelPendienteLateralSec1")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelPendienteLateralSec1.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelPendienteLateralSec1.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelPendienteLateralSec1.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelPendienteLateralSec1.setLineWidth(1)
        self.CEnergiaLabelPendienteLateralSec1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_90.addWidget(self.CEnergiaLabelPendienteLateralSec1, 1, 0, 1, 1)

        self.CEnergiaFieldPendienteLateral2Sec1 = QLineEdit(self.row_43)
        self.CEnergiaFieldPendienteLateral2Sec1.setObjectName(u"CEnergiaFieldPendienteLateral2Sec1")
        sizePolicy5.setHeightForWidth(self.CEnergiaFieldPendienteLateral2Sec1.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldPendienteLateral2Sec1.setSizePolicy(sizePolicy5)
        self.CEnergiaFieldPendienteLateral2Sec1.setMinimumSize(QSize(0, 30))
        self.CEnergiaFieldPendienteLateral2Sec1.setMaximumSize(QSize(150, 16777215))
        self.CEnergiaFieldPendienteLateral2Sec1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_90.addWidget(self.CEnergiaFieldPendienteLateral2Sec1, 2, 1, 1, 1)

        self.CEnergiaFieldAnchoSec1 = QLineEdit(self.row_43)
        self.CEnergiaFieldAnchoSec1.setObjectName(u"CEnergiaFieldAnchoSec1")
        sizePolicy15.setHeightForWidth(self.CEnergiaFieldAnchoSec1.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldAnchoSec1.setSizePolicy(sizePolicy15)
        self.CEnergiaFieldAnchoSec1.setMinimumSize(QSize(110, 30))
        self.CEnergiaFieldAnchoSec1.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldAnchoSec1.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.CEnergiaFieldAnchoSec1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_90.addWidget(self.CEnergiaFieldAnchoSec1, 0, 1, 1, 1)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.CEnergiaComboBoxPendienteLateral2Sec1 = QComboBox(self.row_43)
        self.CEnergiaComboBoxPendienteLateral2Sec1.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec1.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec1.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec1.setObjectName(u"CEnergiaComboBoxPendienteLateral2Sec1")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxPendienteLateral2Sec1.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxPendienteLateral2Sec1.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxPendienteLateral2Sec1.setMinimumSize(QSize(226, 30))
        self.CEnergiaComboBoxPendienteLateral2Sec1.setMaximumSize(QSize(260, 16777215))
        self.CEnergiaComboBoxPendienteLateral2Sec1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxPendienteLateral2Sec1.setEditable(True)
        self.CEnergiaComboBoxPendienteLateral2Sec1.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_81.addWidget(self.CEnergiaComboBoxPendienteLateral2Sec1)


        self.gridLayout_90.addLayout(self.horizontalLayout_81, 2, 2, 1, 1)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxProfundidad1Sec1 = QComboBox(self.row_43)
        self.CEnergiaComboBoxProfundidad1Sec1.addItem("")
        self.CEnergiaComboBoxProfundidad1Sec1.addItem("")
        self.CEnergiaComboBoxProfundidad1Sec1.addItem("")
        self.CEnergiaComboBoxProfundidad1Sec1.addItem("")
        self.CEnergiaComboBoxProfundidad1Sec1.setObjectName(u"CEnergiaComboBoxProfundidad1Sec1")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxProfundidad1Sec1.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxProfundidad1Sec1.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxProfundidad1Sec1.setMinimumSize(QSize(150, 30))
        self.CEnergiaComboBoxProfundidad1Sec1.setMaximumSize(QSize(260, 30))
        self.CEnergiaComboBoxProfundidad1Sec1.setLayoutDirection(Qt.LeftToRight)
        self.CEnergiaComboBoxProfundidad1Sec1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxProfundidad1Sec1.setEditable(True)
        self.CEnergiaComboBoxProfundidad1Sec1.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.CEnergiaComboBoxProfundidad1Sec1.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_82.addWidget(self.CEnergiaComboBoxProfundidad1Sec1)


        self.gridLayout_90.addLayout(self.horizontalLayout_82, 3, 2, 1, 1)


        self.verticalLayout_63.addLayout(self.gridLayout_90)


        self.gridLayout_89.addWidget(self.row_43, 0, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.groupBox_Propiedades_20)

        self.groupBox_Propiedades_23 = QGroupBox(self.widget)
        self.groupBox_Propiedades_23.setObjectName(u"groupBox_Propiedades_23")
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_23.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_23.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_23.setMinimumSize(QSize(750, 0))
        self.groupBox_Propiedades_23.setMaximumSize(QSize(750, 16777215))
        self.groupBox_Propiedades_23.setStyleSheet(u"QGroupBox {\n"
"color: rgb(214, 112, 114);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(214, 112, 114);\n"
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
        self.gridLayout_91 = QGridLayout(self.groupBox_Propiedades_23)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.row_44 = QFrame(self.groupBox_Propiedades_23)
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
        self.gridLayout_92.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_92.setHorizontalSpacing(30)
        self.gridLayout_92.setVerticalSpacing(10)
        self.gridLayout_92.setContentsMargins(10, 5, 20, 5)
        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setSpacing(0)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxProfundidad1Sec2 = QComboBox(self.row_44)
        self.CEnergiaComboBoxProfundidad1Sec2.addItem("")
        self.CEnergiaComboBoxProfundidad1Sec2.addItem("")
        self.CEnergiaComboBoxProfundidad1Sec2.addItem("")
        self.CEnergiaComboBoxProfundidad1Sec2.addItem("")
        self.CEnergiaComboBoxProfundidad1Sec2.setObjectName(u"CEnergiaComboBoxProfundidad1Sec2")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxProfundidad1Sec2.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxProfundidad1Sec2.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxProfundidad1Sec2.setMinimumSize(QSize(150, 30))
        self.CEnergiaComboBoxProfundidad1Sec2.setMaximumSize(QSize(260, 30))
        self.CEnergiaComboBoxProfundidad1Sec2.setLayoutDirection(Qt.LeftToRight)
        self.CEnergiaComboBoxProfundidad1Sec2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxProfundidad1Sec2.setEditable(True)
        self.CEnergiaComboBoxProfundidad1Sec2.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.CEnergiaComboBoxProfundidad1Sec2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_98.addWidget(self.CEnergiaComboBoxProfundidad1Sec2)


        self.gridLayout_92.addLayout(self.horizontalLayout_98, 3, 2, 1, 1)

        self.CEnergiaFieldAnchoSec2 = QLineEdit(self.row_44)
        self.CEnergiaFieldAnchoSec2.setObjectName(u"CEnergiaFieldAnchoSec2")
        sizePolicy15.setHeightForWidth(self.CEnergiaFieldAnchoSec2.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldAnchoSec2.setSizePolicy(sizePolicy15)
        self.CEnergiaFieldAnchoSec2.setMinimumSize(QSize(110, 30))
        self.CEnergiaFieldAnchoSec2.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldAnchoSec2.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.CEnergiaFieldAnchoSec2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_92.addWidget(self.CEnergiaFieldAnchoSec2, 0, 1, 1, 1)

        self.CEnergiaLabelPendienteLateral2Sec2 = QLabel(self.row_44)
        self.CEnergiaLabelPendienteLateral2Sec2.setObjectName(u"CEnergiaLabelPendienteLateral2Sec2")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelPendienteLateral2Sec2.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelPendienteLateral2Sec2.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelPendienteLateral2Sec2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelPendienteLateral2Sec2.setLineWidth(1)
        self.CEnergiaLabelPendienteLateral2Sec2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_92.addWidget(self.CEnergiaLabelPendienteLateral2Sec2, 2, 0, 1, 1)

        self.CEnergiaFieldProfundidad1Sec2 = QLineEdit(self.row_44)
        self.CEnergiaFieldProfundidad1Sec2.setObjectName(u"CEnergiaFieldProfundidad1Sec2")
        sizePolicy5.setHeightForWidth(self.CEnergiaFieldProfundidad1Sec2.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldProfundidad1Sec2.setSizePolicy(sizePolicy5)
        self.CEnergiaFieldProfundidad1Sec2.setMinimumSize(QSize(0, 30))
        self.CEnergiaFieldProfundidad1Sec2.setMaximumSize(QSize(150, 16777215))
        self.CEnergiaFieldProfundidad1Sec2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_92.addWidget(self.CEnergiaFieldProfundidad1Sec2, 3, 1, 1, 1)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxPendienteLateralSec1_2 = QComboBox(self.row_44)
        self.CEnergiaComboBoxPendienteLateralSec1_2.addItem("")
        self.CEnergiaComboBoxPendienteLateralSec1_2.addItem("")
        self.CEnergiaComboBoxPendienteLateralSec1_2.addItem("")
        self.CEnergiaComboBoxPendienteLateralSec1_2.setObjectName(u"CEnergiaComboBoxPendienteLateralSec1_2")
        sizePolicy14.setHeightForWidth(self.CEnergiaComboBoxPendienteLateralSec1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxPendienteLateralSec1_2.setSizePolicy(sizePolicy14)
        self.CEnergiaComboBoxPendienteLateralSec1_2.setMinimumSize(QSize(226, 30))
        self.CEnergiaComboBoxPendienteLateralSec1_2.setMaximumSize(QSize(260, 16777215))
        self.CEnergiaComboBoxPendienteLateralSec1_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxPendienteLateralSec1_2.setEditable(True)
        self.CEnergiaComboBoxPendienteLateralSec1_2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_74.addWidget(self.CEnergiaComboBoxPendienteLateralSec1_2)


        self.gridLayout_92.addLayout(self.horizontalLayout_74, 1, 2, 1, 1)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxAnchoSec2 = QComboBox(self.row_44)
        self.CEnergiaComboBoxAnchoSec2.addItem("")
        self.CEnergiaComboBoxAnchoSec2.addItem("")
        self.CEnergiaComboBoxAnchoSec2.addItem("")
        self.CEnergiaComboBoxAnchoSec2.addItem("")
        self.CEnergiaComboBoxAnchoSec2.setObjectName(u"CEnergiaComboBoxAnchoSec2")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxAnchoSec2.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxAnchoSec2.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxAnchoSec2.setMinimumSize(QSize(150, 30))
        self.CEnergiaComboBoxAnchoSec2.setMaximumSize(QSize(260, 30))
        self.CEnergiaComboBoxAnchoSec2.setLayoutDirection(Qt.LeftToRight)
        self.CEnergiaComboBoxAnchoSec2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxAnchoSec2.setEditable(True)
        self.CEnergiaComboBoxAnchoSec2.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.CEnergiaComboBoxAnchoSec2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_96.addWidget(self.CEnergiaComboBoxAnchoSec2)


        self.gridLayout_92.addLayout(self.horizontalLayout_96, 0, 2, 1, 1)

        self.CEnergiaLabelProfundidadSec2 = QLabel(self.row_44)
        self.CEnergiaLabelProfundidadSec2.setObjectName(u"CEnergiaLabelProfundidadSec2")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelProfundidadSec2.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelProfundidadSec2.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelProfundidadSec2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelProfundidadSec2.setLineWidth(1)
        self.CEnergiaLabelProfundidadSec2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_92.addWidget(self.CEnergiaLabelProfundidadSec2, 3, 0, 1, 1)

        self.CEnergiaFieldPendienteLateralSec2 = QLineEdit(self.row_44)
        self.CEnergiaFieldPendienteLateralSec2.setObjectName(u"CEnergiaFieldPendienteLateralSec2")
        sizePolicy15.setHeightForWidth(self.CEnergiaFieldPendienteLateralSec2.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldPendienteLateralSec2.setSizePolicy(sizePolicy15)
        self.CEnergiaFieldPendienteLateralSec2.setMinimumSize(QSize(110, 30))
        self.CEnergiaFieldPendienteLateralSec2.setMaximumSize(QSize(150, 30))
        self.CEnergiaFieldPendienteLateralSec2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_92.addWidget(self.CEnergiaFieldPendienteLateralSec2, 1, 1, 1, 1)

        self.CEnergiaFieldPendienteLateral2Sec2 = QLineEdit(self.row_44)
        self.CEnergiaFieldPendienteLateral2Sec2.setObjectName(u"CEnergiaFieldPendienteLateral2Sec2")
        sizePolicy5.setHeightForWidth(self.CEnergiaFieldPendienteLateral2Sec2.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldPendienteLateral2Sec2.setSizePolicy(sizePolicy5)
        self.CEnergiaFieldPendienteLateral2Sec2.setMinimumSize(QSize(0, 30))
        self.CEnergiaFieldPendienteLateral2Sec2.setMaximumSize(QSize(150, 16777215))
        self.CEnergiaFieldPendienteLateral2Sec2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_92.addWidget(self.CEnergiaFieldPendienteLateral2Sec2, 2, 1, 1, 1)

        self.CEnergiaLabelBaseSec2 = QLabel(self.row_44)
        self.CEnergiaLabelBaseSec2.setObjectName(u"CEnergiaLabelBaseSec2")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelBaseSec2.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelBaseSec2.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelBaseSec2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelBaseSec2.setLineWidth(1)
        self.CEnergiaLabelBaseSec2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_92.addWidget(self.CEnergiaLabelBaseSec2, 0, 0, 1, 1)

        self.CEnergiaLabelPendienteLateralSec2 = QLabel(self.row_44)
        self.CEnergiaLabelPendienteLateralSec2.setObjectName(u"CEnergiaLabelPendienteLateralSec2")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelPendienteLateralSec2.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelPendienteLateralSec2.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelPendienteLateralSec2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelPendienteLateralSec2.setLineWidth(1)
        self.CEnergiaLabelPendienteLateralSec2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_92.addWidget(self.CEnergiaLabelPendienteLateralSec2, 1, 0, 1, 1)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.CEnergiaComboBoxPendienteLateral2Sec2 = QComboBox(self.row_44)
        self.CEnergiaComboBoxPendienteLateral2Sec2.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec2.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec2.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec2.setObjectName(u"CEnergiaComboBoxPendienteLateral2Sec2")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxPendienteLateral2Sec2.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxPendienteLateral2Sec2.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxPendienteLateral2Sec2.setMinimumSize(QSize(226, 30))
        self.CEnergiaComboBoxPendienteLateral2Sec2.setMaximumSize(QSize(260, 16777215))
        self.CEnergiaComboBoxPendienteLateral2Sec2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxPendienteLateral2Sec2.setEditable(True)
        self.CEnergiaComboBoxPendienteLateral2Sec2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_97.addWidget(self.CEnergiaComboBoxPendienteLateral2Sec2)


        self.gridLayout_92.addLayout(self.horizontalLayout_97, 2, 2, 1, 1)


        self.verticalLayout_64.addLayout(self.gridLayout_92)


        self.gridLayout_91.addWidget(self.row_44, 0, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.groupBox_Propiedades_23)

        self.groupBox_Propiedades_24 = QGroupBox(self.widget)
        self.groupBox_Propiedades_24.setObjectName(u"groupBox_Propiedades_24")
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_24.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_24.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_24.setMinimumSize(QSize(750, 0))
        self.groupBox_Propiedades_24.setMaximumSize(QSize(750, 16777215))
        self.groupBox_Propiedades_24.setStyleSheet(u"QGroupBox {\n"
"color: rgb(214, 112, 114);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(214, 112, 114);\n"
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
        self.gridLayout_102.setHorizontalSpacing(30)
        self.gridLayout_102.setVerticalSpacing(10)
        self.gridLayout_102.setContentsMargins(10, 5, 20, 5)
        self.RHAnalisisLabelCaudal_4 = QLabel(self.row_49)
        self.RHAnalisisLabelCaudal_4.setObjectName(u"RHAnalisisLabelCaudal_4")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelCaudal_4.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelCaudal_4.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelCaudal_4.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelCaudal_4.setLineWidth(1)
        self.RHAnalisisLabelCaudal_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_102.addWidget(self.RHAnalisisLabelCaudal_4, 0, 0, 1, 1)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setSpacing(0)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxAnchoSec2_3 = QComboBox(self.row_49)
        self.CEnergiaComboBoxAnchoSec2_3.addItem("")
        self.CEnergiaComboBoxAnchoSec2_3.addItem("")
        self.CEnergiaComboBoxAnchoSec2_3.addItem("")
        self.CEnergiaComboBoxAnchoSec2_3.addItem("")
        self.CEnergiaComboBoxAnchoSec2_3.setObjectName(u"CEnergiaComboBoxAnchoSec2_3")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxAnchoSec2_3.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxAnchoSec2_3.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxAnchoSec2_3.setMinimumSize(QSize(150, 30))
        self.CEnergiaComboBoxAnchoSec2_3.setMaximumSize(QSize(260, 30))
        self.CEnergiaComboBoxAnchoSec2_3.setLayoutDirection(Qt.LeftToRight)
        self.CEnergiaComboBoxAnchoSec2_3.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxAnchoSec2_3.setEditable(True)
        self.CEnergiaComboBoxAnchoSec2_3.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.CEnergiaComboBoxAnchoSec2_3.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_102.addWidget(self.CEnergiaComboBoxAnchoSec2_3)


        self.gridLayout_102.addLayout(self.horizontalLayout_102, 0, 2, 1, 1)

        self.RHAnalisisFieldCaudal_4 = QLineEdit(self.row_49)
        self.RHAnalisisFieldCaudal_4.setObjectName(u"RHAnalisisFieldCaudal_4")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldCaudal_4.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldCaudal_4.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldCaudal_4.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldCaudal_4.setMaximumSize(QSize(150, 16777215))
        self.RHAnalisisFieldCaudal_4.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_102.addWidget(self.RHAnalisisFieldCaudal_4, 0, 1, 1, 1)


        self.verticalLayout_69.addLayout(self.gridLayout_102)


        self.gridLayout_101.addWidget(self.row_49, 0, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.groupBox_Propiedades_24)

        self.tabConservacionEnergia.addTab(self.rhCalculoCaudal, "")
        self.rhProfundidad = QWidget()
        self.rhProfundidad.setObjectName(u"rhProfundidad")
        self.rhProfundidad.setStyleSheet(u"font: 500 11pt \"Allerta\";")
        self.layoutWidget_2 = QWidget(self.rhProfundidad)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(830, 10, 198, 94))
        self.gridLayout_25 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(60)
        self.gridLayout_25.setVerticalSpacing(0)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.ManningUniformeTextoReiniciar_3 = QLabel(self.layoutWidget_2)
        self.ManningUniformeTextoReiniciar_3.setObjectName(u"ManningUniformeTextoReiniciar_3")
        sizePolicy5.setHeightForWidth(self.ManningUniformeTextoReiniciar_3.sizePolicy().hasHeightForWidth())
        self.ManningUniformeTextoReiniciar_3.setSizePolicy(sizePolicy5)
        self.ManningUniformeTextoReiniciar_3.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"")
        self.ManningUniformeTextoReiniciar_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.ManningUniformeTextoReiniciar_3, 2, 1, 1, 1)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(20)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, -1, -1, 20)
        self.ManningUniformeBotonCalcular_3 = QPushButton(self.layoutWidget_2)
        self.ManningUniformeBotonCalcular_3.setObjectName(u"ManningUniformeBotonCalcular_3")
        self.ManningUniformeBotonCalcular_3.setMinimumSize(QSize(50, 50))
        self.ManningUniformeBotonCalcular_3.setMaximumSize(QSize(40, 40))
        self.ManningUniformeBotonCalcular_3.setStyleSheet(u"background-color: rgb(214, 112, 114);\n"
"border-color: rgb(214, 112, 114);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_37.addWidget(self.ManningUniformeBotonCalcular_3)


        self.gridLayout_25.addLayout(self.horizontalLayout_37, 0, 0, 1, 1)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, -1, -1, 20)
        self.ManningUniformeBotonReiniciar_3 = QPushButton(self.layoutWidget_2)
        self.ManningUniformeBotonReiniciar_3.setObjectName(u"ManningUniformeBotonReiniciar_3")
        self.ManningUniformeBotonReiniciar_3.setMinimumSize(QSize(50, 50))
        self.ManningUniformeBotonReiniciar_3.setMaximumSize(QSize(40, 40))
        self.ManningUniformeBotonReiniciar_3.setStyleSheet(u"background-color: rgb(214, 112, 114);\n"
"border-color: rgb(214, 112, 114);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_38.addWidget(self.ManningUniformeBotonReiniciar_3)


        self.gridLayout_25.addLayout(self.horizontalLayout_38, 0, 1, 1, 1)

        self.ManningUniformeTextoCalcular_3 = QLabel(self.layoutWidget_2)
        self.ManningUniformeTextoCalcular_3.setObjectName(u"ManningUniformeTextoCalcular_3")
        sizePolicy5.setHeightForWidth(self.ManningUniformeTextoCalcular_3.sizePolicy().hasHeightForWidth())
        self.ManningUniformeTextoCalcular_3.setSizePolicy(sizePolicy5)
        self.ManningUniformeTextoCalcular_3.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"")
        self.ManningUniformeTextoCalcular_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.ManningUniformeTextoCalcular_3, 2, 0, 1, 1)

        self.gridLayout_25.setColumnStretch(0, 10)
        self.layoutWidget_3 = QWidget(self.rhProfundidad)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 10, 752, 582))
        self.verticalLayout_31 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_31.setSpacing(1)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.groupBox_Propiedades_25 = QGroupBox(self.layoutWidget_3)
        self.groupBox_Propiedades_25.setObjectName(u"groupBox_Propiedades_25")
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_25.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_25.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_25.setMinimumSize(QSize(750, 0))
        self.groupBox_Propiedades_25.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_25.setStyleSheet(u"QGroupBox {\n"
"color: rgb(214, 112, 114);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(214, 112, 114);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
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
        self.gridLayout_104.setHorizontalSpacing(30)
        self.gridLayout_104.setVerticalSpacing(5)
        self.gridLayout_104.setContentsMargins(10, 10, 20, 5)
        self.CEnergiaFieldAnchoSec1_2 = QLineEdit(self.row_50)
        self.CEnergiaFieldAnchoSec1_2.setObjectName(u"CEnergiaFieldAnchoSec1_2")
        sizePolicy15.setHeightForWidth(self.CEnergiaFieldAnchoSec1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldAnchoSec1_2.setSizePolicy(sizePolicy15)
        self.CEnergiaFieldAnchoSec1_2.setMinimumSize(QSize(110, 30))
        self.CEnergiaFieldAnchoSec1_2.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldAnchoSec1_2.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.CEnergiaFieldAnchoSec1_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_104.addWidget(self.CEnergiaFieldAnchoSec1_2, 0, 1, 1, 1)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxPendienteLateralSec1_3 = QComboBox(self.row_50)
        self.CEnergiaComboBoxPendienteLateralSec1_3.addItem("")
        self.CEnergiaComboBoxPendienteLateralSec1_3.addItem("")
        self.CEnergiaComboBoxPendienteLateralSec1_3.addItem("")
        self.CEnergiaComboBoxPendienteLateralSec1_3.setObjectName(u"CEnergiaComboBoxPendienteLateralSec1_3")
        sizePolicy14.setHeightForWidth(self.CEnergiaComboBoxPendienteLateralSec1_3.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxPendienteLateralSec1_3.setSizePolicy(sizePolicy14)
        self.CEnergiaComboBoxPendienteLateralSec1_3.setMinimumSize(QSize(226, 30))
        self.CEnergiaComboBoxPendienteLateralSec1_3.setMaximumSize(QSize(260, 16777215))
        self.CEnergiaComboBoxPendienteLateralSec1_3.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxPendienteLateralSec1_3.setEditable(True)
        self.CEnergiaComboBoxPendienteLateralSec1_3.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_99.addWidget(self.CEnergiaComboBoxPendienteLateralSec1_3)


        self.gridLayout_104.addLayout(self.horizontalLayout_99, 1, 2, 1, 1)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setSpacing(0)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxAnchoSec1_2 = QComboBox(self.row_50)
        self.CEnergiaComboBoxAnchoSec1_2.addItem("")
        self.CEnergiaComboBoxAnchoSec1_2.addItem("")
        self.CEnergiaComboBoxAnchoSec1_2.addItem("")
        self.CEnergiaComboBoxAnchoSec1_2.addItem("")
        self.CEnergiaComboBoxAnchoSec1_2.setObjectName(u"CEnergiaComboBoxAnchoSec1_2")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxAnchoSec1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxAnchoSec1_2.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxAnchoSec1_2.setMinimumSize(QSize(150, 30))
        self.CEnergiaComboBoxAnchoSec1_2.setMaximumSize(QSize(260, 30))
        self.CEnergiaComboBoxAnchoSec1_2.setLayoutDirection(Qt.LeftToRight)
        self.CEnergiaComboBoxAnchoSec1_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxAnchoSec1_2.setEditable(True)
        self.CEnergiaComboBoxAnchoSec1_2.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.CEnergiaComboBoxAnchoSec1_2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_100.addWidget(self.CEnergiaComboBoxAnchoSec1_2)


        self.gridLayout_104.addLayout(self.horizontalLayout_100, 0, 2, 1, 1)

        self.CEnergiaFieldProfundidad1Sec1_3 = QLineEdit(self.row_50)
        self.CEnergiaFieldProfundidad1Sec1_3.setObjectName(u"CEnergiaFieldProfundidad1Sec1_3")
        sizePolicy5.setHeightForWidth(self.CEnergiaFieldProfundidad1Sec1_3.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldProfundidad1Sec1_3.setSizePolicy(sizePolicy5)
        self.CEnergiaFieldProfundidad1Sec1_3.setMinimumSize(QSize(0, 30))
        self.CEnergiaFieldProfundidad1Sec1_3.setMaximumSize(QSize(150, 16777215))
        self.CEnergiaFieldProfundidad1Sec1_3.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_104.addWidget(self.CEnergiaFieldProfundidad1Sec1_3, 4, 1, 1, 1)

        self.CEnergiaLabelPendienteLateralSec1_2 = QLabel(self.row_50)
        self.CEnergiaLabelPendienteLateralSec1_2.setObjectName(u"CEnergiaLabelPendienteLateralSec1_2")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelPendienteLateralSec1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelPendienteLateralSec1_2.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelPendienteLateralSec1_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelPendienteLateralSec1_2.setLineWidth(1)
        self.CEnergiaLabelPendienteLateralSec1_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_104.addWidget(self.CEnergiaLabelPendienteLateralSec1_2, 1, 0, 1, 1)

        self.CEnergiaFieldProfundidad1Sec1_2 = QLineEdit(self.row_50)
        self.CEnergiaFieldProfundidad1Sec1_2.setObjectName(u"CEnergiaFieldProfundidad1Sec1_2")
        sizePolicy5.setHeightForWidth(self.CEnergiaFieldProfundidad1Sec1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldProfundidad1Sec1_2.setSizePolicy(sizePolicy5)
        self.CEnergiaFieldProfundidad1Sec1_2.setMinimumSize(QSize(0, 30))
        self.CEnergiaFieldProfundidad1Sec1_2.setMaximumSize(QSize(150, 16777215))
        self.CEnergiaFieldProfundidad1Sec1_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_104.addWidget(self.CEnergiaFieldProfundidad1Sec1_2, 3, 1, 1, 1)

        self.CEnergiaLabelProfundidadSec1_3 = QLabel(self.row_50)
        self.CEnergiaLabelProfundidadSec1_3.setObjectName(u"CEnergiaLabelProfundidadSec1_3")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelProfundidadSec1_3.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelProfundidadSec1_3.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelProfundidadSec1_3.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelProfundidadSec1_3.setLineWidth(1)
        self.CEnergiaLabelProfundidadSec1_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_104.addWidget(self.CEnergiaLabelProfundidadSec1_3, 4, 0, 1, 1)

        self.CEnergiaLabelProfundidadSec1_2 = QLabel(self.row_50)
        self.CEnergiaLabelProfundidadSec1_2.setObjectName(u"CEnergiaLabelProfundidadSec1_2")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelProfundidadSec1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelProfundidadSec1_2.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelProfundidadSec1_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelProfundidadSec1_2.setLineWidth(1)
        self.CEnergiaLabelProfundidadSec1_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_104.addWidget(self.CEnergiaLabelProfundidadSec1_2, 3, 0, 1, 1)

        self.CEnergiaFieldPendienteLateralSec1_2 = QLineEdit(self.row_50)
        self.CEnergiaFieldPendienteLateralSec1_2.setObjectName(u"CEnergiaFieldPendienteLateralSec1_2")
        sizePolicy15.setHeightForWidth(self.CEnergiaFieldPendienteLateralSec1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldPendienteLateralSec1_2.setSizePolicy(sizePolicy15)
        self.CEnergiaFieldPendienteLateralSec1_2.setMinimumSize(QSize(110, 30))
        self.CEnergiaFieldPendienteLateralSec1_2.setMaximumSize(QSize(150, 30))
        self.CEnergiaFieldPendienteLateralSec1_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_104.addWidget(self.CEnergiaFieldPendienteLateralSec1_2, 1, 1, 1, 1)

        self.CEnergiaLabelBaseSec1_2 = QLabel(self.row_50)
        self.CEnergiaLabelBaseSec1_2.setObjectName(u"CEnergiaLabelBaseSec1_2")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelBaseSec1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelBaseSec1_2.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelBaseSec1_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelBaseSec1_2.setLineWidth(1)
        self.CEnergiaLabelBaseSec1_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_104.addWidget(self.CEnergiaLabelBaseSec1_2, 0, 0, 1, 1)

        self.CEnergiaLabelPendienteLateral2Sec1_2 = QLabel(self.row_50)
        self.CEnergiaLabelPendienteLateral2Sec1_2.setObjectName(u"CEnergiaLabelPendienteLateral2Sec1_2")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelPendienteLateral2Sec1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelPendienteLateral2Sec1_2.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelPendienteLateral2Sec1_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelPendienteLateral2Sec1_2.setLineWidth(1)
        self.CEnergiaLabelPendienteLateral2Sec1_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_104.addWidget(self.CEnergiaLabelPendienteLateral2Sec1_2, 2, 0, 1, 1)

        self.CEnergiaFieldPendienteLateral2Sec1_2 = QLineEdit(self.row_50)
        self.CEnergiaFieldPendienteLateral2Sec1_2.setObjectName(u"CEnergiaFieldPendienteLateral2Sec1_2")
        sizePolicy5.setHeightForWidth(self.CEnergiaFieldPendienteLateral2Sec1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldPendienteLateral2Sec1_2.setSizePolicy(sizePolicy5)
        self.CEnergiaFieldPendienteLateral2Sec1_2.setMinimumSize(QSize(0, 30))
        self.CEnergiaFieldPendienteLateral2Sec1_2.setMaximumSize(QSize(150, 16777215))
        self.CEnergiaFieldPendienteLateral2Sec1_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_104.addWidget(self.CEnergiaFieldPendienteLateral2Sec1_2, 2, 1, 1, 1)

        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.CEnergiaComboBoxPendienteLateral2Sec1_2 = QComboBox(self.row_50)
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.setObjectName(u"CEnergiaComboBoxPendienteLateral2Sec1_2")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxPendienteLateral2Sec1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.setMinimumSize(QSize(226, 30))
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.setMaximumSize(QSize(260, 16777215))
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.setEditable(True)
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_101.addWidget(self.CEnergiaComboBoxPendienteLateral2Sec1_2)


        self.gridLayout_104.addLayout(self.horizontalLayout_101, 2, 2, 1, 1)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setSpacing(0)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxProfundidad1Sec1_2 = QComboBox(self.row_50)
        self.CEnergiaComboBoxProfundidad1Sec1_2.addItem("")
        self.CEnergiaComboBoxProfundidad1Sec1_2.addItem("")
        self.CEnergiaComboBoxProfundidad1Sec1_2.addItem("")
        self.CEnergiaComboBoxProfundidad1Sec1_2.addItem("")
        self.CEnergiaComboBoxProfundidad1Sec1_2.setObjectName(u"CEnergiaComboBoxProfundidad1Sec1_2")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxProfundidad1Sec1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxProfundidad1Sec1_2.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxProfundidad1Sec1_2.setMinimumSize(QSize(150, 30))
        self.CEnergiaComboBoxProfundidad1Sec1_2.setMaximumSize(QSize(260, 30))
        self.CEnergiaComboBoxProfundidad1Sec1_2.setLayoutDirection(Qt.LeftToRight)
        self.CEnergiaComboBoxProfundidad1Sec1_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxProfundidad1Sec1_2.setEditable(True)
        self.CEnergiaComboBoxProfundidad1Sec1_2.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.CEnergiaComboBoxProfundidad1Sec1_2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_103.addWidget(self.CEnergiaComboBoxProfundidad1Sec1_2)


        self.gridLayout_104.addLayout(self.horizontalLayout_103, 3, 2, 1, 1)

        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.CEnergiaComboBoxPendienteLateral2Sec1_3 = QComboBox(self.row_50)
        self.CEnergiaComboBoxPendienteLateral2Sec1_3.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec1_3.setObjectName(u"CEnergiaComboBoxPendienteLateral2Sec1_3")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxPendienteLateral2Sec1_3.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxPendienteLateral2Sec1_3.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxPendienteLateral2Sec1_3.setMinimumSize(QSize(226, 30))
        self.CEnergiaComboBoxPendienteLateral2Sec1_3.setMaximumSize(QSize(260, 16777215))
        self.CEnergiaComboBoxPendienteLateral2Sec1_3.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxPendienteLateral2Sec1_3.setEditable(True)
        self.CEnergiaComboBoxPendienteLateral2Sec1_3.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_118.addWidget(self.CEnergiaComboBoxPendienteLateral2Sec1_3)


        self.gridLayout_104.addLayout(self.horizontalLayout_118, 4, 2, 1, 1)


        self.verticalLayout_70.addLayout(self.gridLayout_104)


        self.gridLayout_103.addWidget(self.row_50, 0, 1, 1, 1)


        self.verticalLayout_31.addWidget(self.groupBox_Propiedades_25)

        self.groupBox_Propiedades_26 = QGroupBox(self.layoutWidget_3)
        self.groupBox_Propiedades_26.setObjectName(u"groupBox_Propiedades_26")
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_26.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_26.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_26.setMinimumSize(QSize(750, 0))
        self.groupBox_Propiedades_26.setMaximumSize(QSize(750, 16777215))
        self.groupBox_Propiedades_26.setStyleSheet(u"QGroupBox {\n"
"color: rgb(214, 112, 114);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(214, 112, 114);\n"
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
        self.gridLayout_107 = QGridLayout(self.groupBox_Propiedades_26)
        self.gridLayout_107.setObjectName(u"gridLayout_107")
        self.row_52 = QFrame(self.groupBox_Propiedades_26)
        self.row_52.setObjectName(u"row_52")
        self.row_52.setStyleSheet(u"")
        self.row_52.setFrameShape(QFrame.StyledPanel)
        self.row_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.row_52)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_108 = QGridLayout()
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.gridLayout_108.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_108.setHorizontalSpacing(30)
        self.gridLayout_108.setVerticalSpacing(5)
        self.gridLayout_108.setContentsMargins(10, 10, 20, 5)
        self.CEnergiaFieldPendienteLateral2Sec2_2 = QLineEdit(self.row_52)
        self.CEnergiaFieldPendienteLateral2Sec2_2.setObjectName(u"CEnergiaFieldPendienteLateral2Sec2_2")
        sizePolicy5.setHeightForWidth(self.CEnergiaFieldPendienteLateral2Sec2_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldPendienteLateral2Sec2_2.setSizePolicy(sizePolicy5)
        self.CEnergiaFieldPendienteLateral2Sec2_2.setMinimumSize(QSize(0, 30))
        self.CEnergiaFieldPendienteLateral2Sec2_2.setMaximumSize(QSize(150, 16777215))
        self.CEnergiaFieldPendienteLateral2Sec2_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_108.addWidget(self.CEnergiaFieldPendienteLateral2Sec2_2, 2, 1, 1, 1)

        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.CEnergiaComboBoxPendienteLateral2Sec2_2 = QComboBox(self.row_52)
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.addItem("")
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.setObjectName(u"CEnergiaComboBoxPendienteLateral2Sec2_2")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxPendienteLateral2Sec2_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.setMinimumSize(QSize(226, 30))
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.setMaximumSize(QSize(260, 16777215))
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.setEditable(True)
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_116.addWidget(self.CEnergiaComboBoxPendienteLateral2Sec2_2)


        self.gridLayout_108.addLayout(self.horizontalLayout_116, 2, 2, 1, 1)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setSpacing(0)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxPendienteLateralSec1_4 = QComboBox(self.row_52)
        self.CEnergiaComboBoxPendienteLateralSec1_4.addItem("")
        self.CEnergiaComboBoxPendienteLateralSec1_4.addItem("")
        self.CEnergiaComboBoxPendienteLateralSec1_4.addItem("")
        self.CEnergiaComboBoxPendienteLateralSec1_4.setObjectName(u"CEnergiaComboBoxPendienteLateralSec1_4")
        sizePolicy14.setHeightForWidth(self.CEnergiaComboBoxPendienteLateralSec1_4.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxPendienteLateralSec1_4.setSizePolicy(sizePolicy14)
        self.CEnergiaComboBoxPendienteLateralSec1_4.setMinimumSize(QSize(226, 30))
        self.CEnergiaComboBoxPendienteLateralSec1_4.setMaximumSize(QSize(260, 16777215))
        self.CEnergiaComboBoxPendienteLateralSec1_4.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxPendienteLateralSec1_4.setEditable(True)
        self.CEnergiaComboBoxPendienteLateralSec1_4.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_114.addWidget(self.CEnergiaComboBoxPendienteLateralSec1_4)


        self.gridLayout_108.addLayout(self.horizontalLayout_114, 1, 2, 1, 1)

        self.CEnergiaLabelBaseSec2_2 = QLabel(self.row_52)
        self.CEnergiaLabelBaseSec2_2.setObjectName(u"CEnergiaLabelBaseSec2_2")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelBaseSec2_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelBaseSec2_2.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelBaseSec2_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelBaseSec2_2.setLineWidth(1)
        self.CEnergiaLabelBaseSec2_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_108.addWidget(self.CEnergiaLabelBaseSec2_2, 0, 0, 1, 1)

        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setSpacing(0)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxAnchoSec2_2 = QComboBox(self.row_52)
        self.CEnergiaComboBoxAnchoSec2_2.addItem("")
        self.CEnergiaComboBoxAnchoSec2_2.addItem("")
        self.CEnergiaComboBoxAnchoSec2_2.addItem("")
        self.CEnergiaComboBoxAnchoSec2_2.addItem("")
        self.CEnergiaComboBoxAnchoSec2_2.setObjectName(u"CEnergiaComboBoxAnchoSec2_2")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxAnchoSec2_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxAnchoSec2_2.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxAnchoSec2_2.setMinimumSize(QSize(150, 30))
        self.CEnergiaComboBoxAnchoSec2_2.setMaximumSize(QSize(260, 30))
        self.CEnergiaComboBoxAnchoSec2_2.setLayoutDirection(Qt.LeftToRight)
        self.CEnergiaComboBoxAnchoSec2_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxAnchoSec2_2.setEditable(True)
        self.CEnergiaComboBoxAnchoSec2_2.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.CEnergiaComboBoxAnchoSec2_2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_115.addWidget(self.CEnergiaComboBoxAnchoSec2_2)


        self.gridLayout_108.addLayout(self.horizontalLayout_115, 0, 2, 1, 1)

        self.CEnergiaLabelPendienteLateral2Sec2_2 = QLabel(self.row_52)
        self.CEnergiaLabelPendienteLateral2Sec2_2.setObjectName(u"CEnergiaLabelPendienteLateral2Sec2_2")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelPendienteLateral2Sec2_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelPendienteLateral2Sec2_2.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelPendienteLateral2Sec2_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelPendienteLateral2Sec2_2.setLineWidth(1)
        self.CEnergiaLabelPendienteLateral2Sec2_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_108.addWidget(self.CEnergiaLabelPendienteLateral2Sec2_2, 2, 0, 1, 1)

        self.CEnergiaFieldAnchoSec2_2 = QLineEdit(self.row_52)
        self.CEnergiaFieldAnchoSec2_2.setObjectName(u"CEnergiaFieldAnchoSec2_2")
        sizePolicy15.setHeightForWidth(self.CEnergiaFieldAnchoSec2_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldAnchoSec2_2.setSizePolicy(sizePolicy15)
        self.CEnergiaFieldAnchoSec2_2.setMinimumSize(QSize(110, 30))
        self.CEnergiaFieldAnchoSec2_2.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldAnchoSec2_2.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.CEnergiaFieldAnchoSec2_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_108.addWidget(self.CEnergiaFieldAnchoSec2_2, 0, 1, 1, 1)

        self.CEnergiaFieldPendienteLateralSec2_2 = QLineEdit(self.row_52)
        self.CEnergiaFieldPendienteLateralSec2_2.setObjectName(u"CEnergiaFieldPendienteLateralSec2_2")
        sizePolicy15.setHeightForWidth(self.CEnergiaFieldPendienteLateralSec2_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaFieldPendienteLateralSec2_2.setSizePolicy(sizePolicy15)
        self.CEnergiaFieldPendienteLateralSec2_2.setMinimumSize(QSize(110, 30))
        self.CEnergiaFieldPendienteLateralSec2_2.setMaximumSize(QSize(150, 30))
        self.CEnergiaFieldPendienteLateralSec2_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_108.addWidget(self.CEnergiaFieldPendienteLateralSec2_2, 1, 1, 1, 1)

        self.CEnergiaLabelPendienteLateralSec2_2 = QLabel(self.row_52)
        self.CEnergiaLabelPendienteLateralSec2_2.setObjectName(u"CEnergiaLabelPendienteLateralSec2_2")
        sizePolicy6.setHeightForWidth(self.CEnergiaLabelPendienteLateralSec2_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaLabelPendienteLateralSec2_2.setSizePolicy(sizePolicy6)
        self.CEnergiaLabelPendienteLateralSec2_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaLabelPendienteLateralSec2_2.setLineWidth(1)
        self.CEnergiaLabelPendienteLateralSec2_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_108.addWidget(self.CEnergiaLabelPendienteLateralSec2_2, 1, 0, 1, 1)


        self.verticalLayout_72.addLayout(self.gridLayout_108)


        self.gridLayout_107.addWidget(self.row_52, 0, 1, 1, 1)


        self.verticalLayout_31.addWidget(self.groupBox_Propiedades_26)

        self.groupBox_Propiedades_27 = QGroupBox(self.layoutWidget_3)
        self.groupBox_Propiedades_27.setObjectName(u"groupBox_Propiedades_27")
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_27.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_27.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_27.setMinimumSize(QSize(750, 0))
        self.groupBox_Propiedades_27.setMaximumSize(QSize(750, 16777215))
        self.groupBox_Propiedades_27.setStyleSheet(u"QGroupBox {\n"
"color: rgb(214, 112, 114);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(214, 112, 114);\n"
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
        self.gridLayout_109 = QGridLayout(self.groupBox_Propiedades_27)
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.row_53 = QFrame(self.groupBox_Propiedades_27)
        self.row_53.setObjectName(u"row_53")
        self.row_53.setStyleSheet(u"")
        self.row_53.setFrameShape(QFrame.StyledPanel)
        self.row_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.row_53)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_110 = QGridLayout()
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.gridLayout_110.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_110.setHorizontalSpacing(30)
        self.gridLayout_110.setVerticalSpacing(10)
        self.gridLayout_110.setContentsMargins(10, 10, 20, 10)
        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setSpacing(0)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setSizeConstraint(QLayout.SetMinimumSize)
        self.CEnergiaComboBoxAnchoSec2_4 = QComboBox(self.row_53)
        self.CEnergiaComboBoxAnchoSec2_4.addItem("")
        self.CEnergiaComboBoxAnchoSec2_4.addItem("")
        self.CEnergiaComboBoxAnchoSec2_4.addItem("")
        self.CEnergiaComboBoxAnchoSec2_4.addItem("")
        self.CEnergiaComboBoxAnchoSec2_4.setObjectName(u"CEnergiaComboBoxAnchoSec2_4")
        sizePolicy13.setHeightForWidth(self.CEnergiaComboBoxAnchoSec2_4.sizePolicy().hasHeightForWidth())
        self.CEnergiaComboBoxAnchoSec2_4.setSizePolicy(sizePolicy13)
        self.CEnergiaComboBoxAnchoSec2_4.setMinimumSize(QSize(150, 30))
        self.CEnergiaComboBoxAnchoSec2_4.setMaximumSize(QSize(260, 30))
        self.CEnergiaComboBoxAnchoSec2_4.setLayoutDirection(Qt.LeftToRight)
        self.CEnergiaComboBoxAnchoSec2_4.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CEnergiaComboBoxAnchoSec2_4.setEditable(True)
        self.CEnergiaComboBoxAnchoSec2_4.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.CEnergiaComboBoxAnchoSec2_4.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_117.addWidget(self.CEnergiaComboBoxAnchoSec2_4)


        self.gridLayout_110.addLayout(self.horizontalLayout_117, 0, 2, 1, 1)

        self.RHAnalisisFieldCaudal_5 = QLineEdit(self.row_53)
        self.RHAnalisisFieldCaudal_5.setObjectName(u"RHAnalisisFieldCaudal_5")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldCaudal_5.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldCaudal_5.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldCaudal_5.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldCaudal_5.setMaximumSize(QSize(150, 16777215))
        self.RHAnalisisFieldCaudal_5.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_110.addWidget(self.RHAnalisisFieldCaudal_5, 0, 1, 1, 1)

        self.RHAnalisisLabelCaudal_5 = QLabel(self.row_53)
        self.RHAnalisisLabelCaudal_5.setObjectName(u"RHAnalisisLabelCaudal_5")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelCaudal_5.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelCaudal_5.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelCaudal_5.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelCaudal_5.setLineWidth(1)
        self.RHAnalisisLabelCaudal_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_110.addWidget(self.RHAnalisisLabelCaudal_5, 0, 0, 1, 1)

        self.RHAnalisisLabelCaudal_11 = QLabel(self.row_53)
        self.RHAnalisisLabelCaudal_11.setObjectName(u"RHAnalisisLabelCaudal_11")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelCaudal_11.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelCaudal_11.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelCaudal_11.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelCaudal_11.setLineWidth(1)
        self.RHAnalisisLabelCaudal_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_110.addWidget(self.RHAnalisisLabelCaudal_11, 1, 0, 1, 1)

        self.RHAnalisisFieldCaudal_6 = QLineEdit(self.row_53)
        self.RHAnalisisFieldCaudal_6.setObjectName(u"RHAnalisisFieldCaudal_6")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldCaudal_6.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldCaudal_6.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldCaudal_6.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldCaudal_6.setMaximumSize(QSize(150, 16777215))
        self.RHAnalisisFieldCaudal_6.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_110.addWidget(self.RHAnalisisFieldCaudal_6, 1, 1, 1, 1)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.RHCompuertasComboBoxCaudal_2 = QComboBox(self.row_53)
        self.RHCompuertasComboBoxCaudal_2.addItem("")
        self.RHCompuertasComboBoxCaudal_2.addItem("")
        self.RHCompuertasComboBoxCaudal_2.setObjectName(u"RHCompuertasComboBoxCaudal_2")
        sizePolicy11.setHeightForWidth(self.RHCompuertasComboBoxCaudal_2.sizePolicy().hasHeightForWidth())
        self.RHCompuertasComboBoxCaudal_2.setSizePolicy(sizePolicy11)
        self.RHCompuertasComboBoxCaudal_2.setMinimumSize(QSize(150, 36))
        self.RHCompuertasComboBoxCaudal_2.setMaximumSize(QSize(255, 16777215))
        self.RHCompuertasComboBoxCaudal_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHCompuertasComboBoxCaudal_2.setEditable(True)
        self.RHCompuertasComboBoxCaudal_2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_104.addWidget(self.RHCompuertasComboBoxCaudal_2)


        self.gridLayout_110.addLayout(self.horizontalLayout_104, 1, 2, 1, 1)


        self.verticalLayout_73.addLayout(self.gridLayout_110)


        self.gridLayout_109.addWidget(self.row_53, 0, 1, 1, 1)


        self.verticalLayout_31.addWidget(self.groupBox_Propiedades_27)

        self.groupBox_Propiedades_29 = QGroupBox(self.rhProfundidad)
        self.groupBox_Propiedades_29.setObjectName(u"groupBox_Propiedades_29")
        self.groupBox_Propiedades_29.setGeometry(QRect(780, 130, 310, 451))
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_29.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_29.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_29.setMinimumSize(QSize(310, 0))
        self.groupBox_Propiedades_29.setMaximumSize(QSize(310, 16777215))
        self.groupBox_Propiedades_29.setStyleSheet(u"QGroupBox {\n"
"color: rgb(214, 112, 114);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(214, 112, 114);\n"
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
        self.gridLayout_113 = QGridLayout(self.groupBox_Propiedades_29)
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.row_55 = QFrame(self.groupBox_Propiedades_29)
        self.row_55.setObjectName(u"row_55")
        self.row_55.setStyleSheet(u"")
        self.row_55.setFrameShape(QFrame.StyledPanel)
        self.row_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.row_55)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_114 = QGridLayout()
        self.gridLayout_114.setSpacing(10)
        self.gridLayout_114.setObjectName(u"gridLayout_114")
        self.gridLayout_114.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayout_114.setContentsMargins(5, 5, 5, 5)
        self.CEnergiaY2LabelEnergiaCritica = QLabel(self.row_55)
        self.CEnergiaY2LabelEnergiaCritica.setObjectName(u"CEnergiaY2LabelEnergiaCritica")
        sizePolicy16 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.CEnergiaY2LabelEnergiaCritica.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2LabelEnergiaCritica.setSizePolicy(sizePolicy16)
        self.CEnergiaY2LabelEnergiaCritica.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaY2LabelEnergiaCritica.setLineWidth(1)
        self.CEnergiaY2LabelEnergiaCritica.setAlignment(Qt.AlignCenter)

        self.gridLayout_114.addWidget(self.CEnergiaY2LabelEnergiaCritica, 3, 0, 1, 1)

        self.CEnergiaY2LabelProfundidad = QLabel(self.row_55)
        self.CEnergiaY2LabelProfundidad.setObjectName(u"CEnergiaY2LabelProfundidad")
        sizePolicy16.setHeightForWidth(self.CEnergiaY2LabelProfundidad.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2LabelProfundidad.setSizePolicy(sizePolicy16)
        self.CEnergiaY2LabelProfundidad.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaY2LabelProfundidad.setLineWidth(1)
        self.CEnergiaY2LabelProfundidad.setAlignment(Qt.AlignCenter)

        self.gridLayout_114.addWidget(self.CEnergiaY2LabelProfundidad, 0, 0, 1, 1)

        self.CEnergiaY2LabelProfundidad_2 = QLabel(self.row_55)
        self.CEnergiaY2LabelProfundidad_2.setObjectName(u"CEnergiaY2LabelProfundidad_2")
        sizePolicy16.setHeightForWidth(self.CEnergiaY2LabelProfundidad_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2LabelProfundidad_2.setSizePolicy(sizePolicy16)
        self.CEnergiaY2LabelProfundidad_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaY2LabelProfundidad_2.setLineWidth(1)
        self.CEnergiaY2LabelProfundidad_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_114.addWidget(self.CEnergiaY2LabelProfundidad_2, 1, 0, 1, 1)

        self.CEnergiaY2FieldEc = QLineEdit(self.row_55)
        self.CEnergiaY2FieldEc.setObjectName(u"CEnergiaY2FieldEc")
        sizePolicy5.setHeightForWidth(self.CEnergiaY2FieldEc.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2FieldEc.setSizePolicy(sizePolicy5)
        self.CEnergiaY2FieldEc.setMinimumSize(QSize(115, 40))
        self.CEnergiaY2FieldEc.setMaximumSize(QSize(160, 16777215))
        self.CEnergiaY2FieldEc.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_114.addWidget(self.CEnergiaY2FieldEc, 3, 1, 1, 1)

        self.CEnergiaY2FieldYc = QLineEdit(self.row_55)
        self.CEnergiaY2FieldYc.setObjectName(u"CEnergiaY2FieldYc")
        sizePolicy5.setHeightForWidth(self.CEnergiaY2FieldYc.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2FieldYc.setSizePolicy(sizePolicy5)
        self.CEnergiaY2FieldYc.setMinimumSize(QSize(115, 40))
        self.CEnergiaY2FieldYc.setMaximumSize(QSize(160, 16777215))
        self.CEnergiaY2FieldYc.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_114.addWidget(self.CEnergiaY2FieldYc, 2, 1, 1, 1)

        self.CEnergiaY2LabelProfundidadCritica = QLabel(self.row_55)
        self.CEnergiaY2LabelProfundidadCritica.setObjectName(u"CEnergiaY2LabelProfundidadCritica")
        sizePolicy16.setHeightForWidth(self.CEnergiaY2LabelProfundidadCritica.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2LabelProfundidadCritica.setSizePolicy(sizePolicy16)
        self.CEnergiaY2LabelProfundidadCritica.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaY2LabelProfundidadCritica.setLineWidth(1)
        self.CEnergiaY2LabelProfundidadCritica.setAlignment(Qt.AlignCenter)

        self.gridLayout_114.addWidget(self.CEnergiaY2LabelProfundidadCritica, 2, 0, 1, 1)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.CEnergiaY2LabelProfundidadRaiz1 = QLineEdit(self.row_55)
        self.CEnergiaY2LabelProfundidadRaiz1.setObjectName(u"CEnergiaY2LabelProfundidadRaiz1")
        sizePolicy5.setHeightForWidth(self.CEnergiaY2LabelProfundidadRaiz1.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2LabelProfundidadRaiz1.setSizePolicy(sizePolicy5)
        self.CEnergiaY2LabelProfundidadRaiz1.setMinimumSize(QSize(115, 36))
        self.CEnergiaY2LabelProfundidadRaiz1.setMaximumSize(QSize(160, 16777215))
        self.CEnergiaY2LabelProfundidadRaiz1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.verticalLayout_32.addWidget(self.CEnergiaY2LabelProfundidadRaiz1)

        self.CEnergiaY2LabelProfundidadRaiz2 = QLineEdit(self.row_55)
        self.CEnergiaY2LabelProfundidadRaiz2.setObjectName(u"CEnergiaY2LabelProfundidadRaiz2")
        sizePolicy5.setHeightForWidth(self.CEnergiaY2LabelProfundidadRaiz2.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2LabelProfundidadRaiz2.setSizePolicy(sizePolicy5)
        self.CEnergiaY2LabelProfundidadRaiz2.setMinimumSize(QSize(115, 36))
        self.CEnergiaY2LabelProfundidadRaiz2.setMaximumSize(QSize(160, 16777215))
        self.CEnergiaY2LabelProfundidadRaiz2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.verticalLayout_32.addWidget(self.CEnergiaY2LabelProfundidadRaiz2)

        self.CEnergiaY2LabelProfundidadRaiz3 = QLineEdit(self.row_55)
        self.CEnergiaY2LabelProfundidadRaiz3.setObjectName(u"CEnergiaY2LabelProfundidadRaiz3")
        sizePolicy5.setHeightForWidth(self.CEnergiaY2LabelProfundidadRaiz3.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2LabelProfundidadRaiz3.setSizePolicy(sizePolicy5)
        self.CEnergiaY2LabelProfundidadRaiz3.setMinimumSize(QSize(115, 36))
        self.CEnergiaY2LabelProfundidadRaiz3.setMaximumSize(QSize(160, 16777215))
        self.CEnergiaY2LabelProfundidadRaiz3.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.verticalLayout_32.addWidget(self.CEnergiaY2LabelProfundidadRaiz3)


        self.gridLayout_114.addLayout(self.verticalLayout_32, 0, 1, 1, 1)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.CEnergiaY2LabelProfundidadRaiz1_2 = QLineEdit(self.row_55)
        self.CEnergiaY2LabelProfundidadRaiz1_2.setObjectName(u"CEnergiaY2LabelProfundidadRaiz1_2")
        sizePolicy5.setHeightForWidth(self.CEnergiaY2LabelProfundidadRaiz1_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2LabelProfundidadRaiz1_2.setSizePolicy(sizePolicy5)
        self.CEnergiaY2LabelProfundidadRaiz1_2.setMinimumSize(QSize(115, 40))
        self.CEnergiaY2LabelProfundidadRaiz1_2.setMaximumSize(QSize(160, 16777215))
        self.CEnergiaY2LabelProfundidadRaiz1_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.verticalLayout_33.addWidget(self.CEnergiaY2LabelProfundidadRaiz1_2)

        self.CEnergiaY2LabelProfundidadRaiz2_2 = QLineEdit(self.row_55)
        self.CEnergiaY2LabelProfundidadRaiz2_2.setObjectName(u"CEnergiaY2LabelProfundidadRaiz2_2")
        sizePolicy5.setHeightForWidth(self.CEnergiaY2LabelProfundidadRaiz2_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2LabelProfundidadRaiz2_2.setSizePolicy(sizePolicy5)
        self.CEnergiaY2LabelProfundidadRaiz2_2.setMinimumSize(QSize(115, 40))
        self.CEnergiaY2LabelProfundidadRaiz2_2.setMaximumSize(QSize(160, 16777215))
        self.CEnergiaY2LabelProfundidadRaiz2_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.verticalLayout_33.addWidget(self.CEnergiaY2LabelProfundidadRaiz2_2)

        self.CEnergiaY2LabelProfundidadRaiz3_2 = QLineEdit(self.row_55)
        self.CEnergiaY2LabelProfundidadRaiz3_2.setObjectName(u"CEnergiaY2LabelProfundidadRaiz3_2")
        sizePolicy5.setHeightForWidth(self.CEnergiaY2LabelProfundidadRaiz3_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2LabelProfundidadRaiz3_2.setSizePolicy(sizePolicy5)
        self.CEnergiaY2LabelProfundidadRaiz3_2.setMinimumSize(QSize(115, 40))
        self.CEnergiaY2LabelProfundidadRaiz3_2.setMaximumSize(QSize(160, 16777215))
        self.CEnergiaY2LabelProfundidadRaiz3_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.verticalLayout_33.addWidget(self.CEnergiaY2LabelProfundidadRaiz3_2)


        self.gridLayout_114.addLayout(self.verticalLayout_33, 1, 1, 1, 1)

        self.CEnergiaY2LabelEnergiaCritica_2 = QLabel(self.row_55)
        self.CEnergiaY2LabelEnergiaCritica_2.setObjectName(u"CEnergiaY2LabelEnergiaCritica_2")
        sizePolicy6.setHeightForWidth(self.CEnergiaY2LabelEnergiaCritica_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2LabelEnergiaCritica_2.setSizePolicy(sizePolicy6)
        self.CEnergiaY2LabelEnergiaCritica_2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.CEnergiaY2LabelEnergiaCritica_2.setLineWidth(1)
        self.CEnergiaY2LabelEnergiaCritica_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_114.addWidget(self.CEnergiaY2LabelEnergiaCritica_2, 4, 0, 1, 1)

        self.CEnergiaY2FieldEc_2 = QLineEdit(self.row_55)
        self.CEnergiaY2FieldEc_2.setObjectName(u"CEnergiaY2FieldEc_2")
        sizePolicy5.setHeightForWidth(self.CEnergiaY2FieldEc_2.sizePolicy().hasHeightForWidth())
        self.CEnergiaY2FieldEc_2.setSizePolicy(sizePolicy5)
        self.CEnergiaY2FieldEc_2.setMinimumSize(QSize(115, 40))
        self.CEnergiaY2FieldEc_2.setMaximumSize(QSize(160, 16777215))
        self.CEnergiaY2FieldEc_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_114.addWidget(self.CEnergiaY2FieldEc_2, 4, 1, 1, 1)


        self.verticalLayout_75.addLayout(self.gridLayout_114)


        self.gridLayout_113.addWidget(self.row_55, 0, 1, 1, 1)

        self.tabConservacionEnergia.addTab(self.rhProfundidad, "")
        self.stackedWidget.addWidget(self.pagina_conservacionE)
        self.pagina_conservacionM = QWidget()
        self.pagina_conservacionM.setObjectName(u"pagina_conservacionM")
        self.tabResaltosHidraulicos = QTabWidget(self.pagina_conservacionM)
        self.tabResaltosHidraulicos.setObjectName(u"tabResaltosHidraulicos")
        self.tabResaltosHidraulicos.setGeometry(QRect(0, 0, 1121, 613))
        sizePolicy13.setHeightForWidth(self.tabResaltosHidraulicos.sizePolicy().hasHeightForWidth())
        self.tabResaltosHidraulicos.setSizePolicy(sizePolicy13)
        self.tabResaltosHidraulicos.setStyleSheet(u"font: 500 10pt \"Allerta\";\n"
"color: rgb(79, 79, 79);")
        self.tabResaltosHidraulicos.setTabPosition(QTabWidget.West)
        self.rhFuerzaSubsecuente = QWidget()
        self.rhFuerzaSubsecuente.setObjectName(u"rhFuerzaSubsecuente")
        self.rhFuerzaSubsecuente.setStyleSheet(u"\n"
"font: 500 11pt \"Allerta\";")
        self.groupBox_Resultados_17 = QGroupBox(self.rhFuerzaSubsecuente)
        self.groupBox_Resultados_17.setObjectName(u"groupBox_Resultados_17")
        self.groupBox_Resultados_17.setGeometry(QRect(20, 440, 571, 161))
        sizePolicy.setHeightForWidth(self.groupBox_Resultados_17.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_17.setSizePolicy(sizePolicy)
        self.groupBox_Resultados_17.setMinimumSize(QSize(500, 0))
        self.groupBox_Resultados_17.setStyleSheet(u"QGroupBox {\n"
"color: rgb(199, 199, 199);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(199, 199, 199);\n"
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
        self.gridLayout_79 = QGridLayout(self.groupBox_Resultados_17)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.row_38 = QFrame(self.groupBox_Resultados_17)
        self.row_38.setObjectName(u"row_38")
        self.row_38.setStyleSheet(u"")
        self.row_38.setFrameShape(QFrame.StyledPanel)
        self.row_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.row_38)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_80 = QGridLayout()
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.gridLayout_80.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_80.setHorizontalSpacing(10)
        self.gridLayout_80.setVerticalSpacing(15)
        self.gridLayout_80.setContentsMargins(10, 10, 10, 10)
        self.RHAnalisisFieldAltura = QLineEdit(self.row_38)
        self.RHAnalisisFieldAltura.setObjectName(u"RHAnalisisFieldAltura")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldAltura.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldAltura.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldAltura.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldAltura.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_80.addWidget(self.RHAnalisisFieldAltura, 0, 1, 1, 1)

        self.RHAnalisisLabelE1 = QLabel(self.row_38)
        self.RHAnalisisLabelE1.setObjectName(u"RHAnalisisLabelE1")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelE1.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelE1.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelE1.setStyleSheet(u"font: 650 11pt \"Allerta\";\n"
"color: rgb(116, 116, 116);")
        self.RHAnalisisLabelE1.setLineWidth(1)
        self.RHAnalisisLabelE1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_80.addWidget(self.RHAnalisisLabelE1, 1, 0, 1, 1)

        self.RHAnalisisFieldE1 = QLineEdit(self.row_38)
        self.RHAnalisisFieldE1.setObjectName(u"RHAnalisisFieldE1")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldE1.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldE1.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldE1.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldE1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_80.addWidget(self.RHAnalisisFieldE1, 1, 1, 1, 1)

        self.RHAnalisisLabelAltura = QLabel(self.row_38)
        self.RHAnalisisLabelAltura.setObjectName(u"RHAnalisisLabelAltura")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelAltura.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelAltura.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelAltura.setStyleSheet(u"font: 650 11pt \"Allerta\";\n"
"color: rgb(116, 116, 116);")
        self.RHAnalisisLabelAltura.setLineWidth(1)
        self.RHAnalisisLabelAltura.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_80.addWidget(self.RHAnalisisLabelAltura, 0, 0, 1, 1)

        self.RHAnalisisLabelE2 = QLabel(self.row_38)
        self.RHAnalisisLabelE2.setObjectName(u"RHAnalisisLabelE2")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelE2.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelE2.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelE2.setStyleSheet(u"font: 650 11pt \"Allerta\";\n"
"color: rgb(116, 116, 116);")
        self.RHAnalisisLabelE2.setLineWidth(1)
        self.RHAnalisisLabelE2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_80.addWidget(self.RHAnalisisLabelE2, 2, 0, 1, 1)

        self.RHAnalisisFieldE2 = QLineEdit(self.row_38)
        self.RHAnalisisFieldE2.setObjectName(u"RHAnalisisFieldE2")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldE2.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldE2.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldE2.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldE2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_80.addWidget(self.RHAnalisisFieldE2, 2, 1, 1, 1)


        self.verticalLayout_58.addLayout(self.gridLayout_80)


        self.gridLayout_79.addWidget(self.row_38, 0, 0, 1, 1)

        self.groupBox_Propiedades_14 = QGroupBox(self.rhFuerzaSubsecuente)
        self.groupBox_Propiedades_14.setObjectName(u"groupBox_Propiedades_14")
        self.groupBox_Propiedades_14.setGeometry(QRect(20, 10, 790, 231))
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_14.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_14.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_14.setMinimumSize(QSize(790, 0))
        self.groupBox_Propiedades_14.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_14.setStyleSheet(u"QGroupBox {\n"
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
        self.groupBox_Propiedades_14.setAlignment(Qt.AlignCenter)
        self.gridLayout_69 = QGridLayout(self.groupBox_Propiedades_14)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.row_33 = QFrame(self.groupBox_Propiedades_14)
        self.row_33.setObjectName(u"row_33")
        self.row_33.setStyleSheet(u"")
        self.row_33.setFrameShape(QFrame.StyledPanel)
        self.row_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.row_33)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_70 = QGridLayout()
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.gridLayout_70.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_70.setHorizontalSpacing(35)
        self.gridLayout_70.setVerticalSpacing(10)
        self.gridLayout_70.setContentsMargins(10, 10, 20, 10)
        self.RHAnalisisLabelPendienteLateral = QLabel(self.row_33)
        self.RHAnalisisLabelPendienteLateral.setObjectName(u"RHAnalisisLabelPendienteLateral")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelPendienteLateral.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelPendienteLateral.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelPendienteLateral.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelPendienteLateral.setLineWidth(1)
        self.RHAnalisisLabelPendienteLateral.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_70.addWidget(self.RHAnalisisLabelPendienteLateral, 1, 0, 1, 1)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setSizeConstraint(QLayout.SetMinimumSize)
        self.RHAnalisisComboBoxAncho = QComboBox(self.row_33)
        self.RHAnalisisComboBoxAncho.addItem("")
        self.RHAnalisisComboBoxAncho.addItem("")
        self.RHAnalisisComboBoxAncho.addItem("")
        self.RHAnalisisComboBoxAncho.addItem("")
        self.RHAnalisisComboBoxAncho.setObjectName(u"RHAnalisisComboBoxAncho")
        sizePolicy13.setHeightForWidth(self.RHAnalisisComboBoxAncho.sizePolicy().hasHeightForWidth())
        self.RHAnalisisComboBoxAncho.setSizePolicy(sizePolicy13)
        self.RHAnalisisComboBoxAncho.setMinimumSize(QSize(150, 30))
        self.RHAnalisisComboBoxAncho.setMaximumSize(QSize(260, 30))
        self.RHAnalisisComboBoxAncho.setLayoutDirection(Qt.LeftToRight)
        self.RHAnalisisComboBoxAncho.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHAnalisisComboBoxAncho.setEditable(True)
        self.RHAnalisisComboBoxAncho.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHAnalisisComboBoxAncho.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_66.addWidget(self.RHAnalisisComboBoxAncho)


        self.gridLayout_70.addLayout(self.horizontalLayout_66, 0, 2, 1, 1)

        self.RHAnalisisFieldPendienteLateral = QLineEdit(self.row_33)
        self.RHAnalisisFieldPendienteLateral.setObjectName(u"RHAnalisisFieldPendienteLateral")
        sizePolicy15.setHeightForWidth(self.RHAnalisisFieldPendienteLateral.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldPendienteLateral.setSizePolicy(sizePolicy15)
        self.RHAnalisisFieldPendienteLateral.setMinimumSize(QSize(110, 30))
        self.RHAnalisisFieldPendienteLateral.setMaximumSize(QSize(150, 30))
        self.RHAnalisisFieldPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_70.addWidget(self.RHAnalisisFieldPendienteLateral, 1, 1, 1, 1)

        self.RHAnalisisLabelPendienteLateral2 = QLabel(self.row_33)
        self.RHAnalisisLabelPendienteLateral2.setObjectName(u"RHAnalisisLabelPendienteLateral2")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelPendienteLateral2.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelPendienteLateral2.setMinimumSize(QSize(239, 0))
        self.RHAnalisisLabelPendienteLateral2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelPendienteLateral2.setLineWidth(1)
        self.RHAnalisisLabelPendienteLateral2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_70.addWidget(self.RHAnalisisLabelPendienteLateral2, 2, 0, 1, 1)

        self.RHAnalisisFieldCaudal = QLineEdit(self.row_33)
        self.RHAnalisisFieldCaudal.setObjectName(u"RHAnalisisFieldCaudal")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldCaudal.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldCaudal.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldCaudal.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldCaudal.setMaximumSize(QSize(150, 16777215))
        self.RHAnalisisFieldCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_70.addWidget(self.RHAnalisisFieldCaudal, 4, 1, 1, 1)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.RHAnalisisComboBoxCaudal = QComboBox(self.row_33)
        self.RHAnalisisComboBoxCaudal.addItem("")
        self.RHAnalisisComboBoxCaudal.addItem("")
        self.RHAnalisisComboBoxCaudal.setObjectName(u"RHAnalisisComboBoxCaudal")
        sizePolicy5.setHeightForWidth(self.RHAnalisisComboBoxCaudal.sizePolicy().hasHeightForWidth())
        self.RHAnalisisComboBoxCaudal.setSizePolicy(sizePolicy5)
        self.RHAnalisisComboBoxCaudal.setMinimumSize(QSize(150, 30))
        self.RHAnalisisComboBoxCaudal.setMaximumSize(QSize(260, 16777215))
        self.RHAnalisisComboBoxCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHAnalisisComboBoxCaudal.setEditable(True)
        self.RHAnalisisComboBoxCaudal.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_69.addWidget(self.RHAnalisisComboBoxCaudal)


        self.gridLayout_70.addLayout(self.horizontalLayout_69, 4, 2, 1, 1)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.RHAnalisisComboBoxPendienteLateral2 = QComboBox(self.row_33)
        self.RHAnalisisComboBoxPendienteLateral2.addItem("")
        self.RHAnalisisComboBoxPendienteLateral2.addItem("")
        self.RHAnalisisComboBoxPendienteLateral2.addItem("")
        self.RHAnalisisComboBoxPendienteLateral2.setObjectName(u"RHAnalisisComboBoxPendienteLateral2")
        sizePolicy13.setHeightForWidth(self.RHAnalisisComboBoxPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.RHAnalisisComboBoxPendienteLateral2.setSizePolicy(sizePolicy13)
        self.RHAnalisisComboBoxPendienteLateral2.setMinimumSize(QSize(234, 30))
        self.RHAnalisisComboBoxPendienteLateral2.setMaximumSize(QSize(260, 16777215))
        self.RHAnalisisComboBoxPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHAnalisisComboBoxPendienteLateral2.setEditable(True)
        self.RHAnalisisComboBoxPendienteLateral2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_68.addWidget(self.RHAnalisisComboBoxPendienteLateral2)


        self.gridLayout_70.addLayout(self.horizontalLayout_68, 2, 2, 1, 1)

        self.RHAnalisisFieldProfundidad1 = QLineEdit(self.row_33)
        self.RHAnalisisFieldProfundidad1.setObjectName(u"RHAnalisisFieldProfundidad1")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldProfundidad1.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldProfundidad1.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldProfundidad1.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldProfundidad1.setMaximumSize(QSize(150, 16777215))
        self.RHAnalisisFieldProfundidad1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_70.addWidget(self.RHAnalisisFieldProfundidad1, 3, 1, 1, 1)

        self.RHAnalisisLabelBase = QLabel(self.row_33)
        self.RHAnalisisLabelBase.setObjectName(u"RHAnalisisLabelBase")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelBase.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelBase.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelBase.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelBase.setLineWidth(1)
        self.RHAnalisisLabelBase.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_70.addWidget(self.RHAnalisisLabelBase, 0, 0, 1, 1)

        self.RHAnalisisFieldPendienteLateral2 = QLineEdit(self.row_33)
        self.RHAnalisisFieldPendienteLateral2.setObjectName(u"RHAnalisisFieldPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldPendienteLateral2.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldPendienteLateral2.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldPendienteLateral2.setMaximumSize(QSize(150, 16777215))
        self.RHAnalisisFieldPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_70.addWidget(self.RHAnalisisFieldPendienteLateral2, 2, 1, 1, 1)

        self.RHAnalisisLabelProfundidad1 = QLabel(self.row_33)
        self.RHAnalisisLabelProfundidad1.setObjectName(u"RHAnalisisLabelProfundidad1")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelProfundidad1.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelProfundidad1.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelProfundidad1.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelProfundidad1.setLineWidth(1)
        self.RHAnalisisLabelProfundidad1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_70.addWidget(self.RHAnalisisLabelProfundidad1, 3, 0, 1, 1)

        self.RHAnalisisLabelCaudal = QLabel(self.row_33)
        self.RHAnalisisLabelCaudal.setObjectName(u"RHAnalisisLabelCaudal")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelCaudal.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelCaudal.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelCaudal.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelCaudal.setLineWidth(1)
        self.RHAnalisisLabelCaudal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_70.addWidget(self.RHAnalisisLabelCaudal, 4, 0, 1, 1)

        self.RHAnalisisFieldAncho = QLineEdit(self.row_33)
        self.RHAnalisisFieldAncho.setObjectName(u"RHAnalisisFieldAncho")
        sizePolicy15.setHeightForWidth(self.RHAnalisisFieldAncho.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldAncho.setSizePolicy(sizePolicy15)
        self.RHAnalisisFieldAncho.setMinimumSize(QSize(110, 30))
        self.RHAnalisisFieldAncho.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldAncho.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.RHAnalisisFieldAncho.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_70.addWidget(self.RHAnalisisFieldAncho, 0, 1, 1, 1)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setSizeConstraint(QLayout.SetMinimumSize)
        self.RHAnalisisComboBoxPendienteLateral = QComboBox(self.row_33)
        self.RHAnalisisComboBoxPendienteLateral.addItem("")
        self.RHAnalisisComboBoxPendienteLateral.addItem("")
        self.RHAnalisisComboBoxPendienteLateral.addItem("")
        self.RHAnalisisComboBoxPendienteLateral.setObjectName(u"RHAnalisisComboBoxPendienteLateral")
        sizePolicy14.setHeightForWidth(self.RHAnalisisComboBoxPendienteLateral.sizePolicy().hasHeightForWidth())
        self.RHAnalisisComboBoxPendienteLateral.setSizePolicy(sizePolicy14)
        self.RHAnalisisComboBoxPendienteLateral.setMinimumSize(QSize(234, 30))
        self.RHAnalisisComboBoxPendienteLateral.setMaximumSize(QSize(263, 16777215))
        self.RHAnalisisComboBoxPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHAnalisisComboBoxPendienteLateral.setEditable(True)
        self.RHAnalisisComboBoxPendienteLateral.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_62.addWidget(self.RHAnalisisComboBoxPendienteLateral)


        self.gridLayout_70.addLayout(self.horizontalLayout_62, 1, 2, 1, 1)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setSizeConstraint(QLayout.SetMinimumSize)
        self.RHAnalisisComboBoxProfundidad1 = QComboBox(self.row_33)
        self.RHAnalisisComboBoxProfundidad1.addItem("")
        self.RHAnalisisComboBoxProfundidad1.addItem("")
        self.RHAnalisisComboBoxProfundidad1.addItem("")
        self.RHAnalisisComboBoxProfundidad1.addItem("")
        self.RHAnalisisComboBoxProfundidad1.setObjectName(u"RHAnalisisComboBoxProfundidad1")
        sizePolicy13.setHeightForWidth(self.RHAnalisisComboBoxProfundidad1.sizePolicy().hasHeightForWidth())
        self.RHAnalisisComboBoxProfundidad1.setSizePolicy(sizePolicy13)
        self.RHAnalisisComboBoxProfundidad1.setMinimumSize(QSize(150, 30))
        self.RHAnalisisComboBoxProfundidad1.setMaximumSize(QSize(260, 30))
        self.RHAnalisisComboBoxProfundidad1.setLayoutDirection(Qt.LeftToRight)
        self.RHAnalisisComboBoxProfundidad1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHAnalisisComboBoxProfundidad1.setEditable(True)
        self.RHAnalisisComboBoxProfundidad1.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHAnalisisComboBoxProfundidad1.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_67.addWidget(self.RHAnalisisComboBoxProfundidad1)


        self.gridLayout_70.addLayout(self.horizontalLayout_67, 3, 2, 1, 1)


        self.verticalLayout_53.addLayout(self.gridLayout_70)


        self.gridLayout_69.addWidget(self.row_33, 0, 1, 1, 1)

        self.groupBox_Resultados_14 = QGroupBox(self.rhFuerzaSubsecuente)
        self.groupBox_Resultados_14.setObjectName(u"groupBox_Resultados_14")
        self.groupBox_Resultados_14.setGeometry(QRect(590, 440, 480, 161))
        sizePolicy17 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.groupBox_Resultados_14.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_14.setSizePolicy(sizePolicy17)
        self.groupBox_Resultados_14.setMinimumSize(QSize(480, 0))
        self.groupBox_Resultados_14.setMaximumSize(QSize(480, 16777215))
        self.groupBox_Resultados_14.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 190, 167);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
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
        self.gridLayout_71 = QGridLayout(self.groupBox_Resultados_14)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.row_34 = QFrame(self.groupBox_Resultados_14)
        self.row_34.setObjectName(u"row_34")
        self.row_34.setStyleSheet(u"")
        self.row_34.setFrameShape(QFrame.StyledPanel)
        self.row_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.row_34)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_72 = QGridLayout()
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.gridLayout_72.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_72.setHorizontalSpacing(10)
        self.gridLayout_72.setVerticalSpacing(15)
        self.gridLayout_72.setContentsMargins(10, 10, 10, 10)
        self.RHAnalisisFieldEficiencia = QLineEdit(self.row_34)
        self.RHAnalisisFieldEficiencia.setObjectName(u"RHAnalisisFieldEficiencia")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldEficiencia.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldEficiencia.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldEficiencia.setMinimumSize(QSize(0, 40))
        self.RHAnalisisFieldEficiencia.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_72.addWidget(self.RHAnalisisFieldEficiencia, 0, 1, 1, 1)

        self.RHAnalisisLabelEficiencia = QLabel(self.row_34)
        self.RHAnalisisLabelEficiencia.setObjectName(u"RHAnalisisLabelEficiencia")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelEficiencia.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelEficiencia.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelEficiencia.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelEficiencia.setLineWidth(1)
        self.RHAnalisisLabelEficiencia.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_72.addWidget(self.RHAnalisisLabelEficiencia, 0, 0, 1, 1)


        self.verticalLayout_54.addLayout(self.gridLayout_72)


        self.gridLayout_71.addWidget(self.row_34, 0, 0, 1, 1)

        self.groupBox_Propiedades_16 = QGroupBox(self.rhFuerzaSubsecuente)
        self.groupBox_Propiedades_16.setObjectName(u"groupBox_Propiedades_16")
        self.groupBox_Propiedades_16.setGeometry(QRect(20, 240, 1051, 201))
        sizePolicy11.setHeightForWidth(self.groupBox_Propiedades_16.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_16.setSizePolicy(sizePolicy11)
        self.groupBox_Propiedades_16.setMinimumSize(QSize(1051, 0))
        self.groupBox_Propiedades_16.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_16.setStyleSheet(u"QGroupBox {\n"
"color: rgb(163, 160, 159);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-radius: 6px;\n"
"border-color: rgb(163, 160, 159);\n"
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
        self.groupBox_Propiedades_16.setAlignment(Qt.AlignCenter)
        self.gridLayout_84 = QGridLayout(self.groupBox_Propiedades_16)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.row_41 = QFrame(self.groupBox_Propiedades_16)
        self.row_41.setObjectName(u"row_41")
        self.row_41.setStyleSheet(u"")
        self.row_41.setFrameShape(QFrame.StyledPanel)
        self.row_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.row_41)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_85 = QGridLayout()
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.gridLayout_85.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_85.setHorizontalSpacing(35)
        self.gridLayout_85.setVerticalSpacing(10)
        self.gridLayout_85.setContentsMargins(10, 10, 20, 10)
        self.RHAnalisisLabelProfundidad = QLabel(self.row_41)
        self.RHAnalisisLabelProfundidad.setObjectName(u"RHAnalisisLabelProfundidad")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelProfundidad.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelProfundidad.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelProfundidad.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelProfundidad.setLineWidth(1)
        self.RHAnalisisLabelProfundidad.setAlignment(Qt.AlignCenter)

        self.gridLayout_85.addWidget(self.RHAnalisisLabelProfundidad, 1, 0, 1, 1)

        self.RHAnalisisFieldInclinacion = QLineEdit(self.row_41)
        self.RHAnalisisFieldInclinacion.setObjectName(u"RHAnalisisFieldInclinacion")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldInclinacion.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldInclinacion.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldInclinacion.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldInclinacion.setMaximumSize(QSize(150, 16777215))
        self.RHAnalisisFieldInclinacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_85.addWidget(self.RHAnalisisFieldInclinacion, 2, 1, 1, 1)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.RHAnalisisComboBoxInclinacion = QComboBox(self.row_41)
        self.RHAnalisisComboBoxInclinacion.addItem("")
        self.RHAnalisisComboBoxInclinacion.addItem("")
        self.RHAnalisisComboBoxInclinacion.addItem("")
        self.RHAnalisisComboBoxInclinacion.setObjectName(u"RHAnalisisComboBoxInclinacion")
        sizePolicy13.setHeightForWidth(self.RHAnalisisComboBoxInclinacion.sizePolicy().hasHeightForWidth())
        self.RHAnalisisComboBoxInclinacion.setSizePolicy(sizePolicy13)
        self.RHAnalisisComboBoxInclinacion.setMinimumSize(QSize(260, 30))
        self.RHAnalisisComboBoxInclinacion.setMaximumSize(QSize(260, 16777215))
        self.RHAnalisisComboBoxInclinacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHAnalisisComboBoxInclinacion.setEditable(True)
        self.RHAnalisisComboBoxInclinacion.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_84.addWidget(self.RHAnalisisComboBoxInclinacion)


        self.gridLayout_85.addLayout(self.horizontalLayout_84, 2, 2, 1, 1)

        self.RHAnalisisFieldLongitudInclinada = QLineEdit(self.row_41)
        self.RHAnalisisFieldLongitudInclinada.setObjectName(u"RHAnalisisFieldLongitudInclinada")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldLongitudInclinada.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldLongitudInclinada.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldLongitudInclinada.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldLongitudInclinada.setMaximumSize(QSize(150, 16777215))
        self.RHAnalisisFieldLongitudInclinada.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_85.addWidget(self.RHAnalisisFieldLongitudInclinada, 0, 1, 1, 1)

        self.RHAnalisisLabelLongitudInclinada = QLabel(self.row_41)
        self.RHAnalisisLabelLongitudInclinada.setObjectName(u"RHAnalisisLabelLongitudInclinada")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelLongitudInclinada.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelLongitudInclinada.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelLongitudInclinada.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelLongitudInclinada.setLineWidth(1)
        self.RHAnalisisLabelLongitudInclinada.setAlignment(Qt.AlignCenter)

        self.gridLayout_85.addWidget(self.RHAnalisisLabelLongitudInclinada, 0, 0, 1, 1)

        self.RHAnalisisFieldProfundidad = QLineEdit(self.row_41)
        self.RHAnalisisFieldProfundidad.setObjectName(u"RHAnalisisFieldProfundidad")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldProfundidad.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldProfundidad.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldProfundidad.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldProfundidad.setMaximumSize(QSize(150, 16777215))
        self.RHAnalisisFieldProfundidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_85.addWidget(self.RHAnalisisFieldProfundidad, 1, 1, 1, 1)

        self.RHAnalisisLabelInclinacion = QLabel(self.row_41)
        self.RHAnalisisLabelInclinacion.setObjectName(u"RHAnalisisLabelInclinacion")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelInclinacion.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelInclinacion.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelInclinacion.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelInclinacion.setLineWidth(1)
        self.RHAnalisisLabelInclinacion.setAlignment(Qt.AlignCenter)

        self.gridLayout_85.addWidget(self.RHAnalisisLabelInclinacion, 2, 0, 1, 1)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setSizeConstraint(QLayout.SetMinimumSize)
        self.RHAnalisisComboBoxProfundidad = QComboBox(self.row_41)
        self.RHAnalisisComboBoxProfundidad.addItem("")
        self.RHAnalisisComboBoxProfundidad.addItem("")
        self.RHAnalisisComboBoxProfundidad.addItem("")
        self.RHAnalisisComboBoxProfundidad.addItem("")
        self.RHAnalisisComboBoxProfundidad.setObjectName(u"RHAnalisisComboBoxProfundidad")
        sizePolicy11.setHeightForWidth(self.RHAnalisisComboBoxProfundidad.sizePolicy().hasHeightForWidth())
        self.RHAnalisisComboBoxProfundidad.setSizePolicy(sizePolicy11)
        self.RHAnalisisComboBoxProfundidad.setMinimumSize(QSize(150, 30))
        self.RHAnalisisComboBoxProfundidad.setMaximumSize(QSize(260, 30))
        self.RHAnalisisComboBoxProfundidad.setLayoutDirection(Qt.LeftToRight)
        self.RHAnalisisComboBoxProfundidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHAnalisisComboBoxProfundidad.setEditable(True)
        self.RHAnalisisComboBoxProfundidad.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHAnalisisComboBoxProfundidad.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_87.addWidget(self.RHAnalisisComboBoxProfundidad)


        self.gridLayout_85.addLayout(self.horizontalLayout_87, 1, 2, 1, 1)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setSizeConstraint(QLayout.SetMinimumSize)
        self.RHAnalisisComboBoxLongitudInclinada = QComboBox(self.row_41)
        self.RHAnalisisComboBoxLongitudInclinada.addItem("")
        self.RHAnalisisComboBoxLongitudInclinada.addItem("")
        self.RHAnalisisComboBoxLongitudInclinada.addItem("")
        self.RHAnalisisComboBoxLongitudInclinada.addItem("")
        self.RHAnalisisComboBoxLongitudInclinada.setObjectName(u"RHAnalisisComboBoxLongitudInclinada")
        sizePolicy11.setHeightForWidth(self.RHAnalisisComboBoxLongitudInclinada.sizePolicy().hasHeightForWidth())
        self.RHAnalisisComboBoxLongitudInclinada.setSizePolicy(sizePolicy11)
        self.RHAnalisisComboBoxLongitudInclinada.setMinimumSize(QSize(150, 30))
        self.RHAnalisisComboBoxLongitudInclinada.setMaximumSize(QSize(260, 30))
        self.RHAnalisisComboBoxLongitudInclinada.setLayoutDirection(Qt.LeftToRight)
        self.RHAnalisisComboBoxLongitudInclinada.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHAnalisisComboBoxLongitudInclinada.setEditable(True)
        self.RHAnalisisComboBoxLongitudInclinada.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHAnalisisComboBoxLongitudInclinada.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_83.addWidget(self.RHAnalisisComboBoxLongitudInclinada)


        self.gridLayout_85.addLayout(self.horizontalLayout_83, 0, 2, 1, 1)

        self.RHAnalisisLabelFuerza = QLabel(self.row_41)
        self.RHAnalisisLabelFuerza.setObjectName(u"RHAnalisisLabelFuerza")
        sizePolicy6.setHeightForWidth(self.RHAnalisisLabelFuerza.sizePolicy().hasHeightForWidth())
        self.RHAnalisisLabelFuerza.setSizePolicy(sizePolicy6)
        self.RHAnalisisLabelFuerza.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHAnalisisLabelFuerza.setLineWidth(1)
        self.RHAnalisisLabelFuerza.setAlignment(Qt.AlignCenter)

        self.gridLayout_85.addWidget(self.RHAnalisisLabelFuerza, 3, 0, 1, 1)

        self.RHAnalisisFieldFuerza = QLineEdit(self.row_41)
        self.RHAnalisisFieldFuerza.setObjectName(u"RHAnalisisFieldFuerza")
        sizePolicy5.setHeightForWidth(self.RHAnalisisFieldFuerza.sizePolicy().hasHeightForWidth())
        self.RHAnalisisFieldFuerza.setSizePolicy(sizePolicy5)
        self.RHAnalisisFieldFuerza.setMinimumSize(QSize(0, 30))
        self.RHAnalisisFieldFuerza.setMaximumSize(QSize(150, 16777215))
        self.RHAnalisisFieldFuerza.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_85.addWidget(self.RHAnalisisFieldFuerza, 3, 1, 1, 1)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setSizeConstraint(QLayout.SetMinimumSize)
        self.RHAnalisisComboBoxFuerza = QComboBox(self.row_41)
        self.RHAnalisisComboBoxFuerza.addItem("")
        self.RHAnalisisComboBoxFuerza.setObjectName(u"RHAnalisisComboBoxFuerza")
        sizePolicy13.setHeightForWidth(self.RHAnalisisComboBoxFuerza.sizePolicy().hasHeightForWidth())
        self.RHAnalisisComboBoxFuerza.setSizePolicy(sizePolicy13)
        self.RHAnalisisComboBoxFuerza.setMinimumSize(QSize(150, 30))
        self.RHAnalisisComboBoxFuerza.setMaximumSize(QSize(260, 30))
        self.RHAnalisisComboBoxFuerza.setLayoutDirection(Qt.LeftToRight)
        self.RHAnalisisComboBoxFuerza.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHAnalisisComboBoxFuerza.setEditable(True)
        self.RHAnalisisComboBoxFuerza.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHAnalisisComboBoxFuerza.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_70.addWidget(self.RHAnalisisComboBoxFuerza)


        self.gridLayout_85.addLayout(self.horizontalLayout_70, 3, 2, 1, 1)


        self.verticalLayout_61.addLayout(self.gridLayout_85)


        self.gridLayout_84.addWidget(self.row_41, 0, 1, 1, 1)

        self.gridLayoutWidget = QWidget(self.rhFuerzaSubsecuente)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(840, 30, 221, 171))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(10)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.RHAnalisisTextoReiniciar = QLabel(self.gridLayoutWidget)
        self.RHAnalisisTextoReiniciar.setObjectName(u"RHAnalisisTextoReiniciar")
        sizePolicy5.setHeightForWidth(self.RHAnalisisTextoReiniciar.sizePolicy().hasHeightForWidth())
        self.RHAnalisisTextoReiniciar.setSizePolicy(sizePolicy5)
        self.RHAnalisisTextoReiniciar.setStyleSheet(u"color: rgb(84, 84, 84);\n"
"font: 500 12pt \"Allerta\";")
        self.RHAnalisisTextoReiniciar.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.RHAnalisisTextoReiniciar, 2, 1, 1, 1)

        self.RHAnalisisTextoCalcular = QLabel(self.gridLayoutWidget)
        self.RHAnalisisTextoCalcular.setObjectName(u"RHAnalisisTextoCalcular")
        sizePolicy5.setHeightForWidth(self.RHAnalisisTextoCalcular.sizePolicy().hasHeightForWidth())
        self.RHAnalisisTextoCalcular.setSizePolicy(sizePolicy5)
        self.RHAnalisisTextoCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"")
        self.RHAnalisisTextoCalcular.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.RHAnalisisTextoCalcular, 2, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.RHAnalisisBotonCalcular = QPushButton(self.gridLayoutWidget)
        self.RHAnalisisBotonCalcular.setObjectName(u"RHAnalisisBotonCalcular")
        self.RHAnalisisBotonCalcular.setMinimumSize(QSize(50, 50))
        self.RHAnalisisBotonCalcular.setMaximumSize(QSize(40, 40))
        self.RHAnalisisBotonCalcular.setStyleSheet(u"background-color: rgb(250, 190, 167);\n"
"border-color: rgb(250, 190, 167);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_16.addWidget(self.RHAnalisisBotonCalcular)


        self.gridLayout_8.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.RHAnalisisBotonReiniciar = QPushButton(self.gridLayoutWidget)
        self.RHAnalisisBotonReiniciar.setObjectName(u"RHAnalisisBotonReiniciar")
        self.RHAnalisisBotonReiniciar.setMinimumSize(QSize(50, 50))
        self.RHAnalisisBotonReiniciar.setMaximumSize(QSize(40, 40))
        self.RHAnalisisBotonReiniciar.setStyleSheet(u"background-color: rgb(250, 190, 167);\n"
"border-color: rgb(250, 190, 167);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_18.addWidget(self.RHAnalisisBotonReiniciar)


        self.gridLayout_8.addLayout(self.horizontalLayout_18, 0, 1, 1, 1)

        self.gridLayout_8.setColumnStretch(0, 10)
        self.gridLayout_8.setColumnStretch(1, 10)
        self.gridLayout_8.setRowMinimumHeight(0, 10)
        self.gridLayout_8.setRowMinimumHeight(1, 10)
        self.tabResaltosHidraulicos.addTab(self.rhFuerzaSubsecuente, "")
        self.rhPropiedades = QWidget()
        self.rhPropiedades.setObjectName(u"rhPropiedades")
        self.rhPropiedades.setStyleSheet(u"font: 500 11pt \"Allerta\";")
        self.groupBox_Resultados_11 = QGroupBox(self.rhPropiedades)
        self.groupBox_Resultados_11.setObjectName(u"groupBox_Resultados_11")
        self.groupBox_Resultados_11.setGeometry(QRect(590, 410, 480, 181))
        sizePolicy17.setHeightForWidth(self.groupBox_Resultados_11.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_11.setSizePolicy(sizePolicy17)
        self.groupBox_Resultados_11.setMinimumSize(QSize(480, 0))
        self.groupBox_Resultados_11.setMaximumSize(QSize(480, 16777215))
        self.groupBox_Resultados_11.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 190, 167);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
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
        self.gridLayout_56 = QGridLayout(self.groupBox_Resultados_11)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.row_27 = QFrame(self.groupBox_Resultados_11)
        self.row_27.setObjectName(u"row_27")
        self.row_27.setStyleSheet(u"")
        self.row_27.setFrameShape(QFrame.StyledPanel)
        self.row_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.row_27)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_57 = QGridLayout()
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_57.setHorizontalSpacing(10)
        self.gridLayout_57.setVerticalSpacing(30)
        self.gridLayout_57.setContentsMargins(10, 10, 10, 10)
        self.RHPropiedadesLabelClasificacion = QLabel(self.row_27)
        self.RHPropiedadesLabelClasificacion.setObjectName(u"RHPropiedadesLabelClasificacion")
        sizePolicy6.setHeightForWidth(self.RHPropiedadesLabelClasificacion.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesLabelClasificacion.setSizePolicy(sizePolicy6)
        self.RHPropiedadesLabelClasificacion.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHPropiedadesLabelClasificacion.setLineWidth(1)
        self.RHPropiedadesLabelClasificacion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_57.addWidget(self.RHPropiedadesLabelClasificacion, 0, 0, 1, 1)

        self.RHPropiedadesFieldClasificacion = QLineEdit(self.row_27)
        self.RHPropiedadesFieldClasificacion.setObjectName(u"RHPropiedadesFieldClasificacion")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesFieldClasificacion.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesFieldClasificacion.setSizePolicy(sizePolicy5)
        self.RHPropiedadesFieldClasificacion.setMinimumSize(QSize(0, 30))
        self.RHPropiedadesFieldClasificacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_57.addWidget(self.RHPropiedadesFieldClasificacion, 0, 1, 1, 1)

        self.RHPropiedadesFieldLongitud = QLineEdit(self.row_27)
        self.RHPropiedadesFieldLongitud.setObjectName(u"RHPropiedadesFieldLongitud")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesFieldLongitud.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesFieldLongitud.setSizePolicy(sizePolicy5)
        self.RHPropiedadesFieldLongitud.setMinimumSize(QSize(0, 30))
        self.RHPropiedadesFieldLongitud.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_57.addWidget(self.RHPropiedadesFieldLongitud, 1, 1, 1, 1)

        self.RHPropiedadesLabelLongitud = QLabel(self.row_27)
        self.RHPropiedadesLabelLongitud.setObjectName(u"RHPropiedadesLabelLongitud")
        sizePolicy6.setHeightForWidth(self.RHPropiedadesLabelLongitud.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesLabelLongitud.setSizePolicy(sizePolicy6)
        self.RHPropiedadesLabelLongitud.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHPropiedadesLabelLongitud.setLineWidth(1)
        self.RHPropiedadesLabelLongitud.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_57.addWidget(self.RHPropiedadesLabelLongitud, 1, 0, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_57)


        self.gridLayout_56.addWidget(self.row_27, 0, 0, 1, 1)

        self.groupBox_Propiedades_11 = QGroupBox(self.rhPropiedades)
        self.groupBox_Propiedades_11.setObjectName(u"groupBox_Propiedades_11")
        self.groupBox_Propiedades_11.setGeometry(QRect(20, 10, 1051, 391))
        sizePolicy11.setHeightForWidth(self.groupBox_Propiedades_11.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_11.setSizePolicy(sizePolicy11)
        self.groupBox_Propiedades_11.setMinimumSize(QSize(1051, 0))
        self.groupBox_Propiedades_11.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_11.setStyleSheet(u"QGroupBox {\n"
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
        self.groupBox_Propiedades_11.setAlignment(Qt.AlignCenter)
        self.gridLayout_58 = QGridLayout(self.groupBox_Propiedades_11)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.row_28 = QFrame(self.groupBox_Propiedades_11)
        self.row_28.setObjectName(u"row_28")
        self.row_28.setStyleSheet(u"")
        self.row_28.setFrameShape(QFrame.StyledPanel)
        self.row_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.row_28)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_59 = QGridLayout()
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_59.setHorizontalSpacing(35)
        self.gridLayout_59.setVerticalSpacing(10)
        self.gridLayout_59.setContentsMargins(10, 10, 20, 10)
        self.RHPropiedadesFieldPendienteLateral = QLineEdit(self.row_28)
        self.RHPropiedadesFieldPendienteLateral.setObjectName(u"RHPropiedadesFieldPendienteLateral")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesFieldPendienteLateral.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesFieldPendienteLateral.setSizePolicy(sizePolicy5)
        self.RHPropiedadesFieldPendienteLateral.setMinimumSize(QSize(0, 30))
        self.RHPropiedadesFieldPendienteLateral.setMaximumSize(QSize(150, 16777215))
        self.RHPropiedadesFieldPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_59.addWidget(self.RHPropiedadesFieldPendienteLateral, 2, 1, 1, 1)

        self.RHPropiedadesLabelBase = QLabel(self.row_28)
        self.RHPropiedadesLabelBase.setObjectName(u"RHPropiedadesLabelBase")
        sizePolicy6.setHeightForWidth(self.RHPropiedadesLabelBase.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesLabelBase.setSizePolicy(sizePolicy6)
        self.RHPropiedadesLabelBase.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHPropiedadesLabelBase.setLineWidth(1)
        self.RHPropiedadesLabelBase.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_59.addWidget(self.RHPropiedadesLabelBase, 0, 0, 1, 1)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.RHPropiedadesComboBoxDiametro = QComboBox(self.row_28)
        self.RHPropiedadesComboBoxDiametro.addItem("")
        self.RHPropiedadesComboBoxDiametro.addItem("")
        self.RHPropiedadesComboBoxDiametro.addItem("")
        self.RHPropiedadesComboBoxDiametro.addItem("")
        self.RHPropiedadesComboBoxDiametro.setObjectName(u"RHPropiedadesComboBoxDiametro")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesComboBoxDiametro.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesComboBoxDiametro.setSizePolicy(sizePolicy5)
        self.RHPropiedadesComboBoxDiametro.setMinimumSize(QSize(260, 30))
        self.RHPropiedadesComboBoxDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHPropiedadesComboBoxDiametro.setEditable(True)
        self.RHPropiedadesComboBoxDiametro.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_54.addWidget(self.RHPropiedadesComboBoxDiametro)


        self.gridLayout_59.addLayout(self.horizontalLayout_54, 5, 2, 1, 1)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.RHPropiedadesComboBoxPendienteLateral = QComboBox(self.row_28)
        self.RHPropiedadesComboBoxPendienteLateral.addItem("")
        self.RHPropiedadesComboBoxPendienteLateral.addItem("")
        self.RHPropiedadesComboBoxPendienteLateral.addItem("")
        self.RHPropiedadesComboBoxPendienteLateral.setObjectName(u"RHPropiedadesComboBoxPendienteLateral")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesComboBoxPendienteLateral.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesComboBoxPendienteLateral.setSizePolicy(sizePolicy5)
        self.RHPropiedadesComboBoxPendienteLateral.setMinimumSize(QSize(260, 30))
        self.RHPropiedadesComboBoxPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHPropiedadesComboBoxPendienteLateral.setEditable(True)
        self.RHPropiedadesComboBoxPendienteLateral.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_53.addWidget(self.RHPropiedadesComboBoxPendienteLateral)


        self.gridLayout_59.addLayout(self.horizontalLayout_53, 2, 2, 1, 1)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.RHPropiedadesComboBoxPendientaLateral2 = QComboBox(self.row_28)
        self.RHPropiedadesComboBoxPendientaLateral2.addItem("")
        self.RHPropiedadesComboBoxPendientaLateral2.addItem("")
        self.RHPropiedadesComboBoxPendientaLateral2.addItem("")
        self.RHPropiedadesComboBoxPendientaLateral2.setObjectName(u"RHPropiedadesComboBoxPendientaLateral2")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesComboBoxPendientaLateral2.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesComboBoxPendientaLateral2.setSizePolicy(sizePolicy5)
        self.RHPropiedadesComboBoxPendientaLateral2.setMinimumSize(QSize(260, 30))
        self.RHPropiedadesComboBoxPendientaLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHPropiedadesComboBoxPendientaLateral2.setEditable(True)
        self.RHPropiedadesComboBoxPendientaLateral2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_59.addWidget(self.RHPropiedadesComboBoxPendientaLateral2)


        self.gridLayout_59.addLayout(self.horizontalLayout_59, 3, 2, 1, 1)

        self.RHPropiedadesFieldProfundidad = QLineEdit(self.row_28)
        self.RHPropiedadesFieldProfundidad.setObjectName(u"RHPropiedadesFieldProfundidad")
        sizePolicy15.setHeightForWidth(self.RHPropiedadesFieldProfundidad.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesFieldProfundidad.setSizePolicy(sizePolicy15)
        self.RHPropiedadesFieldProfundidad.setMinimumSize(QSize(110, 30))
        self.RHPropiedadesFieldProfundidad.setMaximumSize(QSize(150, 30))
        self.RHPropiedadesFieldProfundidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_59.addWidget(self.RHPropiedadesFieldProfundidad, 1, 1, 1, 1)

        self.RHPropiedadesLabelProfundidad = QLabel(self.row_28)
        self.RHPropiedadesLabelProfundidad.setObjectName(u"RHPropiedadesLabelProfundidad")
        sizePolicy6.setHeightForWidth(self.RHPropiedadesLabelProfundidad.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesLabelProfundidad.setSizePolicy(sizePolicy6)
        self.RHPropiedadesLabelProfundidad.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHPropiedadesLabelProfundidad.setLineWidth(1)
        self.RHPropiedadesLabelProfundidad.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_59.addWidget(self.RHPropiedadesLabelProfundidad, 1, 0, 1, 1)

        self.RHPropiedadesFieldDiametro = QLineEdit(self.row_28)
        self.RHPropiedadesFieldDiametro.setObjectName(u"RHPropiedadesFieldDiametro")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesFieldDiametro.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesFieldDiametro.setSizePolicy(sizePolicy5)
        self.RHPropiedadesFieldDiametro.setMinimumSize(QSize(0, 30))
        self.RHPropiedadesFieldDiametro.setMaximumSize(QSize(150, 16777215))
        self.RHPropiedadesFieldDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_59.addWidget(self.RHPropiedadesFieldDiametro, 5, 1, 1, 1)

        self.RHPropiedadesLabelDiametro = QLabel(self.row_28)
        self.RHPropiedadesLabelDiametro.setObjectName(u"RHPropiedadesLabelDiametro")
        sizePolicy6.setHeightForWidth(self.RHPropiedadesLabelDiametro.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesLabelDiametro.setSizePolicy(sizePolicy6)
        self.RHPropiedadesLabelDiametro.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHPropiedadesLabelDiametro.setLineWidth(1)
        self.RHPropiedadesLabelDiametro.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.RHPropiedadesLabelDiametro, 5, 0, 1, 1)

        self.RHPropiedadesFieldCaudal = QLineEdit(self.row_28)
        self.RHPropiedadesFieldCaudal.setObjectName(u"RHPropiedadesFieldCaudal")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesFieldCaudal.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesFieldCaudal.setSizePolicy(sizePolicy5)
        self.RHPropiedadesFieldCaudal.setMinimumSize(QSize(0, 30))
        self.RHPropiedadesFieldCaudal.setMaximumSize(QSize(150, 16777215))
        self.RHPropiedadesFieldCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_59.addWidget(self.RHPropiedadesFieldCaudal, 4, 1, 1, 1)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setSizeConstraint(QLayout.SetMinimumSize)
        self.RHPropiedadesComboBoxProfundidad = QComboBox(self.row_28)
        self.RHPropiedadesComboBoxProfundidad.addItem("")
        self.RHPropiedadesComboBoxProfundidad.addItem("")
        self.RHPropiedadesComboBoxProfundidad.addItem("")
        self.RHPropiedadesComboBoxProfundidad.addItem("")
        self.RHPropiedadesComboBoxProfundidad.setObjectName(u"RHPropiedadesComboBoxProfundidad")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesComboBoxProfundidad.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesComboBoxProfundidad.setSizePolicy(sizePolicy5)
        self.RHPropiedadesComboBoxProfundidad.setMinimumSize(QSize(150, 36))
        self.RHPropiedadesComboBoxProfundidad.setMaximumSize(QSize(260, 30))
        self.RHPropiedadesComboBoxProfundidad.setLayoutDirection(Qt.LeftToRight)
        self.RHPropiedadesComboBoxProfundidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHPropiedadesComboBoxProfundidad.setEditable(True)
        self.RHPropiedadesComboBoxProfundidad.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHPropiedadesComboBoxProfundidad.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_48.addWidget(self.RHPropiedadesComboBoxProfundidad)


        self.gridLayout_59.addLayout(self.horizontalLayout_48, 1, 2, 1, 1)

        self.RHPropiedadesLabelPendienteLateral2 = QLabel(self.row_28)
        self.RHPropiedadesLabelPendienteLateral2.setObjectName(u"RHPropiedadesLabelPendienteLateral2")
        sizePolicy6.setHeightForWidth(self.RHPropiedadesLabelPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesLabelPendienteLateral2.setSizePolicy(sizePolicy6)
        self.RHPropiedadesLabelPendienteLateral2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHPropiedadesLabelPendienteLateral2.setLineWidth(1)
        self.RHPropiedadesLabelPendienteLateral2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_59.addWidget(self.RHPropiedadesLabelPendienteLateral2, 3, 0, 1, 1)

        self.RHPropiedadesLabelPendienteLateral = QLabel(self.row_28)
        self.RHPropiedadesLabelPendienteLateral.setObjectName(u"RHPropiedadesLabelPendienteLateral")
        sizePolicy6.setHeightForWidth(self.RHPropiedadesLabelPendienteLateral.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesLabelPendienteLateral.setSizePolicy(sizePolicy6)
        self.RHPropiedadesLabelPendienteLateral.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHPropiedadesLabelPendienteLateral.setLineWidth(1)
        self.RHPropiedadesLabelPendienteLateral.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_59.addWidget(self.RHPropiedadesLabelPendienteLateral, 2, 0, 1, 1)

        self.RHPropiedadesFieldPendienteLateral2 = QLineEdit(self.row_28)
        self.RHPropiedadesFieldPendienteLateral2.setObjectName(u"RHPropiedadesFieldPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesFieldPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesFieldPendienteLateral2.setSizePolicy(sizePolicy5)
        self.RHPropiedadesFieldPendienteLateral2.setMinimumSize(QSize(0, 30))
        self.RHPropiedadesFieldPendienteLateral2.setMaximumSize(QSize(150, 16777215))
        self.RHPropiedadesFieldPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_59.addWidget(self.RHPropiedadesFieldPendienteLateral2, 3, 1, 1, 1)

        self.RHPropiedadesLabelCaudal = QLabel(self.row_28)
        self.RHPropiedadesLabelCaudal.setObjectName(u"RHPropiedadesLabelCaudal")
        sizePolicy6.setHeightForWidth(self.RHPropiedadesLabelCaudal.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesLabelCaudal.setSizePolicy(sizePolicy6)
        self.RHPropiedadesLabelCaudal.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHPropiedadesLabelCaudal.setLineWidth(1)
        self.RHPropiedadesLabelCaudal.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.RHPropiedadesLabelCaudal, 4, 0, 1, 1)

        self.RHPropiedadesFieldBase = QLineEdit(self.row_28)
        self.RHPropiedadesFieldBase.setObjectName(u"RHPropiedadesFieldBase")
        sizePolicy15.setHeightForWidth(self.RHPropiedadesFieldBase.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesFieldBase.setSizePolicy(sizePolicy15)
        self.RHPropiedadesFieldBase.setMinimumSize(QSize(110, 30))
        self.RHPropiedadesFieldBase.setMaximumSize(QSize(150, 30))
        self.RHPropiedadesFieldBase.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_59.addWidget(self.RHPropiedadesFieldBase, 0, 1, 1, 1)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.RHPropiedadesComboBoxCaudal = QComboBox(self.row_28)
        self.RHPropiedadesComboBoxCaudal.addItem("")
        self.RHPropiedadesComboBoxCaudal.addItem("")
        self.RHPropiedadesComboBoxCaudal.setObjectName(u"RHPropiedadesComboBoxCaudal")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesComboBoxCaudal.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesComboBoxCaudal.setSizePolicy(sizePolicy5)
        self.RHPropiedadesComboBoxCaudal.setMinimumSize(QSize(150, 36))
        self.RHPropiedadesComboBoxCaudal.setMaximumSize(QSize(260, 16777215))
        self.RHPropiedadesComboBoxCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHPropiedadesComboBoxCaudal.setEditable(True)
        self.RHPropiedadesComboBoxCaudal.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_50.addWidget(self.RHPropiedadesComboBoxCaudal)


        self.gridLayout_59.addLayout(self.horizontalLayout_50, 4, 2, 1, 1)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setSizeConstraint(QLayout.SetMinimumSize)
        self.RHPropiedadesComboBoxBase = QComboBox(self.row_28)
        self.RHPropiedadesComboBoxBase.addItem("")
        self.RHPropiedadesComboBoxBase.addItem("")
        self.RHPropiedadesComboBoxBase.addItem("")
        self.RHPropiedadesComboBoxBase.addItem("")
        self.RHPropiedadesComboBoxBase.setObjectName(u"RHPropiedadesComboBoxBase")
        sizePolicy11.setHeightForWidth(self.RHPropiedadesComboBoxBase.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesComboBoxBase.setSizePolicy(sizePolicy11)
        self.RHPropiedadesComboBoxBase.setMinimumSize(QSize(150, 36))
        self.RHPropiedadesComboBoxBase.setMaximumSize(QSize(260, 30))
        self.RHPropiedadesComboBoxBase.setLayoutDirection(Qt.LeftToRight)
        self.RHPropiedadesComboBoxBase.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHPropiedadesComboBoxBase.setEditable(True)
        self.RHPropiedadesComboBoxBase.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHPropiedadesComboBoxBase.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)

        self.horizontalLayout_49.addWidget(self.RHPropiedadesComboBoxBase)


        self.gridLayout_59.addLayout(self.horizontalLayout_49, 0, 2, 1, 1)


        self.verticalLayout_48.addLayout(self.gridLayout_59)


        self.gridLayout_58.addWidget(self.row_28, 0, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, -1, 10, -1)
        self.geoCImagenCanal_8 = QPushButton(self.groupBox_Propiedades_11)
        self.geoCImagenCanal_8.setObjectName(u"geoCImagenCanal_8")
        self.geoCImagenCanal_8.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.geoCImagenCanal_8.sizePolicy().hasHeightForWidth())
        self.geoCImagenCanal_8.setSizePolicy(sizePolicy5)
        self.geoCImagenCanal_8.setMinimumSize(QSize(260, 213))
        self.geoCImagenCanal_8.setStyleSheet(u"border-image: url(:/geometria/images/geometria/Geometria-rectangular.PNG);\n"
"background-color: rgb(255,255,255);")
        self.geoCImagenCanal_8.setFlat(True)

        self.verticalLayout_22.addWidget(self.geoCImagenCanal_8)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setSpacing(70)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, -1)
        self.RHPropiedadesBotonCalcular = QPushButton(self.groupBox_Propiedades_11)
        self.RHPropiedadesBotonCalcular.setObjectName(u"RHPropiedadesBotonCalcular")
        self.RHPropiedadesBotonCalcular.setMinimumSize(QSize(50, 50))
        self.RHPropiedadesBotonCalcular.setMaximumSize(QSize(40, 40))
        self.RHPropiedadesBotonCalcular.setStyleSheet(u"background-color: rgb(250, 190, 167);\n"
"border-color: rgb(250, 190, 167);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_55.addWidget(self.RHPropiedadesBotonCalcular)

        self.RHPropiedadesBotonReiniciar = QPushButton(self.groupBox_Propiedades_11)
        self.RHPropiedadesBotonReiniciar.setObjectName(u"RHPropiedadesBotonReiniciar")
        self.RHPropiedadesBotonReiniciar.setMinimumSize(QSize(50, 50))
        self.RHPropiedadesBotonReiniciar.setMaximumSize(QSize(40, 40))
        self.RHPropiedadesBotonReiniciar.setStyleSheet(u"background-color: rgb(250, 190, 167);\n"
"border-color: rgb(250, 190, 167);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_55.addWidget(self.RHPropiedadesBotonReiniciar)


        self.verticalLayout_22.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setSpacing(70)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_56.setContentsMargins(10, 0, 10, -1)
        self.RHPropiedadesTextoCalcular = QLabel(self.groupBox_Propiedades_11)
        self.RHPropiedadesTextoCalcular.setObjectName(u"RHPropiedadesTextoCalcular")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesTextoCalcular.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesTextoCalcular.setSizePolicy(sizePolicy5)
        self.RHPropiedadesTextoCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"")
        self.RHPropiedadesTextoCalcular.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.RHPropiedadesTextoCalcular)

        self.RHPropiedadesTextoReiniciar = QLabel(self.groupBox_Propiedades_11)
        self.RHPropiedadesTextoReiniciar.setObjectName(u"RHPropiedadesTextoReiniciar")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesTextoReiniciar.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesTextoReiniciar.setSizePolicy(sizePolicy5)
        self.RHPropiedadesTextoReiniciar.setStyleSheet(u"color: rgb(84, 84, 84);\n"
"font: 500 12pt \"Allerta\";")
        self.RHPropiedadesTextoReiniciar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.RHPropiedadesTextoReiniciar)


        self.verticalLayout_22.addLayout(self.horizontalLayout_56)


        self.horizontalLayout_10.addLayout(self.verticalLayout_22)


        self.gridLayout_58.addLayout(self.horizontalLayout_10, 0, 2, 1, 2)

        self.groupBox_Resultados_15 = QGroupBox(self.rhPropiedades)
        self.groupBox_Resultados_15.setObjectName(u"groupBox_Resultados_15")
        self.groupBox_Resultados_15.setGeometry(QRect(20, 410, 571, 181))
        sizePolicy.setHeightForWidth(self.groupBox_Resultados_15.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_15.setSizePolicy(sizePolicy)
        self.groupBox_Resultados_15.setMinimumSize(QSize(500, 0))
        self.groupBox_Resultados_15.setStyleSheet(u"QGroupBox {\n"
"color: rgb(199, 199, 199);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(199, 199, 199);\n"
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
        self.gridLayout_75 = QGridLayout(self.groupBox_Resultados_15)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.row_36 = QFrame(self.groupBox_Resultados_15)
        self.row_36.setObjectName(u"row_36")
        self.row_36.setStyleSheet(u"")
        self.row_36.setFrameShape(QFrame.StyledPanel)
        self.row_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.row_36)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_76 = QGridLayout()
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.gridLayout_76.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_76.setHorizontalSpacing(10)
        self.gridLayout_76.setVerticalSpacing(15)
        self.gridLayout_76.setContentsMargins(10, 10, 10, 10)
        self.RHPropiedadesLabelFroude = QLabel(self.row_36)
        self.RHPropiedadesLabelFroude.setObjectName(u"RHPropiedadesLabelFroude")
        sizePolicy6.setHeightForWidth(self.RHPropiedadesLabelFroude.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesLabelFroude.setSizePolicy(sizePolicy6)
        self.RHPropiedadesLabelFroude.setStyleSheet(u"font: 650 11pt \"Allerta\";\n"
"color: rgb(116, 116, 116);")
        self.RHPropiedadesLabelFroude.setLineWidth(1)
        self.RHPropiedadesLabelFroude.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_76.addWidget(self.RHPropiedadesLabelFroude, 0, 0, 1, 1)

        self.RHPropiedadesFieldFroude = QLineEdit(self.row_36)
        self.RHPropiedadesFieldFroude.setObjectName(u"RHPropiedadesFieldFroude")
        sizePolicy5.setHeightForWidth(self.RHPropiedadesFieldFroude.sizePolicy().hasHeightForWidth())
        self.RHPropiedadesFieldFroude.setSizePolicy(sizePolicy5)
        self.RHPropiedadesFieldFroude.setMinimumSize(QSize(0, 40))
        self.RHPropiedadesFieldFroude.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_76.addWidget(self.RHPropiedadesFieldFroude, 0, 1, 1, 1)


        self.verticalLayout_56.addLayout(self.gridLayout_76)


        self.gridLayout_75.addWidget(self.row_36, 0, 0, 1, 1)

        self.tabResaltosHidraulicos.addTab(self.rhPropiedades, "")
        self.rhTipo = QWidget()
        self.rhTipo.setObjectName(u"rhTipo")
        self.rhTipo.setStyleSheet(u"font: 500 11pt \"Allerta\";")
        self.groupBox_Propiedades_13 = QGroupBox(self.rhTipo)
        self.groupBox_Propiedades_13.setObjectName(u"groupBox_Propiedades_13")
        self.groupBox_Propiedades_13.setGeometry(QRect(20, 10, 850, 391))
        sizePolicy11.setHeightForWidth(self.groupBox_Propiedades_13.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_13.setSizePolicy(sizePolicy11)
        self.groupBox_Propiedades_13.setMinimumSize(QSize(850, 0))
        self.groupBox_Propiedades_13.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_13.setStyleSheet(u"QGroupBox {\n"
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
        self.groupBox_Propiedades_13.setAlignment(Qt.AlignCenter)
        self.gridLayout_65 = QGridLayout(self.groupBox_Propiedades_13)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.row_31 = QFrame(self.groupBox_Propiedades_13)
        self.row_31.setObjectName(u"row_31")
        self.row_31.setStyleSheet(u"")
        self.row_31.setFrameShape(QFrame.StyledPanel)
        self.row_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.row_31)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_66 = QGridLayout()
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.gridLayout_66.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_66.setHorizontalSpacing(25)
        self.gridLayout_66.setVerticalSpacing(15)
        self.gridLayout_66.setContentsMargins(10, 10, 20, 10)
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setSizeConstraint(QLayout.SetMinimumSize)
        self.RHTipoComboBoxProfundidad = QComboBox(self.row_31)
        self.RHTipoComboBoxProfundidad.addItem("")
        self.RHTipoComboBoxProfundidad.addItem("")
        self.RHTipoComboBoxProfundidad.addItem("")
        self.RHTipoComboBoxProfundidad.addItem("")
        self.RHTipoComboBoxProfundidad.setObjectName(u"RHTipoComboBoxProfundidad")
        sizePolicy5.setHeightForWidth(self.RHTipoComboBoxProfundidad.sizePolicy().hasHeightForWidth())
        self.RHTipoComboBoxProfundidad.setSizePolicy(sizePolicy5)
        self.RHTipoComboBoxProfundidad.setMinimumSize(QSize(150, 36))
        self.RHTipoComboBoxProfundidad.setMaximumSize(QSize(260, 30))
        self.RHTipoComboBoxProfundidad.setLayoutDirection(Qt.LeftToRight)
        self.RHTipoComboBoxProfundidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHTipoComboBoxProfundidad.setEditable(True)
        self.RHTipoComboBoxProfundidad.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHTipoComboBoxProfundidad.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_51.addWidget(self.RHTipoComboBoxProfundidad)


        self.gridLayout_66.addLayout(self.horizontalLayout_51, 1, 2, 1, 1)

        self.RHTipoLabelProfundidad = QLabel(self.row_31)
        self.RHTipoLabelProfundidad.setObjectName(u"RHTipoLabelProfundidad")
        sizePolicy6.setHeightForWidth(self.RHTipoLabelProfundidad.sizePolicy().hasHeightForWidth())
        self.RHTipoLabelProfundidad.setSizePolicy(sizePolicy6)
        self.RHTipoLabelProfundidad.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHTipoLabelProfundidad.setLineWidth(1)
        self.RHTipoLabelProfundidad.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_66.addWidget(self.RHTipoLabelProfundidad, 1, 0, 1, 1)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.RHTipoComboBoxPendientaLateral = QComboBox(self.row_31)
        self.RHTipoComboBoxPendientaLateral.addItem("")
        self.RHTipoComboBoxPendientaLateral.addItem("")
        self.RHTipoComboBoxPendientaLateral.addItem("")
        self.RHTipoComboBoxPendientaLateral.setObjectName(u"RHTipoComboBoxPendientaLateral")
        sizePolicy5.setHeightForWidth(self.RHTipoComboBoxPendientaLateral.sizePolicy().hasHeightForWidth())
        self.RHTipoComboBoxPendientaLateral.setSizePolicy(sizePolicy5)
        self.RHTipoComboBoxPendientaLateral.setMinimumSize(QSize(260, 30))
        self.RHTipoComboBoxPendientaLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHTipoComboBoxPendientaLateral.setEditable(True)
        self.RHTipoComboBoxPendientaLateral.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_71.addWidget(self.RHTipoComboBoxPendientaLateral)


        self.gridLayout_66.addLayout(self.horizontalLayout_71, 3, 2, 1, 1)

        self.RHTipoFieldInclinacion = QLineEdit(self.row_31)
        self.RHTipoFieldInclinacion.setObjectName(u"RHTipoFieldInclinacion")
        sizePolicy5.setHeightForWidth(self.RHTipoFieldInclinacion.sizePolicy().hasHeightForWidth())
        self.RHTipoFieldInclinacion.setSizePolicy(sizePolicy5)
        self.RHTipoFieldInclinacion.setMinimumSize(QSize(0, 30))
        self.RHTipoFieldInclinacion.setMaximumSize(QSize(150, 16777215))
        self.RHTipoFieldInclinacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_66.addWidget(self.RHTipoFieldInclinacion, 5, 1, 1, 1)

        self.RHTipoFieldBase = QLineEdit(self.row_31)
        self.RHTipoFieldBase.setObjectName(u"RHTipoFieldBase")
        sizePolicy15.setHeightForWidth(self.RHTipoFieldBase.sizePolicy().hasHeightForWidth())
        self.RHTipoFieldBase.setSizePolicy(sizePolicy15)
        self.RHTipoFieldBase.setMinimumSize(QSize(110, 30))
        self.RHTipoFieldBase.setMaximumSize(QSize(150, 30))
        self.RHTipoFieldBase.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_66.addWidget(self.RHTipoFieldBase, 0, 1, 1, 1)

        self.RHTipoLabelPendienteLateral2 = QLabel(self.row_31)
        self.RHTipoLabelPendienteLateral2.setObjectName(u"RHTipoLabelPendienteLateral2")
        sizePolicy6.setHeightForWidth(self.RHTipoLabelPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.RHTipoLabelPendienteLateral2.setSizePolicy(sizePolicy6)
        self.RHTipoLabelPendienteLateral2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHTipoLabelPendienteLateral2.setLineWidth(1)
        self.RHTipoLabelPendienteLateral2.setAlignment(Qt.AlignCenter)

        self.gridLayout_66.addWidget(self.RHTipoLabelPendienteLateral2, 4, 0, 1, 1)

        self.RHTipoLabelPendienteLateral = QLabel(self.row_31)
        self.RHTipoLabelPendienteLateral.setObjectName(u"RHTipoLabelPendienteLateral")
        sizePolicy6.setHeightForWidth(self.RHTipoLabelPendienteLateral.sizePolicy().hasHeightForWidth())
        self.RHTipoLabelPendienteLateral.setSizePolicy(sizePolicy6)
        self.RHTipoLabelPendienteLateral.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHTipoLabelPendienteLateral.setLineWidth(1)
        self.RHTipoLabelPendienteLateral.setAlignment(Qt.AlignCenter)

        self.gridLayout_66.addWidget(self.RHTipoLabelPendienteLateral, 3, 0, 1, 1)

        self.RHTipoLabelCaudal = QLabel(self.row_31)
        self.RHTipoLabelCaudal.setObjectName(u"RHTipoLabelCaudal")
        sizePolicy6.setHeightForWidth(self.RHTipoLabelCaudal.sizePolicy().hasHeightForWidth())
        self.RHTipoLabelCaudal.setSizePolicy(sizePolicy6)
        self.RHTipoLabelCaudal.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHTipoLabelCaudal.setLineWidth(1)
        self.RHTipoLabelCaudal.setAlignment(Qt.AlignCenter)

        self.gridLayout_66.addWidget(self.RHTipoLabelCaudal, 6, 0, 1, 1)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setSizeConstraint(QLayout.SetMinimumSize)
        self.RHTipoComboBoxBase = QComboBox(self.row_31)
        self.RHTipoComboBoxBase.addItem("")
        self.RHTipoComboBoxBase.addItem("")
        self.RHTipoComboBoxBase.addItem("")
        self.RHTipoComboBoxBase.addItem("")
        self.RHTipoComboBoxBase.setObjectName(u"RHTipoComboBoxBase")
        sizePolicy11.setHeightForWidth(self.RHTipoComboBoxBase.sizePolicy().hasHeightForWidth())
        self.RHTipoComboBoxBase.setSizePolicy(sizePolicy11)
        self.RHTipoComboBoxBase.setMinimumSize(QSize(150, 36))
        self.RHTipoComboBoxBase.setMaximumSize(QSize(260, 30))
        self.RHTipoComboBoxBase.setLayoutDirection(Qt.LeftToRight)
        self.RHTipoComboBoxBase.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHTipoComboBoxBase.setEditable(True)
        self.RHTipoComboBoxBase.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHTipoComboBoxBase.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_63.addWidget(self.RHTipoComboBoxBase)


        self.gridLayout_66.addLayout(self.horizontalLayout_63, 0, 2, 1, 1)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.RHTipoComboBoxCaudal = QComboBox(self.row_31)
        self.RHTipoComboBoxCaudal.addItem("")
        self.RHTipoComboBoxCaudal.addItem("")
        self.RHTipoComboBoxCaudal.setObjectName(u"RHTipoComboBoxCaudal")
        sizePolicy5.setHeightForWidth(self.RHTipoComboBoxCaudal.sizePolicy().hasHeightForWidth())
        self.RHTipoComboBoxCaudal.setSizePolicy(sizePolicy5)
        self.RHTipoComboBoxCaudal.setMinimumSize(QSize(150, 36))
        self.RHTipoComboBoxCaudal.setMaximumSize(QSize(260, 16777215))
        self.RHTipoComboBoxCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHTipoComboBoxCaudal.setEditable(True)
        self.RHTipoComboBoxCaudal.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_52.addWidget(self.RHTipoComboBoxCaudal)


        self.gridLayout_66.addLayout(self.horizontalLayout_52, 6, 2, 1, 1)

        self.RHTipoFieldPendienteLateral = QLineEdit(self.row_31)
        self.RHTipoFieldPendienteLateral.setObjectName(u"RHTipoFieldPendienteLateral")
        sizePolicy5.setHeightForWidth(self.RHTipoFieldPendienteLateral.sizePolicy().hasHeightForWidth())
        self.RHTipoFieldPendienteLateral.setSizePolicy(sizePolicy5)
        self.RHTipoFieldPendienteLateral.setMinimumSize(QSize(0, 30))
        self.RHTipoFieldPendienteLateral.setMaximumSize(QSize(150, 16777215))
        self.RHTipoFieldPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_66.addWidget(self.RHTipoFieldPendienteLateral, 3, 1, 1, 1)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.RHTipoComboBoxNormal = QComboBox(self.row_31)
        self.RHTipoComboBoxNormal.addItem("")
        self.RHTipoComboBoxNormal.addItem("")
        self.RHTipoComboBoxNormal.addItem("")
        self.RHTipoComboBoxNormal.addItem("")
        self.RHTipoComboBoxNormal.setObjectName(u"RHTipoComboBoxNormal")
        sizePolicy5.setHeightForWidth(self.RHTipoComboBoxNormal.sizePolicy().hasHeightForWidth())
        self.RHTipoComboBoxNormal.setSizePolicy(sizePolicy5)
        self.RHTipoComboBoxNormal.setMinimumSize(QSize(150, 36))
        self.RHTipoComboBoxNormal.setMaximumSize(QSize(260, 30))
        self.RHTipoComboBoxNormal.setLayoutDirection(Qt.LeftToRight)
        self.RHTipoComboBoxNormal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHTipoComboBoxNormal.setEditable(True)
        self.RHTipoComboBoxNormal.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHTipoComboBoxNormal.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_61.addWidget(self.RHTipoComboBoxNormal)


        self.gridLayout_66.addLayout(self.horizontalLayout_61, 2, 2, 1, 1)

        self.RHTipoFieldProfundidad = QLineEdit(self.row_31)
        self.RHTipoFieldProfundidad.setObjectName(u"RHTipoFieldProfundidad")
        sizePolicy15.setHeightForWidth(self.RHTipoFieldProfundidad.sizePolicy().hasHeightForWidth())
        self.RHTipoFieldProfundidad.setSizePolicy(sizePolicy15)
        self.RHTipoFieldProfundidad.setMinimumSize(QSize(110, 30))
        self.RHTipoFieldProfundidad.setMaximumSize(QSize(150, 30))
        self.RHTipoFieldProfundidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_66.addWidget(self.RHTipoFieldProfundidad, 1, 1, 1, 1)

        self.RHTipoLabelProfundidadNormal = QLabel(self.row_31)
        self.RHTipoLabelProfundidadNormal.setObjectName(u"RHTipoLabelProfundidadNormal")
        sizePolicy6.setHeightForWidth(self.RHTipoLabelProfundidadNormal.sizePolicy().hasHeightForWidth())
        self.RHTipoLabelProfundidadNormal.setSizePolicy(sizePolicy6)
        self.RHTipoLabelProfundidadNormal.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHTipoLabelProfundidadNormal.setLineWidth(1)
        self.RHTipoLabelProfundidadNormal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_66.addWidget(self.RHTipoLabelProfundidadNormal, 2, 0, 1, 1)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.RHTipoComboBoxInclinacion = QComboBox(self.row_31)
        self.RHTipoComboBoxInclinacion.addItem("")
        self.RHTipoComboBoxInclinacion.addItem("")
        self.RHTipoComboBoxInclinacion.addItem("")
        self.RHTipoComboBoxInclinacion.setObjectName(u"RHTipoComboBoxInclinacion")
        sizePolicy5.setHeightForWidth(self.RHTipoComboBoxInclinacion.sizePolicy().hasHeightForWidth())
        self.RHTipoComboBoxInclinacion.setSizePolicy(sizePolicy5)
        self.RHTipoComboBoxInclinacion.setMinimumSize(QSize(260, 30))
        self.RHTipoComboBoxInclinacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHTipoComboBoxInclinacion.setEditable(True)
        self.RHTipoComboBoxInclinacion.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_60.addWidget(self.RHTipoComboBoxInclinacion)


        self.gridLayout_66.addLayout(self.horizontalLayout_60, 5, 2, 1, 1)

        self.RHTipoLabelInclinacion = QLabel(self.row_31)
        self.RHTipoLabelInclinacion.setObjectName(u"RHTipoLabelInclinacion")
        sizePolicy6.setHeightForWidth(self.RHTipoLabelInclinacion.sizePolicy().hasHeightForWidth())
        self.RHTipoLabelInclinacion.setSizePolicy(sizePolicy6)
        self.RHTipoLabelInclinacion.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHTipoLabelInclinacion.setLineWidth(1)
        self.RHTipoLabelInclinacion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_66.addWidget(self.RHTipoLabelInclinacion, 5, 0, 1, 1)

        self.RHTipoFieldNormal = QLineEdit(self.row_31)
        self.RHTipoFieldNormal.setObjectName(u"RHTipoFieldNormal")
        sizePolicy5.setHeightForWidth(self.RHTipoFieldNormal.sizePolicy().hasHeightForWidth())
        self.RHTipoFieldNormal.setSizePolicy(sizePolicy5)
        self.RHTipoFieldNormal.setMinimumSize(QSize(0, 30))
        self.RHTipoFieldNormal.setMaximumSize(QSize(150, 16777215))
        self.RHTipoFieldNormal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_66.addWidget(self.RHTipoFieldNormal, 2, 1, 1, 1)

        self.RHTipoLabelBase = QLabel(self.row_31)
        self.RHTipoLabelBase.setObjectName(u"RHTipoLabelBase")
        sizePolicy6.setHeightForWidth(self.RHTipoLabelBase.sizePolicy().hasHeightForWidth())
        self.RHTipoLabelBase.setSizePolicy(sizePolicy6)
        self.RHTipoLabelBase.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHTipoLabelBase.setLineWidth(1)
        self.RHTipoLabelBase.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_66.addWidget(self.RHTipoLabelBase, 0, 0, 1, 1)

        self.RHTipoFieldCaudal = QLineEdit(self.row_31)
        self.RHTipoFieldCaudal.setObjectName(u"RHTipoFieldCaudal")
        sizePolicy5.setHeightForWidth(self.RHTipoFieldCaudal.sizePolicy().hasHeightForWidth())
        self.RHTipoFieldCaudal.setSizePolicy(sizePolicy5)
        self.RHTipoFieldCaudal.setMinimumSize(QSize(0, 30))
        self.RHTipoFieldCaudal.setMaximumSize(QSize(150, 16777215))
        self.RHTipoFieldCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_66.addWidget(self.RHTipoFieldCaudal, 6, 1, 1, 1)

        self.RHTipoFieldPendienteLateral2 = QLineEdit(self.row_31)
        self.RHTipoFieldPendienteLateral2.setObjectName(u"RHTipoFieldPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.RHTipoFieldPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.RHTipoFieldPendienteLateral2.setSizePolicy(sizePolicy5)
        self.RHTipoFieldPendienteLateral2.setMinimumSize(QSize(0, 30))
        self.RHTipoFieldPendienteLateral2.setMaximumSize(QSize(150, 16777215))
        self.RHTipoFieldPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_66.addWidget(self.RHTipoFieldPendienteLateral2, 4, 1, 1, 1)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.RHTipoComboBoxPendienteLateral2 = QComboBox(self.row_31)
        self.RHTipoComboBoxPendienteLateral2.addItem("")
        self.RHTipoComboBoxPendienteLateral2.addItem("")
        self.RHTipoComboBoxPendienteLateral2.addItem("")
        self.RHTipoComboBoxPendienteLateral2.setObjectName(u"RHTipoComboBoxPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.RHTipoComboBoxPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.RHTipoComboBoxPendienteLateral2.setSizePolicy(sizePolicy5)
        self.RHTipoComboBoxPendienteLateral2.setMinimumSize(QSize(260, 30))
        self.RHTipoComboBoxPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHTipoComboBoxPendienteLateral2.setEditable(True)
        self.RHTipoComboBoxPendienteLateral2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_72.addWidget(self.RHTipoComboBoxPendienteLateral2)


        self.gridLayout_66.addLayout(self.horizontalLayout_72, 4, 2, 1, 1)


        self.verticalLayout_51.addLayout(self.gridLayout_66)


        self.gridLayout_65.addWidget(self.row_31, 0, 1, 1, 1)

        self.groupBox_Resultados_16 = QGroupBox(self.rhTipo)
        self.groupBox_Resultados_16.setObjectName(u"groupBox_Resultados_16")
        self.groupBox_Resultados_16.setGeometry(QRect(20, 410, 571, 181))
        sizePolicy.setHeightForWidth(self.groupBox_Resultados_16.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_16.setSizePolicy(sizePolicy)
        self.groupBox_Resultados_16.setMinimumSize(QSize(500, 0))
        self.groupBox_Resultados_16.setStyleSheet(u"QGroupBox {\n"
"color: rgb(199, 199, 199);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(199, 199, 199);\n"
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
        self.gridLayout_77 = QGridLayout(self.groupBox_Resultados_16)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.row_37 = QFrame(self.groupBox_Resultados_16)
        self.row_37.setObjectName(u"row_37")
        self.row_37.setStyleSheet(u"")
        self.row_37.setFrameShape(QFrame.StyledPanel)
        self.row_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.row_37)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_78 = QGridLayout()
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.gridLayout_78.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_78.setHorizontalSpacing(10)
        self.gridLayout_78.setVerticalSpacing(15)
        self.gridLayout_78.setContentsMargins(10, 10, 10, 10)
        self.RHTipoFieldSubsecuente = QLineEdit(self.row_37)
        self.RHTipoFieldSubsecuente.setObjectName(u"RHTipoFieldSubsecuente")
        sizePolicy5.setHeightForWidth(self.RHTipoFieldSubsecuente.sizePolicy().hasHeightForWidth())
        self.RHTipoFieldSubsecuente.setSizePolicy(sizePolicy5)
        self.RHTipoFieldSubsecuente.setMinimumSize(QSize(0, 30))
        self.RHTipoFieldSubsecuente.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_78.addWidget(self.RHTipoFieldSubsecuente, 0, 1, 1, 1)

        self.RHTipoLabelSubsecuente = QLabel(self.row_37)
        self.RHTipoLabelSubsecuente.setObjectName(u"RHTipoLabelSubsecuente")
        sizePolicy6.setHeightForWidth(self.RHTipoLabelSubsecuente.sizePolicy().hasHeightForWidth())
        self.RHTipoLabelSubsecuente.setSizePolicy(sizePolicy6)
        self.RHTipoLabelSubsecuente.setStyleSheet(u"font: 650 11pt \"Allerta\";\n"
"color: rgb(116, 116, 116);")
        self.RHTipoLabelSubsecuente.setLineWidth(1)
        self.RHTipoLabelSubsecuente.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_78.addWidget(self.RHTipoLabelSubsecuente, 0, 0, 1, 1)

        self.RHTipoLabelAsterisco = QLabel(self.row_37)
        self.RHTipoLabelAsterisco.setObjectName(u"RHTipoLabelAsterisco")
        sizePolicy6.setHeightForWidth(self.RHTipoLabelAsterisco.sizePolicy().hasHeightForWidth())
        self.RHTipoLabelAsterisco.setSizePolicy(sizePolicy6)
        self.RHTipoLabelAsterisco.setStyleSheet(u"font: 650 11pt \"Allerta\";\n"
"color: rgb(116, 116, 116);")
        self.RHTipoLabelAsterisco.setLineWidth(1)
        self.RHTipoLabelAsterisco.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_78.addWidget(self.RHTipoLabelAsterisco, 1, 0, 1, 1)

        self.RHTipoFieldAsterisco = QLineEdit(self.row_37)
        self.RHTipoFieldAsterisco.setObjectName(u"RHTipoFieldAsterisco")
        sizePolicy5.setHeightForWidth(self.RHTipoFieldAsterisco.sizePolicy().hasHeightForWidth())
        self.RHTipoFieldAsterisco.setSizePolicy(sizePolicy5)
        self.RHTipoFieldAsterisco.setMinimumSize(QSize(0, 30))
        self.RHTipoFieldAsterisco.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_78.addWidget(self.RHTipoFieldAsterisco, 1, 1, 1, 1)


        self.verticalLayout_57.addLayout(self.gridLayout_78)


        self.gridLayout_77.addWidget(self.row_37, 0, 0, 1, 1)

        self.groupBox_Resultados_13 = QGroupBox(self.rhTipo)
        self.groupBox_Resultados_13.setObjectName(u"groupBox_Resultados_13")
        self.groupBox_Resultados_13.setGeometry(QRect(590, 410, 480, 181))
        sizePolicy17.setHeightForWidth(self.groupBox_Resultados_13.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_13.setSizePolicy(sizePolicy17)
        self.groupBox_Resultados_13.setMinimumSize(QSize(480, 0))
        self.groupBox_Resultados_13.setMaximumSize(QSize(480, 16777215))
        self.groupBox_Resultados_13.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 190, 167);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
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
        self.gridLayout_67 = QGridLayout(self.groupBox_Resultados_13)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.row_32 = QFrame(self.groupBox_Resultados_13)
        self.row_32.setObjectName(u"row_32")
        self.row_32.setStyleSheet(u"")
        self.row_32.setFrameShape(QFrame.StyledPanel)
        self.row_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.row_32)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_68 = QGridLayout()
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.gridLayout_68.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_68.setHorizontalSpacing(10)
        self.gridLayout_68.setVerticalSpacing(15)
        self.gridLayout_68.setContentsMargins(10, 10, 10, 10)
        self.RHTipoFieldTipo = QLineEdit(self.row_32)
        self.RHTipoFieldTipo.setObjectName(u"RHTipoFieldTipo")
        sizePolicy5.setHeightForWidth(self.RHTipoFieldTipo.sizePolicy().hasHeightForWidth())
        self.RHTipoFieldTipo.setSizePolicy(sizePolicy5)
        self.RHTipoFieldTipo.setMinimumSize(QSize(0, 40))
        self.RHTipoFieldTipo.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_68.addWidget(self.RHTipoFieldTipo, 0, 1, 1, 1)

        self.RHTipoLabelTipo = QLabel(self.row_32)
        self.RHTipoLabelTipo.setObjectName(u"RHTipoLabelTipo")
        sizePolicy6.setHeightForWidth(self.RHTipoLabelTipo.sizePolicy().hasHeightForWidth())
        self.RHTipoLabelTipo.setSizePolicy(sizePolicy6)
        self.RHTipoLabelTipo.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHTipoLabelTipo.setLineWidth(1)
        self.RHTipoLabelTipo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_68.addWidget(self.RHTipoLabelTipo, 0, 0, 1, 1)


        self.verticalLayout_52.addLayout(self.gridLayout_68)


        self.gridLayout_67.addWidget(self.row_32, 0, 0, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.rhTipo)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(890, 20, 171, 171))
        self.gridLayout_21 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setHorizontalSpacing(5)
        self.gridLayout_21.setVerticalSpacing(0)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.RHTipoTextoReiniciar = QLabel(self.gridLayoutWidget_4)
        self.RHTipoTextoReiniciar.setObjectName(u"RHTipoTextoReiniciar")
        sizePolicy5.setHeightForWidth(self.RHTipoTextoReiniciar.sizePolicy().hasHeightForWidth())
        self.RHTipoTextoReiniciar.setSizePolicy(sizePolicy5)
        self.RHTipoTextoReiniciar.setStyleSheet(u"color: rgb(84, 84, 84);\n"
"font: 500 12pt \"Allerta\";")
        self.RHTipoTextoReiniciar.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.RHTipoTextoReiniciar, 2, 1, 1, 1)

        self.RHTipoTextoCalcular = QLabel(self.gridLayoutWidget_4)
        self.RHTipoTextoCalcular.setObjectName(u"RHTipoTextoCalcular")
        sizePolicy5.setHeightForWidth(self.RHTipoTextoCalcular.sizePolicy().hasHeightForWidth())
        self.RHTipoTextoCalcular.setSizePolicy(sizePolicy5)
        self.RHTipoTextoCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"")
        self.RHTipoTextoCalcular.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.RHTipoTextoCalcular, 2, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.RHTipoBotonCalcular = QPushButton(self.gridLayoutWidget_4)
        self.RHTipoBotonCalcular.setObjectName(u"RHTipoBotonCalcular")
        self.RHTipoBotonCalcular.setMinimumSize(QSize(50, 50))
        self.RHTipoBotonCalcular.setMaximumSize(QSize(40, 40))
        self.RHTipoBotonCalcular.setStyleSheet(u"background-color: rgb(250, 190, 167);\n"
"border-color: rgb(250, 190, 167);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.RHTipoBotonCalcular)


        self.gridLayout_21.addLayout(self.horizontalLayout_20, 0, 0, 1, 1)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.RHTipoBotonReiniciar = QPushButton(self.gridLayoutWidget_4)
        self.RHTipoBotonReiniciar.setObjectName(u"RHTipoBotonReiniciar")
        self.RHTipoBotonReiniciar.setMinimumSize(QSize(50, 50))
        self.RHTipoBotonReiniciar.setMaximumSize(QSize(40, 40))
        self.RHTipoBotonReiniciar.setStyleSheet(u"background-color: rgb(250, 190, 167);\n"
"border-color: rgb(250, 190, 167);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_34.addWidget(self.RHTipoBotonReiniciar)


        self.gridLayout_21.addLayout(self.horizontalLayout_34, 0, 1, 1, 1)

        self.gridLayout_21.setColumnStretch(0, 10)
        self.gridLayout_21.setColumnStretch(1, 10)
        self.gridLayout_21.setRowMinimumHeight(0, 10)
        self.gridLayout_21.setRowMinimumHeight(1, 10)
        self.tabResaltosHidraulicos.addTab(self.rhTipo, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"font: 500 11pt \"Allerta\";")
        self.groupBox_Propiedades_15 = QGroupBox(self.tab)
        self.groupBox_Propiedades_15.setObjectName(u"groupBox_Propiedades_15")
        self.groupBox_Propiedades_15.setGeometry(QRect(20, 20, 700, 371))
        sizePolicy5.setHeightForWidth(self.groupBox_Propiedades_15.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_15.setSizePolicy(sizePolicy5)
        self.groupBox_Propiedades_15.setMinimumSize(QSize(380, 0))
        self.groupBox_Propiedades_15.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_15.setStyleSheet(u"QGroupBox {\n"
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
        self.groupBox_Propiedades_15.setAlignment(Qt.AlignCenter)
        self.gridLayout_73 = QGridLayout(self.groupBox_Propiedades_15)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.row_35 = QFrame(self.groupBox_Propiedades_15)
        self.row_35.setObjectName(u"row_35")
        self.row_35.setStyleSheet(u"")
        self.row_35.setFrameShape(QFrame.StyledPanel)
        self.row_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.row_35)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_74 = QGridLayout()
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.gridLayout_74.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_74.setHorizontalSpacing(35)
        self.gridLayout_74.setVerticalSpacing(15)
        self.gridLayout_74.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.RHCompuertasComboBoxPendienteLateral = QComboBox(self.row_35)
        self.RHCompuertasComboBoxPendienteLateral.addItem("")
        self.RHCompuertasComboBoxPendienteLateral.addItem("")
        self.RHCompuertasComboBoxPendienteLateral.addItem("")
        self.RHCompuertasComboBoxPendienteLateral.setObjectName(u"RHCompuertasComboBoxPendienteLateral")
        sizePolicy5.setHeightForWidth(self.RHCompuertasComboBoxPendienteLateral.sizePolicy().hasHeightForWidth())
        self.RHCompuertasComboBoxPendienteLateral.setSizePolicy(sizePolicy5)
        self.RHCompuertasComboBoxPendienteLateral.setMinimumSize(QSize(254, 30))
        self.RHCompuertasComboBoxPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHCompuertasComboBoxPendienteLateral.setEditable(True)
        self.RHCompuertasComboBoxPendienteLateral.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_78.addWidget(self.RHCompuertasComboBoxPendienteLateral)


        self.gridLayout_74.addLayout(self.horizontalLayout_78, 2, 2, 1, 1)

        self.RHCompuertasLabelCaudal = QLabel(self.row_35)
        self.RHCompuertasLabelCaudal.setObjectName(u"RHCompuertasLabelCaudal")
        sizePolicy6.setHeightForWidth(self.RHCompuertasLabelCaudal.sizePolicy().hasHeightForWidth())
        self.RHCompuertasLabelCaudal.setSizePolicy(sizePolicy6)
        self.RHCompuertasLabelCaudal.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHCompuertasLabelCaudal.setLineWidth(1)
        self.RHCompuertasLabelCaudal.setAlignment(Qt.AlignCenter)

        self.gridLayout_74.addWidget(self.RHCompuertasLabelCaudal, 4, 0, 1, 1)

        self.RHCompuertasLabelPendienteLateral = QLabel(self.row_35)
        self.RHCompuertasLabelPendienteLateral.setObjectName(u"RHCompuertasLabelPendienteLateral")
        sizePolicy6.setHeightForWidth(self.RHCompuertasLabelPendienteLateral.sizePolicy().hasHeightForWidth())
        self.RHCompuertasLabelPendienteLateral.setSizePolicy(sizePolicy6)
        self.RHCompuertasLabelPendienteLateral.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHCompuertasLabelPendienteLateral.setLineWidth(1)
        self.RHCompuertasLabelPendienteLateral.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_74.addWidget(self.RHCompuertasLabelPendienteLateral, 2, 0, 1, 1)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setSpacing(6)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.RHCompuertasComboBoxAncho = QComboBox(self.row_35)
        self.RHCompuertasComboBoxAncho.addItem("")
        self.RHCompuertasComboBoxAncho.addItem("")
        self.RHCompuertasComboBoxAncho.addItem("")
        self.RHCompuertasComboBoxAncho.addItem("")
        self.RHCompuertasComboBoxAncho.setObjectName(u"RHCompuertasComboBoxAncho")
        sizePolicy11.setHeightForWidth(self.RHCompuertasComboBoxAncho.sizePolicy().hasHeightForWidth())
        self.RHCompuertasComboBoxAncho.setSizePolicy(sizePolicy11)
        self.RHCompuertasComboBoxAncho.setMinimumSize(QSize(150, 30))
        self.RHCompuertasComboBoxAncho.setMaximumSize(QSize(260, 30))
        self.RHCompuertasComboBoxAncho.setLayoutDirection(Qt.LeftToRight)
        self.RHCompuertasComboBoxAncho.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHCompuertasComboBoxAncho.setEditable(True)
        self.RHCompuertasComboBoxAncho.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHCompuertasComboBoxAncho.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_75.addWidget(self.RHCompuertasComboBoxAncho)


        self.gridLayout_74.addLayout(self.horizontalLayout_75, 0, 2, 1, 1)

        self.RHCompuertasFieldPendienteLateral = QLineEdit(self.row_35)
        self.RHCompuertasFieldPendienteLateral.setObjectName(u"RHCompuertasFieldPendienteLateral")
        sizePolicy5.setHeightForWidth(self.RHCompuertasFieldPendienteLateral.sizePolicy().hasHeightForWidth())
        self.RHCompuertasFieldPendienteLateral.setSizePolicy(sizePolicy5)
        self.RHCompuertasFieldPendienteLateral.setMinimumSize(QSize(0, 30))
        self.RHCompuertasFieldPendienteLateral.setMaximumSize(QSize(150, 16777215))
        self.RHCompuertasFieldPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_74.addWidget(self.RHCompuertasFieldPendienteLateral, 2, 1, 1, 1)

        self.RHCompuertasFieldCaudal = QLineEdit(self.row_35)
        self.RHCompuertasFieldCaudal.setObjectName(u"RHCompuertasFieldCaudal")
        sizePolicy5.setHeightForWidth(self.RHCompuertasFieldCaudal.sizePolicy().hasHeightForWidth())
        self.RHCompuertasFieldCaudal.setSizePolicy(sizePolicy5)
        self.RHCompuertasFieldCaudal.setMinimumSize(QSize(0, 30))
        self.RHCompuertasFieldCaudal.setMaximumSize(QSize(150, 16777215))
        self.RHCompuertasFieldCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_74.addWidget(self.RHCompuertasFieldCaudal, 4, 1, 1, 1)

        self.RHCompuertasFieldPendienteLateral2 = QLineEdit(self.row_35)
        self.RHCompuertasFieldPendienteLateral2.setObjectName(u"RHCompuertasFieldPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.RHCompuertasFieldPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.RHCompuertasFieldPendienteLateral2.setSizePolicy(sizePolicy5)
        self.RHCompuertasFieldPendienteLateral2.setMinimumSize(QSize(0, 30))
        self.RHCompuertasFieldPendienteLateral2.setMaximumSize(QSize(150, 16777215))
        self.RHCompuertasFieldPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_74.addWidget(self.RHCompuertasFieldPendienteLateral2, 3, 1, 1, 1)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setSpacing(6)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.RHCompuertasComboBoxProfundidad = QComboBox(self.row_35)
        self.RHCompuertasComboBoxProfundidad.addItem("")
        self.RHCompuertasComboBoxProfundidad.addItem("")
        self.RHCompuertasComboBoxProfundidad.addItem("")
        self.RHCompuertasComboBoxProfundidad.addItem("")
        self.RHCompuertasComboBoxProfundidad.setObjectName(u"RHCompuertasComboBoxProfundidad")
        sizePolicy5.setHeightForWidth(self.RHCompuertasComboBoxProfundidad.sizePolicy().hasHeightForWidth())
        self.RHCompuertasComboBoxProfundidad.setSizePolicy(sizePolicy5)
        self.RHCompuertasComboBoxProfundidad.setMinimumSize(QSize(150, 30))
        self.RHCompuertasComboBoxProfundidad.setMaximumSize(QSize(260, 30))
        self.RHCompuertasComboBoxProfundidad.setLayoutDirection(Qt.LeftToRight)
        self.RHCompuertasComboBoxProfundidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHCompuertasComboBoxProfundidad.setEditable(True)
        self.RHCompuertasComboBoxProfundidad.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHCompuertasComboBoxProfundidad.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_76.addWidget(self.RHCompuertasComboBoxProfundidad)


        self.gridLayout_74.addLayout(self.horizontalLayout_76, 1, 2, 1, 1)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.RHCompuertasComboBoxCaudal = QComboBox(self.row_35)
        self.RHCompuertasComboBoxCaudal.addItem("")
        self.RHCompuertasComboBoxCaudal.addItem("")
        self.RHCompuertasComboBoxCaudal.setObjectName(u"RHCompuertasComboBoxCaudal")
        sizePolicy11.setHeightForWidth(self.RHCompuertasComboBoxCaudal.sizePolicy().hasHeightForWidth())
        self.RHCompuertasComboBoxCaudal.setSizePolicy(sizePolicy11)
        self.RHCompuertasComboBoxCaudal.setMinimumSize(QSize(150, 36))
        self.RHCompuertasComboBoxCaudal.setMaximumSize(QSize(255, 16777215))
        self.RHCompuertasComboBoxCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHCompuertasComboBoxCaudal.setEditable(True)
        self.RHCompuertasComboBoxCaudal.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_77.addWidget(self.RHCompuertasComboBoxCaudal)


        self.gridLayout_74.addLayout(self.horizontalLayout_77, 4, 2, 1, 1)

        self.RHCompuertasLabelBase = QLabel(self.row_35)
        self.RHCompuertasLabelBase.setObjectName(u"RHCompuertasLabelBase")
        sizePolicy6.setHeightForWidth(self.RHCompuertasLabelBase.sizePolicy().hasHeightForWidth())
        self.RHCompuertasLabelBase.setSizePolicy(sizePolicy6)
        self.RHCompuertasLabelBase.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHCompuertasLabelBase.setLineWidth(1)
        self.RHCompuertasLabelBase.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_74.addWidget(self.RHCompuertasLabelBase, 0, 0, 1, 1)

        self.RHCompuertasFieldProfundidad = QLineEdit(self.row_35)
        self.RHCompuertasFieldProfundidad.setObjectName(u"RHCompuertasFieldProfundidad")
        sizePolicy15.setHeightForWidth(self.RHCompuertasFieldProfundidad.sizePolicy().hasHeightForWidth())
        self.RHCompuertasFieldProfundidad.setSizePolicy(sizePolicy15)
        self.RHCompuertasFieldProfundidad.setMinimumSize(QSize(110, 30))
        self.RHCompuertasFieldProfundidad.setMaximumSize(QSize(150, 30))
        self.RHCompuertasFieldProfundidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_74.addWidget(self.RHCompuertasFieldProfundidad, 1, 1, 1, 1)

        self.RHCompuertasLabelPendienteLateral2 = QLabel(self.row_35)
        self.RHCompuertasLabelPendienteLateral2.setObjectName(u"RHCompuertasLabelPendienteLateral2")
        sizePolicy6.setHeightForWidth(self.RHCompuertasLabelPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.RHCompuertasLabelPendienteLateral2.setSizePolicy(sizePolicy6)
        self.RHCompuertasLabelPendienteLateral2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHCompuertasLabelPendienteLateral2.setLineWidth(1)
        self.RHCompuertasLabelPendienteLateral2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_74.addWidget(self.RHCompuertasLabelPendienteLateral2, 3, 0, 1, 1)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.RHCompuertasComboBoxPendienteLateral2 = QComboBox(self.row_35)
        self.RHCompuertasComboBoxPendienteLateral2.addItem("")
        self.RHCompuertasComboBoxPendienteLateral2.addItem("")
        self.RHCompuertasComboBoxPendienteLateral2.addItem("")
        self.RHCompuertasComboBoxPendienteLateral2.setObjectName(u"RHCompuertasComboBoxPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.RHCompuertasComboBoxPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.RHCompuertasComboBoxPendienteLateral2.setSizePolicy(sizePolicy5)
        self.RHCompuertasComboBoxPendienteLateral2.setMinimumSize(QSize(254, 30))
        self.RHCompuertasComboBoxPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHCompuertasComboBoxPendienteLateral2.setEditable(True)
        self.RHCompuertasComboBoxPendienteLateral2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_79.addWidget(self.RHCompuertasComboBoxPendienteLateral2)


        self.gridLayout_74.addLayout(self.horizontalLayout_79, 3, 2, 1, 1)

        self.RHCompuertasFieldAncho = QLineEdit(self.row_35)
        self.RHCompuertasFieldAncho.setObjectName(u"RHCompuertasFieldAncho")
        sizePolicy15.setHeightForWidth(self.RHCompuertasFieldAncho.sizePolicy().hasHeightForWidth())
        self.RHCompuertasFieldAncho.setSizePolicy(sizePolicy15)
        self.RHCompuertasFieldAncho.setMinimumSize(QSize(110, 30))
        self.RHCompuertasFieldAncho.setMaximumSize(QSize(150, 30))
        self.RHCompuertasFieldAncho.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_74.addWidget(self.RHCompuertasFieldAncho, 0, 1, 1, 1)

        self.RHCompuertasLabelProfundidad = QLabel(self.row_35)
        self.RHCompuertasLabelProfundidad.setObjectName(u"RHCompuertasLabelProfundidad")
        sizePolicy6.setHeightForWidth(self.RHCompuertasLabelProfundidad.sizePolicy().hasHeightForWidth())
        self.RHCompuertasLabelProfundidad.setSizePolicy(sizePolicy6)
        self.RHCompuertasLabelProfundidad.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHCompuertasLabelProfundidad.setLineWidth(1)
        self.RHCompuertasLabelProfundidad.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_74.addWidget(self.RHCompuertasLabelProfundidad, 1, 0, 1, 1)

        self.RHCompuertasLabelDiametro = QLabel(self.row_35)
        self.RHCompuertasLabelDiametro.setObjectName(u"RHCompuertasLabelDiametro")
        sizePolicy6.setHeightForWidth(self.RHCompuertasLabelDiametro.sizePolicy().hasHeightForWidth())
        self.RHCompuertasLabelDiametro.setSizePolicy(sizePolicy6)
        self.RHCompuertasLabelDiametro.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHCompuertasLabelDiametro.setLineWidth(1)
        self.RHCompuertasLabelDiametro.setAlignment(Qt.AlignCenter)

        self.gridLayout_74.addWidget(self.RHCompuertasLabelDiametro, 5, 0, 1, 1)

        self.RHCompuertasFieldDiametro = QLineEdit(self.row_35)
        self.RHCompuertasFieldDiametro.setObjectName(u"RHCompuertasFieldDiametro")
        sizePolicy5.setHeightForWidth(self.RHCompuertasFieldDiametro.sizePolicy().hasHeightForWidth())
        self.RHCompuertasFieldDiametro.setSizePolicy(sizePolicy5)
        self.RHCompuertasFieldDiametro.setMinimumSize(QSize(0, 30))
        self.RHCompuertasFieldDiametro.setMaximumSize(QSize(150, 16777215))
        self.RHCompuertasFieldDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_74.addWidget(self.RHCompuertasFieldDiametro, 5, 1, 1, 1)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setSpacing(6)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.RHCompuertasComboBoxDiametro = QComboBox(self.row_35)
        self.RHCompuertasComboBoxDiametro.addItem("")
        self.RHCompuertasComboBoxDiametro.addItem("")
        self.RHCompuertasComboBoxDiametro.addItem("")
        self.RHCompuertasComboBoxDiametro.addItem("")
        self.RHCompuertasComboBoxDiametro.setObjectName(u"RHCompuertasComboBoxDiametro")
        sizePolicy11.setHeightForWidth(self.RHCompuertasComboBoxDiametro.sizePolicy().hasHeightForWidth())
        self.RHCompuertasComboBoxDiametro.setSizePolicy(sizePolicy11)
        self.RHCompuertasComboBoxDiametro.setMinimumSize(QSize(150, 30))
        self.RHCompuertasComboBoxDiametro.setMaximumSize(QSize(260, 30))
        self.RHCompuertasComboBoxDiametro.setLayoutDirection(Qt.LeftToRight)
        self.RHCompuertasComboBoxDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHCompuertasComboBoxDiametro.setEditable(True)
        self.RHCompuertasComboBoxDiametro.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHCompuertasComboBoxDiametro.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_80.addWidget(self.RHCompuertasComboBoxDiametro)


        self.gridLayout_74.addLayout(self.horizontalLayout_80, 5, 2, 1, 1)


        self.verticalLayout_55.addLayout(self.gridLayout_74)


        self.gridLayout_73.addWidget(self.row_35, 0, 1, 1, 1)

        self.groupBox_Resultados_18 = QGroupBox(self.tab)
        self.groupBox_Resultados_18.setObjectName(u"groupBox_Resultados_18")
        self.groupBox_Resultados_18.setGeometry(QRect(720, 170, 350, 421))
        sizePolicy17.setHeightForWidth(self.groupBox_Resultados_18.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_18.setSizePolicy(sizePolicy17)
        self.groupBox_Resultados_18.setMinimumSize(QSize(300, 0))
        self.groupBox_Resultados_18.setMaximumSize(QSize(350, 16777215))
        self.groupBox_Resultados_18.setStyleSheet(u"QGroupBox {\n"
"color: rgb(250, 190, 167);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
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
        self.gridLayout_81 = QGridLayout(self.groupBox_Resultados_18)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.row_39 = QFrame(self.groupBox_Resultados_18)
        self.row_39.setObjectName(u"row_39")
        self.row_39.setStyleSheet(u"")
        self.row_39.setFrameShape(QFrame.StyledPanel)
        self.row_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.row_39)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_82 = QGridLayout()
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.gridLayout_82.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_82.setHorizontalSpacing(10)
        self.gridLayout_82.setVerticalSpacing(40)
        self.gridLayout_82.setContentsMargins(10, 10, 10, 10)
        self.RHCompuertasLabelMomentum = QLabel(self.row_39)
        self.RHCompuertasLabelMomentum.setObjectName(u"RHCompuertasLabelMomentum")
        sizePolicy6.setHeightForWidth(self.RHCompuertasLabelMomentum.sizePolicy().hasHeightForWidth())
        self.RHCompuertasLabelMomentum.setSizePolicy(sizePolicy6)
        self.RHCompuertasLabelMomentum.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHCompuertasLabelMomentum.setLineWidth(1)
        self.RHCompuertasLabelMomentum.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_82.addWidget(self.RHCompuertasLabelMomentum, 0, 0, 1, 1)

        self.RHCompuertasFieldFuerza = QLineEdit(self.row_39)
        self.RHCompuertasFieldFuerza.setObjectName(u"RHCompuertasFieldFuerza")
        sizePolicy5.setHeightForWidth(self.RHCompuertasFieldFuerza.sizePolicy().hasHeightForWidth())
        self.RHCompuertasFieldFuerza.setSizePolicy(sizePolicy5)
        self.RHCompuertasFieldFuerza.setMinimumSize(QSize(0, 40))
        self.RHCompuertasFieldFuerza.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_82.addWidget(self.RHCompuertasFieldFuerza, 2, 1, 1, 1)

        self.RHCompuertasFieldMomentum2 = QLineEdit(self.row_39)
        self.RHCompuertasFieldMomentum2.setObjectName(u"RHCompuertasFieldMomentum2")
        sizePolicy5.setHeightForWidth(self.RHCompuertasFieldMomentum2.sizePolicy().hasHeightForWidth())
        self.RHCompuertasFieldMomentum2.setSizePolicy(sizePolicy5)
        self.RHCompuertasFieldMomentum2.setMinimumSize(QSize(0, 40))
        self.RHCompuertasFieldMomentum2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_82.addWidget(self.RHCompuertasFieldMomentum2, 1, 1, 1, 1)

        self.RHCompuertasFieldMomentum = QLineEdit(self.row_39)
        self.RHCompuertasFieldMomentum.setObjectName(u"RHCompuertasFieldMomentum")
        sizePolicy5.setHeightForWidth(self.RHCompuertasFieldMomentum.sizePolicy().hasHeightForWidth())
        self.RHCompuertasFieldMomentum.setSizePolicy(sizePolicy5)
        self.RHCompuertasFieldMomentum.setMinimumSize(QSize(0, 40))
        self.RHCompuertasFieldMomentum.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_82.addWidget(self.RHCompuertasFieldMomentum, 0, 1, 1, 1)

        self.RHCompuertasLabelMomentum2 = QLabel(self.row_39)
        self.RHCompuertasLabelMomentum2.setObjectName(u"RHCompuertasLabelMomentum2")
        sizePolicy6.setHeightForWidth(self.RHCompuertasLabelMomentum2.sizePolicy().hasHeightForWidth())
        self.RHCompuertasLabelMomentum2.setSizePolicy(sizePolicy6)
        self.RHCompuertasLabelMomentum2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHCompuertasLabelMomentum2.setLineWidth(1)
        self.RHCompuertasLabelMomentum2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_82.addWidget(self.RHCompuertasLabelMomentum2, 1, 0, 1, 1)

        self.RHCompuertasLabelFuerza = QLabel(self.row_39)
        self.RHCompuertasLabelFuerza.setObjectName(u"RHCompuertasLabelFuerza")
        sizePolicy6.setHeightForWidth(self.RHCompuertasLabelFuerza.sizePolicy().hasHeightForWidth())
        self.RHCompuertasLabelFuerza.setSizePolicy(sizePolicy6)
        self.RHCompuertasLabelFuerza.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHCompuertasLabelFuerza.setLineWidth(1)
        self.RHCompuertasLabelFuerza.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_82.addWidget(self.RHCompuertasLabelFuerza, 2, 0, 1, 1)

        self.RHCompuertasLabelFuerzaCompuerta = QLabel(self.row_39)
        self.RHCompuertasLabelFuerzaCompuerta.setObjectName(u"RHCompuertasLabelFuerzaCompuerta")
        sizePolicy6.setHeightForWidth(self.RHCompuertasLabelFuerzaCompuerta.sizePolicy().hasHeightForWidth())
        self.RHCompuertasLabelFuerzaCompuerta.setSizePolicy(sizePolicy6)
        self.RHCompuertasLabelFuerzaCompuerta.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHCompuertasLabelFuerzaCompuerta.setLineWidth(1)
        self.RHCompuertasLabelFuerzaCompuerta.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_82.addWidget(self.RHCompuertasLabelFuerzaCompuerta, 3, 0, 1, 1)

        self.RHCompuertasFieldFuerzaCompuerta = QLineEdit(self.row_39)
        self.RHCompuertasFieldFuerzaCompuerta.setObjectName(u"RHCompuertasFieldFuerzaCompuerta")
        sizePolicy5.setHeightForWidth(self.RHCompuertasFieldFuerzaCompuerta.sizePolicy().hasHeightForWidth())
        self.RHCompuertasFieldFuerzaCompuerta.setSizePolicy(sizePolicy5)
        self.RHCompuertasFieldFuerzaCompuerta.setMinimumSize(QSize(0, 40))
        self.RHCompuertasFieldFuerzaCompuerta.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_82.addWidget(self.RHCompuertasFieldFuerzaCompuerta, 3, 1, 1, 1)


        self.verticalLayout_59.addLayout(self.gridLayout_82)


        self.gridLayout_81.addWidget(self.row_39, 0, 0, 1, 1)

        self.groupBox_Propiedades_17 = QGroupBox(self.tab)
        self.groupBox_Propiedades_17.setObjectName(u"groupBox_Propiedades_17")
        self.groupBox_Propiedades_17.setGeometry(QRect(20, 410, 700, 181))
        sizePolicy11.setHeightForWidth(self.groupBox_Propiedades_17.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_17.setSizePolicy(sizePolicy11)
        self.groupBox_Propiedades_17.setMinimumSize(QSize(700, 0))
        self.groupBox_Propiedades_17.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_17.setStyleSheet(u"QGroupBox {\n"
"color: rgb(163, 160, 159);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-radius: 6px;\n"
"border-color: rgb(163, 160, 159);\n"
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
        self.groupBox_Propiedades_17.setAlignment(Qt.AlignCenter)
        self.gridLayout_86 = QGridLayout(self.groupBox_Propiedades_17)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.row_42 = QFrame(self.groupBox_Propiedades_17)
        self.row_42.setObjectName(u"row_42")
        self.row_42.setStyleSheet(u"")
        self.row_42.setFrameShape(QFrame.StyledPanel)
        self.row_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.row_42)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_87 = QGridLayout()
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.gridLayout_87.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_87.setHorizontalSpacing(35)
        self.gridLayout_87.setVerticalSpacing(20)
        self.gridLayout_87.setContentsMargins(20, 5, 20, 5)
        self.RHCompuertasFieldDensidad = QLineEdit(self.row_42)
        self.RHCompuertasFieldDensidad.setObjectName(u"RHCompuertasFieldDensidad")
        sizePolicy5.setHeightForWidth(self.RHCompuertasFieldDensidad.sizePolicy().hasHeightForWidth())
        self.RHCompuertasFieldDensidad.setSizePolicy(sizePolicy5)
        self.RHCompuertasFieldDensidad.setMinimumSize(QSize(0, 30))
        self.RHCompuertasFieldDensidad.setMaximumSize(QSize(150, 16777215))
        self.RHCompuertasFieldDensidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_87.addWidget(self.RHCompuertasFieldDensidad, 1, 1, 1, 1)

        self.RHCompuertasLabelDensidad = QLabel(self.row_42)
        self.RHCompuertasLabelDensidad.setObjectName(u"RHCompuertasLabelDensidad")
        sizePolicy6.setHeightForWidth(self.RHCompuertasLabelDensidad.sizePolicy().hasHeightForWidth())
        self.RHCompuertasLabelDensidad.setSizePolicy(sizePolicy6)
        self.RHCompuertasLabelDensidad.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHCompuertasLabelDensidad.setLineWidth(1)
        self.RHCompuertasLabelDensidad.setAlignment(Qt.AlignCenter)

        self.gridLayout_87.addWidget(self.RHCompuertasLabelDensidad, 1, 0, 1, 1)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setSizeConstraint(QLayout.SetMinimumSize)
        self.RHCompuertasComboBoxDensidad = QComboBox(self.row_42)
        self.RHCompuertasComboBoxDensidad.addItem("")
        self.RHCompuertasComboBoxDensidad.setObjectName(u"RHCompuertasComboBoxDensidad")
        sizePolicy11.setHeightForWidth(self.RHCompuertasComboBoxDensidad.sizePolicy().hasHeightForWidth())
        self.RHCompuertasComboBoxDensidad.setSizePolicy(sizePolicy11)
        self.RHCompuertasComboBoxDensidad.setMinimumSize(QSize(150, 36))
        self.RHCompuertasComboBoxDensidad.setMaximumSize(QSize(260, 30))
        self.RHCompuertasComboBoxDensidad.setLayoutDirection(Qt.LeftToRight)
        self.RHCompuertasComboBoxDensidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHCompuertasComboBoxDensidad.setEditable(True)
        self.RHCompuertasComboBoxDensidad.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHCompuertasComboBoxDensidad.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_88.addWidget(self.RHCompuertasComboBoxDensidad)


        self.gridLayout_87.addLayout(self.horizontalLayout_88, 1, 2, 1, 1)

        self.RHCompuertasLabelProfundidad2 = QLabel(self.row_42)
        self.RHCompuertasLabelProfundidad2.setObjectName(u"RHCompuertasLabelProfundidad2")
        sizePolicy6.setHeightForWidth(self.RHCompuertasLabelProfundidad2.sizePolicy().hasHeightForWidth())
        self.RHCompuertasLabelProfundidad2.setSizePolicy(sizePolicy6)
        self.RHCompuertasLabelProfundidad2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.RHCompuertasLabelProfundidad2.setLineWidth(1)
        self.RHCompuertasLabelProfundidad2.setAlignment(Qt.AlignCenter)

        self.gridLayout_87.addWidget(self.RHCompuertasLabelProfundidad2, 0, 0, 1, 1)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setSizeConstraint(QLayout.SetFixedSize)
        self.RHCompuertasComboBoxProfundidad2 = QComboBox(self.row_42)
        self.RHCompuertasComboBoxProfundidad2.addItem("")
        self.RHCompuertasComboBoxProfundidad2.addItem("")
        self.RHCompuertasComboBoxProfundidad2.addItem("")
        self.RHCompuertasComboBoxProfundidad2.addItem("")
        self.RHCompuertasComboBoxProfundidad2.setObjectName(u"RHCompuertasComboBoxProfundidad2")
        sizePolicy11.setHeightForWidth(self.RHCompuertasComboBoxProfundidad2.sizePolicy().hasHeightForWidth())
        self.RHCompuertasComboBoxProfundidad2.setSizePolicy(sizePolicy11)
        self.RHCompuertasComboBoxProfundidad2.setMinimumSize(QSize(150, 36))
        self.RHCompuertasComboBoxProfundidad2.setMaximumSize(QSize(260, 30))
        self.RHCompuertasComboBoxProfundidad2.setLayoutDirection(Qt.LeftToRight)
        self.RHCompuertasComboBoxProfundidad2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHCompuertasComboBoxProfundidad2.setEditable(True)
        self.RHCompuertasComboBoxProfundidad2.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.RHCompuertasComboBoxProfundidad2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_86.addWidget(self.RHCompuertasComboBoxProfundidad2)


        self.gridLayout_87.addLayout(self.horizontalLayout_86, 0, 2, 1, 1)

        self.RHCompuertasFieldProfundidad2 = QLineEdit(self.row_42)
        self.RHCompuertasFieldProfundidad2.setObjectName(u"RHCompuertasFieldProfundidad2")
        sizePolicy5.setHeightForWidth(self.RHCompuertasFieldProfundidad2.sizePolicy().hasHeightForWidth())
        self.RHCompuertasFieldProfundidad2.setSizePolicy(sizePolicy5)
        self.RHCompuertasFieldProfundidad2.setMinimumSize(QSize(0, 30))
        self.RHCompuertasFieldProfundidad2.setMaximumSize(QSize(150, 16777215))
        self.RHCompuertasFieldProfundidad2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_87.addWidget(self.RHCompuertasFieldProfundidad2, 0, 1, 1, 1)


        self.verticalLayout_62.addLayout(self.gridLayout_87)


        self.gridLayout_86.addWidget(self.row_42, 0, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.tab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(730, 30, 331, 101))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(10)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.RHCompuertasTextoReiniciar = QLabel(self.gridLayoutWidget_2)
        self.RHCompuertasTextoReiniciar.setObjectName(u"RHCompuertasTextoReiniciar")
        sizePolicy5.setHeightForWidth(self.RHCompuertasTextoReiniciar.sizePolicy().hasHeightForWidth())
        self.RHCompuertasTextoReiniciar.setSizePolicy(sizePolicy5)
        self.RHCompuertasTextoReiniciar.setStyleSheet(u"color: rgb(84, 84, 84);\n"
"font: 500 12pt \"Allerta\";")
        self.RHCompuertasTextoReiniciar.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.RHCompuertasTextoReiniciar, 2, 1, 1, 1)

        self.RHCompuertasTextoCalcular = QLabel(self.gridLayoutWidget_2)
        self.RHCompuertasTextoCalcular.setObjectName(u"RHCompuertasTextoCalcular")
        sizePolicy5.setHeightForWidth(self.RHCompuertasTextoCalcular.sizePolicy().hasHeightForWidth())
        self.RHCompuertasTextoCalcular.setSizePolicy(sizePolicy5)
        self.RHCompuertasTextoCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"")
        self.RHCompuertasTextoCalcular.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.RHCompuertasTextoCalcular, 2, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.RHCompuertasBotonCalcular = QPushButton(self.gridLayoutWidget_2)
        self.RHCompuertasBotonCalcular.setObjectName(u"RHCompuertasBotonCalcular")
        self.RHCompuertasBotonCalcular.setMinimumSize(QSize(50, 50))
        self.RHCompuertasBotonCalcular.setMaximumSize(QSize(40, 40))
        self.RHCompuertasBotonCalcular.setStyleSheet(u"background-color: rgb(250, 190, 167);\n"
"border-color: rgb(250, 190, 167);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_17.addWidget(self.RHCompuertasBotonCalcular)


        self.gridLayout_9.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.RHCompuertasBotonReiniciar = QPushButton(self.gridLayoutWidget_2)
        self.RHCompuertasBotonReiniciar.setObjectName(u"RHCompuertasBotonReiniciar")
        self.RHCompuertasBotonReiniciar.setMinimumSize(QSize(50, 50))
        self.RHCompuertasBotonReiniciar.setMaximumSize(QSize(40, 40))
        self.RHCompuertasBotonReiniciar.setStyleSheet(u"background-color: rgb(250, 190, 167);\n"
"border-color: rgb(250, 190, 167);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_19.addWidget(self.RHCompuertasBotonReiniciar)


        self.gridLayout_9.addLayout(self.horizontalLayout_19, 0, 1, 1, 1)

        self.gridLayout_9.setColumnStretch(0, 10)
        self.gridLayout_9.setColumnStretch(1, 10)
        self.gridLayout_9.setRowMinimumHeight(0, 10)
        self.gridLayout_9.setRowMinimumHeight(1, 10)
        self.tabResaltosHidraulicos.addTab(self.tab, "")
        self.stackedWidget.addWidget(self.pagina_conservacionM)
        self.pagina_manning = QWidget()
        self.pagina_manning.setObjectName(u"pagina_manning")
        self.tabManning = QTabWidget(self.pagina_manning)
        self.tabManning.setObjectName(u"tabManning")
        self.tabManning.setGeometry(QRect(0, 0, 1117, 610))
        sizePolicy5.setHeightForWidth(self.tabManning.sizePolicy().hasHeightForWidth())
        self.tabManning.setSizePolicy(sizePolicy5)
        self.tabManning.setStyleSheet(u"font: 500 10pt \"Allerta\";\n"
"color: rgb(79, 79, 79);")
        self.tabManning.setTabPosition(QTabWidget.West)
        self.mngFlujoCritico = QWidget()
        self.mngFlujoCritico.setObjectName(u"mngFlujoCritico")
        self.mngFlujoCritico.setFont(font6)
        self.mngFlujoCritico.setStyleSheet(u"background-color: rgb(31, 37, 70);\n"
"border-color: rgb(50, 59, 113);\n"
"font: 500 11pt \"Allerta\";")
        self.gridLayout_38 = QGridLayout(self.mngFlujoCritico)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.groupBox_Resultados_7 = QGroupBox(self.mngFlujoCritico)
        self.groupBox_Resultados_7.setObjectName(u"groupBox_Resultados_7")
        sizePolicy11.setHeightForWidth(self.groupBox_Resultados_7.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_7.setSizePolicy(sizePolicy11)
        self.groupBox_Resultados_7.setStyleSheet(u"QGroupBox {\n"
"color: rgb(114, 161, 228);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(114, 161, 228);\n"
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
        self.gridLayout_40 = QGridLayout(self.groupBox_Resultados_7)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.row_19 = QFrame(self.groupBox_Resultados_7)
        self.row_19.setObjectName(u"row_19")
        self.row_19.setStyleSheet(u"")
        self.row_19.setFrameShape(QFrame.StyledPanel)
        self.row_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.row_19)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_41 = QGridLayout()
        self.gridLayout_41.setSpacing(15)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_41.setContentsMargins(15, 15, 15, 15)
        self.ManningCriticaLabelFieldProfundidadCritica = QLineEdit(self.row_19)
        self.ManningCriticaLabelFieldProfundidadCritica.setObjectName(u"ManningCriticaLabelFieldProfundidadCritica")
        sizePolicy5.setHeightForWidth(self.ManningCriticaLabelFieldProfundidadCritica.sizePolicy().hasHeightForWidth())
        self.ManningCriticaLabelFieldProfundidadCritica.setSizePolicy(sizePolicy5)
        self.ManningCriticaLabelFieldProfundidadCritica.setMinimumSize(QSize(0, 30))
        self.ManningCriticaLabelFieldProfundidadCritica.setMaximumSize(QSize(16777215, 30))
        self.ManningCriticaLabelFieldProfundidadCritica.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_41.addWidget(self.ManningCriticaLabelFieldProfundidadCritica, 0, 1, 1, 1)

        self.ManningCriticaLabelProfundidadCritica = QLabel(self.row_19)
        self.ManningCriticaLabelProfundidadCritica.setObjectName(u"ManningCriticaLabelProfundidadCritica")
        sizePolicy6.setHeightForWidth(self.ManningCriticaLabelProfundidadCritica.sizePolicy().hasHeightForWidth())
        self.ManningCriticaLabelProfundidadCritica.setSizePolicy(sizePolicy6)
        self.ManningCriticaLabelProfundidadCritica.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningCriticaLabelProfundidadCritica.setLineWidth(1)
        self.ManningCriticaLabelProfundidadCritica.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_41.addWidget(self.ManningCriticaLabelProfundidadCritica, 0, 0, 1, 1)

        self.ManningCriticaLabelVelocidadCritica = QLabel(self.row_19)
        self.ManningCriticaLabelVelocidadCritica.setObjectName(u"ManningCriticaLabelVelocidadCritica")
        sizePolicy6.setHeightForWidth(self.ManningCriticaLabelVelocidadCritica.sizePolicy().hasHeightForWidth())
        self.ManningCriticaLabelVelocidadCritica.setSizePolicy(sizePolicy6)
        self.ManningCriticaLabelVelocidadCritica.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningCriticaLabelVelocidadCritica.setLineWidth(1)
        self.ManningCriticaLabelVelocidadCritica.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_41.addWidget(self.ManningCriticaLabelVelocidadCritica, 1, 0, 1, 1)

        self.ManningCriticaLabelFieldVelocidadCritica = QLineEdit(self.row_19)
        self.ManningCriticaLabelFieldVelocidadCritica.setObjectName(u"ManningCriticaLabelFieldVelocidadCritica")
        sizePolicy5.setHeightForWidth(self.ManningCriticaLabelFieldVelocidadCritica.sizePolicy().hasHeightForWidth())
        self.ManningCriticaLabelFieldVelocidadCritica.setSizePolicy(sizePolicy5)
        self.ManningCriticaLabelFieldVelocidadCritica.setMinimumSize(QSize(0, 30))
        self.ManningCriticaLabelFieldVelocidadCritica.setMaximumSize(QSize(16777215, 30))
        self.ManningCriticaLabelFieldVelocidadCritica.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_41.addWidget(self.ManningCriticaLabelFieldVelocidadCritica, 1, 1, 1, 1)


        self.verticalLayout_39.addLayout(self.gridLayout_41)


        self.gridLayout_40.addWidget(self.row_19, 1, 0, 1, 1)


        self.gridLayout_38.addWidget(self.groupBox_Resultados_7, 7, 0, 1, 2)

        self.groupBox_Propiedades_7 = QGroupBox(self.mngFlujoCritico)
        self.groupBox_Propiedades_7.setObjectName(u"groupBox_Propiedades_7")
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_7.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_7.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_7.setMinimumSize(QSize(750, 0))
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
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_7.setAlignment(Qt.AlignCenter)
        self.gridLayout_42 = QGridLayout(self.groupBox_Propiedades_7)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setSizeConstraint(QLayout.SetNoConstraint)
        self.row_20 = QFrame(self.groupBox_Propiedades_7)
        self.row_20.setObjectName(u"row_20")
        self.row_20.setStyleSheet(u"")
        self.row_20.setFrameShape(QFrame.StyledPanel)
        self.row_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.row_20)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_42.addWidget(self.row_20, 1, 0, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_26.setContentsMargins(10, 0, 10, -1)
        self.ManningCriticaTextoCalcular = QLabel(self.groupBox_Propiedades_7)
        self.ManningCriticaTextoCalcular.setObjectName(u"ManningCriticaTextoCalcular")
        sizePolicy5.setHeightForWidth(self.ManningCriticaTextoCalcular.sizePolicy().hasHeightForWidth())
        self.ManningCriticaTextoCalcular.setSizePolicy(sizePolicy5)
        self.ManningCriticaTextoCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"\n"
"color: rgb(231, 230, 242);")
        self.ManningCriticaTextoCalcular.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.ManningCriticaTextoCalcular)

        self.ManningCriticaTextoReiniciar = QLabel(self.groupBox_Propiedades_7)
        self.ManningCriticaTextoReiniciar.setObjectName(u"ManningCriticaTextoReiniciar")
        sizePolicy5.setHeightForWidth(self.ManningCriticaTextoReiniciar.sizePolicy().hasHeightForWidth())
        self.ManningCriticaTextoReiniciar.setSizePolicy(sizePolicy5)
        self.ManningCriticaTextoReiniciar.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(231, 226, 242);")
        self.ManningCriticaTextoReiniciar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.ManningCriticaTextoReiniciar)


        self.gridLayout_42.addLayout(self.horizontalLayout_26, 6, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_27.setContentsMargins(10, 0, 10, -1)
        self.ManningCriticaBotonCalcular = QPushButton(self.groupBox_Propiedades_7)
        self.ManningCriticaBotonCalcular.setObjectName(u"ManningCriticaBotonCalcular")
        self.ManningCriticaBotonCalcular.setMinimumSize(QSize(50, 50))
        self.ManningCriticaBotonCalcular.setMaximumSize(QSize(50, 50))
        self.ManningCriticaBotonCalcular.setStyleSheet(u"background-color: rgb(114, 161, 228);\n"
"border-color: rgb(114, 161, 228);\n"
"border-width: 2px;\n"
"border-radius: 20px;")

        self.horizontalLayout_27.addWidget(self.ManningCriticaBotonCalcular)

        self.ManningCriticaBotonReiniciar = QPushButton(self.groupBox_Propiedades_7)
        self.ManningCriticaBotonReiniciar.setObjectName(u"ManningCriticaBotonReiniciar")
        self.ManningCriticaBotonReiniciar.setMinimumSize(QSize(50, 50))
        self.ManningCriticaBotonReiniciar.setMaximumSize(QSize(50, 50))
        self.ManningCriticaBotonReiniciar.setStyleSheet(u"background-color: rgb(114, 161, 228);\n"
"border-color: rgb(114, 161, 228);\n"
"border-image: url(:/geometria/images/geometria/reboot.png);\n"
"border-width: 2px;\n"
"border-radius: 20px;")

        self.horizontalLayout_27.addWidget(self.ManningCriticaBotonReiniciar)


        self.gridLayout_42.addLayout(self.horizontalLayout_27, 3, 0, 2, 1)

        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_43.setHorizontalSpacing(50)
        self.gridLayout_43.setVerticalSpacing(20)
        self.gridLayout_43.setContentsMargins(0, 20, 0, 10)
        self.ManningCriticaLabelDiametro = QLabel(self.groupBox_Propiedades_7)
        self.ManningCriticaLabelDiametro.setObjectName(u"ManningCriticaLabelDiametro")
        sizePolicy6.setHeightForWidth(self.ManningCriticaLabelDiametro.sizePolicy().hasHeightForWidth())
        self.ManningCriticaLabelDiametro.setSizePolicy(sizePolicy6)
        self.ManningCriticaLabelDiametro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningCriticaLabelDiametro.setLineWidth(1)
        self.ManningCriticaLabelDiametro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.ManningCriticaLabelDiametro, 1, 0, 1, 1)

        self.ManningCriticaLabelCaudal = QLabel(self.groupBox_Propiedades_7)
        self.ManningCriticaLabelCaudal.setObjectName(u"ManningCriticaLabelCaudal")
        sizePolicy6.setHeightForWidth(self.ManningCriticaLabelCaudal.sizePolicy().hasHeightForWidth())
        self.ManningCriticaLabelCaudal.setSizePolicy(sizePolicy6)
        self.ManningCriticaLabelCaudal.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningCriticaLabelCaudal.setLineWidth(1)
        self.ManningCriticaLabelCaudal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.ManningCriticaLabelCaudal, 2, 0, 1, 1)

        self.ManningCriticaComboBoxCaudal = QComboBox(self.groupBox_Propiedades_7)
        self.ManningCriticaComboBoxCaudal.addItem("")
        self.ManningCriticaComboBoxCaudal.addItem("")
        self.ManningCriticaComboBoxCaudal.setObjectName(u"ManningCriticaComboBoxCaudal")
        sizePolicy11.setHeightForWidth(self.ManningCriticaComboBoxCaudal.sizePolicy().hasHeightForWidth())
        self.ManningCriticaComboBoxCaudal.setSizePolicy(sizePolicy11)
        self.ManningCriticaComboBoxCaudal.setMinimumSize(QSize(150, 36))
        self.ManningCriticaComboBoxCaudal.setMaximumSize(QSize(255, 16777215))
        self.ManningCriticaComboBoxCaudal.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningCriticaComboBoxCaudal.setEditable(True)
        self.ManningCriticaComboBoxCaudal.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_43.addWidget(self.ManningCriticaComboBoxCaudal, 2, 3, 1, 1)

        self.ManningCriticaLabelPendienteLateral = QLabel(self.groupBox_Propiedades_7)
        self.ManningCriticaLabelPendienteLateral.setObjectName(u"ManningCriticaLabelPendienteLateral")
        sizePolicy6.setHeightForWidth(self.ManningCriticaLabelPendienteLateral.sizePolicy().hasHeightForWidth())
        self.ManningCriticaLabelPendienteLateral.setSizePolicy(sizePolicy6)
        self.ManningCriticaLabelPendienteLateral.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningCriticaLabelPendienteLateral.setLineWidth(1)
        self.ManningCriticaLabelPendienteLateral.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.ManningCriticaLabelPendienteLateral, 4, 0, 1, 1)

        self.ManningCriticaLabelBase = QLabel(self.groupBox_Propiedades_7)
        self.ManningCriticaLabelBase.setObjectName(u"ManningCriticaLabelBase")
        sizePolicy6.setHeightForWidth(self.ManningCriticaLabelBase.sizePolicy().hasHeightForWidth())
        self.ManningCriticaLabelBase.setSizePolicy(sizePolicy6)
        self.ManningCriticaLabelBase.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningCriticaLabelBase.setLineWidth(1)
        self.ManningCriticaLabelBase.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.ManningCriticaLabelBase, 0, 0, 1, 1)

        self.ManningCriticaFieldPendienteLateral2 = QLineEdit(self.groupBox_Propiedades_7)
        self.ManningCriticaFieldPendienteLateral2.setObjectName(u"ManningCriticaFieldPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.ManningCriticaFieldPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.ManningCriticaFieldPendienteLateral2.setSizePolicy(sizePolicy5)
        self.ManningCriticaFieldPendienteLateral2.setMinimumSize(QSize(150, 30))
        self.ManningCriticaFieldPendienteLateral2.setMaximumSize(QSize(16777215, 30))
        self.ManningCriticaFieldPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_43.addWidget(self.ManningCriticaFieldPendienteLateral2, 5, 1, 1, 1)

        self.ManningCriticaComboBoxPendientaLateral = QComboBox(self.groupBox_Propiedades_7)
        self.ManningCriticaComboBoxPendientaLateral.addItem("")
        self.ManningCriticaComboBoxPendientaLateral.addItem("")
        self.ManningCriticaComboBoxPendientaLateral.addItem("")
        self.ManningCriticaComboBoxPendientaLateral.setObjectName(u"ManningCriticaComboBoxPendientaLateral")
        sizePolicy5.setHeightForWidth(self.ManningCriticaComboBoxPendientaLateral.sizePolicy().hasHeightForWidth())
        self.ManningCriticaComboBoxPendientaLateral.setSizePolicy(sizePolicy5)
        self.ManningCriticaComboBoxPendientaLateral.setMinimumSize(QSize(246, 30))
        self.ManningCriticaComboBoxPendientaLateral.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningCriticaComboBoxPendientaLateral.setEditable(True)

        self.gridLayout_43.addWidget(self.ManningCriticaComboBoxPendientaLateral, 4, 3, 1, 1)

        self.ManningCriticaLabelPendienteLateral2 = QLabel(self.groupBox_Propiedades_7)
        self.ManningCriticaLabelPendienteLateral2.setObjectName(u"ManningCriticaLabelPendienteLateral2")
        sizePolicy6.setHeightForWidth(self.ManningCriticaLabelPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.ManningCriticaLabelPendienteLateral2.setSizePolicy(sizePolicy6)
        self.ManningCriticaLabelPendienteLateral2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningCriticaLabelPendienteLateral2.setLineWidth(1)
        self.ManningCriticaLabelPendienteLateral2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.ManningCriticaLabelPendienteLateral2, 5, 0, 1, 1)

        self.ManningCriticaFieldCaudal = QLineEdit(self.groupBox_Propiedades_7)
        self.ManningCriticaFieldCaudal.setObjectName(u"ManningCriticaFieldCaudal")
        sizePolicy5.setHeightForWidth(self.ManningCriticaFieldCaudal.sizePolicy().hasHeightForWidth())
        self.ManningCriticaFieldCaudal.setSizePolicy(sizePolicy5)
        self.ManningCriticaFieldCaudal.setMinimumSize(QSize(150, 30))
        self.ManningCriticaFieldCaudal.setMaximumSize(QSize(16777215, 30))
        self.ManningCriticaFieldCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_43.addWidget(self.ManningCriticaFieldCaudal, 2, 1, 1, 1)

        self.ManningCriticaComboBoxDiametro = QComboBox(self.groupBox_Propiedades_7)
        self.ManningCriticaComboBoxDiametro.addItem("")
        self.ManningCriticaComboBoxDiametro.addItem("")
        self.ManningCriticaComboBoxDiametro.addItem("")
        self.ManningCriticaComboBoxDiametro.addItem("")
        self.ManningCriticaComboBoxDiametro.setObjectName(u"ManningCriticaComboBoxDiametro")
        sizePolicy5.setHeightForWidth(self.ManningCriticaComboBoxDiametro.sizePolicy().hasHeightForWidth())
        self.ManningCriticaComboBoxDiametro.setSizePolicy(sizePolicy5)
        self.ManningCriticaComboBoxDiametro.setMinimumSize(QSize(246, 30))
        self.ManningCriticaComboBoxDiametro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningCriticaComboBoxDiametro.setEditable(True)

        self.gridLayout_43.addWidget(self.ManningCriticaComboBoxDiametro, 1, 3, 1, 1)

        self.ManningCriticaComboBoxBase = QComboBox(self.groupBox_Propiedades_7)
        self.ManningCriticaComboBoxBase.addItem("")
        self.ManningCriticaComboBoxBase.addItem("")
        self.ManningCriticaComboBoxBase.addItem("")
        self.ManningCriticaComboBoxBase.addItem("")
        self.ManningCriticaComboBoxBase.setObjectName(u"ManningCriticaComboBoxBase")
        sizePolicy5.setHeightForWidth(self.ManningCriticaComboBoxBase.sizePolicy().hasHeightForWidth())
        self.ManningCriticaComboBoxBase.setSizePolicy(sizePolicy5)
        self.ManningCriticaComboBoxBase.setMinimumSize(QSize(246, 30))
        self.ManningCriticaComboBoxBase.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningCriticaComboBoxBase.setEditable(True)

        self.gridLayout_43.addWidget(self.ManningCriticaComboBoxBase, 0, 3, 1, 1)

        self.ManningCriticaFieldBase = QLineEdit(self.groupBox_Propiedades_7)
        self.ManningCriticaFieldBase.setObjectName(u"ManningCriticaFieldBase")
        sizePolicy7.setHeightForWidth(self.ManningCriticaFieldBase.sizePolicy().hasHeightForWidth())
        self.ManningCriticaFieldBase.setSizePolicy(sizePolicy7)
        self.ManningCriticaFieldBase.setMinimumSize(QSize(150, 30))
        self.ManningCriticaFieldBase.setMaximumSize(QSize(16777215, 30))
        self.ManningCriticaFieldBase.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_43.addWidget(self.ManningCriticaFieldBase, 0, 1, 1, 1)

        self.ManningCriticaFieldPendienteLateral = QLineEdit(self.groupBox_Propiedades_7)
        self.ManningCriticaFieldPendienteLateral.setObjectName(u"ManningCriticaFieldPendienteLateral")
        sizePolicy5.setHeightForWidth(self.ManningCriticaFieldPendienteLateral.sizePolicy().hasHeightForWidth())
        self.ManningCriticaFieldPendienteLateral.setSizePolicy(sizePolicy5)
        self.ManningCriticaFieldPendienteLateral.setMinimumSize(QSize(150, 30))
        self.ManningCriticaFieldPendienteLateral.setMaximumSize(QSize(16777215, 30))
        self.ManningCriticaFieldPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_43.addWidget(self.ManningCriticaFieldPendienteLateral, 4, 1, 1, 1)

        self.ManningCriticaComboBoxPendientaLateral2 = QComboBox(self.groupBox_Propiedades_7)
        self.ManningCriticaComboBoxPendientaLateral2.addItem("")
        self.ManningCriticaComboBoxPendientaLateral2.addItem("")
        self.ManningCriticaComboBoxPendientaLateral2.addItem("")
        self.ManningCriticaComboBoxPendientaLateral2.setObjectName(u"ManningCriticaComboBoxPendientaLateral2")
        sizePolicy5.setHeightForWidth(self.ManningCriticaComboBoxPendientaLateral2.sizePolicy().hasHeightForWidth())
        self.ManningCriticaComboBoxPendientaLateral2.setSizePolicy(sizePolicy5)
        self.ManningCriticaComboBoxPendientaLateral2.setMinimumSize(QSize(246, 30))
        self.ManningCriticaComboBoxPendientaLateral2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningCriticaComboBoxPendientaLateral2.setEditable(True)

        self.gridLayout_43.addWidget(self.ManningCriticaComboBoxPendientaLateral2, 5, 3, 1, 1)

        self.ManningCriticaFieldDiametro = QLineEdit(self.groupBox_Propiedades_7)
        self.ManningCriticaFieldDiametro.setObjectName(u"ManningCriticaFieldDiametro")
        sizePolicy5.setHeightForWidth(self.ManningCriticaFieldDiametro.sizePolicy().hasHeightForWidth())
        self.ManningCriticaFieldDiametro.setSizePolicy(sizePolicy5)
        self.ManningCriticaFieldDiametro.setMinimumSize(QSize(150, 30))
        self.ManningCriticaFieldDiametro.setMaximumSize(QSize(16777215, 30))
        self.ManningCriticaFieldDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_43.addWidget(self.ManningCriticaFieldDiametro, 1, 1, 1, 1)

        self.ManningCriticaLabelVelocidad = QLabel(self.groupBox_Propiedades_7)
        self.ManningCriticaLabelVelocidad.setObjectName(u"ManningCriticaLabelVelocidad")
        sizePolicy6.setHeightForWidth(self.ManningCriticaLabelVelocidad.sizePolicy().hasHeightForWidth())
        self.ManningCriticaLabelVelocidad.setSizePolicy(sizePolicy6)
        self.ManningCriticaLabelVelocidad.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningCriticaLabelVelocidad.setLineWidth(1)
        self.ManningCriticaLabelVelocidad.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.ManningCriticaLabelVelocidad, 3, 0, 1, 1)

        self.ManningCriticaFieldVelocidad = QLineEdit(self.groupBox_Propiedades_7)
        self.ManningCriticaFieldVelocidad.setObjectName(u"ManningCriticaFieldVelocidad")
        sizePolicy5.setHeightForWidth(self.ManningCriticaFieldVelocidad.sizePolicy().hasHeightForWidth())
        self.ManningCriticaFieldVelocidad.setSizePolicy(sizePolicy5)
        self.ManningCriticaFieldVelocidad.setMinimumSize(QSize(150, 30))
        self.ManningCriticaFieldVelocidad.setMaximumSize(QSize(16777215, 30))
        self.ManningCriticaFieldVelocidad.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_43.addWidget(self.ManningCriticaFieldVelocidad, 3, 1, 1, 1)

        self.ManningCriticaComboBoxVelocidad = QComboBox(self.groupBox_Propiedades_7)
        self.ManningCriticaComboBoxVelocidad.addItem("")
        self.ManningCriticaComboBoxVelocidad.setObjectName(u"ManningCriticaComboBoxVelocidad")
        sizePolicy5.setHeightForWidth(self.ManningCriticaComboBoxVelocidad.sizePolicy().hasHeightForWidth())
        self.ManningCriticaComboBoxVelocidad.setSizePolicy(sizePolicy5)
        self.ManningCriticaComboBoxVelocidad.setMinimumSize(QSize(246, 30))
        self.ManningCriticaComboBoxVelocidad.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningCriticaComboBoxVelocidad.setEditable(True)

        self.gridLayout_43.addWidget(self.ManningCriticaComboBoxVelocidad, 3, 3, 1, 1)


        self.gridLayout_42.addLayout(self.gridLayout_43, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.groupBox_Propiedades_7, 6, 0, 1, 2)

        self.tabManning.addTab(self.mngFlujoCritico, "")
        self.mngPendienteCritica = QWidget()
        self.mngPendienteCritica.setObjectName(u"mngPendienteCritica")
        self.mngPendienteCritica.setStyleSheet(u"background-color: rgb(31, 37, 70);\n"
"border-color: rgb(50, 59, 113);\n"
"font: 500 11pt \"Allerta\";")
        self.groupBox_Propiedades_8 = QGroupBox(self.mngPendienteCritica)
        self.groupBox_Propiedades_8.setObjectName(u"groupBox_Propiedades_8")
        self.groupBox_Propiedades_8.setGeometry(QRect(10, 10, 620, 291))
        sizePolicy8.setHeightForWidth(self.groupBox_Propiedades_8.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_8.setSizePolicy(sizePolicy8)
        self.groupBox_Propiedades_8.setMinimumSize(QSize(620, 0))
        self.groupBox_Propiedades_8.setStyleSheet(u"QGroupBox {\n"
"color: rgb(114, 161, 228);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(114, 161, 228);\n"
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
        self.gridLayout_44 = QGridLayout(self.groupBox_Propiedades_8)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.row_21 = QFrame(self.groupBox_Propiedades_8)
        self.row_21.setObjectName(u"row_21")
        self.row_21.setStyleSheet(u"")
        self.row_21.setFrameShape(QFrame.StyledPanel)
        self.row_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.row_21)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_45 = QGridLayout()
        self.gridLayout_45.setSpacing(20)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_45.setContentsMargins(0, 10, 0, 10)
        self.ManningPendienteLabelNumManning = QLabel(self.row_21)
        self.ManningPendienteLabelNumManning.setObjectName(u"ManningPendienteLabelNumManning")
        sizePolicy6.setHeightForWidth(self.ManningPendienteLabelNumManning.sizePolicy().hasHeightForWidth())
        self.ManningPendienteLabelNumManning.setSizePolicy(sizePolicy6)
        self.ManningPendienteLabelNumManning.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningPendienteLabelNumManning.setLineWidth(1)
        self.ManningPendienteLabelNumManning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_45.addWidget(self.ManningPendienteLabelNumManning, 2, 0, 1, 1)

        self.ManningPendienteLabelAncho = QLabel(self.row_21)
        self.ManningPendienteLabelAncho.setObjectName(u"ManningPendienteLabelAncho")
        sizePolicy6.setHeightForWidth(self.ManningPendienteLabelAncho.sizePolicy().hasHeightForWidth())
        self.ManningPendienteLabelAncho.setSizePolicy(sizePolicy6)
        self.ManningPendienteLabelAncho.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningPendienteLabelAncho.setLineWidth(1)
        self.ManningPendienteLabelAncho.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_45.addWidget(self.ManningPendienteLabelAncho, 0, 0, 1, 1)

        self.ManningPendienteComboBoxAncho = QComboBox(self.row_21)
        self.ManningPendienteComboBoxAncho.addItem("")
        self.ManningPendienteComboBoxAncho.addItem("")
        self.ManningPendienteComboBoxAncho.addItem("")
        self.ManningPendienteComboBoxAncho.addItem("")
        self.ManningPendienteComboBoxAncho.setObjectName(u"ManningPendienteComboBoxAncho")
        sizePolicy5.setHeightForWidth(self.ManningPendienteComboBoxAncho.sizePolicy().hasHeightForWidth())
        self.ManningPendienteComboBoxAncho.setSizePolicy(sizePolicy5)
        self.ManningPendienteComboBoxAncho.setMinimumSize(QSize(150, 30))
        self.ManningPendienteComboBoxAncho.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningPendienteComboBoxAncho.setEditable(True)

        self.gridLayout_45.addWidget(self.ManningPendienteComboBoxAncho, 0, 2, 1, 1)

        self.ManningPendienteFieldPendienteLateral = QLineEdit(self.row_21)
        self.ManningPendienteFieldPendienteLateral.setObjectName(u"ManningPendienteFieldPendienteLateral")
        sizePolicy5.setHeightForWidth(self.ManningPendienteFieldPendienteLateral.sizePolicy().hasHeightForWidth())
        self.ManningPendienteFieldPendienteLateral.setSizePolicy(sizePolicy5)
        self.ManningPendienteFieldPendienteLateral.setMinimumSize(QSize(0, 30))
        self.ManningPendienteFieldPendienteLateral.setMaximumSize(QSize(150, 16777215))
        self.ManningPendienteFieldPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_45.addWidget(self.ManningPendienteFieldPendienteLateral, 3, 1, 1, 1)

        self.ManningPendienteFieldNumeManning = QLineEdit(self.row_21)
        self.ManningPendienteFieldNumeManning.setObjectName(u"ManningPendienteFieldNumeManning")
        sizePolicy5.setHeightForWidth(self.ManningPendienteFieldNumeManning.sizePolicy().hasHeightForWidth())
        self.ManningPendienteFieldNumeManning.setSizePolicy(sizePolicy5)
        self.ManningPendienteFieldNumeManning.setMinimumSize(QSize(0, 30))
        self.ManningPendienteFieldNumeManning.setMaximumSize(QSize(150, 16777215))
        self.ManningPendienteFieldNumeManning.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_45.addWidget(self.ManningPendienteFieldNumeManning, 2, 1, 1, 1)

        self.ManningPendienteComboBoxNumManning = QComboBox(self.row_21)
        self.ManningPendienteComboBoxNumManning.addItem("")
        self.ManningPendienteComboBoxNumManning.addItem("")
        self.ManningPendienteComboBoxNumManning.addItem("")
        self.ManningPendienteComboBoxNumManning.setObjectName(u"ManningPendienteComboBoxNumManning")
        sizePolicy5.setHeightForWidth(self.ManningPendienteComboBoxNumManning.sizePolicy().hasHeightForWidth())
        self.ManningPendienteComboBoxNumManning.setSizePolicy(sizePolicy5)
        self.ManningPendienteComboBoxNumManning.setMinimumSize(QSize(150, 30))
        self.ManningPendienteComboBoxNumManning.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningPendienteComboBoxNumManning.setEditable(True)

        self.gridLayout_45.addWidget(self.ManningPendienteComboBoxNumManning, 2, 2, 1, 1)

        self.ManningPendienteComboBoxPendienteLateral = QComboBox(self.row_21)
        self.ManningPendienteComboBoxPendienteLateral.addItem("")
        self.ManningPendienteComboBoxPendienteLateral.setObjectName(u"ManningPendienteComboBoxPendienteLateral")
        sizePolicy5.setHeightForWidth(self.ManningPendienteComboBoxPendienteLateral.sizePolicy().hasHeightForWidth())
        self.ManningPendienteComboBoxPendienteLateral.setSizePolicy(sizePolicy5)
        self.ManningPendienteComboBoxPendienteLateral.setMinimumSize(QSize(150, 30))
        self.ManningPendienteComboBoxPendienteLateral.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningPendienteComboBoxPendienteLateral.setEditable(True)

        self.gridLayout_45.addWidget(self.ManningPendienteComboBoxPendienteLateral, 3, 2, 1, 1)

        self.ManningPendienteFieldDiametro = QLineEdit(self.row_21)
        self.ManningPendienteFieldDiametro.setObjectName(u"ManningPendienteFieldDiametro")
        sizePolicy7.setHeightForWidth(self.ManningPendienteFieldDiametro.sizePolicy().hasHeightForWidth())
        self.ManningPendienteFieldDiametro.setSizePolicy(sizePolicy7)
        self.ManningPendienteFieldDiametro.setMinimumSize(QSize(120, 30))
        self.ManningPendienteFieldDiametro.setMaximumSize(QSize(150, 30))
        self.ManningPendienteFieldDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_45.addWidget(self.ManningPendienteFieldDiametro, 1, 1, 1, 1)

        self.ManningPendienteFieldAncho = QLineEdit(self.row_21)
        self.ManningPendienteFieldAncho.setObjectName(u"ManningPendienteFieldAncho")
        sizePolicy11.setHeightForWidth(self.ManningPendienteFieldAncho.sizePolicy().hasHeightForWidth())
        self.ManningPendienteFieldAncho.setSizePolicy(sizePolicy11)
        self.ManningPendienteFieldAncho.setMinimumSize(QSize(100, 30))
        self.ManningPendienteFieldAncho.setMaximumSize(QSize(150, 30))
        self.ManningPendienteFieldAncho.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_45.addWidget(self.ManningPendienteFieldAncho, 0, 1, 1, 1)

        self.ManningPendienteComboBoxDiametro = QComboBox(self.row_21)
        self.ManningPendienteComboBoxDiametro.addItem("")
        self.ManningPendienteComboBoxDiametro.addItem("")
        self.ManningPendienteComboBoxDiametro.addItem("")
        self.ManningPendienteComboBoxDiametro.addItem("")
        self.ManningPendienteComboBoxDiametro.setObjectName(u"ManningPendienteComboBoxDiametro")
        sizePolicy5.setHeightForWidth(self.ManningPendienteComboBoxDiametro.sizePolicy().hasHeightForWidth())
        self.ManningPendienteComboBoxDiametro.setSizePolicy(sizePolicy5)
        self.ManningPendienteComboBoxDiametro.setMinimumSize(QSize(150, 30))
        self.ManningPendienteComboBoxDiametro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningPendienteComboBoxDiametro.setEditable(True)

        self.gridLayout_45.addWidget(self.ManningPendienteComboBoxDiametro, 1, 2, 1, 1)

        self.ManningPendienteLabelDiametro = QLabel(self.row_21)
        self.ManningPendienteLabelDiametro.setObjectName(u"ManningPendienteLabelDiametro")
        sizePolicy6.setHeightForWidth(self.ManningPendienteLabelDiametro.sizePolicy().hasHeightForWidth())
        self.ManningPendienteLabelDiametro.setSizePolicy(sizePolicy6)
        self.ManningPendienteLabelDiametro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningPendienteLabelDiametro.setLineWidth(1)
        self.ManningPendienteLabelDiametro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_45.addWidget(self.ManningPendienteLabelDiametro, 1, 0, 1, 1)

        self.ManningPendienteLabelPendienteLateral = QLabel(self.row_21)
        self.ManningPendienteLabelPendienteLateral.setObjectName(u"ManningPendienteLabelPendienteLateral")
        sizePolicy6.setHeightForWidth(self.ManningPendienteLabelPendienteLateral.sizePolicy().hasHeightForWidth())
        self.ManningPendienteLabelPendienteLateral.setSizePolicy(sizePolicy6)
        self.ManningPendienteLabelPendienteLateral.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningPendienteLabelPendienteLateral.setLineWidth(1)
        self.ManningPendienteLabelPendienteLateral.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_45.addWidget(self.ManningPendienteLabelPendienteLateral, 3, 0, 1, 1)


        self.verticalLayout_41.addLayout(self.gridLayout_45)


        self.gridLayout_44.addWidget(self.row_21, 0, 0, 1, 1)

        self.groupBox_Resultados_8 = QGroupBox(self.mngPendienteCritica)
        self.groupBox_Resultados_8.setObjectName(u"groupBox_Resultados_8")
        self.groupBox_Resultados_8.setGeometry(QRect(650, 360, 421, 231))
        sizePolicy8.setHeightForWidth(self.groupBox_Resultados_8.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_8.setSizePolicy(sizePolicy8)
        self.groupBox_Resultados_8.setStyleSheet(u"QGroupBox {\n"
"color: rgb(114, 161, 228);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(114, 161, 228);\n"
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
        self.gridLayout_47 = QGridLayout(self.groupBox_Resultados_8)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.row_22 = QFrame(self.groupBox_Resultados_8)
        self.row_22.setObjectName(u"row_22")
        self.row_22.setStyleSheet(u"")
        self.row_22.setFrameShape(QFrame.StyledPanel)
        self.row_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.row_22)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_60 = QGridLayout()
        self.gridLayout_60.setSpacing(15)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gridLayout_60.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_60.setContentsMargins(15, 15, 15, 15)
        self.ManningPendienteFieldPendienteCritica = QLineEdit(self.row_22)
        self.ManningPendienteFieldPendienteCritica.setObjectName(u"ManningPendienteFieldPendienteCritica")
        sizePolicy5.setHeightForWidth(self.ManningPendienteFieldPendienteCritica.sizePolicy().hasHeightForWidth())
        self.ManningPendienteFieldPendienteCritica.setSizePolicy(sizePolicy5)
        self.ManningPendienteFieldPendienteCritica.setMinimumSize(QSize(0, 40))
        self.ManningPendienteFieldPendienteCritica.setMaximumSize(QSize(16777215, 30))
        self.ManningPendienteFieldPendienteCritica.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_60.addWidget(self.ManningPendienteFieldPendienteCritica, 0, 1, 1, 1)

        self.ManningPendienteLabelPendienteCritica = QLabel(self.row_22)
        self.ManningPendienteLabelPendienteCritica.setObjectName(u"ManningPendienteLabelPendienteCritica")
        sizePolicy6.setHeightForWidth(self.ManningPendienteLabelPendienteCritica.sizePolicy().hasHeightForWidth())
        self.ManningPendienteLabelPendienteCritica.setSizePolicy(sizePolicy6)
        self.ManningPendienteLabelPendienteCritica.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningPendienteLabelPendienteCritica.setLineWidth(1)
        self.ManningPendienteLabelPendienteCritica.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_60.addWidget(self.ManningPendienteLabelPendienteCritica, 0, 0, 1, 1)


        self.verticalLayout_42.addLayout(self.gridLayout_60)


        self.gridLayout_47.addWidget(self.row_22, 0, 0, 1, 1)

        self.groupBox_Propiedades_18 = QGroupBox(self.mngPendienteCritica)
        self.groupBox_Propiedades_18.setObjectName(u"groupBox_Propiedades_18")
        self.groupBox_Propiedades_18.setGeometry(QRect(10, 320, 621, 121))
        sizePolicy8.setHeightForWidth(self.groupBox_Propiedades_18.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_18.setSizePolicy(sizePolicy8)
        self.groupBox_Propiedades_18.setMinimumSize(QSize(400, 0))
        self.groupBox_Propiedades_18.setStyleSheet(u"QGroupBox {\n"
"color: rgb(176, 187, 209);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(176, 187, 209);\n"
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
        self.gridLayout_94 = QGridLayout(self.groupBox_Propiedades_18)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.row_46 = QFrame(self.groupBox_Propiedades_18)
        self.row_46.setObjectName(u"row_46")
        self.row_46.setStyleSheet(u"")
        self.row_46.setFrameShape(QFrame.StyledPanel)
        self.row_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.row_46)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_95 = QGridLayout()
        self.gridLayout_95.setSpacing(20)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.gridLayout_95.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_95.setContentsMargins(10, 20, 10, 20)
        self.ManningPendienteFieldCaudal = QLineEdit(self.row_46)
        self.ManningPendienteFieldCaudal.setObjectName(u"ManningPendienteFieldCaudal")
        sizePolicy11.setHeightForWidth(self.ManningPendienteFieldCaudal.sizePolicy().hasHeightForWidth())
        self.ManningPendienteFieldCaudal.setSizePolicy(sizePolicy11)
        self.ManningPendienteFieldCaudal.setMinimumSize(QSize(100, 30))
        self.ManningPendienteFieldCaudal.setMaximumSize(QSize(150, 30))
        self.ManningPendienteFieldCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(176, 187, 209);")

        self.gridLayout_95.addWidget(self.ManningPendienteFieldCaudal, 0, 1, 1, 1)

        self.ManningPendienteLabelCaudal = QLabel(self.row_46)
        self.ManningPendienteLabelCaudal.setObjectName(u"ManningPendienteLabelCaudal")
        sizePolicy6.setHeightForWidth(self.ManningPendienteLabelCaudal.sizePolicy().hasHeightForWidth())
        self.ManningPendienteLabelCaudal.setSizePolicy(sizePolicy6)
        self.ManningPendienteLabelCaudal.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningPendienteLabelCaudal.setLineWidth(1)
        self.ManningPendienteLabelCaudal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_95.addWidget(self.ManningPendienteLabelCaudal, 0, 0, 1, 1)

        self.ManningPendienteComboBoxCaudal = QComboBox(self.row_46)
        self.ManningPendienteComboBoxCaudal.addItem("")
        self.ManningPendienteComboBoxCaudal.addItem("")
        self.ManningPendienteComboBoxCaudal.addItem("")
        self.ManningPendienteComboBoxCaudal.setObjectName(u"ManningPendienteComboBoxCaudal")
        sizePolicy11.setHeightForWidth(self.ManningPendienteComboBoxCaudal.sizePolicy().hasHeightForWidth())
        self.ManningPendienteComboBoxCaudal.setSizePolicy(sizePolicy11)
        self.ManningPendienteComboBoxCaudal.setMinimumSize(QSize(150, 36))
        self.ManningPendienteComboBoxCaudal.setMaximumSize(QSize(255, 16777215))
        self.ManningPendienteComboBoxCaudal.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningPendienteComboBoxCaudal.setEditable(True)
        self.ManningPendienteComboBoxCaudal.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_95.addWidget(self.ManningPendienteComboBoxCaudal, 0, 2, 1, 1)


        self.verticalLayout_66.addLayout(self.gridLayout_95)


        self.gridLayout_94.addWidget(self.row_46, 0, 0, 1, 1)

        self.groupBox_Propiedades_19 = QGroupBox(self.mngPendienteCritica)
        self.groupBox_Propiedades_19.setObjectName(u"groupBox_Propiedades_19")
        self.groupBox_Propiedades_19.setGeometry(QRect(10, 450, 621, 141))
        sizePolicy8.setHeightForWidth(self.groupBox_Propiedades_19.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_19.setSizePolicy(sizePolicy8)
        self.groupBox_Propiedades_19.setMinimumSize(QSize(400, 0))
        self.groupBox_Propiedades_19.setStyleSheet(u"QGroupBox {\n"
"color: rgb(176, 187, 209);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(176, 187, 209);\n"
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
        self.gridLayout_96 = QGridLayout(self.groupBox_Propiedades_19)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.row_47 = QFrame(self.groupBox_Propiedades_19)
        self.row_47.setObjectName(u"row_47")
        self.row_47.setStyleSheet(u"")
        self.row_47.setFrameShape(QFrame.StyledPanel)
        self.row_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.row_47)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_97 = QGridLayout()
        self.gridLayout_97.setSpacing(20)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.gridLayout_97.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_97.setContentsMargins(10, 20, 10, 20)
        self.ManningPendienteFieldProfundidadCritica = QLineEdit(self.row_47)
        self.ManningPendienteFieldProfundidadCritica.setObjectName(u"ManningPendienteFieldProfundidadCritica")
        sizePolicy11.setHeightForWidth(self.ManningPendienteFieldProfundidadCritica.sizePolicy().hasHeightForWidth())
        self.ManningPendienteFieldProfundidadCritica.setSizePolicy(sizePolicy11)
        self.ManningPendienteFieldProfundidadCritica.setMinimumSize(QSize(100, 30))
        self.ManningPendienteFieldProfundidadCritica.setMaximumSize(QSize(150, 30))
        self.ManningPendienteFieldProfundidadCritica.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(176, 187, 209);")

        self.gridLayout_97.addWidget(self.ManningPendienteFieldProfundidadCritica, 0, 1, 1, 1)

        self.ManningPendienteLabelProfundidadCritica = QLabel(self.row_47)
        self.ManningPendienteLabelProfundidadCritica.setObjectName(u"ManningPendienteLabelProfundidadCritica")
        sizePolicy6.setHeightForWidth(self.ManningPendienteLabelProfundidadCritica.sizePolicy().hasHeightForWidth())
        self.ManningPendienteLabelProfundidadCritica.setSizePolicy(sizePolicy6)
        self.ManningPendienteLabelProfundidadCritica.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningPendienteLabelProfundidadCritica.setLineWidth(1)
        self.ManningPendienteLabelProfundidadCritica.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_97.addWidget(self.ManningPendienteLabelProfundidadCritica, 0, 0, 1, 1)

        self.ManningPendienteComboBoxProfundidadCritica = QComboBox(self.row_47)
        self.ManningPendienteComboBoxProfundidadCritica.addItem("")
        self.ManningPendienteComboBoxProfundidadCritica.addItem("")
        self.ManningPendienteComboBoxProfundidadCritica.addItem("")
        self.ManningPendienteComboBoxProfundidadCritica.addItem("")
        self.ManningPendienteComboBoxProfundidadCritica.addItem("")
        self.ManningPendienteComboBoxProfundidadCritica.setObjectName(u"ManningPendienteComboBoxProfundidadCritica")
        sizePolicy5.setHeightForWidth(self.ManningPendienteComboBoxProfundidadCritica.sizePolicy().hasHeightForWidth())
        self.ManningPendienteComboBoxProfundidadCritica.setSizePolicy(sizePolicy5)
        self.ManningPendienteComboBoxProfundidadCritica.setMinimumSize(QSize(150, 30))
        self.ManningPendienteComboBoxProfundidadCritica.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(176, 187, 209);")
        self.ManningPendienteComboBoxProfundidadCritica.setEditable(True)

        self.gridLayout_97.addWidget(self.ManningPendienteComboBoxProfundidadCritica, 0, 2, 1, 1)


        self.verticalLayout_67.addLayout(self.gridLayout_97)


        self.gridLayout_96.addWidget(self.row_47, 0, 0, 1, 1)

        self.verticalLayoutWidget = QWidget(self.mngPendienteCritica)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 20, 423, 311))
        self.verticalLayout_21 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.geoCImagenCanal_10 = QPushButton(self.verticalLayoutWidget)
        self.geoCImagenCanal_10.setObjectName(u"geoCImagenCanal_10")
        self.geoCImagenCanal_10.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.geoCImagenCanal_10.sizePolicy().hasHeightForWidth())
        self.geoCImagenCanal_10.setSizePolicy(sizePolicy5)
        self.geoCImagenCanal_10.setMinimumSize(QSize(260, 213))
        self.geoCImagenCanal_10.setStyleSheet(u"border-image: url(:/geometria/images/geometria/Geometria-rectangular.PNG);\n"
"background-color: rgb(255,255,255);")
        self.geoCImagenCanal_10.setFlat(True)

        self.horizontalLayout_21.addWidget(self.geoCImagenCanal_10)


        self.verticalLayout_21.addLayout(self.horizontalLayout_21)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(10)
        self.gridLayout_10.setVerticalSpacing(0)
        self.ManningPendienteTextoReiniciar = QLabel(self.verticalLayoutWidget)
        self.ManningPendienteTextoReiniciar.setObjectName(u"ManningPendienteTextoReiniciar")
        sizePolicy5.setHeightForWidth(self.ManningPendienteTextoReiniciar.sizePolicy().hasHeightForWidth())
        self.ManningPendienteTextoReiniciar.setSizePolicy(sizePolicy5)
        self.ManningPendienteTextoReiniciar.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"\n"
"color: rgb(231, 230, 242);")
        self.ManningPendienteTextoReiniciar.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.ManningPendienteTextoReiniciar, 2, 1, 1, 1)

        self.ManningPendienteTextoCalcular = QLabel(self.verticalLayoutWidget)
        self.ManningPendienteTextoCalcular.setObjectName(u"ManningPendienteTextoCalcular")
        sizePolicy5.setHeightForWidth(self.ManningPendienteTextoCalcular.sizePolicy().hasHeightForWidth())
        self.ManningPendienteTextoCalcular.setSizePolicy(sizePolicy5)
        self.ManningPendienteTextoCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"\n"
"color: rgb(231, 230, 242);\n"
"")
        self.ManningPendienteTextoCalcular.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.ManningPendienteTextoCalcular, 2, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.ManningPendienteBotonCalcular = QPushButton(self.verticalLayoutWidget)
        self.ManningPendienteBotonCalcular.setObjectName(u"ManningPendienteBotonCalcular")
        self.ManningPendienteBotonCalcular.setMinimumSize(QSize(50, 50))
        self.ManningPendienteBotonCalcular.setMaximumSize(QSize(40, 40))
        self.ManningPendienteBotonCalcular.setStyleSheet(u"background-color: rgb(114, 161, 228);\n"
"border-color: rgb(114, 161, 228);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_22.addWidget(self.ManningPendienteBotonCalcular)


        self.gridLayout_10.addLayout(self.horizontalLayout_22, 0, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.ManningPendienteBotonReiniciar = QPushButton(self.verticalLayoutWidget)
        self.ManningPendienteBotonReiniciar.setObjectName(u"ManningPendienteBotonReiniciar")
        self.ManningPendienteBotonReiniciar.setMinimumSize(QSize(50, 50))
        self.ManningPendienteBotonReiniciar.setMaximumSize(QSize(40, 40))
        self.ManningPendienteBotonReiniciar.setStyleSheet(u"background-color: rgb(114, 161, 228);\n"
"border-color: rgb(114, 161, 228);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_23.addWidget(self.ManningPendienteBotonReiniciar)


        self.gridLayout_10.addLayout(self.horizontalLayout_23, 0, 1, 1, 1)

        self.gridLayout_10.setColumnStretch(0, 10)
        self.gridLayout_10.setColumnStretch(1, 10)
        self.gridLayout_10.setRowMinimumHeight(0, 10)
        self.gridLayout_10.setRowMinimumHeight(1, 10)

        self.verticalLayout_21.addLayout(self.gridLayout_10)

        self.tabManning.addTab(self.mngPendienteCritica, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"background-color: rgb(31, 37, 70);\n"
"border-color: rgb(50, 59, 113);\n"
"font: 500 11pt \"Allerta\";")
        self.groupBox_Propiedades_9 = QGroupBox(self.tab_2)
        self.groupBox_Propiedades_9.setObjectName(u"groupBox_Propiedades_9")
        self.groupBox_Propiedades_9.setGeometry(QRect(10, 13, 781, 451))
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_9.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_9.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_9.setMinimumSize(QSize(750, 0))
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
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_9.setAlignment(Qt.AlignCenter)
        self.gridLayout_51 = QGridLayout(self.groupBox_Propiedades_9)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_52 = QGridLayout()
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_52.setHorizontalSpacing(50)
        self.gridLayout_52.setVerticalSpacing(20)
        self.gridLayout_52.setContentsMargins(0, 20, 0, 10)
        self.ManningUniformeComboBoxBase = QComboBox(self.groupBox_Propiedades_9)
        self.ManningUniformeComboBoxBase.addItem("")
        self.ManningUniformeComboBoxBase.addItem("")
        self.ManningUniformeComboBoxBase.addItem("")
        self.ManningUniformeComboBoxBase.addItem("")
        self.ManningUniformeComboBoxBase.setObjectName(u"ManningUniformeComboBoxBase")
        sizePolicy5.setHeightForWidth(self.ManningUniformeComboBoxBase.sizePolicy().hasHeightForWidth())
        self.ManningUniformeComboBoxBase.setSizePolicy(sizePolicy5)
        self.ManningUniformeComboBoxBase.setMinimumSize(QSize(246, 30))
        self.ManningUniformeComboBoxBase.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningUniformeComboBoxBase.setEditable(True)

        self.gridLayout_52.addWidget(self.ManningUniformeComboBoxBase, 0, 3, 1, 1)

        self.ManningUniformeLabelPendienteLateral2 = QLabel(self.groupBox_Propiedades_9)
        self.ManningUniformeLabelPendienteLateral2.setObjectName(u"ManningUniformeLabelPendienteLateral2")
        sizePolicy6.setHeightForWidth(self.ManningUniformeLabelPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.ManningUniformeLabelPendienteLateral2.setSizePolicy(sizePolicy6)
        self.ManningUniformeLabelPendienteLateral2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningUniformeLabelPendienteLateral2.setLineWidth(1)
        self.ManningUniformeLabelPendienteLateral2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.ManningUniformeLabelPendienteLateral2, 5, 0, 1, 1)

        self.ManningUniformeLabelPendienteLateral = QLabel(self.groupBox_Propiedades_9)
        self.ManningUniformeLabelPendienteLateral.setObjectName(u"ManningUniformeLabelPendienteLateral")
        sizePolicy6.setHeightForWidth(self.ManningUniformeLabelPendienteLateral.sizePolicy().hasHeightForWidth())
        self.ManningUniformeLabelPendienteLateral.setSizePolicy(sizePolicy6)
        self.ManningUniformeLabelPendienteLateral.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningUniformeLabelPendienteLateral.setLineWidth(1)
        self.ManningUniformeLabelPendienteLateral.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.ManningUniformeLabelPendienteLateral, 4, 0, 1, 1)

        self.ManningUniformeComboBoxDiametro = QComboBox(self.groupBox_Propiedades_9)
        self.ManningUniformeComboBoxDiametro.addItem("")
        self.ManningUniformeComboBoxDiametro.addItem("")
        self.ManningUniformeComboBoxDiametro.addItem("")
        self.ManningUniformeComboBoxDiametro.addItem("")
        self.ManningUniformeComboBoxDiametro.setObjectName(u"ManningUniformeComboBoxDiametro")
        sizePolicy5.setHeightForWidth(self.ManningUniformeComboBoxDiametro.sizePolicy().hasHeightForWidth())
        self.ManningUniformeComboBoxDiametro.setSizePolicy(sizePolicy5)
        self.ManningUniformeComboBoxDiametro.setMinimumSize(QSize(246, 30))
        self.ManningUniformeComboBoxDiametro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningUniformeComboBoxDiametro.setEditable(True)

        self.gridLayout_52.addWidget(self.ManningUniformeComboBoxDiametro, 1, 3, 1, 1)

        self.ManningUniformeFieldPendienteLateral2 = QLineEdit(self.groupBox_Propiedades_9)
        self.ManningUniformeFieldPendienteLateral2.setObjectName(u"ManningUniformeFieldPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.ManningUniformeFieldPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.ManningUniformeFieldPendienteLateral2.setSizePolicy(sizePolicy5)
        self.ManningUniformeFieldPendienteLateral2.setMinimumSize(QSize(150, 30))
        self.ManningUniformeFieldPendienteLateral2.setMaximumSize(QSize(16777215, 30))
        self.ManningUniformeFieldPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_52.addWidget(self.ManningUniformeFieldPendienteLateral2, 5, 1, 1, 1)

        self.ManningUniformeComboBoxPendienteLateral2 = QComboBox(self.groupBox_Propiedades_9)
        self.ManningUniformeComboBoxPendienteLateral2.addItem("")
        self.ManningUniformeComboBoxPendienteLateral2.addItem("")
        self.ManningUniformeComboBoxPendienteLateral2.addItem("")
        self.ManningUniformeComboBoxPendienteLateral2.setObjectName(u"ManningUniformeComboBoxPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.ManningUniformeComboBoxPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.ManningUniformeComboBoxPendienteLateral2.setSizePolicy(sizePolicy5)
        self.ManningUniformeComboBoxPendienteLateral2.setMinimumSize(QSize(246, 30))
        self.ManningUniformeComboBoxPendienteLateral2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningUniformeComboBoxPendienteLateral2.setEditable(True)

        self.gridLayout_52.addWidget(self.ManningUniformeComboBoxPendienteLateral2, 5, 3, 1, 1)

        self.ManningUniformeFieldDiametro = QLineEdit(self.groupBox_Propiedades_9)
        self.ManningUniformeFieldDiametro.setObjectName(u"ManningUniformeFieldDiametro")
        sizePolicy5.setHeightForWidth(self.ManningUniformeFieldDiametro.sizePolicy().hasHeightForWidth())
        self.ManningUniformeFieldDiametro.setSizePolicy(sizePolicy5)
        self.ManningUniformeFieldDiametro.setMinimumSize(QSize(150, 30))
        self.ManningUniformeFieldDiametro.setMaximumSize(QSize(16777215, 30))
        self.ManningUniformeFieldDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_52.addWidget(self.ManningUniformeFieldDiametro, 1, 1, 1, 1)

        self.ManningUniformeFieldCaudal = QLineEdit(self.groupBox_Propiedades_9)
        self.ManningUniformeFieldCaudal.setObjectName(u"ManningUniformeFieldCaudal")
        sizePolicy5.setHeightForWidth(self.ManningUniformeFieldCaudal.sizePolicy().hasHeightForWidth())
        self.ManningUniformeFieldCaudal.setSizePolicy(sizePolicy5)
        self.ManningUniformeFieldCaudal.setMinimumSize(QSize(150, 30))
        self.ManningUniformeFieldCaudal.setMaximumSize(QSize(16777215, 30))
        self.ManningUniformeFieldCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_52.addWidget(self.ManningUniformeFieldCaudal, 2, 1, 1, 1)

        self.ManningUniformeFieldInclinacion = QLineEdit(self.groupBox_Propiedades_9)
        self.ManningUniformeFieldInclinacion.setObjectName(u"ManningUniformeFieldInclinacion")
        sizePolicy5.setHeightForWidth(self.ManningUniformeFieldInclinacion.sizePolicy().hasHeightForWidth())
        self.ManningUniformeFieldInclinacion.setSizePolicy(sizePolicy5)
        self.ManningUniformeFieldInclinacion.setMinimumSize(QSize(150, 30))
        self.ManningUniformeFieldInclinacion.setMaximumSize(QSize(16777215, 30))
        self.ManningUniformeFieldInclinacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_52.addWidget(self.ManningUniformeFieldInclinacion, 3, 1, 1, 1)

        self.ManningUniformeLabelCaudal = QLabel(self.groupBox_Propiedades_9)
        self.ManningUniformeLabelCaudal.setObjectName(u"ManningUniformeLabelCaudal")
        sizePolicy6.setHeightForWidth(self.ManningUniformeLabelCaudal.sizePolicy().hasHeightForWidth())
        self.ManningUniformeLabelCaudal.setSizePolicy(sizePolicy6)
        self.ManningUniformeLabelCaudal.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningUniformeLabelCaudal.setLineWidth(1)
        self.ManningUniformeLabelCaudal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.ManningUniformeLabelCaudal, 2, 0, 1, 1)

        self.ManningUniformeLabelBase = QLabel(self.groupBox_Propiedades_9)
        self.ManningUniformeLabelBase.setObjectName(u"ManningUniformeLabelBase")
        sizePolicy6.setHeightForWidth(self.ManningUniformeLabelBase.sizePolicy().hasHeightForWidth())
        self.ManningUniformeLabelBase.setSizePolicy(sizePolicy6)
        self.ManningUniformeLabelBase.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningUniformeLabelBase.setLineWidth(1)
        self.ManningUniformeLabelBase.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.ManningUniformeLabelBase, 0, 0, 1, 1)

        self.ManningUniformeLabelInclinacion = QLabel(self.groupBox_Propiedades_9)
        self.ManningUniformeLabelInclinacion.setObjectName(u"ManningUniformeLabelInclinacion")
        sizePolicy6.setHeightForWidth(self.ManningUniformeLabelInclinacion.sizePolicy().hasHeightForWidth())
        self.ManningUniformeLabelInclinacion.setSizePolicy(sizePolicy6)
        self.ManningUniformeLabelInclinacion.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningUniformeLabelInclinacion.setLineWidth(1)
        self.ManningUniformeLabelInclinacion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.ManningUniformeLabelInclinacion, 3, 0, 1, 1)

        self.ManningUniformeComboBoxCaudal = QComboBox(self.groupBox_Propiedades_9)
        self.ManningUniformeComboBoxCaudal.addItem("")
        self.ManningUniformeComboBoxCaudal.addItem("")
        self.ManningUniformeComboBoxCaudal.setObjectName(u"ManningUniformeComboBoxCaudal")
        sizePolicy11.setHeightForWidth(self.ManningUniformeComboBoxCaudal.sizePolicy().hasHeightForWidth())
        self.ManningUniformeComboBoxCaudal.setSizePolicy(sizePolicy11)
        self.ManningUniformeComboBoxCaudal.setMinimumSize(QSize(150, 36))
        self.ManningUniformeComboBoxCaudal.setMaximumSize(QSize(255, 16777215))
        self.ManningUniformeComboBoxCaudal.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningUniformeComboBoxCaudal.setEditable(True)
        self.ManningUniformeComboBoxCaudal.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_52.addWidget(self.ManningUniformeComboBoxCaudal, 2, 3, 1, 1)

        self.ManningUniformeLabelDiametro = QLabel(self.groupBox_Propiedades_9)
        self.ManningUniformeLabelDiametro.setObjectName(u"ManningUniformeLabelDiametro")
        sizePolicy6.setHeightForWidth(self.ManningUniformeLabelDiametro.sizePolicy().hasHeightForWidth())
        self.ManningUniformeLabelDiametro.setSizePolicy(sizePolicy6)
        self.ManningUniformeLabelDiametro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningUniformeLabelDiametro.setLineWidth(1)
        self.ManningUniformeLabelDiametro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.ManningUniformeLabelDiametro, 1, 0, 1, 1)

        self.ManningUniformeFieldPendienteLateral = QLineEdit(self.groupBox_Propiedades_9)
        self.ManningUniformeFieldPendienteLateral.setObjectName(u"ManningUniformeFieldPendienteLateral")
        sizePolicy5.setHeightForWidth(self.ManningUniformeFieldPendienteLateral.sizePolicy().hasHeightForWidth())
        self.ManningUniformeFieldPendienteLateral.setSizePolicy(sizePolicy5)
        self.ManningUniformeFieldPendienteLateral.setMinimumSize(QSize(150, 30))
        self.ManningUniformeFieldPendienteLateral.setMaximumSize(QSize(16777215, 30))
        self.ManningUniformeFieldPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_52.addWidget(self.ManningUniformeFieldPendienteLateral, 4, 1, 1, 1)

        self.ManningUniformeComboBoxPendienteLateral = QComboBox(self.groupBox_Propiedades_9)
        self.ManningUniformeComboBoxPendienteLateral.addItem("")
        self.ManningUniformeComboBoxPendienteLateral.addItem("")
        self.ManningUniformeComboBoxPendienteLateral.addItem("")
        self.ManningUniformeComboBoxPendienteLateral.setObjectName(u"ManningUniformeComboBoxPendienteLateral")
        sizePolicy5.setHeightForWidth(self.ManningUniformeComboBoxPendienteLateral.sizePolicy().hasHeightForWidth())
        self.ManningUniformeComboBoxPendienteLateral.setSizePolicy(sizePolicy5)
        self.ManningUniformeComboBoxPendienteLateral.setMinimumSize(QSize(246, 30))
        self.ManningUniformeComboBoxPendienteLateral.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningUniformeComboBoxPendienteLateral.setEditable(True)

        self.gridLayout_52.addWidget(self.ManningUniformeComboBoxPendienteLateral, 4, 3, 1, 1)

        self.ManningUniformeFieldBase = QLineEdit(self.groupBox_Propiedades_9)
        self.ManningUniformeFieldBase.setObjectName(u"ManningUniformeFieldBase")
        sizePolicy7.setHeightForWidth(self.ManningUniformeFieldBase.sizePolicy().hasHeightForWidth())
        self.ManningUniformeFieldBase.setSizePolicy(sizePolicy7)
        self.ManningUniformeFieldBase.setMinimumSize(QSize(150, 30))
        self.ManningUniformeFieldBase.setMaximumSize(QSize(16777215, 30))
        self.ManningUniformeFieldBase.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_52.addWidget(self.ManningUniformeFieldBase, 0, 1, 1, 1)

        self.ManningUniformeLabelNumManning = QLabel(self.groupBox_Propiedades_9)
        self.ManningUniformeLabelNumManning.setObjectName(u"ManningUniformeLabelNumManning")
        sizePolicy6.setHeightForWidth(self.ManningUniformeLabelNumManning.sizePolicy().hasHeightForWidth())
        self.ManningUniformeLabelNumManning.setSizePolicy(sizePolicy6)
        self.ManningUniformeLabelNumManning.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningUniformeLabelNumManning.setLineWidth(1)
        self.ManningUniformeLabelNumManning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.ManningUniformeLabelNumManning, 6, 0, 1, 1)

        self.ManningUniformeFieldNumManning = QLineEdit(self.groupBox_Propiedades_9)
        self.ManningUniformeFieldNumManning.setObjectName(u"ManningUniformeFieldNumManning")
        sizePolicy5.setHeightForWidth(self.ManningUniformeFieldNumManning.sizePolicy().hasHeightForWidth())
        self.ManningUniformeFieldNumManning.setSizePolicy(sizePolicy5)
        self.ManningUniformeFieldNumManning.setMinimumSize(QSize(150, 30))
        self.ManningUniformeFieldNumManning.setMaximumSize(QSize(16777215, 30))
        self.ManningUniformeFieldNumManning.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_52.addWidget(self.ManningUniformeFieldNumManning, 6, 1, 1, 1)

        self.ManningUniformeComboBoxInclinacion = QComboBox(self.groupBox_Propiedades_9)
        self.ManningUniformeComboBoxInclinacion.addItem("")
        self.ManningUniformeComboBoxInclinacion.addItem("")
        self.ManningUniformeComboBoxInclinacion.addItem("")
        self.ManningUniformeComboBoxInclinacion.setObjectName(u"ManningUniformeComboBoxInclinacion")
        sizePolicy5.setHeightForWidth(self.ManningUniformeComboBoxInclinacion.sizePolicy().hasHeightForWidth())
        self.ManningUniformeComboBoxInclinacion.setSizePolicy(sizePolicy5)
        self.ManningUniformeComboBoxInclinacion.setMinimumSize(QSize(246, 30))
        self.ManningUniformeComboBoxInclinacion.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningUniformeComboBoxInclinacion.setEditable(True)

        self.gridLayout_52.addWidget(self.ManningUniformeComboBoxInclinacion, 3, 3, 1, 1)

        self.ManningUniformeComboBoxNumManning = QComboBox(self.groupBox_Propiedades_9)
        self.ManningUniformeComboBoxNumManning.addItem("")
        self.ManningUniformeComboBoxNumManning.addItem("")
        self.ManningUniformeComboBoxNumManning.addItem("")
        self.ManningUniformeComboBoxNumManning.setObjectName(u"ManningUniformeComboBoxNumManning")
        sizePolicy5.setHeightForWidth(self.ManningUniformeComboBoxNumManning.sizePolicy().hasHeightForWidth())
        self.ManningUniformeComboBoxNumManning.setSizePolicy(sizePolicy5)
        self.ManningUniformeComboBoxNumManning.setMinimumSize(QSize(150, 30))
        self.ManningUniformeComboBoxNumManning.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(211, 212, 216);")
        self.ManningUniformeComboBoxNumManning.setEditable(True)

        self.gridLayout_52.addWidget(self.ManningUniformeComboBoxNumManning, 6, 3, 1, 1)


        self.gridLayout_51.addLayout(self.gridLayout_52, 0, 0, 1, 1)

        self.row_25 = QFrame(self.groupBox_Propiedades_9)
        self.row_25.setObjectName(u"row_25")
        self.row_25.setStyleSheet(u"")
        self.row_25.setFrameShape(QFrame.StyledPanel)
        self.row_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.row_25)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_51.addWidget(self.row_25, 1, 0, 1, 1)

        self.groupBox_Resultados_9 = QGroupBox(self.tab_2)
        self.groupBox_Resultados_9.setObjectName(u"groupBox_Resultados_9")
        self.groupBox_Resultados_9.setGeometry(QRect(10, 488, 1070, 111))
        sizePolicy11.setHeightForWidth(self.groupBox_Resultados_9.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_9.setSizePolicy(sizePolicy11)
        self.groupBox_Resultados_9.setStyleSheet(u"QGroupBox {\n"
"color: rgb(114, 161, 228);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(114, 161, 228);\n"
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
        self.gridLayout_53 = QGridLayout(self.groupBox_Resultados_9)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.row_26 = QFrame(self.groupBox_Resultados_9)
        self.row_26.setObjectName(u"row_26")
        self.row_26.setStyleSheet(u"")
        self.row_26.setFrameShape(QFrame.StyledPanel)
        self.row_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.row_26)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_54 = QGridLayout()
        self.gridLayout_54.setSpacing(15)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_54.setContentsMargins(15, 15, 15, 15)
        self.ManningUniformeLabelNormal = QLabel(self.row_26)
        self.ManningUniformeLabelNormal.setObjectName(u"ManningUniformeLabelNormal")
        sizePolicy6.setHeightForWidth(self.ManningUniformeLabelNormal.sizePolicy().hasHeightForWidth())
        self.ManningUniformeLabelNormal.setSizePolicy(sizePolicy6)
        self.ManningUniformeLabelNormal.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 650 11pt \"Allerta\";")
        self.ManningUniformeLabelNormal.setLineWidth(1)
        self.ManningUniformeLabelNormal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_54.addWidget(self.ManningUniformeLabelNormal, 0, 0, 1, 1)

        self.geoCFieldAngulo_4 = QLineEdit(self.row_26)
        self.geoCFieldAngulo_4.setObjectName(u"geoCFieldAngulo_4")
        sizePolicy5.setHeightForWidth(self.geoCFieldAngulo_4.sizePolicy().hasHeightForWidth())
        self.geoCFieldAngulo_4.setSizePolicy(sizePolicy5)
        self.geoCFieldAngulo_4.setMinimumSize(QSize(0, 30))
        self.geoCFieldAngulo_4.setMaximumSize(QSize(16777215, 30))
        self.geoCFieldAngulo_4.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_54.addWidget(self.geoCFieldAngulo_4, 0, 1, 1, 1)


        self.verticalLayout_46.addLayout(self.gridLayout_54)


        self.gridLayout_53.addWidget(self.row_26, 1, 0, 1, 1)

        self.verticalLayoutWidget_2 = QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(810, 30, 261, 241))
        self.verticalLayout_26 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setHorizontalSpacing(10)
        self.gridLayout_20.setVerticalSpacing(30)
        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
".checkbox label:after {\n"
"  content: '';\n"
"  display: table;\n"
"  clear: both;\n"
"}\n"
"\n"
".checkbox .cr {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border: 1px solid #a9a9a9;\n"
"  border-radius: .25em;\n"
"  width: 1.3em;\n"
"  height: 1.3em;\n"
"  float: left;\n"
"  margin-right: .5em;\n"
"}")

        self.gridLayout_20.addWidget(self.checkBox_3, 1, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
".checkbox label:after,\n"
".radio label:after {\n"
"  content: '';\n"
"  display: table;\n"
"  clear: both;\n"
"}\n"
"\n"
".checkbox .cr,\n"
".radio .cr {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border: 1px solid #a9a9a9;\n"
"  border-radius: .25em;\n"
"  width: 1.3em;\n"
"  height: 1.3em;\n"
"  float: left;\n"
"  margin-right: .5em;\n"
"}\n"
"\n"
".radio .cr {\n"
"  border-radius: 50%;\n"
"}\n"
"\n"
".checkbox .cr .cr-icon,\n"
".radio .cr .cr-icon {\n"
"  position: absolute;\n"
"  font-size: .8em;\n"
"  line-height: 0;\n"
"  top: 50%;\n"
"  left: 13%;\n"
"}\n"
"\n"
".radio .cr .cr-icon {\n"
"  margin-left: 0.04em;\n"
"}")

        self.gridLayout_20.addWidget(self.checkBox_2, 0, 0, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(60)
        self.gridLayout_14.setVerticalSpacing(0)
        self.ManningUniformeTextoReiniciar = QLabel(self.verticalLayoutWidget_2)
        self.ManningUniformeTextoReiniciar.setObjectName(u"ManningUniformeTextoReiniciar")
        sizePolicy5.setHeightForWidth(self.ManningUniformeTextoReiniciar.sizePolicy().hasHeightForWidth())
        self.ManningUniformeTextoReiniciar.setSizePolicy(sizePolicy5)
        self.ManningUniformeTextoReiniciar.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"\n"
"color: rgb(231, 230, 242);")
        self.ManningUniformeTextoReiniciar.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ManningUniformeTextoReiniciar, 2, 1, 1, 1)

        self.ManningUniformeTextoCalcular = QLabel(self.verticalLayoutWidget_2)
        self.ManningUniformeTextoCalcular.setObjectName(u"ManningUniformeTextoCalcular")
        sizePolicy5.setHeightForWidth(self.ManningUniformeTextoCalcular.sizePolicy().hasHeightForWidth())
        self.ManningUniformeTextoCalcular.setSizePolicy(sizePolicy5)
        self.ManningUniformeTextoCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"\n"
"color: rgb(231, 230, 242);\n"
"")
        self.ManningUniformeTextoCalcular.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ManningUniformeTextoCalcular, 2, 0, 1, 1)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.ManningUniformeBotonCalcular = QPushButton(self.verticalLayoutWidget_2)
        self.ManningUniformeBotonCalcular.setObjectName(u"ManningUniformeBotonCalcular")
        self.ManningUniformeBotonCalcular.setMinimumSize(QSize(50, 50))
        self.ManningUniformeBotonCalcular.setMaximumSize(QSize(40, 40))
        self.ManningUniformeBotonCalcular.setStyleSheet(u"background-color: rgb(114, 161, 228);\n"
"border-color: rgb(114, 161, 228);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_32.addWidget(self.ManningUniformeBotonCalcular)


        self.gridLayout_14.addLayout(self.horizontalLayout_32, 0, 0, 1, 1)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.ManningUniformeBotonReiniciar = QPushButton(self.verticalLayoutWidget_2)
        self.ManningUniformeBotonReiniciar.setObjectName(u"ManningUniformeBotonReiniciar")
        self.ManningUniformeBotonReiniciar.setMinimumSize(QSize(50, 50))
        self.ManningUniformeBotonReiniciar.setMaximumSize(QSize(40, 40))
        self.ManningUniformeBotonReiniciar.setStyleSheet(u"background-color: rgb(114, 161, 228);\n"
"border-color: rgb(114, 161, 228);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_33.addWidget(self.ManningUniformeBotonReiniciar)


        self.gridLayout_14.addLayout(self.horizontalLayout_33, 0, 1, 1, 1)

        self.gridLayout_14.setColumnStretch(0, 10)
        self.gridLayout_14.setColumnStretch(1, 10)
        self.gridLayout_14.setRowMinimumHeight(0, 10)
        self.gridLayout_14.setRowMinimumHeight(1, 10)

        self.gridLayout_20.addLayout(self.gridLayout_14, 2, 0, 1, 1)


        self.verticalLayout_26.addLayout(self.gridLayout_20)

        self.tabManning.addTab(self.tab_2, "")
        self.stackedWidget.addWidget(self.pagina_manning)
        self.pagina_FGV = QWidget()
        self.pagina_FGV.setObjectName(u"pagina_FGV")
        self.tabFGV = QTabWidget(self.pagina_FGV)
        self.tabFGV.setObjectName(u"tabFGV")
        self.tabFGV.setGeometry(QRect(0, 0, 1121, 613))
        sizePolicy13.setHeightForWidth(self.tabFGV.sizePolicy().hasHeightForWidth())
        self.tabFGV.setSizePolicy(sizePolicy13)
        self.tabFGV.setStyleSheet(u"font: 500 10pt \"Allerta\";\n"
"color: rgb(79, 79, 79);")
        self.tabFGV.setTabPosition(QTabWidget.West)
        self.rhLongitud = QWidget()
        self.rhLongitud.setObjectName(u"rhLongitud")
        self.rhLongitud.setStyleSheet(u"\n"
"font: 500 11pt \"Allerta\";")
        self.groupBox_Propiedades_21 = QGroupBox(self.rhLongitud)
        self.groupBox_Propiedades_21.setObjectName(u"groupBox_Propiedades_21")
        self.groupBox_Propiedades_21.setGeometry(QRect(20, 10, 750, 441))
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_21.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_21.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_21.setMinimumSize(QSize(750, 0))
        self.groupBox_Propiedades_21.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_21.setStyleSheet(u"QGroupBox {\n"
"color: rgb(217, 165, 181);\n"
"font: bold; \n"
"border: 2px solid;\n"
"border-color: rgb(217, 165, 181);\n"
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
        self.FGVFieldAncho = QLineEdit(self.row_45)
        self.FGVFieldAncho.setObjectName(u"FGVFieldAncho")
        sizePolicy15.setHeightForWidth(self.FGVFieldAncho.sizePolicy().hasHeightForWidth())
        self.FGVFieldAncho.setSizePolicy(sizePolicy15)
        self.FGVFieldAncho.setMinimumSize(QSize(110, 30))
        self.FGVFieldAncho.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.FGVFieldAncho.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.FGVFieldAncho.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_98.addWidget(self.FGVFieldAncho, 0, 1, 1, 1)

        self.FGVFieldPendienteLateral2 = QLineEdit(self.row_45)
        self.FGVFieldPendienteLateral2.setObjectName(u"FGVFieldPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.FGVFieldPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.FGVFieldPendienteLateral2.setSizePolicy(sizePolicy5)
        self.FGVFieldPendienteLateral2.setMinimumSize(QSize(0, 30))
        self.FGVFieldPendienteLateral2.setMaximumSize(QSize(150, 16777215))
        self.FGVFieldPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_98.addWidget(self.FGVFieldPendienteLateral2, 5, 1, 1, 1)

        self.FGVFieldProfundidad2 = QLineEdit(self.row_45)
        self.FGVFieldProfundidad2.setObjectName(u"FGVFieldProfundidad2")
        sizePolicy5.setHeightForWidth(self.FGVFieldProfundidad2.sizePolicy().hasHeightForWidth())
        self.FGVFieldProfundidad2.setSizePolicy(sizePolicy5)
        self.FGVFieldProfundidad2.setMinimumSize(QSize(0, 30))
        self.FGVFieldProfundidad2.setMaximumSize(QSize(150, 16777215))
        self.FGVFieldProfundidad2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_98.addWidget(self.FGVFieldProfundidad2, 7, 1, 1, 1)

        self.FGVLabelProfundidad1 = QLabel(self.row_45)
        self.FGVLabelProfundidad1.setObjectName(u"FGVLabelProfundidad1")
        sizePolicy6.setHeightForWidth(self.FGVLabelProfundidad1.sizePolicy().hasHeightForWidth())
        self.FGVLabelProfundidad1.setSizePolicy(sizePolicy6)
        self.FGVLabelProfundidad1.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVLabelProfundidad1.setLineWidth(1)
        self.FGVLabelProfundidad1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_98.addWidget(self.FGVLabelProfundidad1, 6, 0, 1, 1)

        self.FGVFieldInclinacion = QLineEdit(self.row_45)
        self.FGVFieldInclinacion.setObjectName(u"FGVFieldInclinacion")
        sizePolicy5.setHeightForWidth(self.FGVFieldInclinacion.sizePolicy().hasHeightForWidth())
        self.FGVFieldInclinacion.setSizePolicy(sizePolicy5)
        self.FGVFieldInclinacion.setMinimumSize(QSize(0, 30))
        self.FGVFieldInclinacion.setMaximumSize(QSize(150, 16777215))
        self.FGVFieldInclinacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_98.addWidget(self.FGVFieldInclinacion, 2, 1, 1, 1)

        self.FGVFieldPendienteLateral = QLineEdit(self.row_45)
        self.FGVFieldPendienteLateral.setObjectName(u"FGVFieldPendienteLateral")
        sizePolicy15.setHeightForWidth(self.FGVFieldPendienteLateral.sizePolicy().hasHeightForWidth())
        self.FGVFieldPendienteLateral.setSizePolicy(sizePolicy15)
        self.FGVFieldPendienteLateral.setMinimumSize(QSize(110, 30))
        self.FGVFieldPendienteLateral.setMaximumSize(QSize(150, 30))
        self.FGVFieldPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_98.addWidget(self.FGVFieldPendienteLateral, 4, 1, 1, 1)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setSpacing(0)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVComboBoxInclinacion = QComboBox(self.row_45)
        self.FGVComboBoxInclinacion.addItem("")
        self.FGVComboBoxInclinacion.addItem("")
        self.FGVComboBoxInclinacion.addItem("")
        self.FGVComboBoxInclinacion.setObjectName(u"FGVComboBoxInclinacion")
        sizePolicy14.setHeightForWidth(self.FGVComboBoxInclinacion.sizePolicy().hasHeightForWidth())
        self.FGVComboBoxInclinacion.setSizePolicy(sizePolicy14)
        self.FGVComboBoxInclinacion.setMinimumSize(QSize(234, 30))
        self.FGVComboBoxInclinacion.setMaximumSize(QSize(260, 16777215))
        self.FGVComboBoxInclinacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVComboBoxInclinacion.setEditable(True)
        self.FGVComboBoxInclinacion.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_92.addWidget(self.FGVComboBoxInclinacion)


        self.gridLayout_98.addLayout(self.horizontalLayout_92, 2, 2, 1, 1)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.FGVComboBoxCaudal = QComboBox(self.row_45)
        self.FGVComboBoxCaudal.addItem("")
        self.FGVComboBoxCaudal.addItem("")
        self.FGVComboBoxCaudal.setObjectName(u"FGVComboBoxCaudal")
        sizePolicy5.setHeightForWidth(self.FGVComboBoxCaudal.sizePolicy().hasHeightForWidth())
        self.FGVComboBoxCaudal.setSizePolicy(sizePolicy5)
        self.FGVComboBoxCaudal.setMinimumSize(QSize(150, 30))
        self.FGVComboBoxCaudal.setMaximumSize(QSize(260, 16777215))
        self.FGVComboBoxCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVComboBoxCaudal.setEditable(True)
        self.FGVComboBoxCaudal.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_89.addWidget(self.FGVComboBoxCaudal)


        self.gridLayout_98.addLayout(self.horizontalLayout_89, 8, 2, 1, 1)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVComboBoxPendienteLateral = QComboBox(self.row_45)
        self.FGVComboBoxPendienteLateral.addItem("")
        self.FGVComboBoxPendienteLateral.addItem("")
        self.FGVComboBoxPendienteLateral.addItem("")
        self.FGVComboBoxPendienteLateral.setObjectName(u"FGVComboBoxPendienteLateral")
        sizePolicy14.setHeightForWidth(self.FGVComboBoxPendienteLateral.sizePolicy().hasHeightForWidth())
        self.FGVComboBoxPendienteLateral.setSizePolicy(sizePolicy14)
        self.FGVComboBoxPendienteLateral.setMinimumSize(QSize(234, 30))
        self.FGVComboBoxPendienteLateral.setMaximumSize(QSize(260, 16777215))
        self.FGVComboBoxPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVComboBoxPendienteLateral.setEditable(True)
        self.FGVComboBoxPendienteLateral.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_65.addWidget(self.FGVComboBoxPendienteLateral)


        self.gridLayout_98.addLayout(self.horizontalLayout_65, 4, 2, 1, 1)

        self.FGVLabelInclinacion = QLabel(self.row_45)
        self.FGVLabelInclinacion.setObjectName(u"FGVLabelInclinacion")
        sizePolicy6.setHeightForWidth(self.FGVLabelInclinacion.sizePolicy().hasHeightForWidth())
        self.FGVLabelInclinacion.setSizePolicy(sizePolicy6)
        self.FGVLabelInclinacion.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVLabelInclinacion.setLineWidth(1)
        self.FGVLabelInclinacion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_98.addWidget(self.FGVLabelInclinacion, 2, 0, 1, 1)

        self.FGVLabelDiametro = QLabel(self.row_45)
        self.FGVLabelDiametro.setObjectName(u"FGVLabelDiametro")
        sizePolicy6.setHeightForWidth(self.FGVLabelDiametro.sizePolicy().hasHeightForWidth())
        self.FGVLabelDiametro.setSizePolicy(sizePolicy6)
        self.FGVLabelDiametro.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVLabelDiametro.setLineWidth(1)
        self.FGVLabelDiametro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_98.addWidget(self.FGVLabelDiametro, 1, 0, 1, 1)

        self.FGVLabelCaudal = QLabel(self.row_45)
        self.FGVLabelCaudal.setObjectName(u"FGVLabelCaudal")
        sizePolicy6.setHeightForWidth(self.FGVLabelCaudal.sizePolicy().hasHeightForWidth())
        self.FGVLabelCaudal.setSizePolicy(sizePolicy6)
        self.FGVLabelCaudal.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVLabelCaudal.setLineWidth(1)
        self.FGVLabelCaudal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_98.addWidget(self.FGVLabelCaudal, 8, 0, 1, 1)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.FGVComboBoxPendienteLateral2 = QComboBox(self.row_45)
        self.FGVComboBoxPendienteLateral2.addItem("")
        self.FGVComboBoxPendienteLateral2.addItem("")
        self.FGVComboBoxPendienteLateral2.addItem("")
        self.FGVComboBoxPendienteLateral2.setObjectName(u"FGVComboBoxPendienteLateral2")
        sizePolicy13.setHeightForWidth(self.FGVComboBoxPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.FGVComboBoxPendienteLateral2.setSizePolicy(sizePolicy13)
        self.FGVComboBoxPendienteLateral2.setMinimumSize(QSize(234, 30))
        self.FGVComboBoxPendienteLateral2.setMaximumSize(QSize(260, 16777215))
        self.FGVComboBoxPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVComboBoxPendienteLateral2.setEditable(True)
        self.FGVComboBoxPendienteLateral2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_85.addWidget(self.FGVComboBoxPendienteLateral2)


        self.gridLayout_98.addLayout(self.horizontalLayout_85, 5, 2, 1, 1)

        self.FGVFieldCaudal = QLineEdit(self.row_45)
        self.FGVFieldCaudal.setObjectName(u"FGVFieldCaudal")
        sizePolicy5.setHeightForWidth(self.FGVFieldCaudal.sizePolicy().hasHeightForWidth())
        self.FGVFieldCaudal.setSizePolicy(sizePolicy5)
        self.FGVFieldCaudal.setMinimumSize(QSize(0, 30))
        self.FGVFieldCaudal.setMaximumSize(QSize(150, 16777215))
        self.FGVFieldCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_98.addWidget(self.FGVFieldCaudal, 8, 1, 1, 1)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVComboBoxProfundidad2 = QComboBox(self.row_45)
        self.FGVComboBoxProfundidad2.addItem("")
        self.FGVComboBoxProfundidad2.addItem("")
        self.FGVComboBoxProfundidad2.addItem("")
        self.FGVComboBoxProfundidad2.addItem("")
        self.FGVComboBoxProfundidad2.setObjectName(u"FGVComboBoxProfundidad2")
        sizePolicy13.setHeightForWidth(self.FGVComboBoxProfundidad2.sizePolicy().hasHeightForWidth())
        self.FGVComboBoxProfundidad2.setSizePolicy(sizePolicy13)
        self.FGVComboBoxProfundidad2.setMinimumSize(QSize(150, 30))
        self.FGVComboBoxProfundidad2.setMaximumSize(QSize(260, 30))
        self.FGVComboBoxProfundidad2.setLayoutDirection(Qt.LeftToRight)
        self.FGVComboBoxProfundidad2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVComboBoxProfundidad2.setEditable(True)
        self.FGVComboBoxProfundidad2.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.FGVComboBoxProfundidad2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_94.addWidget(self.FGVComboBoxProfundidad2)


        self.gridLayout_98.addLayout(self.horizontalLayout_94, 7, 2, 1, 1)

        self.FGVLabelProfundidad2 = QLabel(self.row_45)
        self.FGVLabelProfundidad2.setObjectName(u"FGVLabelProfundidad2")
        sizePolicy6.setHeightForWidth(self.FGVLabelProfundidad2.sizePolicy().hasHeightForWidth())
        self.FGVLabelProfundidad2.setSizePolicy(sizePolicy6)
        self.FGVLabelProfundidad2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVLabelProfundidad2.setLineWidth(1)
        self.FGVLabelProfundidad2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_98.addWidget(self.FGVLabelProfundidad2, 7, 0, 1, 1)

        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVComboBoxProfundidad1 = QComboBox(self.row_45)
        self.FGVComboBoxProfundidad1.addItem("")
        self.FGVComboBoxProfundidad1.addItem("")
        self.FGVComboBoxProfundidad1.addItem("")
        self.FGVComboBoxProfundidad1.addItem("")
        self.FGVComboBoxProfundidad1.setObjectName(u"FGVComboBoxProfundidad1")
        sizePolicy13.setHeightForWidth(self.FGVComboBoxProfundidad1.sizePolicy().hasHeightForWidth())
        self.FGVComboBoxProfundidad1.setSizePolicy(sizePolicy13)
        self.FGVComboBoxProfundidad1.setMinimumSize(QSize(150, 30))
        self.FGVComboBoxProfundidad1.setMaximumSize(QSize(260, 30))
        self.FGVComboBoxProfundidad1.setLayoutDirection(Qt.LeftToRight)
        self.FGVComboBoxProfundidad1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVComboBoxProfundidad1.setEditable(True)
        self.FGVComboBoxProfundidad1.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.FGVComboBoxProfundidad1.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_91.addWidget(self.FGVComboBoxProfundidad1)


        self.gridLayout_98.addLayout(self.horizontalLayout_91, 6, 2, 1, 1)

        self.FGVFieldProfundidad1 = QLineEdit(self.row_45)
        self.FGVFieldProfundidad1.setObjectName(u"FGVFieldProfundidad1")
        sizePolicy5.setHeightForWidth(self.FGVFieldProfundidad1.sizePolicy().hasHeightForWidth())
        self.FGVFieldProfundidad1.setSizePolicy(sizePolicy5)
        self.FGVFieldProfundidad1.setMinimumSize(QSize(0, 30))
        self.FGVFieldProfundidad1.setMaximumSize(QSize(150, 16777215))
        self.FGVFieldProfundidad1.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_98.addWidget(self.FGVFieldProfundidad1, 6, 1, 1, 1)

        self.FGVLabelPendienteLateral = QLabel(self.row_45)
        self.FGVLabelPendienteLateral.setObjectName(u"FGVLabelPendienteLateral")
        sizePolicy6.setHeightForWidth(self.FGVLabelPendienteLateral.sizePolicy().hasHeightForWidth())
        self.FGVLabelPendienteLateral.setSizePolicy(sizePolicy6)
        self.FGVLabelPendienteLateral.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVLabelPendienteLateral.setLineWidth(1)
        self.FGVLabelPendienteLateral.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_98.addWidget(self.FGVLabelPendienteLateral, 4, 0, 1, 1)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVComboBoxAncho = QComboBox(self.row_45)
        self.FGVComboBoxAncho.addItem("")
        self.FGVComboBoxAncho.addItem("")
        self.FGVComboBoxAncho.addItem("")
        self.FGVComboBoxAncho.addItem("")
        self.FGVComboBoxAncho.setObjectName(u"FGVComboBoxAncho")
        sizePolicy13.setHeightForWidth(self.FGVComboBoxAncho.sizePolicy().hasHeightForWidth())
        self.FGVComboBoxAncho.setSizePolicy(sizePolicy13)
        self.FGVComboBoxAncho.setMinimumSize(QSize(150, 30))
        self.FGVComboBoxAncho.setMaximumSize(QSize(260, 30))
        self.FGVComboBoxAncho.setLayoutDirection(Qt.LeftToRight)
        self.FGVComboBoxAncho.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVComboBoxAncho.setEditable(True)
        self.FGVComboBoxAncho.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.FGVComboBoxAncho.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_90.addWidget(self.FGVComboBoxAncho)


        self.gridLayout_98.addLayout(self.horizontalLayout_90, 0, 2, 1, 1)

        self.FGVLabelAncho = QLabel(self.row_45)
        self.FGVLabelAncho.setObjectName(u"FGVLabelAncho")
        sizePolicy6.setHeightForWidth(self.FGVLabelAncho.sizePolicy().hasHeightForWidth())
        self.FGVLabelAncho.setSizePolicy(sizePolicy6)
        self.FGVLabelAncho.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVLabelAncho.setLineWidth(1)
        self.FGVLabelAncho.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_98.addWidget(self.FGVLabelAncho, 0, 0, 1, 1)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVComboBoxDiametro = QComboBox(self.row_45)
        self.FGVComboBoxDiametro.addItem("")
        self.FGVComboBoxDiametro.addItem("")
        self.FGVComboBoxDiametro.addItem("")
        self.FGVComboBoxDiametro.addItem("")
        self.FGVComboBoxDiametro.setObjectName(u"FGVComboBoxDiametro")
        sizePolicy13.setHeightForWidth(self.FGVComboBoxDiametro.sizePolicy().hasHeightForWidth())
        self.FGVComboBoxDiametro.setSizePolicy(sizePolicy13)
        self.FGVComboBoxDiametro.setMinimumSize(QSize(150, 30))
        self.FGVComboBoxDiametro.setMaximumSize(QSize(260, 30))
        self.FGVComboBoxDiametro.setLayoutDirection(Qt.LeftToRight)
        self.FGVComboBoxDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVComboBoxDiametro.setEditable(True)
        self.FGVComboBoxDiametro.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.FGVComboBoxDiametro.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_93.addWidget(self.FGVComboBoxDiametro)


        self.gridLayout_98.addLayout(self.horizontalLayout_93, 1, 2, 1, 1)

        self.FGVLabelPendienteLateral2 = QLabel(self.row_45)
        self.FGVLabelPendienteLateral2.setObjectName(u"FGVLabelPendienteLateral2")
        sizePolicy6.setHeightForWidth(self.FGVLabelPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.FGVLabelPendienteLateral2.setSizePolicy(sizePolicy6)
        self.FGVLabelPendienteLateral2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVLabelPendienteLateral2.setLineWidth(1)
        self.FGVLabelPendienteLateral2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_98.addWidget(self.FGVLabelPendienteLateral2, 5, 0, 1, 1)

        self.FGVFieldDiametro = QLineEdit(self.row_45)
        self.FGVFieldDiametro.setObjectName(u"FGVFieldDiametro")
        sizePolicy15.setHeightForWidth(self.FGVFieldDiametro.sizePolicy().hasHeightForWidth())
        self.FGVFieldDiametro.setSizePolicy(sizePolicy15)
        self.FGVFieldDiametro.setMinimumSize(QSize(110, 30))
        self.FGVFieldDiametro.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.FGVFieldDiametro.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.FGVFieldDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_98.addWidget(self.FGVFieldDiametro, 1, 1, 1, 1)

        self.FGVLabelManning = QLabel(self.row_45)
        self.FGVLabelManning.setObjectName(u"FGVLabelManning")
        sizePolicy6.setHeightForWidth(self.FGVLabelManning.sizePolicy().hasHeightForWidth())
        self.FGVLabelManning.setSizePolicy(sizePolicy6)
        self.FGVLabelManning.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVLabelManning.setLineWidth(1)
        self.FGVLabelManning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_98.addWidget(self.FGVLabelManning, 3, 0, 1, 1)

        self.FGVFieldNumManning = QLineEdit(self.row_45)
        self.FGVFieldNumManning.setObjectName(u"FGVFieldNumManning")
        sizePolicy5.setHeightForWidth(self.FGVFieldNumManning.sizePolicy().hasHeightForWidth())
        self.FGVFieldNumManning.setSizePolicy(sizePolicy5)
        self.FGVFieldNumManning.setMinimumSize(QSize(0, 30))
        self.FGVFieldNumManning.setMaximumSize(QSize(150, 16777215))
        self.FGVFieldNumManning.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_98.addWidget(self.FGVFieldNumManning, 3, 1, 1, 1)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setSizeConstraint(QLayout.SetMinimumSize)
        self.RHAnalisisComboBoxPendienteLateral_5 = QComboBox(self.row_45)
        self.RHAnalisisComboBoxPendienteLateral_5.addItem("")
        self.RHAnalisisComboBoxPendienteLateral_5.setObjectName(u"RHAnalisisComboBoxPendienteLateral_5")
        sizePolicy14.setHeightForWidth(self.RHAnalisisComboBoxPendienteLateral_5.sizePolicy().hasHeightForWidth())
        self.RHAnalisisComboBoxPendienteLateral_5.setSizePolicy(sizePolicy14)
        self.RHAnalisisComboBoxPendienteLateral_5.setMinimumSize(QSize(234, 30))
        self.RHAnalisisComboBoxPendienteLateral_5.setMaximumSize(QSize(260, 16777215))
        self.RHAnalisisComboBoxPendienteLateral_5.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.RHAnalisisComboBoxPendienteLateral_5.setEditable(True)
        self.RHAnalisisComboBoxPendienteLateral_5.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_95.addWidget(self.RHAnalisisComboBoxPendienteLateral_5)


        self.gridLayout_98.addLayout(self.horizontalLayout_95, 3, 2, 1, 1)


        self.verticalLayout_65.addLayout(self.gridLayout_98)


        self.gridLayout_93.addWidget(self.row_45, 0, 1, 1, 1)

        self.groupBox_Resultados_19 = QGroupBox(self.rhLongitud)
        self.groupBox_Resultados_19.setObjectName(u"groupBox_Resultados_19")
        self.groupBox_Resultados_19.setGeometry(QRect(20, 470, 1055, 121))
        sizePolicy17.setHeightForWidth(self.groupBox_Resultados_19.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_19.setSizePolicy(sizePolicy17)
        self.groupBox_Resultados_19.setMinimumSize(QSize(1055, 0))
        self.groupBox_Resultados_19.setMaximumSize(QSize(480, 16777215))
        self.groupBox_Resultados_19.setStyleSheet(u"QGroupBox {\n"
"color: rgb(217, 165, 181);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(217, 165, 181);\n"
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
        self.gridLayout_88.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_88.setHorizontalSpacing(10)
        self.gridLayout_88.setVerticalSpacing(15)
        self.gridLayout_88.setContentsMargins(10, 10, 10, 10)
        self.FGVFieldDistanciaX = QLineEdit(self.row_40)
        self.FGVFieldDistanciaX.setObjectName(u"FGVFieldDistanciaX")
        sizePolicy5.setHeightForWidth(self.FGVFieldDistanciaX.sizePolicy().hasHeightForWidth())
        self.FGVFieldDistanciaX.setSizePolicy(sizePolicy5)
        self.FGVFieldDistanciaX.setMinimumSize(QSize(0, 40))
        self.FGVFieldDistanciaX.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_88.addWidget(self.FGVFieldDistanciaX, 0, 1, 1, 1)

        self.FGVLabelDistanciaX = QLabel(self.row_40)
        self.FGVLabelDistanciaX.setObjectName(u"FGVLabelDistanciaX")
        sizePolicy6.setHeightForWidth(self.FGVLabelDistanciaX.sizePolicy().hasHeightForWidth())
        self.FGVLabelDistanciaX.setSizePolicy(sizePolicy6)
        self.FGVLabelDistanciaX.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVLabelDistanciaX.setLineWidth(1)
        self.FGVLabelDistanciaX.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_88.addWidget(self.FGVLabelDistanciaX, 0, 0, 1, 1)


        self.verticalLayout_60.addLayout(self.gridLayout_88)


        self.gridLayout_83.addWidget(self.row_40, 0, 0, 1, 1)

        self.RHAnalisisTextoCalcular_4 = QLabel(self.rhLongitud)
        self.RHAnalisisTextoCalcular_4.setObjectName(u"RHAnalisisTextoCalcular_4")
        self.RHAnalisisTextoCalcular_4.setGeometry(QRect(800, 30, 271, 91))
        sizePolicy5.setHeightForWidth(self.RHAnalisisTextoCalcular_4.sizePolicy().hasHeightForWidth())
        self.RHAnalisisTextoCalcular_4.setSizePolicy(sizePolicy5)
        self.RHAnalisisTextoCalcular_4.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"")
        self.RHAnalisisTextoCalcular_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.verticalLayoutWidget_3 = QWidget(self.rhLongitud)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(800, 130, 264, 312))
        self.verticalLayout_25 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.geoCImagenCanal_11 = QPushButton(self.verticalLayoutWidget_3)
        self.geoCImagenCanal_11.setObjectName(u"geoCImagenCanal_11")
        self.geoCImagenCanal_11.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.geoCImagenCanal_11.sizePolicy().hasHeightForWidth())
        self.geoCImagenCanal_11.setSizePolicy(sizePolicy5)
        self.geoCImagenCanal_11.setMinimumSize(QSize(260, 213))
        self.geoCImagenCanal_11.setStyleSheet(u"border-image: url(:/geometria/images/geometria/Geometria-rectangular.PNG);\n"
"background-color: rgb(255,255,255);")
        self.geoCImagenCanal_11.setFlat(True)

        self.horizontalLayout_39.addWidget(self.geoCImagenCanal_11)


        self.verticalLayout_25.addLayout(self.horizontalLayout_39)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setHorizontalSpacing(10)
        self.gridLayout_24.setVerticalSpacing(0)
        self.FGVTextoReiniciar = QLabel(self.verticalLayoutWidget_3)
        self.FGVTextoReiniciar.setObjectName(u"FGVTextoReiniciar")
        sizePolicy5.setHeightForWidth(self.FGVTextoReiniciar.sizePolicy().hasHeightForWidth())
        self.FGVTextoReiniciar.setSizePolicy(sizePolicy5)
        self.FGVTextoReiniciar.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"")
        self.FGVTextoReiniciar.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.FGVTextoReiniciar, 2, 1, 1, 1)

        self.FGVTextoCalcular = QLabel(self.verticalLayoutWidget_3)
        self.FGVTextoCalcular.setObjectName(u"FGVTextoCalcular")
        sizePolicy5.setHeightForWidth(self.FGVTextoCalcular.sizePolicy().hasHeightForWidth())
        self.FGVTextoCalcular.setSizePolicy(sizePolicy5)
        self.FGVTextoCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.FGVTextoCalcular.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.FGVTextoCalcular, 2, 0, 1, 1)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.FGVBotonCalcular = QPushButton(self.verticalLayoutWidget_3)
        self.FGVBotonCalcular.setObjectName(u"FGVBotonCalcular")
        self.FGVBotonCalcular.setMinimumSize(QSize(50, 50))
        self.FGVBotonCalcular.setMaximumSize(QSize(40, 40))
        self.FGVBotonCalcular.setStyleSheet(u"background-color: rgb(217, 165, 181);\n"
"border-color: rgb(217, 165, 181);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_40.addWidget(self.FGVBotonCalcular)


        self.gridLayout_24.addLayout(self.horizontalLayout_40, 0, 0, 1, 1)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.FGVBotonReiniciar = QPushButton(self.verticalLayoutWidget_3)
        self.FGVBotonReiniciar.setObjectName(u"FGVBotonReiniciar")
        self.FGVBotonReiniciar.setMinimumSize(QSize(50, 50))
        self.FGVBotonReiniciar.setMaximumSize(QSize(40, 40))
        self.FGVBotonReiniciar.setStyleSheet(u"background-color: rgb(217, 165, 181);\n"
"border-color: rgb(217, 165, 181);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_41.addWidget(self.FGVBotonReiniciar)


        self.gridLayout_24.addLayout(self.horizontalLayout_41, 0, 1, 1, 1)

        self.gridLayout_24.setColumnStretch(0, 10)
        self.gridLayout_24.setColumnStretch(1, 10)
        self.gridLayout_24.setRowMinimumHeight(0, 10)
        self.gridLayout_24.setRowMinimumHeight(1, 10)

        self.verticalLayout_25.addLayout(self.gridLayout_24)

        self.tabFGV.addTab(self.rhLongitud, "")
        self.rhPasoDirecto = QWidget()
        self.rhPasoDirecto.setObjectName(u"rhPasoDirecto")
        self.rhPasoDirecto.setStyleSheet(u"font: 500 11pt \"Allerta\";")
        self.RHAnalisisTextoCalcular_5 = QLabel(self.rhPasoDirecto)
        self.RHAnalisisTextoCalcular_5.setObjectName(u"RHAnalisisTextoCalcular_5")
        self.RHAnalisisTextoCalcular_5.setGeometry(QRect(800, 30, 271, 131))
        sizePolicy5.setHeightForWidth(self.RHAnalisisTextoCalcular_5.sizePolicy().hasHeightForWidth())
        self.RHAnalisisTextoCalcular_5.setSizePolicy(sizePolicy5)
        self.RHAnalisisTextoCalcular_5.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"")
        self.RHAnalisisTextoCalcular_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupBox_Propiedades_22 = QGroupBox(self.rhPasoDirecto)
        self.groupBox_Propiedades_22.setObjectName(u"groupBox_Propiedades_22")
        self.groupBox_Propiedades_22.setGeometry(QRect(20, 10, 770, 441))
        sizePolicy13.setHeightForWidth(self.groupBox_Propiedades_22.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_22.setSizePolicy(sizePolicy13)
        self.groupBox_Propiedades_22.setMinimumSize(QSize(770, 0))
        self.groupBox_Propiedades_22.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_22.setStyleSheet(u"QGroupBox {\n"
"color: rgb(217, 165, 181);\n"
"font: bold; \n"
"border: 2px solid;\n"
"font: 700 11pt \"Allerta\";\n"
"border-color: rgb(217, 165, 181);\n"
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
        self.gridLayout_105 = QGridLayout(self.groupBox_Propiedades_22)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
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
        self.gridLayout_106.setVerticalSpacing(10)
        self.gridLayout_106.setContentsMargins(20, 10, 20, 10)
        self.FGVPasoDFieldAncho = QLineEdit(self.row_51)
        self.FGVPasoDFieldAncho.setObjectName(u"FGVPasoDFieldAncho")
        sizePolicy15.setHeightForWidth(self.FGVPasoDFieldAncho.sizePolicy().hasHeightForWidth())
        self.FGVPasoDFieldAncho.setSizePolicy(sizePolicy15)
        self.FGVPasoDFieldAncho.setMinimumSize(QSize(110, 30))
        self.FGVPasoDFieldAncho.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.FGVPasoDFieldAncho.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.FGVPasoDFieldAncho.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_106.addWidget(self.FGVPasoDFieldAncho, 0, 1, 1, 1)

        self.FGVPasoDFieldCaudal = QLineEdit(self.row_51)
        self.FGVPasoDFieldCaudal.setObjectName(u"FGVPasoDFieldCaudal")
        sizePolicy5.setHeightForWidth(self.FGVPasoDFieldCaudal.sizePolicy().hasHeightForWidth())
        self.FGVPasoDFieldCaudal.setSizePolicy(sizePolicy5)
        self.FGVPasoDFieldCaudal.setMinimumSize(QSize(0, 30))
        self.FGVPasoDFieldCaudal.setMaximumSize(QSize(150, 16777215))
        self.FGVPasoDFieldCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_106.addWidget(self.FGVPasoDFieldCaudal, 8, 1, 1, 1)

        self.FGVPasoDLabelProfundidadObjetivo = QLabel(self.row_51)
        self.FGVPasoDLabelProfundidadObjetivo.setObjectName(u"FGVPasoDLabelProfundidadObjetivo")
        sizePolicy6.setHeightForWidth(self.FGVPasoDLabelProfundidadObjetivo.sizePolicy().hasHeightForWidth())
        self.FGVPasoDLabelProfundidadObjetivo.setSizePolicy(sizePolicy6)
        self.FGVPasoDLabelProfundidadObjetivo.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVPasoDLabelProfundidadObjetivo.setLineWidth(1)
        self.FGVPasoDLabelProfundidadObjetivo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_106.addWidget(self.FGVPasoDLabelProfundidadObjetivo, 7, 0, 1, 1)

        self.FGVPasoDLabelAncho = QLabel(self.row_51)
        self.FGVPasoDLabelAncho.setObjectName(u"FGVPasoDLabelAncho")
        sizePolicy6.setHeightForWidth(self.FGVPasoDLabelAncho.sizePolicy().hasHeightForWidth())
        self.FGVPasoDLabelAncho.setSizePolicy(sizePolicy6)
        self.FGVPasoDLabelAncho.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVPasoDLabelAncho.setLineWidth(1)
        self.FGVPasoDLabelAncho.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_106.addWidget(self.FGVPasoDLabelAncho, 0, 0, 1, 1)

        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setSpacing(0)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVPasoDComboBoxNumManning = QComboBox(self.row_51)
        self.FGVPasoDComboBoxNumManning.addItem("")
        self.FGVPasoDComboBoxNumManning.setObjectName(u"FGVPasoDComboBoxNumManning")
        sizePolicy14.setHeightForWidth(self.FGVPasoDComboBoxNumManning.sizePolicy().hasHeightForWidth())
        self.FGVPasoDComboBoxNumManning.setSizePolicy(sizePolicy14)
        self.FGVPasoDComboBoxNumManning.setMinimumSize(QSize(234, 30))
        self.FGVPasoDComboBoxNumManning.setMaximumSize(QSize(260, 16777215))
        self.FGVPasoDComboBoxNumManning.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVPasoDComboBoxNumManning.setEditable(True)
        self.FGVPasoDComboBoxNumManning.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_113.addWidget(self.FGVPasoDComboBoxNumManning)


        self.gridLayout_106.addLayout(self.horizontalLayout_113, 3, 2, 1, 1)

        self.FGVPasoDLabelNumManning = QLabel(self.row_51)
        self.FGVPasoDLabelNumManning.setObjectName(u"FGVPasoDLabelNumManning")
        sizePolicy6.setHeightForWidth(self.FGVPasoDLabelNumManning.sizePolicy().hasHeightForWidth())
        self.FGVPasoDLabelNumManning.setSizePolicy(sizePolicy6)
        self.FGVPasoDLabelNumManning.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVPasoDLabelNumManning.setLineWidth(1)
        self.FGVPasoDLabelNumManning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_106.addWidget(self.FGVPasoDLabelNumManning, 3, 0, 1, 1)

        self.FGVPasoDFieldNumManning = QLineEdit(self.row_51)
        self.FGVPasoDFieldNumManning.setObjectName(u"FGVPasoDFieldNumManning")
        sizePolicy5.setHeightForWidth(self.FGVPasoDFieldNumManning.sizePolicy().hasHeightForWidth())
        self.FGVPasoDFieldNumManning.setSizePolicy(sizePolicy5)
        self.FGVPasoDFieldNumManning.setMinimumSize(QSize(0, 30))
        self.FGVPasoDFieldNumManning.setMaximumSize(QSize(150, 16777215))
        self.FGVPasoDFieldNumManning.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_106.addWidget(self.FGVPasoDFieldNumManning, 3, 1, 1, 1)

        self.FGVPasoDFieldPendienteLateral = QLineEdit(self.row_51)
        self.FGVPasoDFieldPendienteLateral.setObjectName(u"FGVPasoDFieldPendienteLateral")
        sizePolicy15.setHeightForWidth(self.FGVPasoDFieldPendienteLateral.sizePolicy().hasHeightForWidth())
        self.FGVPasoDFieldPendienteLateral.setSizePolicy(sizePolicy15)
        self.FGVPasoDFieldPendienteLateral.setMinimumSize(QSize(110, 30))
        self.FGVPasoDFieldPendienteLateral.setMaximumSize(QSize(150, 30))
        self.FGVPasoDFieldPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_106.addWidget(self.FGVPasoDFieldPendienteLateral, 4, 1, 1, 1)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setSpacing(0)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVPasoDComboBoxInclinacion = QComboBox(self.row_51)
        self.FGVPasoDComboBoxInclinacion.addItem("")
        self.FGVPasoDComboBoxInclinacion.addItem("")
        self.FGVPasoDComboBoxInclinacion.addItem("")
        self.FGVPasoDComboBoxInclinacion.setObjectName(u"FGVPasoDComboBoxInclinacion")
        sizePolicy14.setHeightForWidth(self.FGVPasoDComboBoxInclinacion.sizePolicy().hasHeightForWidth())
        self.FGVPasoDComboBoxInclinacion.setSizePolicy(sizePolicy14)
        self.FGVPasoDComboBoxInclinacion.setMinimumSize(QSize(234, 30))
        self.FGVPasoDComboBoxInclinacion.setMaximumSize(QSize(260, 16777215))
        self.FGVPasoDComboBoxInclinacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVPasoDComboBoxInclinacion.setEditable(True)
        self.FGVPasoDComboBoxInclinacion.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_105.addWidget(self.FGVPasoDComboBoxInclinacion)


        self.gridLayout_106.addLayout(self.horizontalLayout_105, 2, 2, 1, 1)

        self.FGVPasoDLabelDiametro = QLabel(self.row_51)
        self.FGVPasoDLabelDiametro.setObjectName(u"FGVPasoDLabelDiametro")
        sizePolicy6.setHeightForWidth(self.FGVPasoDLabelDiametro.sizePolicy().hasHeightForWidth())
        self.FGVPasoDLabelDiametro.setSizePolicy(sizePolicy6)
        self.FGVPasoDLabelDiametro.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVPasoDLabelDiametro.setLineWidth(1)
        self.FGVPasoDLabelDiametro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_106.addWidget(self.FGVPasoDLabelDiametro, 1, 0, 1, 1)

        self.FGVPasoDLabelPendienteLateral2 = QLabel(self.row_51)
        self.FGVPasoDLabelPendienteLateral2.setObjectName(u"FGVPasoDLabelPendienteLateral2")
        sizePolicy6.setHeightForWidth(self.FGVPasoDLabelPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.FGVPasoDLabelPendienteLateral2.setSizePolicy(sizePolicy6)
        self.FGVPasoDLabelPendienteLateral2.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVPasoDLabelPendienteLateral2.setLineWidth(1)
        self.FGVPasoDLabelPendienteLateral2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_106.addWidget(self.FGVPasoDLabelPendienteLateral2, 5, 0, 1, 1)

        self.FGVPasoDFieldDiametro = QLineEdit(self.row_51)
        self.FGVPasoDFieldDiametro.setObjectName(u"FGVPasoDFieldDiametro")
        sizePolicy15.setHeightForWidth(self.FGVPasoDFieldDiametro.sizePolicy().hasHeightForWidth())
        self.FGVPasoDFieldDiametro.setSizePolicy(sizePolicy15)
        self.FGVPasoDFieldDiametro.setMinimumSize(QSize(110, 30))
        self.FGVPasoDFieldDiametro.setMaximumSize(QSize(150, 30))
#if QT_CONFIG(tooltip)
        self.FGVPasoDFieldDiametro.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.FGVPasoDFieldDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")

        self.gridLayout_106.addWidget(self.FGVPasoDFieldDiametro, 1, 1, 1, 1)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setSpacing(0)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVPasoDComboBoxAncho = QComboBox(self.row_51)
        self.FGVPasoDComboBoxAncho.addItem("")
        self.FGVPasoDComboBoxAncho.addItem("")
        self.FGVPasoDComboBoxAncho.addItem("")
        self.FGVPasoDComboBoxAncho.addItem("")
        self.FGVPasoDComboBoxAncho.setObjectName(u"FGVPasoDComboBoxAncho")
        sizePolicy13.setHeightForWidth(self.FGVPasoDComboBoxAncho.sizePolicy().hasHeightForWidth())
        self.FGVPasoDComboBoxAncho.setSizePolicy(sizePolicy13)
        self.FGVPasoDComboBoxAncho.setMinimumSize(QSize(150, 30))
        self.FGVPasoDComboBoxAncho.setMaximumSize(QSize(260, 30))
        self.FGVPasoDComboBoxAncho.setLayoutDirection(Qt.LeftToRight)
        self.FGVPasoDComboBoxAncho.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVPasoDComboBoxAncho.setEditable(True)
        self.FGVPasoDComboBoxAncho.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.FGVPasoDComboBoxAncho.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_111.addWidget(self.FGVPasoDComboBoxAncho)


        self.gridLayout_106.addLayout(self.horizontalLayout_111, 0, 2, 1, 1)

        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.FGVPasoDComboBoxCaudal = QComboBox(self.row_51)
        self.FGVPasoDComboBoxCaudal.addItem("")
        self.FGVPasoDComboBoxCaudal.addItem("")
        self.FGVPasoDComboBoxCaudal.setObjectName(u"FGVPasoDComboBoxCaudal")
        sizePolicy5.setHeightForWidth(self.FGVPasoDComboBoxCaudal.sizePolicy().hasHeightForWidth())
        self.FGVPasoDComboBoxCaudal.setSizePolicy(sizePolicy5)
        self.FGVPasoDComboBoxCaudal.setMinimumSize(QSize(150, 30))
        self.FGVPasoDComboBoxCaudal.setMaximumSize(QSize(260, 16777215))
        self.FGVPasoDComboBoxCaudal.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVPasoDComboBoxCaudal.setEditable(True)
        self.FGVPasoDComboBoxCaudal.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_106.addWidget(self.FGVPasoDComboBoxCaudal)


        self.gridLayout_106.addLayout(self.horizontalLayout_106, 8, 2, 1, 1)

        self.FGVPasoDFieldProfundidadControl = QLineEdit(self.row_51)
        self.FGVPasoDFieldProfundidadControl.setObjectName(u"FGVPasoDFieldProfundidadControl")
        sizePolicy5.setHeightForWidth(self.FGVPasoDFieldProfundidadControl.sizePolicy().hasHeightForWidth())
        self.FGVPasoDFieldProfundidadControl.setSizePolicy(sizePolicy5)
        self.FGVPasoDFieldProfundidadControl.setMinimumSize(QSize(0, 30))
        self.FGVPasoDFieldProfundidadControl.setMaximumSize(QSize(150, 16777215))
        self.FGVPasoDFieldProfundidadControl.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_106.addWidget(self.FGVPasoDFieldProfundidadControl, 6, 1, 1, 1)

        self.FGVPasoDLabelProfundidadControl = QLabel(self.row_51)
        self.FGVPasoDLabelProfundidadControl.setObjectName(u"FGVPasoDLabelProfundidadControl")
        sizePolicy6.setHeightForWidth(self.FGVPasoDLabelProfundidadControl.sizePolicy().hasHeightForWidth())
        self.FGVPasoDLabelProfundidadControl.setSizePolicy(sizePolicy6)
        self.FGVPasoDLabelProfundidadControl.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVPasoDLabelProfundidadControl.setLineWidth(1)
        self.FGVPasoDLabelProfundidadControl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_106.addWidget(self.FGVPasoDLabelProfundidadControl, 6, 0, 1, 1)

        self.FGVPasoDLabelInclinacion = QLabel(self.row_51)
        self.FGVPasoDLabelInclinacion.setObjectName(u"FGVPasoDLabelInclinacion")
        sizePolicy6.setHeightForWidth(self.FGVPasoDLabelInclinacion.sizePolicy().hasHeightForWidth())
        self.FGVPasoDLabelInclinacion.setSizePolicy(sizePolicy6)
        self.FGVPasoDLabelInclinacion.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVPasoDLabelInclinacion.setLineWidth(1)
        self.FGVPasoDLabelInclinacion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_106.addWidget(self.FGVPasoDLabelInclinacion, 2, 0, 1, 1)

        self.FGVPasoDLabelCaudal = QLabel(self.row_51)
        self.FGVPasoDLabelCaudal.setObjectName(u"FGVPasoDLabelCaudal")
        sizePolicy6.setHeightForWidth(self.FGVPasoDLabelCaudal.sizePolicy().hasHeightForWidth())
        self.FGVPasoDLabelCaudal.setSizePolicy(sizePolicy6)
        self.FGVPasoDLabelCaudal.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVPasoDLabelCaudal.setLineWidth(1)
        self.FGVPasoDLabelCaudal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_106.addWidget(self.FGVPasoDLabelCaudal, 8, 0, 1, 1)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.FGVPasoDComboBoxPendienteLateral2 = QComboBox(self.row_51)
        self.FGVPasoDComboBoxPendienteLateral2.addItem("")
        self.FGVPasoDComboBoxPendienteLateral2.addItem("")
        self.FGVPasoDComboBoxPendienteLateral2.addItem("")
        self.FGVPasoDComboBoxPendienteLateral2.setObjectName(u"FGVPasoDComboBoxPendienteLateral2")
        sizePolicy13.setHeightForWidth(self.FGVPasoDComboBoxPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.FGVPasoDComboBoxPendienteLateral2.setSizePolicy(sizePolicy13)
        self.FGVPasoDComboBoxPendienteLateral2.setMinimumSize(QSize(234, 30))
        self.FGVPasoDComboBoxPendienteLateral2.setMaximumSize(QSize(260, 16777215))
        self.FGVPasoDComboBoxPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVPasoDComboBoxPendienteLateral2.setEditable(True)
        self.FGVPasoDComboBoxPendienteLateral2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_108.addWidget(self.FGVPasoDComboBoxPendienteLateral2)


        self.gridLayout_106.addLayout(self.horizontalLayout_108, 5, 2, 1, 1)

        self.FGVPasoDFieldProfundidadObjetivo = QLineEdit(self.row_51)
        self.FGVPasoDFieldProfundidadObjetivo.setObjectName(u"FGVPasoDFieldProfundidadObjetivo")
        sizePolicy5.setHeightForWidth(self.FGVPasoDFieldProfundidadObjetivo.sizePolicy().hasHeightForWidth())
        self.FGVPasoDFieldProfundidadObjetivo.setSizePolicy(sizePolicy5)
        self.FGVPasoDFieldProfundidadObjetivo.setMinimumSize(QSize(0, 30))
        self.FGVPasoDFieldProfundidadObjetivo.setMaximumSize(QSize(150, 16777215))
        self.FGVPasoDFieldProfundidadObjetivo.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_106.addWidget(self.FGVPasoDFieldProfundidadObjetivo, 7, 1, 1, 1)

        self.FGVPasoDFieldPendienteLateral2 = QLineEdit(self.row_51)
        self.FGVPasoDFieldPendienteLateral2.setObjectName(u"FGVPasoDFieldPendienteLateral2")
        sizePolicy5.setHeightForWidth(self.FGVPasoDFieldPendienteLateral2.sizePolicy().hasHeightForWidth())
        self.FGVPasoDFieldPendienteLateral2.setSizePolicy(sizePolicy5)
        self.FGVPasoDFieldPendienteLateral2.setMinimumSize(QSize(0, 30))
        self.FGVPasoDFieldPendienteLateral2.setMaximumSize(QSize(150, 16777215))
        self.FGVPasoDFieldPendienteLateral2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_106.addWidget(self.FGVPasoDFieldPendienteLateral2, 5, 1, 1, 1)

        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setSpacing(0)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVPasoDComboBoxPendienteControl = QComboBox(self.row_51)
        self.FGVPasoDComboBoxPendienteControl.addItem("")
        self.FGVPasoDComboBoxPendienteControl.addItem("")
        self.FGVPasoDComboBoxPendienteControl.addItem("")
        self.FGVPasoDComboBoxPendienteControl.addItem("")
        self.FGVPasoDComboBoxPendienteControl.setObjectName(u"FGVPasoDComboBoxPendienteControl")
        sizePolicy13.setHeightForWidth(self.FGVPasoDComboBoxPendienteControl.sizePolicy().hasHeightForWidth())
        self.FGVPasoDComboBoxPendienteControl.setSizePolicy(sizePolicy13)
        self.FGVPasoDComboBoxPendienteControl.setMinimumSize(QSize(150, 30))
        self.FGVPasoDComboBoxPendienteControl.setMaximumSize(QSize(260, 30))
        self.FGVPasoDComboBoxPendienteControl.setLayoutDirection(Qt.LeftToRight)
        self.FGVPasoDComboBoxPendienteControl.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVPasoDComboBoxPendienteControl.setEditable(True)
        self.FGVPasoDComboBoxPendienteControl.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.FGVPasoDComboBoxPendienteControl.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_110.addWidget(self.FGVPasoDComboBoxPendienteControl)


        self.gridLayout_106.addLayout(self.horizontalLayout_110, 6, 2, 1, 1)

        self.FGVPasoDLabelPendienteLateral = QLabel(self.row_51)
        self.FGVPasoDLabelPendienteLateral.setObjectName(u"FGVPasoDLabelPendienteLateral")
        sizePolicy6.setHeightForWidth(self.FGVPasoDLabelPendienteLateral.sizePolicy().hasHeightForWidth())
        self.FGVPasoDLabelPendienteLateral.setSizePolicy(sizePolicy6)
        self.FGVPasoDLabelPendienteLateral.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVPasoDLabelPendienteLateral.setLineWidth(1)
        self.FGVPasoDLabelPendienteLateral.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_106.addWidget(self.FGVPasoDLabelPendienteLateral, 4, 0, 1, 1)

        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setSpacing(0)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVPasoDComboBoxPendienteObjetivo = QComboBox(self.row_51)
        self.FGVPasoDComboBoxPendienteObjetivo.addItem("")
        self.FGVPasoDComboBoxPendienteObjetivo.addItem("")
        self.FGVPasoDComboBoxPendienteObjetivo.addItem("")
        self.FGVPasoDComboBoxPendienteObjetivo.addItem("")
        self.FGVPasoDComboBoxPendienteObjetivo.setObjectName(u"FGVPasoDComboBoxPendienteObjetivo")
        sizePolicy13.setHeightForWidth(self.FGVPasoDComboBoxPendienteObjetivo.sizePolicy().hasHeightForWidth())
        self.FGVPasoDComboBoxPendienteObjetivo.setSizePolicy(sizePolicy13)
        self.FGVPasoDComboBoxPendienteObjetivo.setMinimumSize(QSize(150, 30))
        self.FGVPasoDComboBoxPendienteObjetivo.setMaximumSize(QSize(260, 30))
        self.FGVPasoDComboBoxPendienteObjetivo.setLayoutDirection(Qt.LeftToRight)
        self.FGVPasoDComboBoxPendienteObjetivo.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVPasoDComboBoxPendienteObjetivo.setEditable(True)
        self.FGVPasoDComboBoxPendienteObjetivo.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.FGVPasoDComboBoxPendienteObjetivo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_109.addWidget(self.FGVPasoDComboBoxPendienteObjetivo)


        self.gridLayout_106.addLayout(self.horizontalLayout_109, 7, 2, 1, 1)

        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setSpacing(0)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVPasoDComboBoxDiametro = QComboBox(self.row_51)
        self.FGVPasoDComboBoxDiametro.addItem("")
        self.FGVPasoDComboBoxDiametro.addItem("")
        self.FGVPasoDComboBoxDiametro.addItem("")
        self.FGVPasoDComboBoxDiametro.addItem("")
        self.FGVPasoDComboBoxDiametro.setObjectName(u"FGVPasoDComboBoxDiametro")
        sizePolicy13.setHeightForWidth(self.FGVPasoDComboBoxDiametro.sizePolicy().hasHeightForWidth())
        self.FGVPasoDComboBoxDiametro.setSizePolicy(sizePolicy13)
        self.FGVPasoDComboBoxDiametro.setMinimumSize(QSize(150, 30))
        self.FGVPasoDComboBoxDiametro.setMaximumSize(QSize(260, 30))
        self.FGVPasoDComboBoxDiametro.setLayoutDirection(Qt.LeftToRight)
        self.FGVPasoDComboBoxDiametro.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVPasoDComboBoxDiametro.setEditable(True)
        self.FGVPasoDComboBoxDiametro.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.FGVPasoDComboBoxDiametro.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_112.addWidget(self.FGVPasoDComboBoxDiametro)


        self.gridLayout_106.addLayout(self.horizontalLayout_112, 1, 2, 1, 1)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setSpacing(0)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setSizeConstraint(QLayout.SetMinimumSize)
        self.FGVPasoDComboBoxPendienteLateral = QComboBox(self.row_51)
        self.FGVPasoDComboBoxPendienteLateral.addItem("")
        self.FGVPasoDComboBoxPendienteLateral.addItem("")
        self.FGVPasoDComboBoxPendienteLateral.addItem("")
        self.FGVPasoDComboBoxPendienteLateral.setObjectName(u"FGVPasoDComboBoxPendienteLateral")
        sizePolicy14.setHeightForWidth(self.FGVPasoDComboBoxPendienteLateral.sizePolicy().hasHeightForWidth())
        self.FGVPasoDComboBoxPendienteLateral.setSizePolicy(sizePolicy14)
        self.FGVPasoDComboBoxPendienteLateral.setMinimumSize(QSize(234, 30))
        self.FGVPasoDComboBoxPendienteLateral.setMaximumSize(QSize(260, 16777215))
        self.FGVPasoDComboBoxPendienteLateral.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.FGVPasoDComboBoxPendienteLateral.setEditable(True)
        self.FGVPasoDComboBoxPendienteLateral.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_107.addWidget(self.FGVPasoDComboBoxPendienteLateral)


        self.gridLayout_106.addLayout(self.horizontalLayout_107, 4, 2, 1, 1)

        self.FGVPasoDFieldInclinacion = QLineEdit(self.row_51)
        self.FGVPasoDFieldInclinacion.setObjectName(u"FGVPasoDFieldInclinacion")
        sizePolicy5.setHeightForWidth(self.FGVPasoDFieldInclinacion.sizePolicy().hasHeightForWidth())
        self.FGVPasoDFieldInclinacion.setSizePolicy(sizePolicy5)
        self.FGVPasoDFieldInclinacion.setMinimumSize(QSize(0, 30))
        self.FGVPasoDFieldInclinacion.setMaximumSize(QSize(150, 16777215))
        self.FGVPasoDFieldInclinacion.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_106.addWidget(self.FGVPasoDFieldInclinacion, 2, 1, 1, 1)


        self.verticalLayout_71.addLayout(self.gridLayout_106)


        self.gridLayout_105.addWidget(self.row_51, 0, 1, 1, 1)

        self.layoutWidget = QWidget(self.rhPasoDirecto)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(800, 160, 262, 121))
        self.gridLayout_26 = QGridLayout(self.layoutWidget)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setHorizontalSpacing(10)
        self.gridLayout_26.setVerticalSpacing(0)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.FGVPasoDTextoReiniciar = QLabel(self.layoutWidget)
        self.FGVPasoDTextoReiniciar.setObjectName(u"FGVPasoDTextoReiniciar")
        sizePolicy5.setHeightForWidth(self.FGVPasoDTextoReiniciar.sizePolicy().hasHeightForWidth())
        self.FGVPasoDTextoReiniciar.setSizePolicy(sizePolicy5)
        self.FGVPasoDTextoReiniciar.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"")
        self.FGVPasoDTextoReiniciar.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.FGVPasoDTextoReiniciar, 2, 1, 1, 1)

        self.FGVPasoDTextoCalcular = QLabel(self.layoutWidget)
        self.FGVPasoDTextoCalcular.setObjectName(u"FGVPasoDTextoCalcular")
        sizePolicy5.setHeightForWidth(self.FGVPasoDTextoCalcular.sizePolicy().hasHeightForWidth())
        self.FGVPasoDTextoCalcular.setSizePolicy(sizePolicy5)
        self.FGVPasoDTextoCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"color: rgb(84, 84, 84);\n"
"\n"
"")
        self.FGVPasoDTextoCalcular.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.FGVPasoDTextoCalcular, 2, 0, 1, 1)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.FGVPasoDBotonCalcular = QPushButton(self.layoutWidget)
        self.FGVPasoDBotonCalcular.setObjectName(u"FGVPasoDBotonCalcular")
        self.FGVPasoDBotonCalcular.setMinimumSize(QSize(50, 50))
        self.FGVPasoDBotonCalcular.setMaximumSize(QSize(40, 40))
        self.FGVPasoDBotonCalcular.setStyleSheet(u"background-color: rgb(217, 165, 181);\n"
"border-color: rgb(217, 165, 181);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_45.addWidget(self.FGVPasoDBotonCalcular)


        self.gridLayout_26.addLayout(self.horizontalLayout_45, 0, 0, 1, 1)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.FGVPasoDBotonReiniciar = QPushButton(self.layoutWidget)
        self.FGVPasoDBotonReiniciar.setObjectName(u"FGVPasoDBotonReiniciar")
        self.FGVPasoDBotonReiniciar.setMinimumSize(QSize(50, 50))
        self.FGVPasoDBotonReiniciar.setMaximumSize(QSize(40, 40))
        self.FGVPasoDBotonReiniciar.setStyleSheet(u"background-color: rgb(217, 165, 181);\n"
"border-color: rgb(217, 165, 181);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_46.addWidget(self.FGVPasoDBotonReiniciar)


        self.gridLayout_26.addLayout(self.horizontalLayout_46, 0, 1, 1, 1)

        self.gridLayout_26.setColumnStretch(0, 10)
        self.gridLayout_26.setColumnStretch(1, 10)
        self.gridLayout_26.setRowMinimumHeight(0, 10)
        self.gridLayout_26.setRowMinimumHeight(1, 10)
        self.FGVPasoDBotonDescargarCSV = QPushButton(self.rhPasoDirecto)
        self.FGVPasoDBotonDescargarCSV.setObjectName(u"FGVPasoDBotonDescargarCSV")
        self.FGVPasoDBotonDescargarCSV.setEnabled(False)
        self.FGVPasoDBotonDescargarCSV.setGeometry(QRect(800, 310, 260, 50))
        sizePolicy18 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(0)
        sizePolicy18.setHeightForWidth(self.FGVPasoDBotonDescargarCSV.sizePolicy().hasHeightForWidth())
        self.FGVPasoDBotonDescargarCSV.setSizePolicy(sizePolicy18)
        self.FGVPasoDBotonDescargarCSV.setMinimumSize(QSize(260, 50))
        self.FGVPasoDBotonDescargarCSV.setMaximumSize(QSize(40, 40))
        self.FGVPasoDBotonDescargarCSV.setStyleSheet(u"background-color: rgb(163, 160, 159);\n"
"border-width: 5px;\n"
"border-color: rgb(163, 160, 159);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Allerta\";\n"
"\n"
"")
        self.FGVPasoDBotonDescargarCSV.setCheckable(False)
        self.FGVPasoDBotonDescargarCSV.setChecked(False)
        self.FGVPasoDBotonDescargarCSV.setAutoDefault(False)
        self.FGVPasoDBotonDescargarPerfil = QPushButton(self.rhPasoDirecto)
        self.FGVPasoDBotonDescargarPerfil.setObjectName(u"FGVPasoDBotonDescargarPerfil")
        self.FGVPasoDBotonDescargarPerfil.setEnabled(False)
        self.FGVPasoDBotonDescargarPerfil.setGeometry(QRect(800, 390, 260, 50))
        sizePolicy18.setHeightForWidth(self.FGVPasoDBotonDescargarPerfil.sizePolicy().hasHeightForWidth())
        self.FGVPasoDBotonDescargarPerfil.setSizePolicy(sizePolicy18)
        self.FGVPasoDBotonDescargarPerfil.setMinimumSize(QSize(260, 50))
        self.FGVPasoDBotonDescargarPerfil.setMaximumSize(QSize(40, 40))
        self.FGVPasoDBotonDescargarPerfil.setStyleSheet(u"background-color: rgb(163, 160, 159);\n"
"border-width: 5px;\n"
"border-color: rgb(163, 160, 159);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Allerta\";\n"
"\n"
"")
        self.groupBox_Resultados_21 = QGroupBox(self.rhPasoDirecto)
        self.groupBox_Resultados_21.setObjectName(u"groupBox_Resultados_21")
        self.groupBox_Resultados_21.setGeometry(QRect(20, 460, 750, 141))
        sizePolicy17.setHeightForWidth(self.groupBox_Resultados_21.sizePolicy().hasHeightForWidth())
        self.groupBox_Resultados_21.setSizePolicy(sizePolicy17)
        self.groupBox_Resultados_21.setMinimumSize(QSize(750, 0))
        self.groupBox_Resultados_21.setMaximumSize(QSize(480, 16777215))
        self.groupBox_Resultados_21.setStyleSheet(u"QGroupBox {\n"
"color: rgb(217, 165, 181);\n"
"font: bold; \n"
"font: 700 11pt \"Allerta\";\n"
"border: 2px solid;\n"
"border-color: rgb(217, 165, 181);\n"
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
        self.gridLayout_99 = QGridLayout(self.groupBox_Resultados_21)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.row_48 = QFrame(self.groupBox_Resultados_21)
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
        self.gridLayout_100.setHorizontalSpacing(10)
        self.gridLayout_100.setVerticalSpacing(15)
        self.gridLayout_100.setContentsMargins(10, 10, 10, 10)
        self.FGVPasoDLabelPasos = QLabel(self.row_48)
        self.FGVPasoDLabelPasos.setObjectName(u"FGVPasoDLabelPasos")
        sizePolicy6.setHeightForWidth(self.FGVPasoDLabelPasos.sizePolicy().hasHeightForWidth())
        self.FGVPasoDLabelPasos.setSizePolicy(sizePolicy6)
        self.FGVPasoDLabelPasos.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVPasoDLabelPasos.setLineWidth(1)
        self.FGVPasoDLabelPasos.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_100.addWidget(self.FGVPasoDLabelPasos, 0, 0, 1, 1)

        self.FGVPasoDFieldPasos = QLineEdit(self.row_48)
        self.FGVPasoDFieldPasos.setObjectName(u"FGVPasoDFieldPasos")
        sizePolicy5.setHeightForWidth(self.FGVPasoDFieldPasos.sizePolicy().hasHeightForWidth())
        self.FGVPasoDFieldPasos.setSizePolicy(sizePolicy5)
        self.FGVPasoDFieldPasos.setMinimumSize(QSize(0, 36))
        self.FGVPasoDFieldPasos.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_100.addWidget(self.FGVPasoDFieldPasos, 0, 1, 1, 1)

        self.FGVPasoDLabelDatum = QLabel(self.row_48)
        self.FGVPasoDLabelDatum.setObjectName(u"FGVPasoDLabelDatum")
        sizePolicy6.setHeightForWidth(self.FGVPasoDLabelDatum.sizePolicy().hasHeightForWidth())
        self.FGVPasoDLabelDatum.setSizePolicy(sizePolicy6)
        self.FGVPasoDLabelDatum.setStyleSheet(u"font: 650 11pt \"Allerta\";")
        self.FGVPasoDLabelDatum.setLineWidth(1)
        self.FGVPasoDLabelDatum.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_100.addWidget(self.FGVPasoDLabelDatum, 1, 0, 1, 1)

        self.FGVPasoDFieldDatum = QLineEdit(self.row_48)
        self.FGVPasoDFieldDatum.setObjectName(u"FGVPasoDFieldDatum")
        sizePolicy5.setHeightForWidth(self.FGVPasoDFieldDatum.sizePolicy().hasHeightForWidth())
        self.FGVPasoDFieldDatum.setSizePolicy(sizePolicy5)
        self.FGVPasoDFieldDatum.setMinimumSize(QSize(0, 36))
        self.FGVPasoDFieldDatum.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";")

        self.gridLayout_100.addWidget(self.FGVPasoDFieldDatum, 1, 1, 1, 1)


        self.verticalLayout_68.addLayout(self.gridLayout_100)


        self.gridLayout_99.addWidget(self.row_48, 0, 0, 1, 1)

        self.tabFGV.addTab(self.rhPasoDirecto, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabFGV.addTab(self.tab_5, "")
        self.stackedWidget.addWidget(self.pagina_FGV)

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
        font7 = QFont()
        font7.setBold(False)
        font7.setItalic(False)
        self.creditsLabel.setFont(font7)
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


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabGeometria.setCurrentIndex(0)
        self.tabConservacionEnergia.setCurrentIndex(0)
        self.tabResaltosHidraulicos.setCurrentIndex(0)
        self.tabManning.setCurrentIndex(0)
        self.tabFGV.setCurrentIndex(0)


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
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
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
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" "
                        "style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">HidrApp - La forma m\u00e1s f\u00e1cil de dise\u00f1ar canales y estructuras hidr\u00e1ulicas.</span></p></body></html>", None))
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
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"Blabla", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.conservacion_de_energia.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:18pt; font-weight:500; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:30px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.conservacion_de_energia.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.conservacion_de_energia.setPlainText("")
#if QT_CONFIG(tooltip)
        self.geometria.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:18pt; font-weight:500; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:30px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geometria.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.geometria.setPlainText("")
#if QT_CONFIG(tooltip)
        self.resalto_hidraulico.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:18pt; font-weight:500; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:30px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.resalto_hidraulico.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.resalto_hidraulico.setPlainText("")
#if QT_CONFIG(tooltip)
        self.comprobacion_diseno.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:18pt; font-weight:500; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:30px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.comprobacion_diseno.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.comprobacion_diseno.setPlainText("")
#if QT_CONFIG(tooltip)
        self.FRV.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:18pt; font-weight:500; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:30px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FRV.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.FRV.setPlainText("")
#if QT_CONFIG(tooltip)
        self.manning.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:18pt; font-weight:500; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:30px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.manning.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.manning.setPlainText("")
#if QT_CONFIG(tooltip)
        self.diseno.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:18pt; font-weight:500; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:30px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.diseno.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.diseno.setPlainText("")
#if QT_CONFIG(tooltip)
        self.FGV.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:18pt; font-weight:500; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:30px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGV.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.FGV.setPlainText("")
        self.botonMenuGeometria.setText(QCoreApplication.translate("MainWindow", u"Geometr\u00eda", None))
        self.botonMenuConservacionE.setText(QCoreApplication.translate("MainWindow", u"Conservaci\u00f3n de \n"
"energ\u00eda", None))
        self.botonMenuConservacionM.setText(QCoreApplication.translate("MainWindow", u"Conservaci\u00f3n del\n"
"Momentum", None))
        self.botonMenuComprobacion.setText(QCoreApplication.translate("MainWindow", u"Comprobaci\u00f3n\n"
"de dise\u00f1o", None))
        self.botonMenuDiseno.setText(QCoreApplication.translate("MainWindow", u"Dise\u00f1o", None))
        self.botonMenuManning.setText(QCoreApplication.translate("MainWindow", u"Ecuaci\u00f3n de \n"
" Manning", None))
        self.botonMenuFGV.setText(QCoreApplication.translate("MainWindow", u"Flujo \n"
" Gradualmente \n"
" Variado", None))
        self.botonMenuManningFRV.setText(QCoreApplication.translate("MainWindow", u"Flujo\n"
"Rapidamente\n"
"Variado", None))
        self.groupBox_Propiedades.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
        self.geoCTextoCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.geoCTextoReiniciar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.geoCBotonCalcular.setText("")
        self.geoCBotonReiniciar.setText("")
        self.geoCComboBoxDiametro.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.geoCComboBoxDiametro.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.geoCComboBoxDiametro.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.geoCComboBoxDiametro.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.geoCComboBoxDiametro.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.geoLabelRelacionLlenado.setText(QCoreApplication.translate("MainWindow", u"Relaci\u00f3n de llenado", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldDiametro.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldDiametro.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldDiametro.setInputMask("")
        self.geoCFieldDiametro.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoLabelDiametro.setText(QCoreApplication.translate("MainWindow", u"Di\u00e1metro (Di)", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldRelacionLlenado.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldRelacionLlenado.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldRelacionLlenado.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoCFieldRelacionLlenado.setPlaceholderText("")
        self.geoCComboBoxRelacionLlenado.setItemText(0, QCoreApplication.translate("MainWindow", u"Adimensional", None))

        self.geoCComboBoxRelacionLlenado.setCurrentText(QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.groupBox_Resultados.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.geoCLabelAngulo.setText(QCoreApplication.translate("MainWindow", u"\u00c1ngulo (\u03b8)", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldRadio.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldRadio.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldRadio.setText("")
        self.geoCFieldRadio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldArea.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldArea.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldArea.setText("")
        self.geoCFieldArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[metros cuadrados]", None))
        self.geoCLabelAnchoSuperficial.setText(QCoreApplication.translate("MainWindow", u"Ancho superficial (T)", None))
        self.geoCLabelProfundidadHidraulica.setText(QCoreApplication.translate("MainWindow", u"Profundidad hidr\u00e1ulica (D)", None))
        self.geoCLabelPerimetro.setText(QCoreApplication.translate("MainWindow", u"Per\u00edmetro mojado (P)", None))
        self.geoCLabelArea.setText(QCoreApplication.translate("MainWindow", u"\u00c1rea mojada (A)", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldAnchoSuperficial.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldAnchoSuperficial.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldAnchoSuperficial.setText("")
        self.geoCFieldAnchoSuperficial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.geoCLabelRadio.setText(QCoreApplication.translate("MainWindow", u"Radio Hidr\u00e1ulico (R)", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldPerimetro.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldPerimetro.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldPerimetro.setText("")
        self.geoCFieldPerimetro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldProfundidadHidraulica.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldProfundidadHidraulica.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldProfundidadHidraulica.setText("")
        self.geoCFieldProfundidadHidraulica.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.geoCLabelProfundidadNormal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad Normal (y<span style=\" vertical-align:sub;\">n</span>)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldAngulo.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldAngulo.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldAngulo.setText("")
        self.geoCFieldAngulo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[radianes]", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldProfundidadNormal.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldProfundidadNormal.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldProfundidadNormal.setText("")
        self.geoCFieldProfundidadNormal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.geoCImagenCanal.setText("")
#if QT_CONFIG(tooltip)
        self.groupBox_Canal.setToolTip(QCoreApplication.translate("MainWindow", u"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 7px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.groupBox_Canal.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.groupBox_Canal.setTitle(QCoreApplication.translate("MainWindow", u"Tipo de canal", None))
        self.geoBotonCircular.setText("")
        self.tabGeometria.setTabText(self.tabGeometria.indexOf(self.geometriaCircular), QCoreApplication.translate("MainWindow", u"Circular", None))
        self.groupBox_Propiedades_3.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldAncho.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldAncho.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldAncho.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoCFieldAncho.setPlaceholderText("")
        self.geoRComboBoxPendienteLateral.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.geoRComboBoxPendienteLateral.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.geoRComboBoxPendienteLateral.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.geoRComboBoxPendienteLateral.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.geoRLabelAncho.setText(QCoreApplication.translate("MainWindow", u"Ancho (b)", None))
        self.geoRLabelPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:11pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Inclinaci\u00f3n lateral derecha</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldPendienteLateral.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldPendienteLateral.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoCFieldPendienteLateral.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.geoCFieldProfundidadSeccion.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldProfundidadSeccion.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldProfundidadSeccion.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoCFieldProfundidadSeccion.setPlaceholderText("")
        self.geoRComboBoxProfundidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.geoRComboBoxProfundidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.geoRComboBoxProfundidad.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.geoRComboBoxProfundidad.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.geoRComboBoxProfundidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.geoRLabelProfundidadSeccion.setText(QCoreApplication.translate("MainWindow", u"Profundidad de secci\u00f3n (d)", None))
        self.geoRComboBoxAncho.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.geoRComboBoxAncho.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.geoRComboBoxAncho.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.geoRComboBoxAncho.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.geoRComboBoxAncho.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.geoRLabelPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:11pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Inclinaci\u00f3n lateral izquierda</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldPendienteLateral2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldPendienteLateral2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoCFieldPendienteLateral2.setPlaceholderText("")
        self.geoRComboBoxPendienteLateral2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.geoRComboBoxPendienteLateral2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.geoRComboBoxPendienteLateral2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.geoRComboBoxPendienteLateral2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.geoRTextoCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.geoRTextoReiniciar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.geoRBotonCalcular.setText("")
        self.geoRBotonReiniciar.setText("")
#if QT_CONFIG(tooltip)
        self.groupBox_Canal_3.setToolTip(QCoreApplication.translate("MainWindow", u"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 7px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.groupBox_Canal_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.groupBox_Canal_3.setTitle(QCoreApplication.translate("MainWindow", u"Tipo de canal", None))
        self.geoBotonRectangular.setText("")
        self.groupBox_Resultados_3.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
#if QT_CONFIG(tooltip)
        self.geoRFieldPerimetro.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoRFieldPerimetro.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoRFieldPerimetro.setText("")
        self.geoRFieldPerimetro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[metros]", None))
#if QT_CONFIG(tooltip)
        self.geoRFieldRadio.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoRFieldRadio.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoRFieldRadio.setText("")
        self.geoRFieldRadio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[metros]", None))
        self.geoRLabelArea.setText(QCoreApplication.translate("MainWindow", u"\u00c1rea mojada (A)", None))
#if QT_CONFIG(tooltip)
        self.geoRFieldArea.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoRFieldArea.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoRFieldArea.setText("")
        self.geoRFieldArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[metros cuadrados]", None))
        self.geoRLabelRadio.setText(QCoreApplication.translate("MainWindow", u"Radio Hidr\u00e1ulico (R)", None))
        self.geoRLabelAnchoSuperficial.setText(QCoreApplication.translate("MainWindow", u"Ancho superficial (T)", None))
        self.geoRLabelPerimetro.setText(QCoreApplication.translate("MainWindow", u"Per\u00edmetro mojado (P)", None))
        self.geoRLabelProfundidadHidraulica.setText(QCoreApplication.translate("MainWindow", u"Profundidad hidr\u00e1ulica (D)", None))
#if QT_CONFIG(tooltip)
        self.geoRFieldAnchoSuperficial.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoRFieldAnchoSuperficial.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoRFieldAnchoSuperficial.setText("")
        self.geoRFieldAnchoSuperficial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[metros]", None))
#if QT_CONFIG(tooltip)
        self.geoRFieldProfundidadHidraulica.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoRFieldProfundidadHidraulica.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoRFieldProfundidadHidraulica.setText("")
        self.geoRFieldProfundidadHidraulica.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[metros]", None))
        self.geoRImagenCanal.setText("")
        self.tabGeometria.setTabText(self.tabGeometria.indexOf(self.geometriaNoCircular), QCoreApplication.translate("MainWindow", u"No circular", None))
        self.groupBox_Resultados_6.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.geoFroudeLabelRadio.setText(QCoreApplication.translate("MainWindow", u"Froude (Fr)", None))
#if QT_CONFIG(tooltip)
        self.geoFroudeFieldFroude.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoFroudeFieldFroude.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoFroudeFieldFroude.setText("")
        self.geoFroudeFieldFroude.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[adimensional]", None))
        self.groupBox_Propiedades_6.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
        self.geoFroudeBotonCalcular.setText("")
        self.geoFroudeBotonReiniciar.setText("")
        self.geoFroudeComboBoxAncho.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.geoFroudeComboBoxAncho.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.geoFroudeComboBoxAncho.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.geoFroudeComboBoxAncho.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.geoFroudeComboBoxAncho.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(tooltip)
        self.geoFroudeFieldPendienteLateral.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoFroudeFieldPendienteLateral.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoFroudeFieldPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoFroudeFieldPendienteLateral.setPlaceholderText("")
        self.geoFroudeComboBoxCaudal.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.geoFroudeComboBoxCaudal.setItemText(1, QCoreApplication.translate("MainWindow", u"Litros/segundos", None))

        self.geoFroudeComboBoxCaudal.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
#if QT_CONFIG(tooltip)
        self.geoFroudeFieldPendienteLateral2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoFroudeFieldPendienteLateral2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoFroudeFieldPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoFroudeFieldPendienteLateral2.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.geoFroudeFieldCaudal.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoFroudeFieldCaudal.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoFroudeFieldCaudal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoFroudeFieldCaudal.setPlaceholderText("")
        self.geoFroudeLabelPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral izquierda</p></body></html>", None))
        self.geoFroudeLabelPendienteLateral_3.setText(QCoreApplication.translate("MainWindow", u"Caudal (Q)", None))
        self.geoFroudeLabelPendienteLateral_4.setText(QCoreApplication.translate("MainWindow", u"Di\u00e1metro (D)", None))
#if QT_CONFIG(tooltip)
        self.geoFroudeFieldProfundidadSeccion.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoFroudeFieldProfundidadSeccion.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoFroudeFieldProfundidadSeccion.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoFroudeFieldProfundidadSeccion.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.geoFroudeFieldDiametro.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoFroudeFieldDiametro.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoFroudeFieldDiametro.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoFroudeFieldDiametro.setPlaceholderText("")
        self.geoFroudeLabelPendienteLateral_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral derecha</p></body></html>", None))
        self.geoFroudeComboBoxProfundidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.geoFroudeComboBoxProfundidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.geoFroudeComboBoxProfundidad.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.geoFroudeComboBoxProfundidad.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.geoFroudeComboBoxProfundidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.geoFroudeComboBoxDiametro.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.geoFroudeComboBoxDiametro.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.geoFroudeComboBoxDiametro.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.geoFroudeComboBoxDiametro.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.geoFroudeComboBoxDiametro.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.geoFroudeLabelProfundidadSeccion.setText(QCoreApplication.translate("MainWindow", u"Profundidad de secci\u00f3n (d)", None))
        self.geoFroudeComboBoxPendienteLateral.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.geoFroudeComboBoxPendienteLateral.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.geoFroudeComboBoxPendienteLateral.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.geoFroudeComboBoxPendienteLateral.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.geoFroudeComboBoxPendienteLateral2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.geoFroudeComboBoxPendienteLateral2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.geoFroudeComboBoxPendienteLateral2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.geoFroudeComboBoxPendienteLateral2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.geoFroudeLabelAncho.setText(QCoreApplication.translate("MainWindow", u"Ancho (b)", None))
#if QT_CONFIG(tooltip)
        self.geoFroudeFieldAncho.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoFroudeFieldAncho.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoFroudeFieldAncho.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoFroudeFieldAncho.setPlaceholderText("")
        self.geoFroudeLabelVelocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad (v)", None))
#if QT_CONFIG(tooltip)
        self.geoFroudeFieldVelocidad.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoFroudeFieldVelocidad.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoFroudeFieldVelocidad.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geoFroudeFieldVelocidad.setPlaceholderText("")
        self.geoFroudeComboBoxVelocidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros/segundos", None))

        self.geoFroudeComboBoxVelocidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros/segundos", None))
        self.geoFroudeTextoCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.geoFroudeTextoReiniciar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.tabGeometria.setTabText(self.tabGeometria.indexOf(self.geometriaFroude), QCoreApplication.translate("MainWindow", u"Froude", None))
        self.ManningUniformeTextoReiniciar_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.ManningUniformeBotonCalcular_2.setText("")
        self.ManningUniformeBotonReiniciar_2.setText("")
        self.ManningUniformeTextoCalcular_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.groupBox_Propiedades_28.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldCaudal_7.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldCaudal_7.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldCaudal_7.setText("")
        self.RHAnalisisFieldCaudal_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m\u00b3/s]", None))
        self.RHAnalisisLabelCaudal_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Caudal (Q)</p></body></html>", None))
        self.RHAnalisisLabelCaudal_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Velocidad</p><p>(v)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldCaudal_8.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldCaudal_8.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldCaudal_8.setText("")
        self.RHAnalisisFieldCaudal_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m/s]", None))
        self.groupBox_Propiedades_20.setTitle(QCoreApplication.translate("MainWindow", u"Secci\u00f3n 1", None))
        self.CEnergiaComboBoxPendienteLateralSec1.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxPendienteLateralSec1.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.CEnergiaComboBoxPendienteLateralSec1.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.CEnergiaComboBoxPendienteLateralSec1.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxAnchoSec1.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaComboBoxAnchoSec1.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.CEnergiaComboBoxAnchoSec1.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.CEnergiaComboBoxAnchoSec1.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.CEnergiaComboBoxAnchoSec1.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaLabelProfundidadSec1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad (y<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
        self.CEnergiaLabelPendienteLateral2Sec1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral izquierda</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldPendienteLateralSec1.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateralSec1.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateralSec1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldPendienteLateralSec1.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldProfundidad1Sec1.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldProfundidad1Sec1.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldProfundidad1Sec1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldProfundidad1Sec1.setPlaceholderText("")
        self.CEnergiaLabelBaseSec1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ancho (b<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
        self.CEnergiaLabelPendienteLateralSec1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral derecha</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldPendienteLateral2Sec1.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateral2Sec1.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateral2Sec1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldPendienteLateral2Sec1.setPlaceholderText("")
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldAnchoSec1.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldAnchoSec1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldAnchoSec1.setPlaceholderText("")
        self.CEnergiaComboBoxPendienteLateral2Sec1.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxPendienteLateral2Sec1.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.CEnergiaComboBoxPendienteLateral2Sec1.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.CEnergiaComboBoxPendienteLateral2Sec1.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxProfundidad1Sec1.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaComboBoxProfundidad1Sec1.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.CEnergiaComboBoxProfundidad1Sec1.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.CEnergiaComboBoxProfundidad1Sec1.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.CEnergiaComboBoxProfundidad1Sec1.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.groupBox_Propiedades_23.setTitle(QCoreApplication.translate("MainWindow", u"Secci\u00f3n 2", None))
        self.CEnergiaComboBoxProfundidad1Sec2.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaComboBoxProfundidad1Sec2.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.CEnergiaComboBoxProfundidad1Sec2.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.CEnergiaComboBoxProfundidad1Sec2.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.CEnergiaComboBoxProfundidad1Sec2.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldAnchoSec2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldAnchoSec2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldAnchoSec2.setPlaceholderText("")
        self.CEnergiaLabelPendienteLateral2Sec2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral izquierda</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldProfundidad1Sec2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldProfundidad1Sec2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldProfundidad1Sec2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldProfundidad1Sec2.setPlaceholderText("")
        self.CEnergiaComboBoxPendienteLateralSec1_2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxPendienteLateralSec1_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.CEnergiaComboBoxPendienteLateralSec1_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.CEnergiaComboBoxPendienteLateralSec1_2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxAnchoSec2.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaComboBoxAnchoSec2.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.CEnergiaComboBoxAnchoSec2.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.CEnergiaComboBoxAnchoSec2.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.CEnergiaComboBoxAnchoSec2.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaLabelProfundidadSec2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad (y<span style=\" vertical-align:sub;\">2</span>)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldPendienteLateralSec2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateralSec2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateralSec2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldPendienteLateralSec2.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldPendienteLateral2Sec2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateral2Sec2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateral2Sec2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldPendienteLateral2Sec2.setPlaceholderText("")
        self.CEnergiaLabelBaseSec2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ancho (b<span style=\" vertical-align:sub;\">2</span>)</p></body></html>", None))
        self.CEnergiaLabelPendienteLateralSec2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral derecha</p></body></html>", None))
        self.CEnergiaComboBoxPendienteLateral2Sec2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxPendienteLateral2Sec2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.CEnergiaComboBoxPendienteLateral2Sec2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.CEnergiaComboBoxPendienteLateral2Sec2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.groupBox_Propiedades_24.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
        self.RHAnalisisLabelCaudal_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Escal\u00f3n (\u0394z)</p></body></html>", None))
        self.CEnergiaComboBoxAnchoSec2_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaComboBoxAnchoSec2_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.CEnergiaComboBoxAnchoSec2_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.CEnergiaComboBoxAnchoSec2_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.CEnergiaComboBoxAnchoSec2_3.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldCaudal_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldCaudal_4.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldCaudal_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHAnalisisFieldCaudal_4.setPlaceholderText("")
        self.tabConservacionEnergia.setTabText(self.tabConservacionEnergia.indexOf(self.rhCalculoCaudal), QCoreApplication.translate("MainWindow", u"Caudal", None))
        self.ManningUniformeTextoReiniciar_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.ManningUniformeBotonCalcular_3.setText("")
        self.ManningUniformeBotonReiniciar_3.setText("")
        self.ManningUniformeTextoCalcular_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.groupBox_Propiedades_25.setTitle(QCoreApplication.translate("MainWindow", u"Secci\u00f3n 1", None))
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldAnchoSec1_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldAnchoSec1_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldAnchoSec1_2.setPlaceholderText("")
        self.CEnergiaComboBoxPendienteLateralSec1_3.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxPendienteLateralSec1_3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.CEnergiaComboBoxPendienteLateralSec1_3.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.CEnergiaComboBoxPendienteLateralSec1_3.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxAnchoSec1_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaComboBoxAnchoSec1_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.CEnergiaComboBoxAnchoSec1_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.CEnergiaComboBoxAnchoSec1_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.CEnergiaComboBoxAnchoSec1_2.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldProfundidad1Sec1_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldProfundidad1Sec1_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldProfundidad1Sec1_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldProfundidad1Sec1_3.setPlaceholderText("")
        self.CEnergiaLabelPendienteLateralSec1_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral derecha</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldProfundidad1Sec1_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldProfundidad1Sec1_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldProfundidad1Sec1_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldProfundidad1Sec1_2.setPlaceholderText("")
        self.CEnergiaLabelProfundidadSec1_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Velocidad (v<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
        self.CEnergiaLabelProfundidadSec1_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad (y<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldPendienteLateralSec1_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateralSec1_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateralSec1_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldPendienteLateralSec1_2.setPlaceholderText("")
        self.CEnergiaLabelBaseSec1_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ancho (b<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
        self.CEnergiaLabelPendienteLateral2Sec1_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral izquierda</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldPendienteLateral2Sec1_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateral2Sec1_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateral2Sec1_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldPendienteLateral2Sec1_2.setPlaceholderText("")
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.CEnergiaComboBoxPendienteLateral2Sec1_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.CEnergiaComboBoxPendienteLateral2Sec1_2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxProfundidad1Sec1_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaComboBoxProfundidad1Sec1_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.CEnergiaComboBoxProfundidad1Sec1_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.CEnergiaComboBoxProfundidad1Sec1_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.CEnergiaComboBoxProfundidad1Sec1_2.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaComboBoxPendienteLateral2Sec1_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros/segundos", None))

        self.CEnergiaComboBoxPendienteLateral2Sec1_3.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros/segundos", None))
        self.groupBox_Propiedades_26.setTitle(QCoreApplication.translate("MainWindow", u"Secci\u00f3n 2", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldPendienteLateral2Sec2_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateral2Sec2_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateral2Sec2_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldPendienteLateral2Sec2_2.setPlaceholderText("")
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.CEnergiaComboBoxPendienteLateral2Sec2_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.CEnergiaComboBoxPendienteLateral2Sec2_2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxPendienteLateralSec1_4.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaComboBoxPendienteLateralSec1_4.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.CEnergiaComboBoxPendienteLateralSec1_4.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.CEnergiaComboBoxPendienteLateralSec1_4.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.CEnergiaLabelBaseSec2_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ancho (b<span style=\" vertical-align:sub;\">2</span>)</p></body></html>", None))
        self.CEnergiaComboBoxAnchoSec2_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaComboBoxAnchoSec2_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.CEnergiaComboBoxAnchoSec2_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.CEnergiaComboBoxAnchoSec2_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.CEnergiaComboBoxAnchoSec2_2.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaLabelPendienteLateral2Sec2_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral izquierda</p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldAnchoSec2_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldAnchoSec2_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldAnchoSec2_2.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.CEnergiaFieldPendienteLateralSec2_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateralSec2_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaFieldPendienteLateralSec2_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CEnergiaFieldPendienteLateralSec2_2.setPlaceholderText("")
        self.CEnergiaLabelPendienteLateralSec2_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral derecha</p></body></html>", None))
        self.groupBox_Propiedades_27.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
        self.CEnergiaComboBoxAnchoSec2_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.CEnergiaComboBoxAnchoSec2_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.CEnergiaComboBoxAnchoSec2_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.CEnergiaComboBoxAnchoSec2_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.CEnergiaComboBoxAnchoSec2_4.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldCaudal_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldCaudal_5.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldCaudal_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHAnalisisFieldCaudal_5.setPlaceholderText("")
        self.RHAnalisisLabelCaudal_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Escal\u00f3n (\u0394z)</p></body></html>", None))
        self.RHAnalisisLabelCaudal_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Caudal (Q)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldCaudal_6.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldCaudal_6.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldCaudal_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHAnalisisFieldCaudal_6.setPlaceholderText("")
        self.RHCompuertasComboBoxCaudal_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.RHCompuertasComboBoxCaudal_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Litros/segundos", None))

        self.RHCompuertasComboBoxCaudal_2.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.groupBox_Propiedades_29.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.CEnergiaY2LabelEnergiaCritica.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>E<span style=\" vertical-align:sub;\">c</span></p></body></html>", None))
        self.CEnergiaY2LabelProfundidad.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>y<span style=\" vertical-align:sub;\">2</span></p></body></html>", None))
        self.CEnergiaY2LabelProfundidad_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>y<span style=\" vertical-align:sub;\">1n</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaY2FieldEc.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaY2FieldEc.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaY2FieldEc.setText("")
        self.CEnergiaY2FieldEc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaY2FieldYc.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaY2FieldYc.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaY2FieldYc.setText("")
        self.CEnergiaY2FieldYc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.CEnergiaY2LabelProfundidadCritica.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>y<span style=\" vertical-align:sub;\">c</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaY2LabelProfundidadRaiz1.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaY2LabelProfundidadRaiz1.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaY2LabelProfundidadRaiz1.setText("")
        self.CEnergiaY2LabelProfundidadRaiz1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaY2LabelProfundidadRaiz2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaY2LabelProfundidadRaiz2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaY2LabelProfundidadRaiz2.setText("")
        self.CEnergiaY2LabelProfundidadRaiz2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaY2LabelProfundidadRaiz3.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaY2LabelProfundidadRaiz3.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaY2LabelProfundidadRaiz3.setText("")
        self.CEnergiaY2LabelProfundidadRaiz3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaY2LabelProfundidadRaiz1_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaY2LabelProfundidadRaiz1_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaY2LabelProfundidadRaiz1_2.setText("")
        self.CEnergiaY2LabelProfundidadRaiz1_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaY2LabelProfundidadRaiz2_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaY2LabelProfundidadRaiz2_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaY2LabelProfundidadRaiz2_2.setText("")
        self.CEnergiaY2LabelProfundidadRaiz2_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaY2LabelProfundidadRaiz3_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaY2LabelProfundidadRaiz3_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaY2LabelProfundidadRaiz3_2.setText("")
        self.CEnergiaY2LabelProfundidadRaiz3_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.CEnergiaY2LabelEnergiaCritica_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Represamiento</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CEnergiaY2FieldEc_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CEnergiaY2FieldEc_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CEnergiaY2FieldEc_2.setText("")
        self.CEnergiaY2FieldEc_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.tabConservacionEnergia.setTabText(self.tabConservacionEnergia.indexOf(self.rhProfundidad), QCoreApplication.translate("MainWindow", u"Profundidad", None))
        self.groupBox_Resultados_17.setTitle(QCoreApplication.translate("MainWindow", u"C\u00e1lculos realizados", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldAltura.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldAltura.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldAltura.setText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.RHAnalisisFieldAltura.setPlaceholderText("")
        self.RHAnalisisLabelE1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Energ\u00eda espec\u00edfica (E<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldE1.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldE1.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldE1.setText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.RHAnalisisFieldE1.setPlaceholderText("")
        self.RHAnalisisLabelAltura.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Altura (z<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
        self.RHAnalisisLabelE2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Energ\u00eda espec\u00edfica (E<span style=\" vertical-align:sub;\">2</span>)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldE2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldE2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldE2.setText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.RHAnalisisFieldE2.setPlaceholderText("")
        self.groupBox_Propiedades_14.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
        self.RHAnalisisLabelPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral derecha</p></body></html>", None))
        self.RHAnalisisComboBoxAncho.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHAnalisisComboBoxAncho.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHAnalisisComboBoxAncho.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHAnalisisComboBoxAncho.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHAnalisisComboBoxAncho.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldPendienteLateral.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldPendienteLateral.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHAnalisisFieldPendienteLateral.setPlaceholderText("")
        self.RHAnalisisLabelPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral izquierda</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldCaudal.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldCaudal.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldCaudal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHAnalisisFieldCaudal.setPlaceholderText("")
        self.RHAnalisisComboBoxCaudal.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.RHAnalisisComboBoxCaudal.setItemText(1, QCoreApplication.translate("MainWindow", u"Litros/segundos", None))

        self.RHAnalisisComboBoxCaudal.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.RHAnalisisComboBoxPendienteLateral2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.RHAnalisisComboBoxPendienteLateral2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.RHAnalisisComboBoxPendienteLateral2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.RHAnalisisComboBoxPendienteLateral2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldProfundidad1.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldProfundidad1.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldProfundidad1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHAnalisisFieldProfundidad1.setPlaceholderText("")
        self.RHAnalisisLabelBase.setText(QCoreApplication.translate("MainWindow", u"Ancho (b)", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldPendienteLateral2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldPendienteLateral2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHAnalisisFieldPendienteLateral2.setPlaceholderText("")
        self.RHAnalisisLabelProfundidad1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad (y<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
        self.RHAnalisisLabelCaudal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Caudal (Q)</p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldAncho.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldAncho.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHAnalisisFieldAncho.setPlaceholderText("")
        self.RHAnalisisComboBoxPendienteLateral.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.RHAnalisisComboBoxPendienteLateral.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.RHAnalisisComboBoxPendienteLateral.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.RHAnalisisComboBoxPendienteLateral.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.RHAnalisisComboBoxProfundidad1.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHAnalisisComboBoxProfundidad1.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHAnalisisComboBoxProfundidad1.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHAnalisisComboBoxProfundidad1.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHAnalisisComboBoxProfundidad1.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.groupBox_Resultados_14.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldEficiencia.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldEficiencia.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldEficiencia.setText(QCoreApplication.translate("MainWindow", u"[porcentaje]", None))
        self.RHAnalisisFieldEficiencia.setPlaceholderText("")
        self.RHAnalisisLabelEficiencia.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Eficiencia del</p><p>resalto hidr\u00e1ulico</p></body></html>", None))
        self.groupBox_Propiedades_16.setTitle(QCoreApplication.translate("MainWindow", u"Par\u00e1metros opcionales", None))
        self.RHAnalisisLabelProfundidad.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad (y<span style=\" vertical-align:sub;\">n</span>)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldInclinacion.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldInclinacion.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldInclinacion.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHAnalisisFieldInclinacion.setPlaceholderText("")
        self.RHAnalisisComboBoxInclinacion.setItemText(0, QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.RHAnalisisComboBoxInclinacion.setItemText(1, QCoreApplication.translate("MainWindow", u"Grados", None))
        self.RHAnalisisComboBoxInclinacion.setItemText(2, QCoreApplication.translate("MainWindow", u"Radianes", None))

        self.RHAnalisisComboBoxInclinacion.setCurrentText(QCoreApplication.translate("MainWindow", u"Adimensional", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldLongitudInclinada.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldLongitudInclinada.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldLongitudInclinada.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHAnalisisFieldLongitudInclinada.setPlaceholderText("")
        self.RHAnalisisLabelLongitudInclinada.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Longitud zona inclinada (L)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldProfundidad.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldProfundidad.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldProfundidad.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHAnalisisFieldProfundidad.setPlaceholderText("")
        self.RHAnalisisLabelInclinacion.setText(QCoreApplication.translate("MainWindow", u"Inclinaci\u00f3n canal (S0)", None))
        self.RHAnalisisComboBoxProfundidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHAnalisisComboBoxProfundidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHAnalisisComboBoxProfundidad.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHAnalisisComboBoxProfundidad.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHAnalisisComboBoxProfundidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHAnalisisComboBoxLongitudInclinada.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHAnalisisComboBoxLongitudInclinada.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHAnalisisComboBoxLongitudInclinada.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHAnalisisComboBoxLongitudInclinada.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHAnalisisComboBoxLongitudInclinada.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHAnalisisLabelFuerza.setText(QCoreApplication.translate("MainWindow", u"Fuerza (f)", None))
#if QT_CONFIG(tooltip)
        self.RHAnalisisFieldFuerza.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHAnalisisFieldFuerza.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHAnalisisFieldFuerza.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHAnalisisFieldFuerza.setPlaceholderText("")
        self.RHAnalisisComboBoxFuerza.setItemText(0, QCoreApplication.translate("MainWindow", u"Newtons", None))

        self.RHAnalisisComboBoxFuerza.setCurrentText(QCoreApplication.translate("MainWindow", u"Newtons", None))
        self.RHAnalisisTextoReiniciar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.RHAnalisisTextoCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.RHAnalisisBotonCalcular.setText("")
        self.RHAnalisisBotonReiniciar.setText("")
        self.tabResaltosHidraulicos.setTabText(self.tabResaltosHidraulicos.indexOf(self.rhFuerzaSubsecuente), QCoreApplication.translate("MainWindow", u"An\u00e1lisis de R.H", None))
        self.groupBox_Resultados_11.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.RHPropiedadesLabelClasificacion.setText(QCoreApplication.translate("MainWindow", u"Clasificaci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.RHPropiedadesFieldClasificacion.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldClasificacion.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldClasificacion.setText("")
        self.RHPropiedadesFieldClasificacion.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.RHPropiedadesFieldLongitud.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldLongitud.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldLongitud.setText("")
        self.RHPropiedadesFieldLongitud.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.RHPropiedadesLabelLongitud.setText(QCoreApplication.translate("MainWindow", u"Longitud", None))
        self.groupBox_Propiedades_11.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
#if QT_CONFIG(tooltip)
        self.RHPropiedadesFieldPendienteLateral.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldPendienteLateral.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHPropiedadesFieldPendienteLateral.setPlaceholderText("")
        self.RHPropiedadesLabelBase.setText(QCoreApplication.translate("MainWindow", u"Ancho (b)", None))
        self.RHPropiedadesComboBoxDiametro.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHPropiedadesComboBoxDiametro.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHPropiedadesComboBoxDiametro.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHPropiedadesComboBoxDiametro.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHPropiedadesComboBoxDiametro.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHPropiedadesComboBoxPendienteLateral.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.RHPropiedadesComboBoxPendienteLateral.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.RHPropiedadesComboBoxPendienteLateral.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.RHPropiedadesComboBoxPendienteLateral.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.RHPropiedadesComboBoxPendientaLateral2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.RHPropiedadesComboBoxPendientaLateral2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.RHPropiedadesComboBoxPendientaLateral2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.RHPropiedadesComboBoxPendientaLateral2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
#if QT_CONFIG(tooltip)
        self.RHPropiedadesFieldProfundidad.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldProfundidad.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldProfundidad.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHPropiedadesFieldProfundidad.setPlaceholderText("")
        self.RHPropiedadesLabelProfundidad.setText(QCoreApplication.translate("MainWindow", u"Profundidad aguas\n"
"arriba (y)", None))
#if QT_CONFIG(tooltip)
        self.RHPropiedadesFieldDiametro.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldDiametro.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldDiametro.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHPropiedadesFieldDiametro.setPlaceholderText("")
        self.RHPropiedadesLabelDiametro.setText(QCoreApplication.translate("MainWindow", u"Di\u00e1metro (D)", None))
#if QT_CONFIG(tooltip)
        self.RHPropiedadesFieldCaudal.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldCaudal.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldCaudal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHPropiedadesFieldCaudal.setPlaceholderText("")
        self.RHPropiedadesComboBoxProfundidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHPropiedadesComboBoxProfundidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHPropiedadesComboBoxProfundidad.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHPropiedadesComboBoxProfundidad.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHPropiedadesComboBoxProfundidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHPropiedadesLabelPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral</p><p>izquierda</p></body></html>", None))
        self.RHPropiedadesLabelPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral</p><p>derecha</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHPropiedadesFieldPendienteLateral2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldPendienteLateral2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHPropiedadesFieldPendienteLateral2.setPlaceholderText("")
        self.RHPropiedadesLabelCaudal.setText(QCoreApplication.translate("MainWindow", u"Caudal (Q)", None))
#if QT_CONFIG(tooltip)
        self.RHPropiedadesFieldBase.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldBase.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldBase.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHPropiedadesFieldBase.setPlaceholderText("")
        self.RHPropiedadesComboBoxCaudal.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros c\u00fabicos/segundos", None))
        self.RHPropiedadesComboBoxCaudal.setItemText(1, QCoreApplication.translate("MainWindow", u"Litros/segundos", None))

        self.RHPropiedadesComboBoxCaudal.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros c\u00fabicos/segundos", None))
        self.RHPropiedadesComboBoxBase.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHPropiedadesComboBoxBase.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHPropiedadesComboBoxBase.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHPropiedadesComboBoxBase.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHPropiedadesComboBoxBase.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.geoCImagenCanal_8.setText("")
        self.RHPropiedadesBotonCalcular.setText("")
        self.RHPropiedadesBotonReiniciar.setText("")
        self.RHPropiedadesTextoCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.RHPropiedadesTextoReiniciar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.groupBox_Resultados_15.setTitle(QCoreApplication.translate("MainWindow", u"C\u00e1lculos realizados", None))
        self.RHPropiedadesLabelFroude.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Froude (Fr)</p><p><span style=\" font-style:italic;\">(clasificaci\u00f3n)</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHPropiedadesFieldFroude.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldFroude.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.RHPropiedadesFieldFroude.setText("")
        self.RHPropiedadesFieldFroude.setPlaceholderText("")
        self.tabResaltosHidraulicos.setTabText(self.tabResaltosHidraulicos.indexOf(self.rhPropiedades), QCoreApplication.translate("MainWindow", u"Propiedades R.H", None))
        self.groupBox_Propiedades_13.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
        self.RHTipoComboBoxProfundidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHTipoComboBoxProfundidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHTipoComboBoxProfundidad.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHTipoComboBoxProfundidad.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHTipoComboBoxProfundidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHTipoLabelProfundidad.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad aguas arriba (y)</p></body></html>", None))
        self.RHTipoComboBoxPendientaLateral.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.RHTipoComboBoxPendientaLateral.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.RHTipoComboBoxPendientaLateral.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.RHTipoComboBoxPendientaLateral.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
#if QT_CONFIG(tooltip)
        self.RHTipoFieldInclinacion.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHTipoFieldInclinacion.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHTipoFieldInclinacion.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHTipoFieldInclinacion.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.RHTipoFieldBase.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHTipoFieldBase.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHTipoFieldBase.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHTipoFieldBase.setPlaceholderText("")
        self.RHTipoLabelPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral izquierda</p></body></html>", None))
        self.RHTipoLabelPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral derecha</p></body></html>", None))
        self.RHTipoLabelCaudal.setText(QCoreApplication.translate("MainWindow", u"Caudal (Q)", None))
        self.RHTipoComboBoxBase.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHTipoComboBoxBase.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHTipoComboBoxBase.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHTipoComboBoxBase.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHTipoComboBoxBase.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHTipoComboBoxCaudal.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.RHTipoComboBoxCaudal.setItemText(1, QCoreApplication.translate("MainWindow", u"Litros/segundos", None))

        self.RHTipoComboBoxCaudal.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
#if QT_CONFIG(tooltip)
        self.RHTipoFieldPendienteLateral.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHTipoFieldPendienteLateral.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.RHTipoFieldPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHTipoFieldPendienteLateral.setPlaceholderText("")
        self.RHTipoComboBoxNormal.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHTipoComboBoxNormal.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHTipoComboBoxNormal.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHTipoComboBoxNormal.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHTipoComboBoxNormal.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(tooltip)
        self.RHTipoFieldProfundidad.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHTipoFieldProfundidad.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHTipoFieldProfundidad.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHTipoFieldProfundidad.setPlaceholderText("")
        self.RHTipoLabelProfundidadNormal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad normal aguas abajo (y<span style=\" vertical-align:sub;\">n</span>)</p></body></html>", None))
        self.RHTipoComboBoxInclinacion.setItemText(0, QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.RHTipoComboBoxInclinacion.setItemText(1, QCoreApplication.translate("MainWindow", u"Grados", None))
        self.RHTipoComboBoxInclinacion.setItemText(2, QCoreApplication.translate("MainWindow", u"Radianes", None))

        self.RHTipoComboBoxInclinacion.setCurrentText(QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.RHTipoLabelInclinacion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n canal (S<span style=\" vertical-align:sub;\">0</span>)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHTipoFieldNormal.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHTipoFieldNormal.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHTipoFieldNormal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHTipoFieldNormal.setPlaceholderText("")
        self.RHTipoLabelBase.setText(QCoreApplication.translate("MainWindow", u"Ancho (b)", None))
#if QT_CONFIG(tooltip)
        self.RHTipoFieldCaudal.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHTipoFieldCaudal.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHTipoFieldCaudal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHTipoFieldCaudal.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.RHTipoFieldPendienteLateral2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHTipoFieldPendienteLateral2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.RHTipoFieldPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHTipoFieldPendienteLateral2.setPlaceholderText("")
        self.RHTipoComboBoxPendienteLateral2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.RHTipoComboBoxPendienteLateral2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.RHTipoComboBoxPendienteLateral2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.RHTipoComboBoxPendienteLateral2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.groupBox_Resultados_16.setTitle(QCoreApplication.translate("MainWindow", u"C\u00e1lculos realizados", None))
#if QT_CONFIG(tooltip)
        self.RHTipoFieldSubsecuente.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHTipoFieldSubsecuente.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHTipoFieldSubsecuente.setText("")
        self.RHTipoFieldSubsecuente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.RHTipoLabelSubsecuente.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad subsecuente (y<span style=\" vertical-align:sub;\">2</span>)</p></body></html>", None))
        self.RHTipoLabelAsterisco.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad (y*)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHTipoFieldAsterisco.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHTipoFieldAsterisco.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHTipoFieldAsterisco.setText("")
        self.RHTipoFieldAsterisco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.groupBox_Resultados_13.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
#if QT_CONFIG(tooltip)
        self.RHTipoFieldTipo.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHTipoFieldTipo.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHTipoFieldTipo.setText("")
        self.RHTipoFieldTipo.setPlaceholderText("")
        self.RHTipoLabelTipo.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.RHTipoTextoReiniciar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.RHTipoTextoCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.RHTipoBotonCalcular.setText("")
        self.RHTipoBotonReiniciar.setText("")
        self.tabResaltosHidraulicos.setTabText(self.tabResaltosHidraulicos.indexOf(self.rhTipo), QCoreApplication.translate("MainWindow", u"Tipo de resalto", None))
        self.groupBox_Propiedades_15.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
        self.RHCompuertasComboBoxPendienteLateral.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.RHCompuertasComboBoxPendienteLateral.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.RHCompuertasComboBoxPendienteLateral.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.RHCompuertasComboBoxPendienteLateral.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.RHCompuertasLabelCaudal.setText(QCoreApplication.translate("MainWindow", u"Caudal (Q)", None))
        self.RHCompuertasLabelPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral</p><p>derecha</p></body></html>", None))
        self.RHCompuertasComboBoxAncho.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHCompuertasComboBoxAncho.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHCompuertasComboBoxAncho.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHCompuertasComboBoxAncho.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHCompuertasComboBoxAncho.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(tooltip)
        self.RHCompuertasFieldPendienteLateral.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHCompuertasFieldPendienteLateral.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHCompuertasFieldPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHCompuertasFieldPendienteLateral.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.RHCompuertasFieldCaudal.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHCompuertasFieldCaudal.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHCompuertasFieldCaudal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHCompuertasFieldCaudal.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.RHCompuertasFieldPendienteLateral2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHCompuertasFieldPendienteLateral2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHCompuertasFieldPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHCompuertasFieldPendienteLateral2.setPlaceholderText("")
        self.RHCompuertasComboBoxProfundidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHCompuertasComboBoxProfundidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHCompuertasComboBoxProfundidad.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHCompuertasComboBoxProfundidad.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHCompuertasComboBoxProfundidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHCompuertasComboBoxCaudal.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.RHCompuertasComboBoxCaudal.setItemText(1, QCoreApplication.translate("MainWindow", u"Litros/segundos", None))

        self.RHCompuertasComboBoxCaudal.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.RHCompuertasLabelBase.setText(QCoreApplication.translate("MainWindow", u"Ancho (b)", None))
#if QT_CONFIG(tooltip)
        self.RHCompuertasFieldProfundidad.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHCompuertasFieldProfundidad.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHCompuertasFieldProfundidad.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHCompuertasFieldProfundidad.setPlaceholderText("")
        self.RHCompuertasLabelPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral</p><p>izquierda</p></body></html>", None))
        self.RHCompuertasComboBoxPendienteLateral2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.RHCompuertasComboBoxPendienteLateral2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.RHCompuertasComboBoxPendienteLateral2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.RHCompuertasComboBoxPendienteLateral2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
#if QT_CONFIG(tooltip)
        self.RHCompuertasFieldAncho.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHCompuertasFieldAncho.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHCompuertasFieldAncho.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHCompuertasFieldAncho.setPlaceholderText("")
        self.RHCompuertasLabelProfundidad.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad (y<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
        self.RHCompuertasLabelDiametro.setText(QCoreApplication.translate("MainWindow", u"Di\u00e1metro (D)", None))
#if QT_CONFIG(tooltip)
        self.RHCompuertasFieldDiametro.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHCompuertasFieldDiametro.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHCompuertasFieldDiametro.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHCompuertasFieldDiametro.setPlaceholderText("")
        self.RHCompuertasComboBoxDiametro.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHCompuertasComboBoxDiametro.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHCompuertasComboBoxDiametro.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHCompuertasComboBoxDiametro.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHCompuertasComboBoxDiametro.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.groupBox_Resultados_18.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.RHCompuertasLabelMomentum.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Momentum (M<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHCompuertasFieldFuerza.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHCompuertasFieldFuerza.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHCompuertasFieldFuerza.setText("")
        self.RHCompuertasFieldFuerza.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[N]", None))
#if QT_CONFIG(tooltip)
        self.RHCompuertasFieldMomentum2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHCompuertasFieldMomentum2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHCompuertasFieldMomentum2.setText("")
        self.RHCompuertasFieldMomentum2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
#if QT_CONFIG(tooltip)
        self.RHCompuertasFieldMomentum.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHCompuertasFieldMomentum.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHCompuertasFieldMomentum.setText("")
        self.RHCompuertasFieldMomentum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.RHCompuertasLabelMomentum2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Momentum (M<span style=\" vertical-align:sub;\">2</span>)</p></body></html>", None))
        self.RHCompuertasLabelFuerza.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Fuerza </p><p>espec\u00edfica (F*)</p></body></html>", None))
        self.RHCompuertasLabelFuerzaCompuerta.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Fuerza </p><p>compuerta (F)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RHCompuertasFieldFuerzaCompuerta.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHCompuertasFieldFuerzaCompuerta.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHCompuertasFieldFuerzaCompuerta.setText("")
        self.RHCompuertasFieldFuerzaCompuerta.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[N]", None))
        self.groupBox_Propiedades_17.setTitle(QCoreApplication.translate("MainWindow", u"Par\u00e1metros opcionales", None))
#if QT_CONFIG(tooltip)
        self.RHCompuertasFieldDensidad.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHCompuertasFieldDensidad.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHCompuertasFieldDensidad.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHCompuertasFieldDensidad.setPlaceholderText("")
        self.RHCompuertasLabelDensidad.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Densidad (<span style=\" font-family:'Google Sans Text','arial','sans-serif'; font-size:14px; font-weight:400; color:#4d5156; background-color:#ffffff;\">\u03c1)</span></p></body></html>", None))
        self.RHCompuertasComboBoxDensidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Kilogramos/metros\u00b3", None))

        self.RHCompuertasComboBoxDensidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Kilogramos/metros\u00b3", None))
        self.RHCompuertasLabelProfundidad2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad (y<span style=\" vertical-align:sub;\">2</span>)</p></body></html>", None))
        self.RHCompuertasComboBoxProfundidad2.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.RHCompuertasComboBoxProfundidad2.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.RHCompuertasComboBoxProfundidad2.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.RHCompuertasComboBoxProfundidad2.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.RHCompuertasComboBoxProfundidad2.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(tooltip)
        self.RHCompuertasFieldProfundidad2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RHCompuertasFieldProfundidad2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RHCompuertasFieldProfundidad2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RHCompuertasFieldProfundidad2.setPlaceholderText("")
        self.RHCompuertasTextoReiniciar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.RHCompuertasTextoCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.RHCompuertasBotonCalcular.setText("")
        self.RHCompuertasBotonReiniciar.setText("")
        self.tabResaltosHidraulicos.setTabText(self.tabResaltosHidraulicos.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Compuertas", None))
        self.groupBox_Resultados_7.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
#if QT_CONFIG(tooltip)
        self.ManningCriticaLabelFieldProfundidadCritica.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningCriticaLabelFieldProfundidadCritica.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ManningCriticaLabelFieldProfundidadCritica.setText("")
        self.ManningCriticaLabelFieldProfundidadCritica.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.ManningCriticaLabelProfundidadCritica.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad cr\u00edtica (y<span style=\" vertical-align:sub;\">c</span>)</p></body></html>", None))
        self.ManningCriticaLabelVelocidadCritica.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Velocidad cr\u00edtica (v<span style=\" vertical-align:sub;\">c</span>)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.ManningCriticaLabelFieldVelocidadCritica.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningCriticaLabelFieldVelocidadCritica.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ManningCriticaLabelFieldVelocidadCritica.setText("")
        self.ManningCriticaLabelFieldVelocidadCritica.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m/s]", None))
        self.groupBox_Propiedades_7.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
        self.ManningCriticaTextoCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.ManningCriticaTextoReiniciar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.ManningCriticaBotonCalcular.setText("")
        self.ManningCriticaBotonReiniciar.setText("")
        self.ManningCriticaLabelDiametro.setText(QCoreApplication.translate("MainWindow", u"Di\u00e1metro (D)", None))
        self.ManningCriticaLabelCaudal.setText(QCoreApplication.translate("MainWindow", u"Caudal (Q)", None))
        self.ManningCriticaComboBoxCaudal.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.ManningCriticaComboBoxCaudal.setItemText(1, QCoreApplication.translate("MainWindow", u"Litros/segundos", None))

        self.ManningCriticaComboBoxCaudal.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.ManningCriticaLabelPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral derecha</p></body></html>", None))
        self.ManningCriticaLabelBase.setText(QCoreApplication.translate("MainWindow", u"Base (b)", None))
#if QT_CONFIG(tooltip)
        self.ManningCriticaFieldPendienteLateral2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningCriticaFieldPendienteLateral2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ManningCriticaFieldPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningCriticaFieldPendienteLateral2.setPlaceholderText("")
        self.ManningCriticaComboBoxPendientaLateral.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.ManningCriticaComboBoxPendientaLateral.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.ManningCriticaComboBoxPendientaLateral.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.ManningCriticaComboBoxPendientaLateral.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.ManningCriticaLabelPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral izquierda</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.ManningCriticaFieldCaudal.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningCriticaFieldCaudal.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ManningCriticaFieldCaudal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningCriticaFieldCaudal.setPlaceholderText("")
        self.ManningCriticaComboBoxDiametro.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.ManningCriticaComboBoxDiametro.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.ManningCriticaComboBoxDiametro.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.ManningCriticaComboBoxDiametro.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.ManningCriticaComboBoxDiametro.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.ManningCriticaComboBoxBase.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.ManningCriticaComboBoxBase.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.ManningCriticaComboBoxBase.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.ManningCriticaComboBoxBase.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.ManningCriticaComboBoxBase.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(tooltip)
        self.ManningCriticaFieldBase.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningCriticaFieldBase.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ManningCriticaFieldBase.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningCriticaFieldBase.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.ManningCriticaFieldPendienteLateral.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningCriticaFieldPendienteLateral.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ManningCriticaFieldPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningCriticaFieldPendienteLateral.setPlaceholderText("")
        self.ManningCriticaComboBoxPendientaLateral2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.ManningCriticaComboBoxPendientaLateral2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.ManningCriticaComboBoxPendientaLateral2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.ManningCriticaComboBoxPendientaLateral2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
#if QT_CONFIG(tooltip)
        self.ManningCriticaFieldDiametro.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningCriticaFieldDiametro.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ManningCriticaFieldDiametro.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningCriticaFieldDiametro.setPlaceholderText("")
        self.ManningCriticaLabelVelocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad (v)", None))
#if QT_CONFIG(tooltip)
        self.ManningCriticaFieldVelocidad.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningCriticaFieldVelocidad.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ManningCriticaFieldVelocidad.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningCriticaFieldVelocidad.setPlaceholderText("")
        self.ManningCriticaComboBoxVelocidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros/segundos", None))

        self.ManningCriticaComboBoxVelocidad.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros/segundos", None))
        self.tabManning.setTabText(self.tabManning.indexOf(self.mngFlujoCritico), QCoreApplication.translate("MainWindow", u"Condici\u00f3n cr\u00edtica", None))
        self.groupBox_Propiedades_8.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
        self.ManningPendienteLabelNumManning.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Manning (n)", None))
        self.ManningPendienteLabelAncho.setText(QCoreApplication.translate("MainWindow", u"Ancho (b)", None))
        self.ManningPendienteComboBoxAncho.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.ManningPendienteComboBoxAncho.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.ManningPendienteComboBoxAncho.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.ManningPendienteComboBoxAncho.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.ManningPendienteComboBoxAncho.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(tooltip)
        self.ManningPendienteFieldPendienteLateral.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningPendienteFieldPendienteLateral.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ManningPendienteFieldPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningPendienteFieldPendienteLateral.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.ManningPendienteFieldNumeManning.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningPendienteFieldNumeManning.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ManningPendienteFieldNumeManning.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningPendienteFieldNumeManning.setPlaceholderText("")
        self.ManningPendienteComboBoxNumManning.setItemText(0, QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.ManningPendienteComboBoxNumManning.setItemText(1, QCoreApplication.translate("MainWindow", u"Grados", None))
        self.ManningPendienteComboBoxNumManning.setItemText(2, QCoreApplication.translate("MainWindow", u"Radianes", None))

        self.ManningPendienteComboBoxNumManning.setCurrentText(QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.ManningPendienteComboBoxPendienteLateral.setItemText(0, QCoreApplication.translate("MainWindow", u"Adimensional", None))

        self.ManningPendienteComboBoxPendienteLateral.setCurrentText(QCoreApplication.translate("MainWindow", u"Adimensional", None))
#if QT_CONFIG(tooltip)
        self.ManningPendienteFieldDiametro.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningPendienteFieldDiametro.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ManningPendienteFieldDiametro.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningPendienteFieldDiametro.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.ManningPendienteFieldAncho.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningPendienteFieldAncho.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ManningPendienteFieldAncho.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningPendienteFieldAncho.setPlaceholderText("")
        self.ManningPendienteComboBoxDiametro.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.ManningPendienteComboBoxDiametro.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.ManningPendienteComboBoxDiametro.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.ManningPendienteComboBoxDiametro.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.ManningPendienteComboBoxDiametro.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.ManningPendienteLabelDiametro.setText(QCoreApplication.translate("MainWindow", u"Di\u00e1metro (D)", None))
        self.ManningPendienteLabelPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"Pendiente lateral (m)", None))
        self.groupBox_Resultados_8.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
#if QT_CONFIG(tooltip)
        self.ManningPendienteFieldPendienteCritica.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningPendienteFieldPendienteCritica.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ManningPendienteFieldPendienteCritica.setText("")
        self.ManningPendienteFieldPendienteCritica.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[adimensional]", None))
        self.ManningPendienteLabelPendienteCritica.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pendiente </p><p>cr\u00edtica (S<span style=\" vertical-align:sub;\">c</span>)</p></body></html>", None))
        self.groupBox_Propiedades_18.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e9todo Pendiente Cr\u00edtica L\u00edmite", None))
#if QT_CONFIG(tooltip)
        self.ManningPendienteFieldCaudal.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningPendienteFieldCaudal.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ManningPendienteFieldCaudal.setText("")
        self.ManningPendienteFieldCaudal.setPlaceholderText("")
        self.ManningPendienteLabelCaudal.setText(QCoreApplication.translate("MainWindow", u"Caudal (Q)", None))
        self.ManningPendienteComboBoxCaudal.setItemText(0, QCoreApplication.translate("MainWindow", u"No aplica", None))
        self.ManningPendienteComboBoxCaudal.setItemText(1, QCoreApplication.translate("MainWindow", u"Metros c\u00fabicos/segundos", None))
        self.ManningPendienteComboBoxCaudal.setItemText(2, QCoreApplication.translate("MainWindow", u"Litros/segundos", None))

        self.ManningPendienteComboBoxCaudal.setCurrentText(QCoreApplication.translate("MainWindow", u"No aplica", None))
        self.groupBox_Propiedades_19.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e9todo Pendiente Cr\u00edtica Espec\u00edfica", None))
#if QT_CONFIG(tooltip)
        self.ManningPendienteFieldProfundidadCritica.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningPendienteFieldProfundidadCritica.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ManningPendienteFieldProfundidadCritica.setText("")
        self.ManningPendienteFieldProfundidadCritica.setPlaceholderText("")
        self.ManningPendienteLabelProfundidadCritica.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad</p><p>cr\u00edtica (y<span style=\" vertical-align:sub;\">c</span>)</p></body></html>", None))
        self.ManningPendienteComboBoxProfundidadCritica.setItemText(0, QCoreApplication.translate("MainWindow", u"No aplica", None))
        self.ManningPendienteComboBoxProfundidadCritica.setItemText(1, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.ManningPendienteComboBoxProfundidadCritica.setItemText(2, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.ManningPendienteComboBoxProfundidadCritica.setItemText(3, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.ManningPendienteComboBoxProfundidadCritica.setItemText(4, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.ManningPendienteComboBoxProfundidadCritica.setCurrentText(QCoreApplication.translate("MainWindow", u"No aplica", None))
        self.geoCImagenCanal_10.setText("")
        self.ManningPendienteTextoReiniciar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.ManningPendienteTextoCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.ManningPendienteBotonCalcular.setText("")
        self.ManningPendienteBotonReiniciar.setText("")
        self.tabManning.setTabText(self.tabManning.indexOf(self.mngPendienteCritica), QCoreApplication.translate("MainWindow", u"Pendiente cr\u00edtica", None))
        self.groupBox_Propiedades_9.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
        self.ManningUniformeComboBoxBase.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.ManningUniformeComboBoxBase.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.ManningUniformeComboBoxBase.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.ManningUniformeComboBoxBase.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.ManningUniformeComboBoxBase.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.ManningUniformeLabelPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral izquierda</p></body></html>", None))
        self.ManningUniformeLabelPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n lateral derecha</p></body></html>", None))
        self.ManningUniformeComboBoxDiametro.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.ManningUniformeComboBoxDiametro.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.ManningUniformeComboBoxDiametro.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.ManningUniformeComboBoxDiametro.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.ManningUniformeComboBoxDiametro.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(tooltip)
        self.ManningUniformeFieldPendienteLateral2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningUniformeFieldPendienteLateral2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ManningUniformeFieldPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningUniformeFieldPendienteLateral2.setPlaceholderText("")
        self.ManningUniformeComboBoxPendienteLateral2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.ManningUniformeComboBoxPendienteLateral2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.ManningUniformeComboBoxPendienteLateral2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.ManningUniformeComboBoxPendienteLateral2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
#if QT_CONFIG(tooltip)
        self.ManningUniformeFieldDiametro.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningUniformeFieldDiametro.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ManningUniformeFieldDiametro.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningUniformeFieldDiametro.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.ManningUniformeFieldCaudal.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningUniformeFieldCaudal.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ManningUniformeFieldCaudal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningUniformeFieldCaudal.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.ManningUniformeFieldInclinacion.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningUniformeFieldInclinacion.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ManningUniformeFieldInclinacion.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningUniformeFieldInclinacion.setPlaceholderText("")
        self.ManningUniformeLabelCaudal.setText(QCoreApplication.translate("MainWindow", u"Caudal (Q)", None))
        self.ManningUniformeLabelBase.setText(QCoreApplication.translate("MainWindow", u"Base (b)", None))
        self.ManningUniformeLabelInclinacion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n del canal (S<span style=\" vertical-align:sub;\">0</span>)</p></body></html>", None))
        self.ManningUniformeComboBoxCaudal.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.ManningUniformeComboBoxCaudal.setItemText(1, QCoreApplication.translate("MainWindow", u"Litros/segundos", None))

        self.ManningUniformeComboBoxCaudal.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.ManningUniformeLabelDiametro.setText(QCoreApplication.translate("MainWindow", u"Di\u00e1metro (D)", None))
#if QT_CONFIG(tooltip)
        self.ManningUniformeFieldPendienteLateral.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningUniformeFieldPendienteLateral.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ManningUniformeFieldPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningUniformeFieldPendienteLateral.setPlaceholderText("")
        self.ManningUniformeComboBoxPendienteLateral.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.ManningUniformeComboBoxPendienteLateral.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.ManningUniformeComboBoxPendienteLateral.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.ManningUniformeComboBoxPendienteLateral.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
#if QT_CONFIG(tooltip)
        self.ManningUniformeFieldBase.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningUniformeFieldBase.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ManningUniformeFieldBase.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningUniformeFieldBase.setPlaceholderText("")
        self.ManningUniformeLabelNumManning.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Manning (n)", None))
#if QT_CONFIG(tooltip)
        self.ManningUniformeFieldNumManning.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ManningUniformeFieldNumManning.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ManningUniformeFieldNumManning.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ManningUniformeFieldNumManning.setPlaceholderText("")
        self.ManningUniformeComboBoxInclinacion.setItemText(0, QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.ManningUniformeComboBoxInclinacion.setItemText(1, QCoreApplication.translate("MainWindow", u"Grados", None))
        self.ManningUniformeComboBoxInclinacion.setItemText(2, QCoreApplication.translate("MainWindow", u"Radianes", None))

        self.ManningUniformeComboBoxInclinacion.setCurrentText(QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.ManningUniformeComboBoxNumManning.setItemText(0, QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.ManningUniformeComboBoxNumManning.setItemText(1, QCoreApplication.translate("MainWindow", u"Grados", None))
        self.ManningUniformeComboBoxNumManning.setItemText(2, QCoreApplication.translate("MainWindow", u"Radianes", None))

        self.ManningUniformeComboBoxNumManning.setCurrentText(QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.groupBox_Resultados_9.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.ManningUniformeLabelNormal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad normal (y<span style=\" vertical-align:sub;\">n</span>)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.geoCFieldAngulo_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.geoCFieldAngulo_4.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.geoCFieldAngulo_4.setText("")
        self.geoCFieldAngulo_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Sistema Anglosaj\u00f3n\n"
"de Unidades", None))
#if QT_CONFIG(whatsthis)
        self.checkBox_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Sistema Internacional\n"
"de Unidades", None))
        self.ManningUniformeTextoReiniciar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.ManningUniformeTextoCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.ManningUniformeBotonCalcular.setText("")
        self.ManningUniformeBotonReiniciar.setText("")
        self.tabManning.setTabText(self.tabManning.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Flujo uniforme", None))
        self.groupBox_Propiedades_21.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
#if QT_CONFIG(whatsthis)
        self.FGVFieldAncho.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.FGVFieldAncho.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVFieldAncho.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.FGVFieldPendienteLateral2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVFieldPendienteLateral2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVFieldPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVFieldPendienteLateral2.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.FGVFieldProfundidad2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVFieldProfundidad2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVFieldProfundidad2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVFieldProfundidad2.setPlaceholderText("")
        self.FGVLabelProfundidad1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad (y<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.FGVFieldInclinacion.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVFieldInclinacion.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVFieldInclinacion.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVFieldInclinacion.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.FGVFieldPendienteLateral.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVFieldPendienteLateral.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVFieldPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVFieldPendienteLateral.setPlaceholderText("")
        self.FGVComboBoxInclinacion.setItemText(0, QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.FGVComboBoxInclinacion.setItemText(1, QCoreApplication.translate("MainWindow", u"Grados", None))
        self.FGVComboBoxInclinacion.setItemText(2, QCoreApplication.translate("MainWindow", u"Radianes", None))

        self.FGVComboBoxInclinacion.setCurrentText(QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.FGVComboBoxCaudal.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.FGVComboBoxCaudal.setItemText(1, QCoreApplication.translate("MainWindow", u"Litros/segundos", None))

        self.FGVComboBoxCaudal.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.FGVComboBoxPendienteLateral.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.FGVComboBoxPendienteLateral.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.FGVComboBoxPendienteLateral.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.FGVComboBoxPendienteLateral.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.FGVLabelInclinacion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n del canal (S<span style=\" vertical-align:sub;\">0</span>)</p></body></html>", None))
        self.FGVLabelDiametro.setText(QCoreApplication.translate("MainWindow", u"Di\u00e1metro (D)", None))
        self.FGVLabelCaudal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Caudal (Q)</p></body></html>", None))
        self.FGVComboBoxPendienteLateral2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.FGVComboBoxPendienteLateral2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.FGVComboBoxPendienteLateral2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.FGVComboBoxPendienteLateral2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
#if QT_CONFIG(tooltip)
        self.FGVFieldCaudal.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVFieldCaudal.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVFieldCaudal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVFieldCaudal.setPlaceholderText("")
        self.FGVComboBoxProfundidad2.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVComboBoxProfundidad2.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.FGVComboBoxProfundidad2.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.FGVComboBoxProfundidad2.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.FGVComboBoxProfundidad2.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVLabelProfundidad2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad (y<span style=\" vertical-align:sub;\">2</span>)</p></body></html>", None))
        self.FGVComboBoxProfundidad1.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVComboBoxProfundidad1.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.FGVComboBoxProfundidad1.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.FGVComboBoxProfundidad1.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.FGVComboBoxProfundidad1.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
#if QT_CONFIG(tooltip)
        self.FGVFieldProfundidad1.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVFieldProfundidad1.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVFieldProfundidad1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVFieldProfundidad1.setPlaceholderText("")
        self.FGVLabelPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pendiente lateral (m<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
        self.FGVComboBoxAncho.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVComboBoxAncho.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.FGVComboBoxAncho.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.FGVComboBoxAncho.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.FGVComboBoxAncho.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVLabelAncho.setText(QCoreApplication.translate("MainWindow", u"Ancho (b)", None))
        self.FGVComboBoxDiametro.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVComboBoxDiametro.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.FGVComboBoxDiametro.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.FGVComboBoxDiametro.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.FGVComboBoxDiametro.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVLabelPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pendiente lateral (m<span style=\" vertical-align:sub;\">2</span>)</p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.FGVFieldDiametro.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.FGVFieldDiametro.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVFieldDiametro.setPlaceholderText("")
        self.FGVLabelManning.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Manning (n)", None))
#if QT_CONFIG(tooltip)
        self.FGVFieldNumManning.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVFieldNumManning.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVFieldNumManning.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVFieldNumManning.setPlaceholderText("")
        self.RHAnalisisComboBoxPendienteLateral_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Adimensional", None))

        self.RHAnalisisComboBoxPendienteLateral_5.setCurrentText(QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.groupBox_Resultados_19.setTitle(QCoreApplication.translate("MainWindow", u"Resultados", None))
#if QT_CONFIG(tooltip)
        self.FGVFieldDistanciaX.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVFieldDistanciaX.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVFieldDistanciaX.setText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.FGVFieldDistanciaX.setPlaceholderText("")
        self.FGVLabelDistanciaX.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Distancia (x)</p></body></html>", None))
        self.RHAnalisisTextoCalcular_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcula la longitud que requiere </p><p>el flujo para pasar de una </p><p>profundidad a otra.</p><p><br/></p></body></html>", None))
        self.geoCImagenCanal_11.setText("")
        self.FGVTextoReiniciar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.FGVTextoCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.FGVBotonCalcular.setText("")
        self.FGVBotonReiniciar.setText("")
        self.tabFGV.setTabText(self.tabFGV.indexOf(self.rhLongitud), QCoreApplication.translate("MainWindow", u"Integral", None))
        self.RHAnalisisTextoCalcular_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">Calcula el perfil de un flujo </p><p align=\"justify\">gradualmente variado a partir </p><p align=\"justify\">de una aproximaci\u00f3n de </p><p align=\"justify\">diferencias finitas. <br/></p></body></html>", None))
        self.groupBox_Propiedades_22.setTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
#if QT_CONFIG(whatsthis)
        self.FGVPasoDFieldAncho.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.FGVPasoDFieldAncho.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVPasoDFieldAncho.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.FGVPasoDFieldCaudal.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVPasoDFieldCaudal.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVPasoDFieldCaudal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVPasoDFieldCaudal.setPlaceholderText("")
        self.FGVPasoDLabelProfundidadObjetivo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad objetivo (y<span style=\" vertical-align:sub;\">2</span>)</p></body></html>", None))
        self.FGVPasoDLabelAncho.setText(QCoreApplication.translate("MainWindow", u"Ancho (b)", None))
        self.FGVPasoDComboBoxNumManning.setItemText(0, QCoreApplication.translate("MainWindow", u"Adimensional", None))

        self.FGVPasoDComboBoxNumManning.setCurrentText(QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.FGVPasoDLabelNumManning.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Manning (n)", None))
#if QT_CONFIG(tooltip)
        self.FGVPasoDFieldNumManning.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVPasoDFieldNumManning.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVPasoDFieldNumManning.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVPasoDFieldNumManning.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.FGVPasoDFieldPendienteLateral.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVPasoDFieldPendienteLateral.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVPasoDFieldPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVPasoDFieldPendienteLateral.setPlaceholderText("")
        self.FGVPasoDComboBoxInclinacion.setItemText(0, QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.FGVPasoDComboBoxInclinacion.setItemText(1, QCoreApplication.translate("MainWindow", u"Grados", None))
        self.FGVPasoDComboBoxInclinacion.setItemText(2, QCoreApplication.translate("MainWindow", u"Radianes", None))

        self.FGVPasoDComboBoxInclinacion.setCurrentText(QCoreApplication.translate("MainWindow", u"Adimensional", None))
        self.FGVPasoDLabelDiametro.setText(QCoreApplication.translate("MainWindow", u"Di\u00e1metro (D)", None))
        self.FGVPasoDLabelPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pendiente lateral (m<span style=\" vertical-align:sub;\">2</span>)</p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.FGVPasoDFieldDiametro.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.FGVPasoDFieldDiametro.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVPasoDFieldDiametro.setPlaceholderText("")
        self.FGVPasoDComboBoxAncho.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVPasoDComboBoxAncho.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.FGVPasoDComboBoxAncho.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.FGVPasoDComboBoxAncho.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.FGVPasoDComboBoxAncho.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVPasoDComboBoxCaudal.setItemText(0, QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
        self.FGVPasoDComboBoxCaudal.setItemText(1, QCoreApplication.translate("MainWindow", u"Litros/segundos", None))

        self.FGVPasoDComboBoxCaudal.setCurrentText(QCoreApplication.translate("MainWindow", u"Metros\u00b3/segundos", None))
#if QT_CONFIG(tooltip)
        self.FGVPasoDFieldProfundidadControl.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVPasoDFieldProfundidadControl.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVPasoDFieldProfundidadControl.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVPasoDFieldProfundidadControl.setPlaceholderText("")
        self.FGVPasoDLabelProfundidadControl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Profundidad de control (y<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
        self.FGVPasoDLabelInclinacion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Inclinaci\u00f3n del canal (S<span style=\" vertical-align:sub;\">0</span>)</p></body></html>", None))
        self.FGVPasoDLabelCaudal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Caudal (Q)</p></body></html>", None))
        self.FGVPasoDComboBoxPendienteLateral2.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.FGVPasoDComboBoxPendienteLateral2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.FGVPasoDComboBoxPendienteLateral2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.FGVPasoDComboBoxPendienteLateral2.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
#if QT_CONFIG(tooltip)
        self.FGVPasoDFieldProfundidadObjetivo.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVPasoDFieldProfundidadObjetivo.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVPasoDFieldProfundidadObjetivo.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVPasoDFieldProfundidadObjetivo.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.FGVPasoDFieldPendienteLateral2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVPasoDFieldPendienteLateral2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVPasoDFieldPendienteLateral2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVPasoDFieldPendienteLateral2.setPlaceholderText("")
        self.FGVPasoDComboBoxPendienteControl.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVPasoDComboBoxPendienteControl.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.FGVPasoDComboBoxPendienteControl.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.FGVPasoDComboBoxPendienteControl.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.FGVPasoDComboBoxPendienteControl.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVPasoDLabelPendienteLateral.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pendiente lateral (m<span style=\" vertical-align:sub;\">1</span>)</p></body></html>", None))
        self.FGVPasoDComboBoxPendienteObjetivo.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVPasoDComboBoxPendienteObjetivo.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.FGVPasoDComboBoxPendienteObjetivo.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.FGVPasoDComboBoxPendienteObjetivo.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.FGVPasoDComboBoxPendienteObjetivo.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVPasoDComboBoxDiametro.setItemText(0, QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVPasoDComboBoxDiametro.setItemText(1, QCoreApplication.translate("MainWindow", u"Cent\u00edmetros", None))
        self.FGVPasoDComboBoxDiametro.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.FGVPasoDComboBoxDiametro.setItemText(3, QCoreApplication.translate("MainWindow", u"Pulgadas", None))

        self.FGVPasoDComboBoxDiametro.setCurrentText(QCoreApplication.translate("MainWindow", u"Mil\u00edmetros", None))
        self.FGVPasoDComboBoxPendienteLateral.setItemText(0, QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
        self.FGVPasoDComboBoxPendienteLateral.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03b1 - Grados", None))
        self.FGVPasoDComboBoxPendienteLateral.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03b1 - Radianes", None))

        self.FGVPasoDComboBoxPendienteLateral.setCurrentText(QCoreApplication.translate("MainWindow", u"m - Adimensional", None))
#if QT_CONFIG(tooltip)
        self.FGVPasoDFieldInclinacion.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVPasoDFieldInclinacion.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVPasoDFieldInclinacion.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVPasoDFieldInclinacion.setPlaceholderText("")
        self.FGVPasoDTextoReiniciar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reiniciar</p></body></html>", None))
        self.FGVPasoDTextoCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.FGVPasoDBotonCalcular.setText("")
        self.FGVPasoDBotonReiniciar.setText("")
        self.FGVPasoDBotonDescargarCSV.setText(QCoreApplication.translate("MainWindow", u"Descargar archivo .csv", None))
        self.FGVPasoDBotonDescargarPerfil.setText(QCoreApplication.translate("MainWindow", u"Descargar perfil", None))
        self.groupBox_Resultados_21.setTitle(QCoreApplication.translate("MainWindow", u"Par\u00e1metros m\u00e9todo", None))
        self.FGVPasoDLabelPasos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pasos</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.FGVPasoDFieldPasos.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVPasoDFieldPasos.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVPasoDFieldPasos.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVPasoDFieldPasos.setPlaceholderText("")
        self.FGVPasoDLabelDatum.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Datum</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.FGVPasoDFieldDatum.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FGVPasoDFieldDatum.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FGVPasoDFieldDatum.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FGVPasoDFieldDatum.setPlaceholderText("")
        self.tabFGV.setTabText(self.tabFGV.indexOf(self.rhPasoDirecto), QCoreApplication.translate("MainWindow", u"Paso directo", None))
        self.tabFGV.setTabText(self.tabFGV.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Paso est\u00e1ndar", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Universidad de los Andes - 2021", None))
    # retranslateUi

