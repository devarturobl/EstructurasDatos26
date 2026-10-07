from nicegui import ui

originales = [5, 9, 2, 7, 9, 6, 3, 5, 4, 7, 9, 3, 5, 4, 7, 7, 8, 2]
valores = originales.copy()

def burburja_asc():
    global valores
    n = len(valores)
    for i in range(n):
        for j in range(0, n-i-1):
            if valores[j] > valores[j+1]:
                valores[j], valores[j+1] = valores[j+1], valores[j]
    actualizar_grafico()

def burburja_desc():
    global valores
    n = len(valores)
    for i in range(n):
        for j in range(0, n-i-1):
            if valores[j] < valores[j+1]:
                valores[j], valores[j+1] = valores[j+1], valores[j]
    actualizar_grafico()

def reiniciar():
    global valores
    valores = originales.copy()
    actualizar_grafico()

def actualizar_grafico():
    # Actualizamos los datos del gráfico utilizando su referencia guardada
    grafico.options['xAxis']['data'] = [str(i + 1) for i in range(len(valores))]
    grafico.options['series'][0]['data'] = valores
    grafico.update() # Forzar a que la interfaz vuelva a renderizar el gráfico
    
# Interface del programa
ui.page_title('Visualizador de Listas en Python con NiceGui')

# Contenedor principal
with ui.column():
    ui.label("Practica de listas con metodos de ordenamiento")
    with ui.column():
        ui.label("Grafico de Datos en la lista")
        
        # Guardamos la instancia del gráfico en una variable 'grafico'
        grafico = ui.echart({
            'xAxis': {
                'type': 'category',
                'data': [str(i + 1) for i in range(len(valores))]
            },
            'yAxis': {
                'type': 'value'
            },
            'series': [{
                'type': 'bar',
                'data': valores,
                'itemStyle': {
                    'color': '#3b82f6'
                }
            }]
        })
        
    with ui.column():
        with ui.row():
            ui.button('Burbuja Ascendente', on_click=burburja_asc)
            ui.button('Burbuja Descendente', on_click=burburja_desc)
            ui.button('Reiniciar', on_click=reiniciar)
                        
ui.run()