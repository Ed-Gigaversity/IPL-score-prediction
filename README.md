# IPL First Innings Score Prediction Web App

![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![scikit-learn](https://img.shields.io/badge/Library-Scikit_Learn-orange.svg)

## Overview
This project is a machine learning web application that predicts the first innings score in an IPL (Indian Premier League) cricket match. The app is built using Flask and uses a Linear Regression model trained on historical IPL data. Users can input match details and get a predicted score range for the first innings.

## Features
- Predicts first innings scores for IPL matches based on team and match conditions
- User-friendly web interface built with Flask
- Model trained on real IPL data
- Team logos shown for both input and results for a professional look
- Ready for deployment (e.g., Heroku)

## Demo
A glimpse of the web app:

![Web App Demo](readme_resources/ipl-first-innings-score-web-app.gif)

## Live App
You can try the deployed app here:
[https://ipl-first-innings-score.herokuapp.com](https://ipl-first-innings-score.herokuapp.com)

> **Note:** If you see an application error (see image below), it may be due to Heroku's free dyno limits. Please try again later or deploy locally.

![Heroku Error](readme_resources/application-error-heroku.png)

## Project Structure
```
├── app.py                      # Flask web app (main logic)
├── First Innings Score Prediction - IPL.py  # Model training script
├── first-innings-score-lr-model.pkl        # Trained model (not tracked in git)
├── ipl.csv                     # IPL dataset (not tracked in git)
├── requirements.txt            # Python dependencies
├── static/                     # Static files (CSS, images, JS)
│   ├── styles.css              # Main stylesheet for UI
│   ├── csk.png, mi.jpg, ...    # Team logos used in UI and results
│   └── ipl-favicon.ico         # Favicon for the app
├── templates/                  # HTML templates rendered by Flask
│   ├── index.html              # Main UI page (user input form, now with team logos)
│   └── result.html             # Results page (shows prediction and team logos)
├── readme_resources/           # Images and GIFs for README
└── .gitignore                  # Git ignore rules
```

### Folder Usage
- **static/**: Contains all static files such as CSS (`styles.css`), images (team logos, favicon), and JavaScript. Team logos are now shown in the UI and results.
- **templates/**: Contains HTML files (`index.html` for the main UI, `result.html` for displaying results). Flask uses this folder to render dynamic content based on user input and model predictions.

## Getting Started
### Prerequisites
- Python 3.6+
- pip (Python package manager)

### Installation
1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd IPL-First-Innings-Score-Prediction-Deployment-master
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **(Optional) Retrain the model:**
   If you want to retrain the model, run:
   ```sh
   python "First Innings Score Prediction - IPL.py"
   ```
   This will generate a new `first-innings-score-lr-model.pkl` file.

4. **Run the app locally:**
   ```sh
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## Usage
- Open the web app in your browser.
- Select the batting and bowling teams (team logos will appear), enter the current match stats, and click Predict.
- The app will display a predicted score range for the first innings, along with both teams' logos for a professional look.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is for educational purposes. Please refer to the original dataset and model sources for their respective licenses.

## Credits
- [Original Project & Model Details](https://github.com/anujvyas/Machine-Learning-Projects/tree/master/First%20Innings%20Score%20Predicton%20-%20IPL)
- Dataset: IPL match data


