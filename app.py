from flask import Flask, render_template, request

app = Flask(__name__)

# a GET route?
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer == request.form['customer']
        customer == request.form['customer']
        customer == request.form['customer']
        customer == request.form['customer']

if __name__ == '__main__':
    app.debug = True
    app.run()