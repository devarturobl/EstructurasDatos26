from nicegui import ui

originales = [1, 34, 55, 22, 5, 9, 2, 7, 9, 6, 3, 5, 4, 7, 9, 3, 5, 4, 7, 7, 8, 2, 1, 20, 10]
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
    grafico.options['xAxis']['data'] = [str(i + 1) for i in range(len(valores))]
    grafico.options['series'][0]['data'] = valores
    grafico.update()
    
    # Actualizar tarjetas de métricas dinámicamente
    lbl_min.set_text(str(min(valores)))
    lbl_max.set_text(str(max(valores)))
    lbl_prom.set_text(f"{sum(valores)/len(valores):.1f}")

# Configuración de página y estilos globales oscuros (Dark Theme profesional)
ui.page_title('Visualizador de Ordenamiento Pro')
ui.add_head_html('''
<style>
    body {
        background-color: #090d16;
        color: #f1f5f9;
        font-family: 'Inter', system-ui, sans-serif;
        margin: 0;
        overflow-x: hidden;
    }
    .glass-card {
        background: rgba(17, 24, 39, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        border-radius: 20px;
    }
</style>
''')

# Contenedor principal a pantalla completa (flexbox que ocupa el 100% de la altura de la ventana)
with ui.column().classes('w-screen h-screen p-6 justify-between items-center box-border'):
    
    # --- ENCABEZADO ---
    with ui.row().classes('w-full max-w-7xl justify-between items-center'):
        with ui.column().classes('gap-0'):
            ui.label('DATALAB STUDIO').classes('text-xs font-extrabold tracking-widest text-indigo-400 uppercase')
            ui.label('Algoritmo de Ordenamiento Burbuja').classes('text-2xl md:text-3xl font-black text-white')
        ui.badge('Python + NiceGUI', color='indigo').props('outline')

    # --- TARJETAS DE MÉTRICAS RÁPIDAS ---
    with ui.row().classes('w-full max-w-7xl gap-4'):
        with ui.card().classes('glass-card flex-1 p-4 flex-row items-center gap-4'):
            ui.icon('functions', size='md').classes('text-indigo-400')
            with ui.column().classes('gap-0'):
                ui.label('MÍNIMO').classes('text-xs text-slate-400 font-bold')
                lbl_min = ui.label(str(min(valores))).classes('text-xl font-bold text-white')
                
        with ui.card().classes('glass-card flex-1 p-4 flex-row items-center gap-4'):
            ui.icon('trending_up', size='md').classes('text-cyan-400')
            with ui.column().classes('gap-0'):
                ui.label('MÁXIMO').classes('text-xs text-slate-400 font-bold')
                lbl_max = ui.label(str(max(valores))).classes('text-xl font-bold text-white')
                
        with ui.card().classes('glass-card flex-1 p-4 flex-row items-center gap-4'):
            ui.icon('bar_chart', size='md').classes('text-emerald-400')
            with ui.column().classes('gap-0'):
                ui.label('PROMEDIO').classes('text-xs text-slate-400 font-bold')
                lbl_prom = ui.label(f"{sum(valores)/len(valores):.1f}").classes('text-xl font-bold text-white')

    # --- CONTENEDOR CENTRAL: GRÁFICO A PANTALLA COMPLETA FLEXIBLE ---
    with ui.card().classes('glass-card w-full max-w-7xl flex-1 p-6 flex flex-col justify-center items-center my-2'):
        grafico = ui.echart({
            'backgroundColor': 'transparent',
            'grid': {'top': 30, 'bottom': 30, 'left': 40, 'right': 20},
            'tooltip': {'trigger': 'axis'},
            'xAxis': {
                'type': 'category',
                'data': [str(i + 1) for i in range(len(valores))],
                'axisLine': {'lineStyle': {'color': '#334155'}},
                'axisLabel': {'color': '#94a3b8', 'fontSize': 11}
            },
            'yAxis': {
                'type': 'value',
                'splitLine': {'lineStyle': {'color': 'rgba(255, 255, 255, 0.05)'}},
                'axisLabel': {'color': '#94a3b8', 'fontSize': 11}
            },
            'series': [{
                'type': 'bar',
                'data': valores,
                'barMaxWidth': 35,
                'itemStyle': {
                    'color': {
                        'type': 'linear', 'x': 0, 'y': 0, 'x2': 0, 'y2': 1,
                        'colorStops': [
                            {'offset': 0, 'color': '#6366f1'},  # Índigo brillante
                            {'offset': 1, 'color': '#06b6d4'}   # Cian moderno
                        ]
                    },
                    'borderRadius': [6, 6, 0, 0]
                }
            }]
        }).classes('w-full h-full')

    # --- PANEL DE CONTROL (BOTONES) ---
    with ui.row().classes('w-full max-w-7xl justify-center gap-4 py-2'):
        ui.button('Burbuja Ascendente', icon='arrow_upward', on_click=burburja_asc).props('unelevated color=indigo rounded').classes('px-6 py-3 font-semibold shadow-lg')
        ui.button('Burbuja Descendente', icon='arrow_downward', on_click=burburja_desc).props('unelevated color=cyan rounded').classes('px-6 py-3 font-semibold text-slate-900 shadow-lg')
        ui.button('Reiniciar Original', icon='restart_alt', on_click=reiniciar).props('outline color=grey-5 rounded').classes('px-6 py-3 font-semibold text-white')

ui.run(port=8080)