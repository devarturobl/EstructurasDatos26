from nicegui import ui

originales = [5, 9, 2, 7, 9, 6, 3, 5, 4, 7, 9, 3, 5, 4, 7, 7, 8, 2]
valores = originales.copy()

# Interface del programa
ui.page_title('Visualizador de Listas en Python con NiceGui')

# Contenedor principal
with ui.column():
    ui.label("Practica de listas con metodos de ordenamiento")
    with ui.column():
        ui.label("Grafico de Datos en la lista")
        # Lista de valores proporcionada
        # Configuración del gráfico de barras usando ECharts
        ui.echart({
            'xAxis': {
                'type': 'category',
                'data': [str(i + 1) for i in range(len(valores))]  # Etiquetas para el eje X (índices del 1 al 18)
            },
            'yAxis': {
                'type': 'value'
            },
            'series': [{
                'type': 'bar',
                'data': valores,
                'itemStyle': {
                    'color': '#3b82f6'  # Color de las barras (azul moderno)
                }
            }]
        })

ui.run()