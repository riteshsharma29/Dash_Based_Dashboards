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

# # read configuration
# config = configparser.ConfigParser()
# config.read(os.path.join("config","dash_playlist.cfg"))
#
# # read dashboard tab titles/headers
# tab_header = config["TAB_HEADER_LIST"]["TAB_HEADER"]
# tab_header = tab_header.replace("[", "").replace("]", "")
# tab_header = tab_header.split(",")
#
# # read dashboard playlist titles/headers
# title_list_1 = config["TAB_PLAYLIST_HEADER"]["TAB1_LIST_HEADER"]
# title_list_1 = title_list_1.replace("[", "").replace("]", "")
# title_list_1 = title_list_1.split(",")
#
# title_list_2 = config["TAB_PLAYLIST_HEADER"]["TAB2_LIST_HEADER"]
# title_list_2 = title_list_2.replace("[", "").replace("]", "")
# title_list_2 = title_list_2.split(",")
#
# title_list_3 = config["TAB_PLAYLIST_HEADER"]["TAB3_LIST_HEADER"]
# title_list_3 = title_list_3.replace("[", "").replace("]", "")
# title_list_3 = title_list_3.split(",")
#
# title_list_4 = config["TAB_PLAYLIST_HEADER"]["TAB4_LIST_HEADER"]
# title_list_4 = title_list_4.replace("[", "").replace("]", "")
# title_list_4 = title_list_4.split(",")
#
# title_list_5 = config["TAB_PLAYLIST_HEADER"]["TAB5_LIST_HEADER"]
# title_list_5 = title_list_5.replace("[", "").replace("]", "")
# title_list_5 = title_list_5.split(",")
#
# title_list_6 = config["TAB_PLAYLIST_HEADER"]["TAB6_LIST_HEADER"]
# title_list_6 = title_list_6.replace("[", "").replace("]", "")
# title_list_6 = title_list_6.split(",")
#
#
# # read dashboard playlist url's
# url_list_1 = config["TAB_PLAYLIST_URL_LIST"]["TAB1_URL_LIST"]
# url_list_1 = url_list_1.replace("[", "").replace("]", "")
# url_list_1 = url_list_1.split(",")
#
# url_list_2 = config["TAB_PLAYLIST_URL_LIST"]["TAB2_URL_LIST"]
# url_list_2 = url_list_2.replace("[", "").replace("]", "")
# url_list_2 = url_list_2.split(",")
#
# url_list_3 = config["TAB_PLAYLIST_URL_LIST"]["TAB3_URL_LIST"]
# url_list_3 = url_list_3.replace("[", "").replace("]", "")
# url_list_3 = url_list_3.split(",")
#
# url_list_4 = config["TAB_PLAYLIST_URL_LIST"]["TAB4_URL_LIST"]
# url_list_4 = url_list_4.replace("[", "").replace("]", "")
# url_list_4 = url_list_4.split(",")
#
# url_list_5 = config["TAB_PLAYLIST_URL_LIST"]["TAB5_URL_LIST"]
# url_list_5 = url_list_5.replace("[", "").replace("]", "")
# url_list_5 = url_list_5.split(",")
#
# url_list_6 = config["TAB_PLAYLIST_URL_LIST"]["TAB6_URL_LIST"]
# url_list_6 = url_list_6.replace("[", "").replace("]", "")
# url_list_6 = url_list_6.split(",")

##################################################################################################################################

# Populate 1st tab

tab1_content_1 = [dbc.CardHeader("Introduction"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/WvhQhj4n6b8")]),]
tab1_content_2 = [dbc.CardHeader("List"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/9rLdQP3g4fw")]),]
tab1_content_3 = [dbc.CardHeader("Tuple"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/GstQPTWpt88")]),]
tab1_content_4 = [dbc.CardHeader("Dictionary"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/rZjhId0VkuY")]),]
tab1_content_5 = [dbc.CardHeader("Strings"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/lSItwlnF0eU")]),]
tab1_content_6 = [dbc.CardHeader("Set"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/MEPlLAjPvXY")]),]
tab1_content_7 = [dbc.CardHeader("Operators"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/Pm9FOpOwhlA")]),]
tab1_content_8 = [dbc.CardHeader("Built-In"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/NBIs5FgYmB8")]),]

row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab1_content_1, color="primary", outline=True)),
        dbc.Col(dbc.Card(tab1_content_2, color="secondary", outline=True)),
        dbc.Col(dbc.Card(tab1_content_3, color="info", outline=True)),
        dbc.Col(dbc.Card(tab1_content_4, color="info2", outline=True)),
    ],
    className="mb-4",
)

row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab1_content_5, color="success", outline=True)),
        dbc.Col(dbc.Card(tab1_content_6, color="warning", outline=True)),
        dbc.Col(dbc.Card(tab1_content_7, color="danger", outline=True)),
        dbc.Col(dbc.Card(tab1_content_8, color="danger 2", outline=True)),
    ],
    className="mb-4",
)

tab1_rowlist = [row_1, row_2]

##################################################################################################################################

# Populate 2nd tab

tab2_content_1 = [dbc.CardHeader("Modules"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/7GXaobCrBb4")]),]
tab2_content_2 = [dbc.CardHeader("Generator"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/bD05uGo_sVI")]),]
tab2_content_3 = [dbc.CardHeader("List Comprehension"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/AhSvKGTh28Q")]),]
tab2_content_4 = [dbc.CardHeader("Dictionary Comprehension"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/id1oaiBEGsk")]),]
tab2_content_5 = [dbc.CardHeader("Lambda"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/RQRCWDK9UkA")]),]
tab2_content_6 = [dbc.CardHeader("Functions"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/oSPMmeaiQ68")]),]
tab2_content_7 = [dbc.CardHeader("Classes"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/SRu1GAfr3LA")]),]
tab2_content_8 = [dbc.CardHeader("Itertools"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/Ie8sUyqKuQU")]),]

row_3 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab2_content_1, color="primary", outline=True)),
        dbc.Col(dbc.Card(tab2_content_2, color="secondary", outline=True)),
        dbc.Col(dbc.Card(tab2_content_3, color="info", outline=True)),
        dbc.Col(dbc.Card(tab2_content_4, color="info2", outline=True)),
    ],
    className="mb-4",
)

row_4 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab2_content_5, color="success", outline=True)),
        dbc.Col(dbc.Card(tab2_content_6, color="warning", outline=True)),
        dbc.Col(dbc.Card(tab2_content_7, color="danger", outline=True)),
        dbc.Col(dbc.Card(tab2_content_8, color="danger 2", outline=True)),
    ],
    className="mb-4",
)

tab2_rowlist = [row_3, row_4]

##################################################################################################################################

# Populate 3rd tab

tab3_content_1 = [dbc.CardHeader("Pandas"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/UB3DE5Bgfx4")]),]
tab3_content_2 = [dbc.CardHeader("Numpy"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/8JfDAm9y_7s")]),]
tab3_content_3 = [dbc.CardHeader("Seaborn"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/TLdXM0A7SR8")]),]
tab3_content_4 = [dbc.CardHeader("Scikit Learn"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/bwZ3Qiuj3i8")]),]
tab3_content_5 = [dbc.CardHeader("Poltly"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/GGL6U0k8WYA")]),]
tab3_content_6 = [dbc.CardHeader("NLTK"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/U8m5ug9Q54M")]),]
tab3_content_7 = [dbc.CardHeader("Tensorflow"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/yX8KuPZCAMo")]),]
tab3_content_8 = [dbc.CardHeader("Pyspark"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/PRzSWWsyHZg")]),]

row_5 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab3_content_1, color="primary", outline=True)),
        dbc.Col(dbc.Card(tab3_content_2, color="secondary", outline=True)),
        dbc.Col(dbc.Card(tab3_content_3, color="info", outline=True)),
        dbc.Col(dbc.Card(tab3_content_4, color="info2", outline=True)),
    ],
    className="mb-4",
)

row_6 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab3_content_5, color="success", outline=True)),
        dbc.Col(dbc.Card(tab3_content_6, color="warning", outline=True)),
        dbc.Col(dbc.Card(tab3_content_7, color="danger", outline=True)),
        dbc.Col(dbc.Card(tab3_content_8, color="danger 2", outline=True)),
    ],
    className="mb-4",
)

tab3_rowlist = [row_5, row_6]

##################################################################################################################################

# Populate 4th tab

tab4_content_1 = [dbc.CardHeader("Dash"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/NM8Ue4znLP8")]),]
tab4_content_2 = [dbc.CardHeader("Sreamlit"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/_9WiB2PDO7k")]),]
tab4_content_3 = [dbc.CardHeader("Gradio"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/O_3FINRtwhs")]),]
tab4_content_4 = [dbc.CardHeader("PysimpleGUI"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/-_z2RPAH0Qk")]),]
tab4_content_5 = [dbc.CardHeader("Tkinter"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/itRLRfuL_PQ")]),]
tab4_content_6 = [dbc.CardHeader("Wxpython"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/itRLRfuL_PQ")]),]
tab4_content_7 = [dbc.CardHeader("PyQT6"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/ot94H3-d5d8")]),]
tab4_content_8 = [dbc.CardHeader("DearPyGui"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/2RocXKPPx4o")]),]

row_7 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab4_content_1, color="primary", outline=True)),
        dbc.Col(dbc.Card(tab4_content_2, color="secondary", outline=True)),
        dbc.Col(dbc.Card(tab4_content_3, color="info", outline=True)),
        dbc.Col(dbc.Card(tab4_content_4, color="info2", outline=True)),
    ],
    className="mb-4",
)

row_8 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab4_content_5, color="success", outline=True)),
        dbc.Col(dbc.Card(tab4_content_6, color="warning", outline=True)),
        dbc.Col(dbc.Card(tab4_content_7, color="danger", outline=True)),
        dbc.Col(dbc.Card(tab4_content_8, color="danger 2", outline=True)),
    ],
    className="mb-4",
)

tab4_rowlist = [row_7, row_8]


##################################################################################################################################

# Populate 5th tab

tab5_content_1 = [dbc.CardHeader("Django"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/e1IyzVyrLSU")]),]
tab5_content_2 = [dbc.CardHeader("Flask"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/Z1RJmh_OqeA")]),]
tab5_content_3 = [dbc.CardHeader("Web2py"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/Z9hV_x8xJ8M")]),]
tab5_content_4 = [dbc.CardHeader("Pyramid"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/wgMj6ZsCiBk")]),]
tab5_content_5 = [dbc.CardHeader("Cherrypy"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/rCHj3Di5M0A")]),]
tab5_content_6 = [dbc.CardHeader("Pelican"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/gqJb2OpkJiQ")]),]
tab5_content_7 = [dbc.CardHeader("API"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/KM_9in6ei50")]),]
tab5_content_8 = [dbc.CardHeader("FastAPI"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/62pP9pfzNRs")]),]

row_9 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab5_content_1, color="primary", outline=True)),
        dbc.Col(dbc.Card(tab5_content_2, color="secondary", outline=True)),
        dbc.Col(dbc.Card(tab5_content_3, color="info", outline=True)),
        dbc.Col(dbc.Card(tab5_content_4, color="info2", outline=True)),
    ],
    className="mb-4",
)

row_10 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab5_content_5, color="success", outline=True)),
        dbc.Col(dbc.Card(tab5_content_6, color="warning", outline=True)),
        dbc.Col(dbc.Card(tab5_content_7, color="danger", outline=True)),
        dbc.Col(dbc.Card(tab5_content_8, color="danger 2", outline=True)),
    ],
    className="mb-4",
)

tab5_rowlist = [row_9, row_10]

##################################################################################################################################

# Populate 6th tab

tab6_content_1 = [dbc.CardHeader("Selenium"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/o3tYiyE_OXE")]),]
tab6_content_2 = [dbc.CardHeader("RobotFramework"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/d-KWz7euLlc")]),]
tab6_content_3 = [dbc.CardHeader("Pywinauto"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/mhNIHgJPP3g")]),]
tab6_content_4 = [dbc.CardHeader("Pyautogui"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/1RE5tSPO2RI")]),]
tab6_content_5 = [dbc.CardHeader("Openpyxl"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/FpgdFkup3ew")]),]
tab6_content_6 = [dbc.CardHeader("Ansible"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/EcnqJbxBcM0")]),]
tab6_content_7 = [dbc.CardHeader("BeautifulSoup4"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/ng2o98k983k")]),]
tab6_content_8 = [dbc.CardHeader("Camelot"),dbc.CardBody([html.Iframe(src="https://www.youtube.com/embed/XmYSyqGbW2s")]),]

row_11 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab6_content_1, color="primary", outline=True)),
        dbc.Col(dbc.Card(tab6_content_2, color="secondary", outline=True)),
        dbc.Col(dbc.Card(tab6_content_3, color="info", outline=True)),
        dbc.Col(dbc.Card(tab6_content_4, color="info2", outline=True)),
    ],
    className="mb-4",
)

row_12 = dbc.Row(
    [
        dbc.Col(dbc.Card(tab6_content_5, color="success", outline=True)),
        dbc.Col(dbc.Card(tab6_content_6, color="warning", outline=True)),
        dbc.Col(dbc.Card(tab6_content_7, color="danger", outline=True)),
        dbc.Col(dbc.Card(tab6_content_8, color="danger 2", outline=True)),
    ],
    className="mb-4",
)

tab6_rowlist = [row_11, row_12]

##################################################################################################################################


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Header('Python Playlist Dashboard',style={'color': 'blue','fontSize': '50px','text-align': 'center'}),
    html.H1('Place all topics which you want Learn/Teach/Share on 1 Page using Python',style={'color': 'blue','fontSize': '30px','text-align': 'center'}),
    html.Br(),
    dbc.Tabs([
       dbc.Tab([
           html.Ol([
               html.Br(),
               html.Div(tab1_rowlist),
           ])], label="BASICS"),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Div(tab2_rowlist),
           ])], label="ADVANCE"),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Div(tab3_rowlist),
            ])], label="DATA SCIENCE/ENGINEERING"),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Div(tab4_rowlist),
            ])], label="USER INTERFACE / DASHBOARD"),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Div(tab5_rowlist),
            ])], label="WEB DEVELOPMENT"),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Div(tab6_rowlist),
            ])], label="AUTOMATION")
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)

