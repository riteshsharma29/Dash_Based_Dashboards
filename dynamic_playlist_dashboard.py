import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import configparser
import os
import sys

'''
https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/
'''

# read configuration
config = configparser.ConfigParser()
config.read(os.path.join("config","dash_playlist.cfg"))

# read dashboard tab titles/headers
tab_header = config["TAB_HEADER_LIST"]["TAB_HEADER"]
tab_header = tab_header.replace("[", "").replace("]", "")
tab_header = tab_header.split(",")

# read dashboard playlist titles/headers
title_list_1 = config["TAB_PLAYLIST_HEADER"]["TAB1_LIST_HEADER"]
title_list_2 = config["TAB_PLAYLIST_HEADER"]["TAB2_LIST_HEADER"]
title_list_3 = config["TAB_PLAYLIST_HEADER"]["TAB3_LIST_HEADER"]
title_list_4 = config["TAB_PLAYLIST_HEADER"]["TAB4_LIST_HEADER"]
title_list_5 = config["TAB_PLAYLIST_HEADER"]["TAB5_LIST_HEADER"]
title_list_6 = config["TAB_PLAYLIST_HEADER"]["TAB6_LIST_HEADER"]

# read dashboard playlist url's
url_list_1 = config["TAB_PLAYLIST_URL_LIST"]["TAB1_URL_LIST"]
url_list_2 = config["TAB_PLAYLIST_URL_LIST"]["TAB2_URL_LIST"]
url_list_3 = config["TAB_PLAYLIST_URL_LIST"]["TAB3_URL_LIST"]
url_list_4 = config["TAB_PLAYLIST_URL_LIST"]["TAB4_URL_LIST"]
url_list_5 = config["TAB_PLAYLIST_URL_LIST"]["TAB5_URL_LIST"]
url_list_6 = config["TAB_PLAYLIST_URL_LIST"]["TAB6_URL_LIST"]


##################################################################################################################################

def Populate_Tab(title_list_name,url_list_name):

    title_list_name = title_list_name.replace("[", "").replace("]", "")
    title_list_name = title_list_name.split(",")

    url_list_name = url_list_name.replace("[", "").replace("]", "")
    url_list_name = url_list_name.split(",")

    tab_content_1 = [dbc.CardHeader(title_list_name[0].strip(chr(34))),
                      dbc.CardBody([html.Iframe(src=url_list_name[0].strip(chr(34)),allow="fullscreen",height="100%",width="100%")]), ]
    tab_content_2 = [dbc.CardHeader(title_list_name[1].strip(chr(34))),
                      dbc.CardBody([html.Iframe(src=url_list_name[1].strip(chr(34)),allow="fullscreen",height="100%",width="100%")]), ]
    tab_content_3 = [dbc.CardHeader(title_list_name[2].strip(chr(34))),
                      dbc.CardBody([html.Iframe(src=url_list_name[2].strip(chr(34)),allow="fullscreen",height="100%",width="100%")]), ]
    tab_content_4 = [dbc.CardHeader(title_list_name[3].strip(chr(34))),
                      dbc.CardBody([html.Iframe(src=url_list_name[3].strip(chr(34)),allow="fullscreen",height="100%",width="100%")]), ]
    tab_content_5 = [dbc.CardHeader(title_list_name[4].strip(chr(34))),
                      dbc.CardBody([html.Iframe(src=url_list_name[4].strip(chr(34)),allow="fullscreen",height="100%",width="100%")]), ]
    tab_content_6 = [dbc.CardHeader(title_list_name[5].strip(chr(34))),
                      dbc.CardBody([html.Iframe(src=url_list_name[5].strip(chr(34)),allow="fullscreen",height="100%",width="100%")]), ]
    tab_content_7 = [dbc.CardHeader(title_list_name[6].strip(chr(34))),
                      dbc.CardBody([html.Iframe(src=url_list_name[6].strip(chr(34)),allow="fullscreen",height="100%",width="100%")]), ]
    tab_content_8 = [dbc.CardHeader(title_list_name[7].strip(chr(34))),
                      dbc.CardBody([html.Iframe(src=url_list_name[7].strip(chr(34)),allow="fullscreen",height="100%",width="100%")]), ]

    row_1 = dbc.Row(
        [
            dbc.Col(dbc.Card(tab_content_1, color="primary", outline=True)),
            dbc.Col(dbc.Card(tab_content_2, color="secondary", outline=True)),
            dbc.Col(dbc.Card(tab_content_3, color="info", outline=True)),
            dbc.Col(dbc.Card(tab_content_4, color="success", outline=True)),
        ],
        className="mb-4",
    )

    row_2 = dbc.Row(
        [
            dbc.Col(dbc.Card(tab_content_5, color="success", outline=True)),
            dbc.Col(dbc.Card(tab_content_6, color="warning", outline=True)),
            dbc.Col(dbc.Card(tab_content_7, color="danger", outline=True)),
            dbc.Col(dbc.Card(tab_content_8, color="secondary", outline=True)),
        ],
        className="mb-4",
    )

    tab_rowlist = [row_1, row_2]

    return tab_rowlist


##################################################################################################################################

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Header('Python Playlist Dashboard',style={'color': 'blue','fontSize': '50px','text-align': 'center'}),
    html.H1('Developed with Dash Framework',style={'color': 'blue','fontSize': '30px','text-align': 'center'}),
    html.Br(),
    dbc.Tabs([
       dbc.Tab([
           html.Ol([
               html.Br(),
               html.Div(Populate_Tab(title_list_1,url_list_1)),
           ])], label=tab_header[0].strip(chr(34))),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Div(Populate_Tab(title_list_2,url_list_2)),
           ])], label=tab_header[1].strip(chr(34))),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Div(Populate_Tab(title_list_3,url_list_3)),
            ])], label=tab_header[2].strip(chr(34))),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Div(Populate_Tab(title_list_4,url_list_4)),
            ])], label=tab_header[3].strip(chr(34))),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Div(Populate_Tab(title_list_5,url_list_5)),
            ])], label=tab_header[4].strip(chr(34))),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Div(Populate_Tab(title_list_6,url_list_6)),
            ])], label=tab_header[5].strip(chr(34)))
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)

