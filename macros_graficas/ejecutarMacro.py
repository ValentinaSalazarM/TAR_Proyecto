import xlwings as xw
import os

def macroPasoDirecto (ruta):
    print ("D: RUTA: ", ruta)
    excel_app = xw.App(visible=False)
    excel_book = excel_app.books.open('macros_graficas' + os.path.sep + 'GraficaPasoDirecto.xlsm')
    macro = excel_book.macro('Módulo1.ModificarDatos')
    macro(ruta)
    excel_book.save()
    excel_book.close()
    excel_app.quit()

    print ("D: Ejecutan2")

def macroPasoEstandar (ruta):
    print ("E: RUTA: ", ruta)
    excel_app = xw.App(visible=False)
    excel_book = excel_app.books.open('macros_graficas' + os.path.sep + 'GraficaPasoEstandar.xlsm')
    macro = excel_book.macro('Módulo1.ModificarDatos')
    macro(ruta)
    excel_book.save()
    excel_book.close()
    excel_app.quit()

    print ("E: Ejecutan2")




