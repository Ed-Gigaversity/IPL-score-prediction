# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'first-innings-score-lr-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = []
    if request.method == 'POST':
        team_logo_map = {
            'Chennai Super Kings': 'csk.png',
            'Delhi Daredevils': 'dc.png',
            'Kings XI Punjab': 'kxip.png',
            'Kolkata Knight Riders': 'kkr.jpg',
            'Mumbai Indians': 'mi.jpg',
            'Rajasthan Royals': 'rr.png',
            'Royal Challengers Bangalore': 'rcb.png',
            'Sunrisers Hyderabad': 'srh.png',
        }
        batting_team = request.form['batting-team']
        batting_logo = team_logo_map.get(batting_team, '')
        temp_array += [
            1 if batting_team == 'Chennai Super Kings' else 0,
            1 if batting_team == 'Delhi Daredevils' else 0,
            1 if batting_team == 'Kings XI Punjab' else 0,
            1 if batting_team == 'Kolkata Knight Riders' else 0,
            1 if batting_team == 'Mumbai Indians' else 0,
            1 if batting_team == 'Rajasthan Royals' else 0,
            1 if batting_team == 'Royal Challengers Bangalore' else 0,
            1 if batting_team == 'Sunrisers Hyderabad' else 0,
        ]
        bowling_team = request.form['bowling-team']
        bowling_logo = team_logo_map.get(bowling_team, '')
        temp_array += [
            1 if bowling_team == 'Chennai Super Kings' else 0,
            1 if bowling_team == 'Delhi Daredevils' else 0,
            1 if bowling_team == 'Kings XI Punjab' else 0,
            1 if bowling_team == 'Kolkata Knight Riders' else 0,
            1 if bowling_team == 'Mumbai Indians' else 0,
            1 if bowling_team == 'Rajasthan Royals' else 0,
            1 if bowling_team == 'Royal Challengers Bangalore' else 0,
            1 if bowling_team == 'Sunrisers Hyderabad' else 0,
        ]
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        temp_array += [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0])
        return render_template('result.html', lower_limit=my_prediction-10, upper_limit=my_prediction+5, batting_team=batting_team, bowling_team=bowling_team, batting_logo=batting_logo, bowling_logo=bowling_logo)



if __name__ == '__main__':
	app.run(debug=True)