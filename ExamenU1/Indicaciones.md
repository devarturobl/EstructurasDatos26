Markdown
# Evaluación Práctica: Laboratorio Visual de Métodos de Listas en Python

**Materia:** Estructuras de Datos / Programación en Python  
**Tipo de Evaluación:** Examen Práctico de Unidad  
**Valor:** 100% de la práctica  

---

## 🎯 Objetivo de la Práctica
Desarrollar una aplicación web interactiva utilizando el framework **NiceGUI** en Python, que permita visualizar de forma gráfica el comportamiento en memoria de los métodos principales de una lista (estructura de datos lineal), incorporando un panel de control con validaciones y notificaciones en tiempo real para evitar errores de ejecución.

---

## 📋 Instrucciones Generales
1. Deberás configurar tu entorno de desarrollo en **Visual Studio Code** e instalar la librería necesaria mediante la terminal:
   ```bash
   pip install nicegui
El programa debe construirse en un único archivo de Python (.py) y ejecutarse correctamente en el navegador web local.

La interfaz debe cumplir obligatoriamente con la visualización dinámica de los bloques de memoria de la lista, mostrando tanto sus valores numéricos como sus respectivos índices.

Se evaluará el manejo correcto de excepciones (bloqueo de errores por listas vacías o índices fuera de rango) y la retroalimentación mediante notificaciones visuales (ui.notify).

⚙️ Requerimientos Funcionales (Métodos a Implementar)
Tu programa debe contener controles interactivos para los siguientes 8 métodos oficiales de las listas en Python:

append(x): Agrega un elemento al final de la lista utilizando el valor introducido en la interfaz. Si el campo está vacío, debe mostrar una alerta de advertencia.

insert(i, x): Inserta un elemento en un índice específico (i) validando que los límites se mantengan dentro del rango permitido de la lista.

pop(i): Remueve y devuelve el elemento ubicado en el índice seleccionado. Debe validar que la lista no se encuentre vacía antes de ejecutar la acción.

remove(x): Busca y elimina la primera ocurrencia del valor exacto indicado. Si el elemento no existe en la lista, debe notificar un error de tipo negative.

sort(): Ordena todos los elementos de la lista de forma ascendente. Si la lista está vacía, debe emitir una advertencia informativa.

reverse(): Invierte el orden actual de los elementos contenidos en la lista de manera instantánea.

count(x): Cuenta e informa mediante una notificación cuántas veces se repite un valor específico dentro de la estructura de datos.

clear(): Vacía por completo todos los elementos de la lista de forma segura.

💻 Código Base de Referencia
Utiliza la siguiente estructura orientativa para asegurar el diseño visual y la reactividad esperada con NiceGUI:

Python
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
    else:
        ui.notify('Error: Debes introducir un valor para usar append().', color='warning')   

# Metodo Insert
def do_insert():
    if val_input.value is not None and idx_input is not None:
        idx = max(0, min(int(idx_input.value), len(item)))
        item.insert(idx, val_input.value)
        render_list()
    else:
        ui.notify('Error: Faltan datos (Valor o Índice) para realizar insert().', color='warning')

# Metodo Pop
def do_pop():
    if not item:
        ui.notify('Error: La lista está vacía, no se puede hacer pop().', color='negative')
        return
    
    if idx_input is not None:
            idx = max(0, min(int(idx_input.value), len(item)))
            item.pop(idx)
            render_list()

# Metodo Clear
def do_clear():
    item.clear()
    render_list()

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
            ui.button('pop(i)', icon='remove', color='warning', on_click=do_pop)
            ui.button('clear()', icon='delete', color='red', on_click=do_clear)

render_list()
ui.run()

📦 Criterios de Evaluación
Funcionamiento lógico (40%): Todos los métodos operan correctamente según la documentación oficial de Python.

Interfaz Gráfica y Reactividad (30%): Los cambios se reflejan visualmente de manera inmediata en pantalla mediante render_list().

Manejo de Errores y Notificaciones (20%): Uso correcto de ui.notify ante entradas vacías o índices no válidos, evitando caídas del sistema (crashes).

Presentación y Código Limpio (10%): Estructura clara, uso de comentarios y buenas prácticas de codificación.