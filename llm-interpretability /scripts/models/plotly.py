'''
***Instructions for Running the Application***

1. Prepare Your Data: Your CSV file should have columns named patient_id, tokens, shap_values, and predicted_phenotypes. Each token or shap_value should be comma-separated within a single cell. Below is an example format:
patient_id,tokens,shap_values,predicted_phenotypes
1,"Patient,has,a,history,of,diabetes","0.5,0.2,0.1,0.8,0.4,0.7","Diabetes Type 2"

2. Run the App: Use the command below, ensuring the correct path to your data file:
python app.py --data-file path_to_your_data_file.csv

3. Access the Interface: Open a browser and go to http://127.0.0.1:8050/ to interact with the application.
'''

import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd
import json
import os
import logging
from datetime import datetime

def setup_logging():
    """Sets up logging for the application."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Logging is set up.")

def load_explanations(file_path: str):
    """Load explanations from a JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_feedback(patient_id, feedback_text):
    """Save feedback to a local CSV file."""
    feedback_file = 'feedback_log.csv'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    feedback_entry = {'timestamp': timestamp, 'patient_id': patient_id, 'feedback': feedback_text}
    df_feedback = pd.DataFrame([feedback_entry])
    if os.path.exists(feedback_file):
        df_feedback.to_csv(feedback_file, mode='a', header=False, index=False)
    else:
        df_feedback.to_csv(feedback_file, index=False)

setup_logging()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("LLM Interpretability for Phenotype Definitions"),
    dcc.Upload(
        id='upload-data',
        children=html.Button('Upload CSV'),
        multiple=False
    ),
    html.Div(id='file-upload-status'),
    html.Div([
        html.Label("Select Patient:"),
        dcc.Dropdown(id='patient-dropdown'),
        html.Label("Select Explanation Type:"),
        dcc.Dropdown(
            id='explanation-type-dropdown',
            options=[{'label': 'SHAP', 'value': 'shap'},
                     {'label': 'LIME', 'value': 'lime'}],
            value='shap'
        ),
    ], style={'margin-bottom': '20px'}),
    
    html.Div(id='sidebar', children=[
        html.H3("Predicted Phenotypes and SNOMED Terms"),
        html.Div(id='phenotype-snomed-display')
    ], style={'width': '20%', 'float': 'left', 'margin-right': '20px'}),
    
    html.Div(id='main-content', children=[
        html.Div(id='clinical-note', children=[
            html.H3("Clinical Note with Token Highlighting:"),
            html.Div(id='highlighted-note')
        ]),
        
        html.Div(id='summary-charts', children=[
            html.H3("Summary Charts:"),
            dcc.RadioItems(
                id='chart-type-toggle',
                options=[{'label': 'Bar Chart', 'value': 'bar'},
                         {'label': 'Heatmap', 'value': 'heatmap'}],
                value='bar',
                inline=True
            ),
            dcc.Graph(id='feature-importance-chart')
        ]),
    ], style={'width': '75%', 'float': 'right'}),
    
    html.Div(id='feedback', children=[
        html.H3("User Feedback"),
        dcc.Textarea(
            id='feedback-text',
            placeholder='Enter your feedback here...',
            style={'width': '100%', 'height': 100},
        ),
        html.Button('Submit Feedback', id='submit-feedback', n_clicks=0),
        html.Div(id='feedback-response')
    ])
])

@app.callback(
    Output('file-upload-status', 'children'),
    Output('patient-dropdown', 'options'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def handle_file_upload(contents, filename):
    """Handle file upload and update patient dropdown."""
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        try:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            patient_options = [{'label': f'Patient {i}', 'value': i} for i in df['patient_id'].unique()]
            return f"Uploaded file: {filename}", patient_options
        except Exception as e:
            logging.error("Error processing uploaded file: %s", e)
            return "There was an error processing the file.", []
    return "No file uploaded.", []

@app.callback(
    Output('highlighted-note', 'children'),
    Output('feature-importance-chart', 'figure'),
    Output('phenotype-snomed-display', 'children'),
    Input('patient-dropdown', 'value'),
    Input('explanation-type-dropdown', 'value'),
    Input('chart-type-toggle', 'value')
)
def update_interface(selected_patient, explanation_type, chart_type):
    """Update the interface based on selected inputs."""
    if selected_patient is None:
        return "", {}, "No patient selected."

    explanations = load_explanations('phenotype_results.json')
    patient_data = explanations.get(str(selected_patient), {})
    tokens = patient_data.get('tokens', [])
    shap_values = patient_data.get('shap_values', [])
    predicted_phenotypes = patient_data.get('predicted_phenotypes', [])
    matched_terms = patient_data.get('matched_snomed_terms', [])

    highlighted_note = [
        html.Span(f'{token} ', style={'background-color': f'rgba(255, 0, 0, {score})'}) 
        for token, score in zip(tokens, shap_values)
    ]

    df_chart = pd.DataFrame({'Tokens': tokens, 'Importance': shap_values})
    if chart_type == 'bar':
        fig = px.bar(df_chart, x='Tokens', y='Importance', title='Token Importance', labels={'Tokens': 'Clinical Tokens', 'Importance': 'Importance Score'})
    else:
        fig = px.density_heatmap(df_chart, x='Tokens', y='Importance', title='Token Importance Heatmap', labels={'Tokens': 'Clinical Tokens', 'Importance': 'Importance Score'})

    phenotype_display = html.Div([
        html.H4("Predicted Phenotypes:"),
        html.Ul([html.Li(phenotype) for phenotype in predicted_phenotypes]),
        html.H4("Matched SNOMED Terms:"),
        html.Ul([html.Li(term) for term in matched_terms])
    ])

    return highlighted_note, fig, phenotype_display

@app.callback(
    Output('feedback-response', 'children'),
    Input('submit-feedback', 'n_clicks'),
    State('feedback-text', 'value'),
    State('patient-dropdown', 'value')
)
def handle_feedback(n_clicks, feedback_text, patient_id):
    """Handle user feedback submission."""
    if n_clicks > 0 and patient_id is not None:
        save_feedback(patient_id, feedback_text)
        logging.info("Feedback received for patient %s: %s", patient_id, feedback_text)
        return "Thank you for your feedback!"
    return ""

if __name__ == '__main__':
    try:
        app.run_server(debug=True)
    except Exception as e:
        logging.error("Error running the server: %s", e)