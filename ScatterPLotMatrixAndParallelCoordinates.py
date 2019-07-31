import plotly.plotly
import plotly.figure_factory as ff
import plotly.graph_objs as go
from plotly.offline import iplot
import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table

df= pd.read_csv('DataWeierstrass.csv', delimiter=';',  skiprows= 1,
                  names = ["professor", "lecture", "participants", "professional_expertise", "motivation", "clear_presentation", "overall_impression"])


'To map String values with quantative values'
df['professor'] = df['professor'].rank(method='dense', ascending=True).astype(int)
df['lecture'] = df['lecture'].rank(method='dense', ascending=True).astype(int)

config = {'scrollZoom': True}



'''Parallel-Coordinates'''
def prepare_parcoords():

    data = [
        go.Parcoords(
            line=dict(color=df['professor'],  # color bar based on Professors
                      #  colorscale = 'Cividis',
                      reversescale=True,
                      showscale=False,
                      ),

            dimensions=list([
                dict(
                    label='professor', values=df['professor']),
                dict(
                    label='lecture', values=df['lecture']),
                dict(
                    label='participants', values=df['participants']),
                dict(
                    label='professional_expertise', values=df['professional_expertise']),
                dict(
                    label='motivation', values=df['motivation']),
                dict(
                    label='clear_presentation', values=df['clear_presentation']),
                dict(
                    label='overall_impression', values=df['overall_impression']),
            ])
        )
    ]

    layout = go.Layout(
        title=go.layout.Title(
            text='Professor Review Distribution',
        ),
        font=dict(
            family="Arial,Times New Roman,Balto,Courier New,Gravitas One,Old Standard TT",
            size=16,
            color='#000000'
        ),
        # margin=go.layout.Margin(
        #     t=200,
        #     pad=4
        # ),
        autosize=False,
        width=1320,
        height=800
    )

    # return iplot(data = data,layout = layout)
    fig = go.Figure(data = data,layout = layout)
    return fig


'''Scatter-Plot Matrix'''
def prepare_scatter_plot():
    classes = np.unique(df['professor'].values).tolist()
    class_code = {classes[k]: k for k in range(44)}
    color_vals = [class_code[cl] for cl in df['professor']]

    data1 = go.Splom(
        dimensions=list([
            dict(
                label='professor', values=df['professor']),
            dict(
                label='lecture', values=df['lecture']),
            dict(
                label='participants', values=df['participants']),
            dict(
                label='professional_expertise', values=df['professional_expertise']),
            dict(
                label='motivation', values=df['motivation']),
            dict(
                label='clear_presentation', values=df['clear_presentation']),
            dict(
                label='overall_impression', values=df['overall_impression']),

        ]),
        marker=dict(color=color_vals,
                    size=6,
                    colorscale='Cividis',
                    showscale=True,
                    reversescale=True,
                    )
    )

    layout = go.Layout(
        title='Professor Review Distribution',
        dragmode='select',
        width=1320,
        height=1000,
        hovermode='closest',
        plot_bgcolor='rgba(241,241,241, 0.80)',
        font=dict(
            family="Arial,Times New Roman,Balto,Courier New,Gravitas One,Old Standard TT",
            size=16,
            color='#000000'
        ),

    )
    data1['diagonal'].update(visible=False)
    # return iplot(data = [data1], layout = layout)
    fig = dict(data = [data1], layout = layout)
    return fig


app = dash.Dash()

app.layout = html.Div([

    html.Div([html.H1(children = "Professor Review Application")],className="row", style={"text-align": "center"}),

    html.Div([
        dash_table.DataTable(
                style_table={'margin':'20px 0px 10px 100px'},
                style_header={'backgroundColor': 'rgb(230, 230, 230)','font-weight':'bold'},
                style_data_conditional=[{
                    'if':{'row_index':'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'
                }],
                style_cell={'minWidth':'100px'},
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                sort_action="native",
                filter_action="native",
                data=df.to_dict('records'),
        ),
        html.Button('Data <=> Visualization!', id='submit-button',n_clicks=0,style= {"border-radius":"4px","font-size":"14px","padding":"3px","margin-bottom":"5px","baackground-color":"#000000"}),

    ],
    style = {"text-align": "center"}
),

html.Div(
    children = html.Div([
            dcc.Dropdown(id = 'dropdown_options',
            options = [
                {'label': 'Scatter-Plot Distribution of Professor Review Metrics','value':'ScatterPlot'},
                {'label': 'Parallel-Coordinate Visualization Connecting Different Metrics of Professor Review','value':'ParallelCoordinates'},
            ],
            placeholder="Select a Visualization...",
            value='ScatterPlot'
        ),
            dcc.Graph(id = "Parallel-coords"
        )
    ])

    ),

])

# callback event to enable charts on click of a button
@app.callback([dash.dependencies.Output("Parallel-coords","style"),dash.dependencies.Output("dropdown_options","style")],
              [dash.dependencies.Input("submit-button", 'n_clicks')]
              )

def on_click(no_of_times):
    no_of_times = no_of_times+1;
    if (no_of_times%2 !=0 ) :
        return [{'display': 'none'},{'display': 'none'}]
    else:
        return [{'display': 'block'},{'display': 'block'}]


# # callback event to change button name on click of a button
# @app.callback(dash.dependencies.Output("submit-button","value"),
#               [dash.dependencies.Input("submit-button", 'n_clicks')]
#               )
#
# def on_click(no_of_times):
#     # no_of_times = no_of_times+1;
#     if (no_of_times%2 !=0 ) :
#         return "Show the Data!"
#     else:
#         return "Visualize this data!"

# callback event to disable table on click of a button
@app.callback(dash.dependencies.Output("table","style_table"),
              [dash.dependencies.Input("submit-button", 'n_clicks')]
              )

def on_click(no_of_times):
    no_of_times = no_of_times+1;
    if (no_of_times%2 !=0 ) :
        return {'display': 'block','margin':'20px 0px 10px 100px'}
    else:
        return {'display': 'none','margin':'20px 0px 10px 100px'}




# callback event to change the charts based on dropdown selection
@app.callback(dash.dependencies.Output("Parallel-coords","figure"),
              [dash.dependencies.Input("dropdown_options","value")]
              )

def update_fig(input_val):

    if(input_val == "ScatterPlot"):
       return prepare_scatter_plot()
    elif (input_val == "ParallelCoordinates"):
        return prepare_parcoords()


if __name__ == "__main__":
    app.run_server(debug=True)
