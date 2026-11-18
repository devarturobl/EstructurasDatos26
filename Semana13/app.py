import os
import random

from nicegui import ui


ELEMENT_COUNT = 20
PALETTE = [
    '#6366f1', '#8b5cf6', '#a855f7', '#d946ef', '#ec4899',
    '#f43f5e', '#f97316', '#f59e0b', '#eab308', '#84cc16',
    '#22c55e', '#10b981', '#14b8a6', '#06b6d4', '#0ea5e9',
    '#3b82f6', '#4f46e5', '#7c3aed', '#c026d3', '#db2777',
]
values = [random.randint(15, 100) for _ in range(ELEMENT_COUNT)]
labels = [f'Elemento {index:02d}' for index in range(1, ELEMENT_COUNT + 1)]
short_labels = [f'{index:02d}' for index in range(1, ELEMENT_COUNT + 1)]


def chart_data() -> list[dict[str, int | str]]:
    return [
        {'name': label, 'value': value}
        for label, value in zip(labels, values)
    ]


def bar_options() -> dict:
    return {
        'tooltip': {'trigger': 'axis', 'axisPointer': {'type': 'shadow'}},
        'grid': {'left': 42, 'right': 20, 'top': 28, 'bottom': 52},
        'xAxis': {
            'type': 'category',
            'data': short_labels,
            'axisLabel': {'color': '#64748b', 'interval': 0},
            'axisLine': {'lineStyle': {'color': '#e2e8f0'}},
            'axisTick': {'show': False},
        },
        'yAxis': {
            'type': 'value',
            'axisLabel': {'color': '#64748b'},
            'splitLine': {'lineStyle': {'color': '#f1f5f9'}},
        },
        'series': [{
            'name': 'Valor',
            'type': 'bar',
            'data': [
                {'value': value, 'itemStyle': {'color': PALETTE[index]}}
                for index, value in enumerate(values)
            ],
            'barMaxWidth': 28,
            'itemStyle': {'borderRadius': [6, 6, 0, 0]},
            'emphasis': {'focus': 'series'},
        }],
    }


def pie_options() -> dict:
    return {
        'tooltip': {
            'trigger': 'item',
            'formatter': '{b}<br/>{c} unidades ({d}%)',
        },
        'legend': {
            'show': False,
        },
        'series': [{
            'name': 'Distribución',
            'type': 'pie',
            'radius': ['42%', '72%'],
            'center': ['50%', '50%'],
            'avoidLabelOverlap': True,
            'itemStyle': {
                'borderColor': '#ffffff',
                'borderWidth': 2,
                'borderRadius': 5,
            },
            'label': {'show': False},
            'emphasis': {
                'scale': True,
                'label': {
                    'show': True,
                    'fontSize': 13,
                    'fontWeight': 'bold',
                    'formatter': '{b}\\n{d}%',
                },
            },
            'data': [
                {
                    **item,
                    'itemStyle': {'color': PALETTE[index]},
                }
                for index, item in enumerate(chart_data())
            ],
        }],
    }


def line_options() -> dict:
    return {
        'tooltip': {'trigger': 'axis'},
        'grid': {'left': 42, 'right': 20, 'top': 28, 'bottom': 42},
        'xAxis': {
            'type': 'category',
            'boundaryGap': False,
            'data': short_labels,
            'axisLabel': {'color': '#64748b', 'interval': 1},
            'axisLine': {'lineStyle': {'color': '#e2e8f0'}},
            'axisTick': {'show': False},
        },
        'yAxis': {
            'type': 'value',
            'axisLabel': {'color': '#64748b'},
            'splitLine': {'lineStyle': {'color': '#f1f5f9'}},
        },
        'series': [{
            'name': 'Valor',
            'type': 'line',
            'data': values,
            'smooth': True,
            'symbol': 'circle',
            'symbolSize': 7,
            'lineStyle': {'width': 3, 'color': '#6366f1'},
            'itemStyle': {'color': '#6366f1', 'borderColor': '#ffffff', 'borderWidth': 2},
            'areaStyle': {'color': 'rgba(99, 102, 241, 0.12)'},
        }],
    }


ui.add_head_html('''
<style>
    body {
        margin: 0;
        background: #f4f6fb;
        color: #172033;
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    .dashboard { max-width: 1440px; margin: 0 auto; padding: 34px 32px 48px; }
    .topbar { display: flex; justify-content: space-between; align-items: center; gap: 20px; }
    .eyebrow { color: #6366f1; font-size: 12px; font-weight: 750; letter-spacing: .12em; text-transform: uppercase; }
    .page-title { color: #172033; font-size: 30px; font-weight: 750; letter-spacing: -.04em; line-height: 1.15; }
    .page-subtitle { color: #748097; font-size: 14px; margin-top: 6px; }
    .refresh-button { border-radius: 10px; font-weight: 650; padding: 9px 16px; }
    .metrics { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px; }
    .metric-card, .chart-card {
        background: #fff;
        border: 1px solid #e8ebf2;
        border-radius: 16px;
        box-shadow: 0 5px 18px rgba(31, 41, 65, .035);
    }
    .metric-card { padding: 19px 21px; min-height: 94px; }
    .metric-label { color: #778198; font-size: 12px; font-weight: 600; }
    .metric-value { color: #202a40; font-size: 25px; font-weight: 740; margin-top: 7px; }
    .charts-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; }
    .chart-card { min-width: 0; padding: 21px 22px 14px; }
    .chart-card--wide { grid-column: 1 / -1; }
    .chart-title { color: #202a40; font-size: 16px; font-weight: 700; }
    .chart-caption { color: #8a93a6; font-size: 12px; margin-top: 4px; }
    .chart-card .q-card, .chart-card .nicegui-chart { width: 100%; }
    @media (max-width: 760px) {
        .dashboard { padding: 24px 16px 36px; }
        .topbar { align-items: flex-start; flex-direction: column; }
        .metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }
        .charts-grid { grid-template-columns: 1fr; }
        .chart-card--wide { grid-column: auto; }
        .chart-card { padding: 17px 14px 10px; }
        .page-title { font-size: 26px; }
    }
</style>
''')

ui.label('Despliegue de datos').classes('eyebrow')

@ui.refreshable
def dashboard() -> None:
    total = sum(values)
    average = total / ELEMENT_COUNT

    with ui.column().classes('dashboard w-full gap-6'):
        with ui.row().classes('topbar w-full'):
            with ui.column().classes('gap-0'):
                ui.label('PANEL DE DATOS').classes('eyebrow')
                ui.label('Explorador de valores').classes('page-title')
                ui.label('Una vista rápida de 20 elementos generados al azar.').classes('page-subtitle')
            ui.button(
                'Generar nuevos datos',
                icon='autorenew',
                on_click=regenerate_data,
            ).props('color=primary unelevated no-caps').classes('refresh-button')

        with ui.element('section').classes('metrics'):
            metric('Elementos', f'{ELEMENT_COUNT}', 'dataset')
            metric('Suma total', f'{total:,}', 'functions')
            metric('Promedio', f'{average:.1f}', 'show_chart')
            metric('Valor máximo', f'{max(values)}', 'north_east')

        with ui.element('section').classes('charts-grid'):
            with ui.element('article').classes('chart-card chart-card--wide'):
                ui.label('Valores por elemento').classes('chart-title')
                ui.label('Comparación individual · pasa el cursor para ver el detalle').classes('chart-caption')
                ui.echart(bar_options()).style('width: 100%; height: 330px;')

            with ui.element('article').classes('chart-card'):
                ui.label('Distribución del total').classes('chart-title')
                ui.label('Participación de cada elemento en el conjunto').classes('chart-caption')
                ui.echart(pie_options()).style('width: 100%; height: 310px;')

            with ui.element('article').classes('chart-card'):
                ui.label('Tendencia entre elementos').classes('chart-title')
                ui.label('Recorrido de los valores en orden').classes('chart-caption')
                ui.echart(line_options()).style('width: 100%; height: 310px;')


def metric(title: str, value: str, icon: str) -> None:
    with ui.element('article').classes('metric-card'):
        with ui.row().classes('w-full items-center justify-between no-wrap'):
            with ui.column().classes('gap-0'):
                ui.label(title).classes('metric-label')
                ui.label(value).classes('metric-value')
            ui.icon(icon).classes('text-indigo-500 text-xl')


def regenerate_data() -> None:
    global values
    values = [random.randint(15, 100) for _ in range(ELEMENT_COUNT)]
    dashboard.refresh()


dashboard()
if __name__ in {"__main__", "__mp_main__"}:
    # Lee el puerto que asigna la nube (por defecto 10000 si corres local)
    port = int(os.environ.get('PORT', 10000))
    ui.run(port=port, host='0.0.0.0', storage_secret='un_secreto_seguro')