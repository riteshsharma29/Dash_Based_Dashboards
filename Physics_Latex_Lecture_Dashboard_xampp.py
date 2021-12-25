import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

'''
REFERENCES :
https://www.cpp.edu/~pbsiegel/supnotes/notes130.html
https://pretagteam.com/question/how-to-use-iframe-in-dashplotly-pythonhtml
https://community.plotly.com/t/adding-a-scrollbar-to-a-sidebar-div/53330/2
https://stackoverflow.com/questions/68269257/local-html-file-wont-load-properly-into-dash-application
'''

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "22rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "overflow": "scroll",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "25rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("LaTeX HTML Dashboard", className="display-4"),
        html.Hr(),
        html.P(
            "Lecture Notes", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Mechanics Lecture 1", href="/M-Lecture-1", active="exact"),
                dbc.NavLink("Mechanics Lecture 2", href="/M-Lecture-2", active="exact"),
                dbc.NavLink("Mechanics Lecture 3", href="/M-Lecture-3", active="exact"),
                dbc.NavLink("Fluids Oscillations Thermodynamics Lecture 1", href="/FOT-Lecture-1", active="exact"),
                dbc.NavLink("Fluids Oscillations Thermodynamics Lecture 2", href="/FOT-Lecture-2", active="exact"),
                dbc.NavLink("Fluids Oscillations Thermodynamics Lecture 3", href="/FOT-Lecture-3", active="exact"),
                dbc.NavLink("Electricity Magnetism Lecture 1", href="/EM-Lecture-1", active="exact"),
                dbc.NavLink("Electricity Magnetism Lecture 2", href="/EM-Lecture-2", active="exact"),
                dbc.NavLink("Electricity Magnetism Lecture 3", href="/EM-Lecture-3", active="exact"),
                dbc.NavLink("Electromagnetic Radiation Special Relativity Lecture 1", href="/ERSR-Lecture-1", active="exact"),
                dbc.NavLink("Electromagnetic Radiation Special Relativity Lecture 2", href="/ERSR-Lecture-2", active="exact"),
                dbc.NavLink("Electromagnetic Radiation Special Relativity Lecture 3", href="/ERSR-Lecture-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Ul([
               html.Div([html.Header('Physics LaTeX Lecture Notes in HTML', style={'color': 'blue', 'fontSize': '35px','text-align': 'left'})]),
               html.Br(),
               html.Li(html.Div([html.A(
                'LaTeX ??? : Is widely used in academia for the communication and publication of scientific documents in many fields, including mathematics, computer science, engineering, physics, chemistry, economics, linguistics, quantitative psychology, philosophy, and political science. ',
                style={'color': 'red','fontSize': '20px'}, href='https://en.wikipedia.org/wiki/LaTeX', target='_blank')]), style={'color': 'red'}),
               html.Br(),
               html.Li(html.Div([html.A(
                'Link to the LaTeX files used in this application',style={'color': 'purple', 'fontSize': '20px'}, href='https://www.cpp.edu/~pbsiegel/supnotes/notes130.html',
                target='_blank')]), style={'color': 'purple'}),
               html.Br(),
               html.Li(html.Div([html.P('The main objective behind sharing this dashboard is to share the concept of taking scientific lectures notes one level up on web for easy online education.',style={'color': 'green','fontSize': '20px'})]),style={'color': 'green'}),
               html.Li(html.Div([html.P('Science Professors can segregate thier Syallabus LaTeX lecture notes all in one place and teach students with ease of going back and forth,scrolling during an On-line class.  ',style={'color': 'green','fontSize': '20px'})]),style={'color': 'green'}),
               html.Li(html.Div([html.P('Applications like these can make On-line education better across schools & universities.',style={'color': 'green','fontSize': '20px'})]),style={'color': 'green'}),
               html.Li(html.Div([html.P('Deploying such quick fire applications makes sharing research & educational work across the community easy.',style={'color': 'green','fontSize': '20px'})]),style={'color': 'green'}),
               html.Li(html.Div([html.P('Have converted each LaTeX lecture document to an HTML webpage and linked to this app with its topic name.',
                                     style={'color': 'green', 'fontSize': '20px'})]), style={'color': 'green'}),
               html.Li(html.Div([html.A('This application is developed in Python with Dash Framework.',style={'color': 'black', 'fontSize': '20px'}, href='https://dash.plotly.com/',
                target='_blank')]), style={'color': 'black'}),
           ])
    elif pathname == "/M-Lecture-1":
        return html.Iframe(src = "http://localhost/Latex/Mechanics_1.tex.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/M-Lecture-2":
        return html.Iframe(src = "http://localhost/Latex/Mechanics_2.tex.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/M-Lecture-3":
        return html.Iframe(src = "http://localhost/Latex/Mechanics_3.tex.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/FOT-Lecture-1":
        return html.Iframe(src = "http://localhost/Latex/Fluids_Oscillations_Thermodynamics_1.tex.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/FOT-Lecture-2":
        return html.Iframe(src = "http://localhost/Latex/Fluids_Oscillations_Thermodynamics_2.tex.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/FOT-Lecture-3":
        return html.Iframe(src = "http://localhost/Latex/Fluids_Oscillations_Thermodynamics_3.tex.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/EM-Lecture-1":
        return html.Iframe(src = "http://localhost/Latex/Electricity_Magnetism_1.tex.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/EM-Lecture-2":
        return html.Iframe(src = "http://localhost/Latex/Electricity_Magnetism_2.tex.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/EM-Lecture-3":
        return html.Iframe(src = "http://localhost/Latex/Electricity_Magnetism_3.tex.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/ERSR-Lecture-1":
        return html.Iframe(src = "http://localhost/Latex/Electromagnetic_Radiation_Special_Relativity_1.tex.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/ERSR-Lecture-2":
        return html.Iframe(src = "http://localhost/Latex/Electromagnetic_Radiation_Special_Relativity_2.tex.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/ERSR-Lecture-3":
        return html.Iframe(src = "http://localhost/Latex/Electromagnetic_Radiation_Special_Relativity_3.tex.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    app.run_server()