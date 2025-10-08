from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contacts')
def contact():
    return render_template('contact.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/trianglearea', methods=['GET', 'POST'])
def trianglearea():
    result = None
    if request.method == 'POST':
        base = float(request.form['base'])
        height = float(request.form['height'])
        result = 0.5 * base * height
    return render_template('areatriangle.html', result=result)


@app.route('/circlearea', methods=['GET', 'POST'])
def circlearea():
    result = None
    if request.method == 'POST':
        radius = float(request.form['radius'])
        result = math.pi * radius * radius
    return render_template('areacircle.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)