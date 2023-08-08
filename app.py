from flask import Flask, render_template

app = Flask(__name__)

# Define your routes
@app.route('/')
def index():
    return render_template('mission.html')

@app.route('/home')
def home():
    return render_template('mission.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == "__main__":
    app.run()
