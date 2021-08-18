import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import configparser
import os
import sys


tab1_content_1 = [dbc.CardHeader("Tutorial 1"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/WvhQhj4n6b8")])]
tab1_content_2 = [dbc.CardHeader("Tutorial 2"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/9rLdQP3g4fw")])]
tab1_content_3 = [dbc.CardHeader("Tutorial 3"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/GstQPTWpt88")])]
tab1_content_4 = [dbc.CardHeader("Tutorial 4"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/rZjhId0VkuY")])]
tab1_content_5 = [dbc.CardHeader("Tutorial 5"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/lSItwlnF0eU")])]
tab1_content_6 = [dbc.CardHeader("Tutorial 6"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/MEPlLAjPvXY")])]
tab1_content_7 = [dbc.CardHeader("Tutorial 7"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/Pm9FOpOwhlA")])]
tab1_content_8 = [dbc.CardHeader("Tutorial 8"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/NBIs5FgYmB8")])]

tab1_row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab1_content_1, color="primary", outline=True)),
        dbc.Col(dbc.Card(tab1_content_2, color="secondary", outline=True)),
        dbc.Col(dbc.Card(tab1_content_3, color="info", outline=True)),
        dbc.Col(dbc.Card(tab1_content_4, color="info2", outline=True)),
    ],
    className="mb-4",
)

tab1_row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab1_content_5, color="success", outline=True)),
        dbc.Col(dbc.Card(tab1_content_6, color="warning", outline=True)),
        dbc.Col(dbc.Card(tab1_content_7, color="danger", outline=True)),
        dbc.Col(dbc.Card(tab1_content_8, color="danger 2", outline=True)),
    ],
    className="mb-4",
)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Header('Python Playlist Dashboard',style={'color': 'blue','fontSize': '50px','text-align': 'center'}),
    html.Br(),
    dbc.Tabs([
       dbc.Tab([
           html.Ol([
               html.Br(),
               html.Div([tab1_row_1,tab1_row_2]),
           ])], label="POC")

    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
