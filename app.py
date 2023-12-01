from flask import Flask, render_template

app = Flask(__name__)
counter = 0

@app.route('/')
def home():
    return render_template('index.html', counter=counter)

@app.route('/increment', methods=['GET'])
def increment_counter():
    global counter
    counter += 1
    return render_template('index.html', counter=counter)

if __name__ == '__main__':
    app.run(debug=True)
