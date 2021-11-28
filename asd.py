        b =  float (widgets.ManningUniformeFieldAncho.text())
        d =  float (widgets.ManningUniformeFieldDiametro.text())
        n =  float (widgets.ManningUniformeFieldNumeManning.text())       
        m1 =  float (widgets.ManningUniformeFieldUniformeLateral.text())
        m2 =  float (widgets.ManningUniformeFieldUniformeLateral2.text())

        ub = widgets.ManningUniformeComboBoxAncho.currentText()
        ub = cambioUnidadesLongitud[ub]
        
        um1 = widgets.ManningUniformeComboBoxUniformeLateral.currentText().split(" - ")[1]
        um1 = cambioUnidadesAngulo[um1]

        um2 = widgets.ManningUniformeComboBoxUniformeLateral2.currentText().split(" - ")[1]
        um2 = cambioUnidadesAngulo[um2]

        ud = widgets.ManningCriticaComboBoxDiametro.currentText()
        ud = cambioUnidadesLongitud[ud]

        uQ = widgets.ManningUniformeComboBoxCaudal.currentText()
        
        if uQ == "No aplica":
            yc = float (widgets.ManningUniformeFieldProfundidadCritica.text())
            UniformeC_especifica(n,yc,b,m1,m2,um1,d,ub,ud,"m")
        else:
            Q = float (widgets.ManningUniformeFieldCaudal.text())
            uQ = "L" if uQ == "Litros/segundos" else uQ == "Metros³/segundos"
            UniformeC_limite(n,Q,b,m1,m2,um1,d,uQ,ub,ud)