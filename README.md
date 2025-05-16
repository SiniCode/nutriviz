# Nutriviz

## Description
Interactive Data Visualization course project at the University of Helsinki.

Nutriviz is designed to support the user with dietary planning by
- visualizing the amount of nutrients in individual products given their amount with respect to the Reference Daily Intake
- filtering products by food categories and special diets and ranking them to maximize/minimize the intake of a selected nutrient
- visualizing the total amount of nutrients in several products given their amounts with respect to the Reference Daily Intake

The project has been implemented using Python and [Plotly Dash](https://dash.plotly.com/).

## Data
- The [original data](https://fineli.fi/fineli/en/avoin-data?) were downloaded from the Finnish Institute of Health and Welfare, Fineli. License: CC-BY 4.0.
- The Reference Daily Intake values were found [here](https://www.fda.gov/food/nutrition-facts-label/daily-value-nutrition-and-supplement-facts-labels#referenceguide).

## Installation
Unfortunately, I didn't have time to deploy the application, but you should be able to run it locally if you follow the instructions below. Before the installation, you should have [poetry](https://python-poetry.org/docs/) installed on your machine.

1. Clone the project.
2. Navigate to the root folder with command
```bash
cd nutriviz/
```
3. Install dependencies with command
```bash
poetry install --no-root
```
4. Run the app with command
```bash
poetry run python3 Src/app.py
```

## Use of generative AI
Microsoft Copilot assisted with solving problems by generating some example code for data processing and creating visualizations. The example code snippets were tested, modified to the project's needs, and integrated into the project's codebase if they were found useful.
