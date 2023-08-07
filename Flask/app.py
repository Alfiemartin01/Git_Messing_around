from flask import Flask, request, redirect

app = Flask(__name__) #Creates a Flask object

@app.route('/') #runs when the url end point matches
def main():
    return("Ping -------- Pong --------- Ping --------- Pong")

@app.route('/post')
def post():
    return(request.method)

@app.route('/google')
def google():
    return redirect('http://www.google.com')

###### Routes Exercise
@app.route('/<int:num>')
def squared(num:int) -> int:
    return(f'{num**2}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) #runs the app in debug mode

