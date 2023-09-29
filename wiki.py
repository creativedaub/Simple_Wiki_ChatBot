from os import system
try:
    from flask import Flask, request, render_template
    import wikipedia
except ModuleNotFoundError:
    choice = ['flask', 'wikipedia']
    for i in choice:
        system(f'pip install {i}')
except NameError:
    print("Run the app again")
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form['user_input']
    response = wikipedia.summary(user_input)
    return response


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except wikipedia.exceptions.PageError:
        print("Page id doesn't match any pages")
