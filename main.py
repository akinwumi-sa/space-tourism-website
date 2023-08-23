from flask import Flask, render_template
import json

app = Flask(__name__)

with open('data.json', 'r') as file:
    datafile = json.load(file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/destination/<name>')
def destination(name):
    destination_data = None
    if name == 'moon':
        destination_data = datafile['destinations'][0]
    elif name == 'mars':
        destination_data = datafile['destinations'][1]
    elif name == 'europa':
        destination_data = datafile['destinations'][2]
    elif name == 'titan':
        destination_data = datafile['destinations'][3]
    return render_template('destination-moon.html', data=destination_data)


@app.route('/crew/<name>')
def crew(name):
    crew_data = None
    if name == 'hurley':
        crew_data = datafile['crew'][0]
    elif name == 'shuttleworth':
        crew_data = datafile['crew'][1]
    elif name == 'glover':
        crew_data = datafile['crew'][2]
    elif name == 'ansari':
        crew_data = datafile['crew'][3]
    return render_template('crew-commander.html', data=crew_data)


@app.route('/technology/<name>')
def technology(name):
    tech_data = None
    if name == 'launch':
        tech_data = datafile['technology'][0]
    elif name == 'spaceport':
        tech_data = datafile['technology'][1]
    elif name == 'capsule':
        tech_data = datafile['technology'][2]
    return render_template('technology-capsule.html', data=tech_data)


if __name__ == '__main__':
    app.run(debug=True)
