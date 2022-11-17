from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/displayResult')
def displayResult():
    return render_template('displayResult.html')

# -------- Back ---------------------------------------------------------- #
@app.route('/back', methods=['GET', 'POST'])
def back():
    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(debug=True)