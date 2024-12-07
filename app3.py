from flask import Flask
import random  # for random numbers

app = Flask(__name__)  


# Function to check leap years
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True  
    return False  


@app.route('/')
def index():
    # Generate a random year between 1 and 2021
    random_year = random.randint(1, 2021)

    
    if leap_year(random_year):
        leap_status = "a leap year"
    else:
        leap_status = "not a leap year"

    
    return f'''
    <html>
        <head>
            <title>Leap Year Checker</title>
        </head>
        <body>
            <h1>Random Year Generator & Leap Year Checker</h1>
            <p>Generated Year: <b>{random_year}</b></p>
            <p>This year is <b>{leap_status}</b>.</p>
        </body>
    </html>
    '''



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
