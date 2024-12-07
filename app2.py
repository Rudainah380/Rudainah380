from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Hello, my name is Rudainah</h1>
        <p>My student ID is 4314797</p>
        <p>I am studying Computer Science</p>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
