import dash
import dash_bootstrap_components as dbc

from dashboard.application.main_app_layout import layout


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY]
)

app.layout = layout