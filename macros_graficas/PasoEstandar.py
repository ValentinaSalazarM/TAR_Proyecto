import xlwings as xw

def ejecutarMacro (ruta):
    print ("RUTA: ", ruta)
    excel_app = xw.App(visible=False)
    excel_book = excel_app.books.open('./GraficaPasoDirecto.xlsm')
    macro = excel_book.macro('Módulo1.ModificarDatos')
    macro(ruta)
    excel_book.save()
    excel_book.close()
    excel_app.quit()

    print ("Ejecutan2")




