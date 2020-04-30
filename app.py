import data_gen

import plotly.graph_objs as go



import dash
from dash.dependencies import  Input,Output,State
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'text' : '#00FF00',
    'plot_color': '#A9A9A9',
    'paper_color': '#696969' 
}

app.layout = html.Div(children=[
    html.H1(children='Hello Dash',
            style = {
                'textAlign': 'center',
                'color':'#FF4500'
        
        }
    ),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    
    html.Div([
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': data_gen.dates, 'y': data_gen.date_cnt, 'type': 'line', 'name': 'SF'},
                    
                ],
                'layout': {
                    'plot_bgcolor': colors['plot_color'],
                    'paper_bgcolor': colors['paper_color'],   
                    'title': 'Visitors Count',
                    'font':{
                        'color': colors['text']
                    }
                }
            }
        )
    ]),
    
    html.Div([
        dcc.Graph(
            id = 'pie',
            figure=go.Figure(
                    data = [ go.Pie(labels = data_gen.states, values = data_gen.states_cnt)],
                    layout= go.Layout(
                        title =  'Statewise vistors'
                    )
            )
        )
    ]),
    
    html.Div([
        dcc.Graph(
            id = 'page-visits',
            figure=go.Figure(
                    data = [ go.Bar(x = data_gen.pages, y = data_gen.pg_cnt)],
                    layout= go.Layout(
                        title =  'Statewise vistors'
                    )
            )
        )
    ]),

    html.Div([
        html.Label('Statewise visitors detail count'),
        dcc.Dropdown(

            id = 'state_select',
            options = data_gen.state_dropdown_options,
            placeholder =  'Select state to view metric',
            value = 'Maharashtra'
        ),
        html.Br()
    ]),

    html.Div([
        dcc.Graph(
            id = 'state-detail-graph'
        )
    ])
    
])

@app.callback(dash.dependencies.Output('state-detail-graph','figure'),
                [dash.dependencies.Input('state_select','value')])

def update_state_detail_graph(state):
    
    data = []

    dt = data_gen.get_cities_count(state)
    #import sys

    
    trace = dict(x= dt['cities'], y= dt['cities_cnt'], type=  'bar')
    

    data.append(trace)
    layout = {'title':'Detailed State Wise Metrics'}
    #print({'data': data,'layout' : layout}, file=sys.stderr)      
    return {'data': data,'layout' : layout}
if __name__ == '__main__':
    app.run_server(debug=True)