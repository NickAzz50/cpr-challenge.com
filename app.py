from flask import Flask, jsonify, render_template, request
from datetime import datetime
import pandas
app = Flask(__name__)
"""
PAGES
Home => Mission Statement
Survey => Allow users to take the survey
Results => Displays the results shown
"""


@app.route('/home')
def home():
    datetime.now()
    return render_template('mission.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/results')
def results():
    return render_template('results.html')





if __name__ == "__main__":
    app.run()
