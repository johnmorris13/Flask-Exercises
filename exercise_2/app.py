from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '''
        <form action="/result" method="get">
            <label for="number">Enter a number:</label><br>
            <input type="text" id="number" name="number"><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/result', methods=['GET'])
def calculate():
    number = request.args.get('number')
    message = ""

    try:
        number = int(number)
        if number % 2 == 0:
            message = f"{number} is even."
        else:
            message = f"{number} is odd."
    except ValueError:
        message = f"{number} is not an integer."

    return render_template_string('''<p>{{ message }}</p><a href="/">Go home</a>''', message=message)

if __name__ == '__main__':
    app.run(debug=True)