from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Hello World</h1>"

@app.route('/about')
def about():
    return "<h1>About Page</h1>"

@app.route('/contact')
def conatct():
    return "<h1>Thank your for using our services, please contact us if you need help<h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


