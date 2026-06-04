import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load and prepare data
spacex_df = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv'
)

# Fallback: use local file if download fails
import os
if spacex_df is None or len(spacex_df) == 0:
    spacex_df = pd.read_csv('spacex_launch_geo.csv')

def get_booster_category(version):
    v = str(version)
    if 'v1.0' in v: return 'v1.0'
    if 'v1.1' in v: return 'v1.1'
    if 'FT' in v: return 'FT'
    if 'B4' in v: return 'B4'
    if 'B5' in v: return 'B5'
    return 'other'

if 'Booster Version Category' not in spacex_df.columns:
    spacex_df['Booster Version Category'] = spacex_df['Booster Version'].apply(get_booster_category)

min_payload = spacex_df['Payload Mass (kg)'].min()
max_payload = spacex_df['Payload Mass (kg)'].max()

launch_sites = spacex_df['Launch Site'].unique().tolist()

# Build the Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(
        'SpaceX Launch Records Dashboard',
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': '40px'}
    ),

    # TASK 1: Dropdown
    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': 'All Sites', 'value': 'ALL'}] +
                [{'label': site, 'value': site} for site in launch_sites],
        value='ALL',
        placeholder='Select a Launch Site here',
        searchable=True
    ),
    html.Br(),

    # Pie chart
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),

    # TASK 3: Range Slider
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={i: str(i) for i in range(0, 10001, 2500)},
        value=[min_payload, max_payload]
    ),

    # Scatter chart
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


# TASK 2: Pie chart callback
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(
            spacex_df,
            values='class',
            names='Launch Site',
            title='Total Success Launches By Site'
        )
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        site_counts = filtered_df['class'].value_counts().reset_index()
        site_counts.columns = ['class', 'count']
        site_counts['outcome'] = site_counts['class'].map({1: 'Success', 0: 'Failure'})
        fig = px.pie(
            site_counts,
            values='count',
            names='outcome',
            title=f'Total Success Launches for site {entered_site}'
        )
    return fig


# TASK 4: Scatter chart callback
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]

    if entered_site == 'ALL':
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title='Correlation between Payload and Success for all Sites'
        )
    else:
        site_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(
            site_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title=f'Correlation between Payload and Success for site {entered_site}'
        )
    return fig


if __name__ == '__main__':
    app.run(debug=True)
