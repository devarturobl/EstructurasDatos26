# Semana 3 Trabajando Estructuras y NiceGUI

## Crear un entorno virtual de desarrollo
```python -m venv .venv```

## Usaremos el Framework NicegUI
### Consulta el framework en:
https://nicegui.io/

### Código de instalación
```pip install nicegui```

### Modo de Uso
1 Importar en el proyecto la libreria
```from nicegui import ui```

2 Trabajando con elementos de nicegui
consulta la lista de elementos en https://nicegui.io/documentation/section_text_elements

    Agregar un boton
```ui.button("Mi Boton")```
    Agregar una Etiqueta
```ui.label("Hola Soy una Etiqueta)```

### Etiqueta para reproducir el app
ui.run(host='127.0.0.1', port=8080, native=False, title="Mi Lista de Tareas")

### Ejuctar la app
```python nombre.py```
