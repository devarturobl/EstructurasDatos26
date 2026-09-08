from nicegui import ui

i.markdown("# Este es mi primer proyecto con NiceGui")
ui.label("Hola a mi primer Etiqueta")
ui.link("Consulta este y otros repositorios", 'https://github.com/devarturobl/EstructurasDatos26')
ui.button("Mi Boton")

ui.run(host='127.0.0.1', port=8080, native=False, title="Mi Lista de Tareas")