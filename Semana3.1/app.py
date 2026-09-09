# Importar la libreri pip install nicegui
from nicegui import ui

# Link de referencia https://docs.python.org/es/3/tutorial/datastructures.html#

# Definir Lista
item = [20, 50, 9, 45]

# Definit los metodos para la lista
def render_list():
    # Dibujar los cuadros de memoria de mi lista
    list_container.clear()
    with list_container:
        if not item:
            ui.label('Lista vacía').classes('text-gray-400 italic')
            return

        with ui.row().classes('items-center gap-2 flex-wrap'):
            for idx, val in enumerate(item):
                with ui.column().classes('items-center gap-1'):
                    # Muestra el valor de elemento
                    ui.label(str(val)).classes('w-16 h-16 flex items-center justify-center '
                        'bg-blue-800 text-white font-bold text-lg rounded-lg shadow-md')
                    # Muestra el indice del elemento
                    ui.label(f'[{idx}]*').classes('text-xs font-semibold text-slate-700')

# Metodo append
def do_append():
    if val_input.value is not None:
        item.append(val_input.value)
        render_list()    

# Metodo Insert
def do_insert():
    if val_input.value is not None and idx_input is not None:
        idx = max(0, min(int(idx_input.value), len(item)))
        item.insert(idx, val_input.value)
        render_list()


# Metodo Pop

# Metodo Clear


# Interface
ui.page_title('Visualizador de Listas en Python con NiceGui')

# Contenedor Principal
with ui.column().classes('p-6 gap-6 w-full'):
    ui.label('Practica Grafica de una Lista').classes('text-2xl font-bold text-state-800')

    # Contenedor de los espacios de memoria
    with ui.card().classes('w-full p-4 min-h-[140px] bg-slate-50 border-slate-200'):
        list_container = ui.row().classes('w-full items-center')

    # Panel de Control (Las entradas y los Metodos)
    with ui.card().classes('w-full p-4 gap-4'):
        ui.label('OPERACIONES').classes('text-sm font-semibold text-slate-500')   

        # Contenedor de entrada de datos
        with ui.row().classes('gap-4 items-center'):
            val_input = ui.number('Valor', placeholder="Introduce un número").classes('w-40')
            idx_input = ui.number('Indice', value=0, min=0).classes('w-40')

        # Contenedor de botones de accion
        with ui.row():
            ui.button('append(x)', icon='add', color='secondary', on_click=do_append)
            ui.button('insert(i)', icon='add_circle', color='info', on_click=do_insert)
            ui.button('pop(i)', icon='remove', color='warning')
            ui.button('clear()', icon='delete', color='red')

render_list()
ui.run()