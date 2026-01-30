from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# Safe path handling (IMPORTANT for Render)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, 'model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:

        league = request.form['league']


        home_team_form = float(request.form['home_team_form'])
        away_team_form = float(request.form['away_team_form'])
        home_goals_scored_avg = float(request.form['home_goals_scored_avg'])
        away_goals_scored_avg = float(request.form['away_goals_scored_avg'])
        home_goals_conceded_avg = float(request.form['home_goals_conceded_avg'])
        away_goals_conceded_avg = float(request.form['away_goals_conceded_avg'])
        home_win_percentage = float(request.form['home_win_percentage'])
        away_win_percentage = float(request.form['away_win_percentage'])

        features = [
            home_team_form,
            away_team_form,
            home_goals_scored_avg,
            away_goals_scored_avg,
            home_goals_conceded_avg,
            away_goals_conceded_avg,
            home_win_percentage,
            away_win_percentage
        ]

        scaled_features = scaler.transform([features])
        prediction = model.predict(scaled_features)[0]

        result_map = {
            0: 'Home Win',
            1: 'Draw',
            2: 'Away Win'
        }

        return render_template(
            'index.html',
            prediction=result_map[prediction],
            selected_league=league
        )

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")


if __name__ == "__main__":
    app.run()
