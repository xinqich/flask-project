from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hello')
def hello():
    return 'Hello, world!'


@app.route('/info')
def info():
    return 'This is an informational page.'

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/calc/<num1>/<num2>')
def handle_calc(num1, num2):
    num1, num2 = list(map(isNumberValid, [num1, num2]))
    for num in [num1, num2]:
        if isinstance(num, tuple):
            return num

    return f'The sum of {num1} and {num2} is {num1 + num2}'


def isNumberValid(value) -> tuple[str, int] | float | int:
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return f'"{value}" is not a number.', 400


@app.route('/reverse/')
def handle_reverse_exception():
    return 'String must not be empty.', 400


@app.route('/reverse/<string>')
def handle_reverse(string):
    return string[::-1]


@app.route('/user/<name>/<age>')
def handle_user(name, age):
    try:
        age = int(age)
        if age <= 0:
            return 'Age must be a positive integer.', 400

        return f"Hello, {name}. You are {age} years old."

    except ValueError:
        return 'Age must be a positive integer.', 400


if __name__ == '__main__':
    app.run(debug=True)
