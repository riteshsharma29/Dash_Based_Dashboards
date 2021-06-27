import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Header('Python Programming Language',style={'color': 'blue','fontSize': '50px','text-align': 'center'}),
    html.Br(),
    html.H1('Multi Purpose High Level Programming Language',style={'color': 'blue','fontSize': '30px','text-align': 'center'}),
    html.Br(),
    html.H2("Excellent documentation website is available for almost each and every module. Click on module link for more details.",style={'color': 'blue','fontSize': '20px','text-align': 'center'}),
    html.Br(),
    dbc.Tabs([
       dbc.Tab([
           html.Ol([
               html.Br(),
               html.Li(html.Div([html.A('Pandas : Is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool.',style={'color': 'black'}, href='https://pandas.pydata.org/', target='_blank')]),style={'color': 'black'}),
               html.Li(html.Div([html.A('NumPy : The fundamental package for scientific computing with Python.',style={'color': 'black'}, href='https://numpy.org/', target='_blank')]),style={'color': 'black'}),
               html.Li(html.Div([html.A('Matplotlib : Is a comprehensive library for creating static, animated, and interactive visualizations in Python.',style={'color': 'black'}, href='https://matplotlib.org/', target='_blank')]),style={'color': 'black'}),
               html.Li(html.Div([html.A('Seaborn : Is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.',style={'color': 'black'}, href='https://seaborn.pydata.org/', target='_blank')]),style={'color': 'black'}),
               html.Li(html.Div([html.A('NLTK : Natural Language Toolkit is a leading platform for building Python programs to work with human language data. ',style={'color': 'black'}, href='https://www.nltk.org/', target='_blank')]),style={'color': 'black'})
           ])], label='Data Analysis'),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Li(html.Div([html.A('Scikit-learn : Is a free software machine learning library for the Python programming language.',style={'color': 'black'}, href='https://scikit-learn.org/stable/', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('TensorFlow : Makes it easy for beginners and experts to create machine learning models for desktop, mobile, web, and cloud. See the sections below to get started.',style={'color': 'black'}, href='https://www.tensorflow.org/learn', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('PyTorch : Is an optimized tensor library primarily used for Deep Learning applications using GPUs and CPUs.',style={'color': 'black'}, href='https://pytorch.org/docs/stable/generated/torch.nn.Module.html', target='_blank')]),style={'color': 'black'})
           ])], label='Machine Learning / Deep Learning'),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Li(html.Div([html.A('MySQL : MySQL driver written in Python which does not depend on MySQL C client libraries and implements the DB API v2.0.',style={'color': 'black'}, href='https://pypi.org/project/mysql-connector-python/', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('SQLite3 : SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language.',style={'color': 'black'}, href='https://docs.python.org/3/library/sqlite3.html', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('Cx_Oracle : Is a module that enables access to Oracle Database and conforms to the Python database API specification.',style={'color': 'black'}, href='https://cx-oracle.readthedocs.io/en/latest/', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('Pymssql : A simple database interface for Python that builds on top of FreeTDS to provide a Python DB-API (PEP-249) interface to Microsoft SQL Server.',style={'color': 'black'}, href='https://pymssql.readthedocs.io/en/stable/', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('Pyodbc : Is an open source Python module that makes accessing ODBC databases simple..',style={'color': 'black'}, href='https://github.com/mkleehammer/pyodbc/wiki', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('SQLAlchemy : Is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.',style={'color': 'black'}, href='https://www.sqlalchemy.org/', target='_blank')]),style={'color': 'black'}),
            ])], label='Database'),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Li(html.Div([html.A('Django : Is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.',style={'color': 'black'}, href='https://www.djangoproject.com/', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('Flask : Is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.',style={'color': 'black'}, href='https://flask.palletsprojects.com/en/2.0.x/', target='_blank')]),style={'color': 'black'})
            ])], label='Web Development'),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Li(html.Div([html.A('Selenium : Is a free (open-source) automated testing framework used to validate web applications across different browsers and platforms.',style={'color': 'black'}, href='https://selenium-python.readthedocs.io/', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('Robot Framework : Is a generic open source automation framework. It can be used for test automation and robotic process automation (RPA).',style={'color': 'black'}, href='https://robotframework.org/', target='_blank')]),style={'color': 'black'})
            ])], label='RPA / Test Automation'),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Li(html.Div([html.A('Bs4 : Aka "Beautiful Soup" is a Python library for pulling data out of HTML and XML files.',style={'color': 'black'}, href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('Requests : Is an elegant and simple HTTP library for Python',style={'color': 'black'}, href='https://docs.python-requests.org/en/master/', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('Scrapy : An open source and collaborative framework for extracting the data you need from websites.',style={'color': 'black'}, href='https://scrapy.org/',target='_blank')]), style={'color': 'black'})
            ])], label='Web Scraping'),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Li(html.Div([html.A('PySimpleGUI : a Python package that enables Python programmers of all levels to create GUIs.',style={'color': 'black'}, href='https://pysimplegui.readthedocs.io/en/latest/call%20reference/', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('Tkinter : Package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit.',style={'color': 'black'}, href='https://docs.python.org/3/library/tkinter.html', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('Gooey : Turn (almost) any command line program into a full GUI application with one line.',style={'color': 'black'}, href='https://github.com/chriskiehl/Gooey', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('PyQt5 : PyQt5 is a comprehensive set of Python bindings for Qt v5.',style={'color': 'black'}, href='https://www.riverbankcomputing.com/static/Docs/PyQt5/', target='_blank')]),style={'color': 'black'})
            ])], label='GUI Development'),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.Li(html.Div([html.A('PyAutoGUI : Lets your Python scripts control the mouse and keyboard to automate interactions with other applications.',style={'color': 'black'}, href='https://pyautogui.readthedocs.io/en/latest/', target='_blank')]),style={'color': 'black'}),
                html.Li(html.Div([html.A('Pywinauto : Is a set of python modules to automate the Microsoft Windows GUI.',style={'color': 'black'}, href='https://pywinauto.readthedocs.io/en/latest/getting_started.html', target='_blank')]),style={'color': 'black'})
            ])], label='GUI Automation')
    ]),
])


if __name__ == '__main__':
    app.run_server(debug=True)
