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
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import argparse
import os
import logging

def setup_logging():
    """Sets up logging for the application."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Logging is set up.")

def parse_arguments():
    """Parse command-line arguments for running the Dash application."""
    parser = argparse.ArgumentParser(description="Run Dash app for LLM interpretability.")
    parser.add_argument('--data-file', required=True, help='Path to the data file (CSV format).')
    return parser.parse_args()

def validate_data_file(data_file: str) -> pd.DataFrame:
    """Validate the existence and structure of the data file."""
    if not os.path.exists(data_file):
        logging.error("Data file not found.")
        raise FileNotFoundError(f"The file {data_file} does not exist.")
    required_columns = {'patient_id', 'tokens', 'shap_values', 'predicted_phenotypes'}
    df = pd.read_csv(data_file)
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        logging.error("Missing columns in data file: %s", ', '.join(missing))
        raise ValueError(f"Missing columns in data file: {', '.join(missing)}")
    logging.info("Data file validated successfully.")
    return df

def prepare_snomed_ct():
    """Integrate SNOMED CT terms (conceptual demonstration)."""
    # In a real implementation, SNOMED CT terms would be loaded and integrated.
    # Here, we'll assume they are used for validation and enhancing interpretability.
    return ["Diabetes Mellitus", "Hypertension"]

def build_snomed_integration():
    """Simulate SNOMED CT integration to validate phenotypes."""
    # This is a placeholder function. In practice, it would ensure predicted phenotypes
    # align with known SNOMED CT codes and provide additional context if needed.
    return ["Diabetes Type 2"]  # Example of matching SNOMED CT term

setup_logging()
args = parse_arguments()
df = validate_data_file(args.data_file)
tokens = df['tokens'].apply(lambda x: x.split(',')).tolist()
shap_values = df['shap_values'].apply(lambda x: list(map(float, x.split(',')))).tolist()
predicted_phenotypes = df['predicted_phenotypes'].tolist()

snomed_terms = prepare_snomed_ct()
matched_terms = build_snomed_integration()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("LLM Interpretability for Phenotype Definitions"),
    html.Div([
        html.Label("Select Patient:"),
        dcc.Dropdown(
            id='patient-dropdown',
            options=[{'label': f'Patient {i}', 'value': i} for i in df['patient_id'].unique()],
            value=df['patient_id'].iloc[0]
        ),
        html.Label("Select Phenotype:"),
        dcc.Dropdown(
            id='phenotype-dropdown',
            options=[{'label': phenotype, 'value': phenotype} for phenotype in predicted_phenotypes],
            value=predicted_phenotypes[0]
        ),
        html.Label("Select Explanation Type:"),
        dcc.Dropdown(
            id='explanation-type-dropdown',
            options=[{'label': 'SHAP', 'value': 'shap'},
                     {'label': 'LIME', 'value': 'lime'}],
            value='shap'
        ),
    ], style={'margin-bottom': '20px'}),
    
    html.Div(id='clinical-note', children=[
        html.H3("Clinical Note with Token Highlighting:"),
        html.Div(id='highlighted-note')
    ]),
    
    html.Div(id='summary-charts', children=[
        html.H3("Summary Charts:"),
        dcc.Graph(id='feature-importance-chart')
    ]),

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
    Output('highlighted-note', 'children'),
    Output('feature-importance-chart', 'figure'),
    Input('patient-dropdown', 'value'),
    Input('phenotype-dropdown', 'value'),
    Input('explanation-type-dropdown', 'value')
)
def update_interface(selected_patient: str, selected_phenotype: str, explanation_type: str):
    """
    Update the interface based on selected inputs, including clinical note highlighting
    and a summary chart of feature importances.
    """
    if explanation_type == 'lime':
        logging.warning("LIME explanation not yet implemented, defaulting to SHAP.")
    
    highlighted_note = [
        html.Span(f'{token} ', style={'background-color': f'rgba(255, 0, 0, {score})'}) 
        for token_list, score_list in zip(tokens, shap_values)
        for token, score in zip(token_list, score_list)
    ]

    df_chart = pd.DataFrame({'Tokens': [t for sublist in tokens for t in sublist], 'Importance': [s for sublist in shap_values for s in sublist]})
    fig = px.bar(df_chart, x='Tokens', y='Importance', title='Token Importance', labels={'Tokens': 'Clinical Tokens', 'Importance': 'Importance Score'})

    return highlighted_note, fig

@app.callback(
    Output('feedback-response', 'children'),
    Input('submit-feedback', 'n_clicks'),
    Input('feedback-text', 'value')
)
def handle_feedback(n_clicks: int, feedback_text: str):
    """Handle user feedback submission."""
    if n_clicks > 0:
        logging.info("Feedback received: %s", feedback_text)
        return "Thank you for your feedback!"

if __name__ == '__main__':
    try:
        app.run_server(debug=True)
    except Exception as e:
        logging.error("Error running the server: %s", e)