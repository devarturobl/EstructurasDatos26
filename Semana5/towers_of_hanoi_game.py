import asyncio
from nicegui import ui

# Configuración de estilos globales con shared=True
ui.add_head_html(
    '<script src="https://cdn.tailwindcss.com"></script>', shared=True
)
ui.add_head_html(
    """
<style>
    .disk-transition {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .peg-glow:hover {
        border-color: #6366f1 !important;
        background-color: rgba(99, 102, 241, 0.05);
    }
</style>
""",
    shared=True,
)


class HanoiGame:

  def __init__(self):
    self.num_disks = 4
    self.pegs = {"A": [], "B": [], "C": []}
    self.selected_peg = None
    self.moves_count = 0
    self.timer_seconds = 0
    self.timer_active = False
    self.game_won = False
    self.auto_solving = False
    self.auto_task = None
    self.ui_updater = None  # Función de callback para refrescar la UI

    # Paleta de colores atractiva para los discos
    self.disk_colors = [
        "bg-rose-500 shadow-rose-500/50",
        "bg-amber-500 shadow-amber-500/50",
        "bg-emerald-500 shadow-emerald-500/50",
        "bg-cyan-500 shadow-cyan-500/50",
        "bg-violet-500 shadow-violet-500/50",
        "bg-fuchsia-500 shadow-fuchsia-500/50",
        "bg-blue-500 shadow-blue-500/50",
    ]
    self.init_pegs()

  def init_pegs(self):
    self.pegs = {
        "A": list(range(self.num_disks, 0, -1)),
        "B": [],
        "C": [],
    }

  def reset_game(self):
    self.auto_solving = False
    if self.auto_task:
      self.auto_task.cancel()

    self.init_pegs()
    self.selected_peg = None
    self.moves_count = 0
    self.timer_seconds = 0
    self.timer_active = False
    self.game_won = False
    self.update_ui()

  def handle_peg_click(self, peg_name: str):
    if self.game_won or self.auto_solving:
      return

    # Iniciar temporizador en el primer movimiento
    if not self.timer_active and (
        self.selected_peg or len(self.pegs[peg_name]) > 0
    ):
      self.timer_active = True

    if self.selected_peg is None:
      if len(self.pegs[peg_name]) > 0:
        self.selected_peg = peg_name
    else:
      if self.selected_peg == peg_name:
        self.selected_peg = None
      else:
        source = self.selected_peg
        dest = peg_name

        if len(self.pegs[source]) > 0:
          disk = self.pegs[source][-1]
          # Validar regla de las Torres de Hanói (disco menor sobre mayor)
          if len(self.pegs[dest]) == 0 or disk < self.pegs[dest][-1]:
            self.pegs[dest].append(self.pegs[source].pop())
            self.moves_count += 1

            if len(self.pegs["C"]) == self.num_disks:
              self.game_won = True
              self.timer_active = False
              ui.notify(
                  f"🎉 ¡Victoria! Completado en {self.moves_count} movimientos.",
                  type="positive",
                  position="center",
                  color="green",
              )
          else:
            ui.notify(
                "¡Movimiento inválido! No puedes poner un disco grande sobre"
                " uno pequeño.",
                type="warning",
            )
        self.selected_peg = None

    self.update_ui()

  async def auto_solve(self):
    if self.auto_solving:
      return
    self.reset_game()
    self.auto_solving = True
    self.timer_active = True
    self.update_ui()

    try:
      await self._hanoi_recursive(self.num_disks, "A", "C", "B")
      if len(self.pegs["C"]) == self.num_disks:
        self.game_won = True
        self.timer_active = False
        ui.notify(
            "🤖 ¡Modo automático completado con éxito!",
            type="positive",
            position="center",
        )
    except asyncio.CancelledError:
      pass
    finally:
      self.auto_solving = False
      self.update_ui()

  async def _hanoi_recursive(self, n, origen, destino, auxiliar):
    if not self.auto_solving:
      return
    if n == 1:
      await asyncio.sleep(0.4)
      if self.pegs[origen]:
        disk = self.pegs[origen].pop()
        self.pegs[destino].append(disk)
        self.moves_count += 1
        self.update_ui()
      return

    await self._hanoi_recursive(n - 1, origen, auxiliar, destino)
    if not self.auto_solving:
      return
    await asyncio.sleep(0.4)
    if self.pegs[origen]:
      disk = self.pegs[origen].pop()
      self.pegs[destino].append(disk)
      self.moves_count += 1
      self.update_ui()
    await self._hanoi_recursive(n - 1, auxiliar, destino, origen)

  def update_ui(self):
    if self.ui_updater:
      self.ui_updater()


# Instancia del juego
game = HanoiGame()

# Interfaz Principal con NiceGUI
with ui.element("div").classes(
    "w-screen h-screen bg-slate-950 text-slate-100 flex flex-col items-center"
    " justify-between p-4 md:p-8 select-none font-sans"
):

  # Header / Título
  with ui.element("div").classes(
      "flex flex-col items-center text-center space-y-2"
  ):
    ui.label("🗼 Torres de Hanói - Arcade Edition").classes(
        "text-3xl md:text-5xl font-black tracking-wider bg-gradient-to-r"
        " from-indigo-400 via-purple-400 to-pink-400 bg-clip-text text-transparent"
    )
    ui.label(
        "Mueve todos los discos de la torre A a la torre C. Regla: Solo un"
        " disco a la vez y nunca uno mayor sobre uno menor."
    ).classes("text-slate-400 text-xs md:text-sm max-w-xl")

  # Contenedor dinámico del tablero
  container = ui.element("div").classes(
      "flex flex-col items-center w-full max-w-4xl"
  )


  def build_game_ui():
    container.clear()
    with container:
      # Barra de estadísticas y controles superiores
      with ui.element("div").classes(
          "flex flex-wrap items-center justify-between w-full bg-slate-900/80"
          " border border-slate-800 p-4 rounded-2xl mb-6 shadow-xl gap-4"
      ):
        with ui.element("div").classes("flex items-center space-x-6"):
          ui.label(f"🔄 Movimientos: {game.moves_count}").classes(
              "text-lg font-bold text-indigo-400"
          )
          global timer_label
          timer_label = ui.label(f"⏱️ Tiempo: {game.timer_seconds}s").classes(
              "text-lg font-bold text-emerald-400"
          )

        with ui.element("div").classes("flex items-center space-x-3"):
          ui.label("Discos:").classes("text-sm text-slate-300 font-medium")
          disk_selector = (
              ui.select(
                  options={3: "3 Discos", 4: "4 Discos", 5: "5 Discos"},
                  value=game.num_disks,
              )
              .classes("w-32 bg-slate-800 text-white rounded-lg")
              .props("dense outlined dark")
          )

          def change_disks(e):
            game.num_disks = int(e.value)
            game.reset_game()

          disk_selector.on_value_change(change_disks)

          ui.button(
              "Reiniciar", on_click=game.reset_game, icon="restart_alt"
          ).classes(
              "bg-slate-800 hover:bg-slate-700 text-slate-200 border"
              " border-slate-700"
          )
          ui.button(
              "🤖 Auto-Resolver",
              on_click=game.auto_solve,
              icon="psychology",
          ).classes(
              "bg-indigo-600 hover:bg-indigo-500 text-white font-semibold"
              f" {'opacity-50 pointer-events-none' if game.auto_solving else ''}"
          )

      # Área de las Torres (El tablero del juego)
      with ui.element("div").classes(
          "grid grid-cols-1 md:grid-cols-3 gap-6 w-full"
      ):
        for peg_name in ["A", "B", "C"]:
          is_selected = game.selected_peg == peg_name
          border_color = (
              "border-indigo-500 bg-indigo-950/20 shadow-lg shadow-indigo-500/10"
              if is_selected
              else "border-slate-800 bg-slate-900/40"
          )

          with (
              ui.element("div")
              .classes(
                  f"relative flex flex-col items-center justify-end h-72"
                  f" border-2 {border_color} rounded-2xl cursor-pointer"
                  " peg-glow disk-transition p-4 group"
              )
              .on("click", lambda p=peg_name: game.handle_peg_click(p))
          ):
            ui.label(peg_name).classes(
                "absolute top-3 left-4 text-xl font-black text-slate-500"
                " group-hover:text-indigo-400"
            )

            if is_selected:
              ui.label("¡Seleccionado!").classes(
                  "absolute top-3 right-4 text-xs font-bold text-indigo-400"
                  " animate-pulse"
              )

            # Poste vertical
            ui.element("div").classes(
                "absolute bottom-4 w-3 h-56 bg-slate-800 rounded-t-lg z-0"
            )
            # Base horizontal
            ui.element("div").classes(
                "absolute bottom-0 w-3/4 h-4 bg-slate-700 rounded-lg z-0"
            )

            # Discos
            with ui.element("div").classes(
                "flex flex-col-reverse items-center justify-end w-full h-52"
                " z-10 pb-1 space-y-1 space-y-reverse"
            ):
              max_disks = game.num_disks
              for disk in game.pegs[peg_name]:
                width_percent = 30 + (disk * (60 / max_disks))
                color_class = game.disk_colors[disk - 1]

                with ui.element("div").classes(
                    f"h-8 rounded-lg flex items-center justify-center font-bold"
                    f" text-xs text-white shadow-md disk-transition"
                    f" {color_class}"
                ).style(f"width: {width_percent}%"):
                  ui.label(str(disk)).classes("drop-shadow")


  # Asignar la función de actualización al juego y renderizar por primera vez
  game.ui_updater = build_game_ui
  build_game_ui()


  # Tarea en segundo plano para el temporizador del juego
  async def timer_ticker():
    while True:
      await asyncio.sleep(1)
      if game.timer_active:
        game.timer_seconds += 1
        timer_label.text = f"⏱️ Tiempo: {game.timer_seconds}s"


  ui.timer(0.1, timer_ticker, once=True)

  # Footer
  with ui.element("div").classes(
      "flex flex-col items-center text-slate-500 text-xs mt-4 space-y-1"
  ):
    ui.label(
        "Diseñado en Python con NiceGUI & Tailwind CSS para Estructura de"
        " Datos"
    ).classes("font-medium")
    ui.label("José Arturo Bustamante Lazcano").classes("text-slate-400")

# Ejecutar la aplicación
ui.run(port=8080, title="Torres de Hanói Interactivo", reload=False)