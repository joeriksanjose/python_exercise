from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello world!'

if __name__ == '__main__':
	# Our app will run on 127.0.0.1:5000 by default.
    app.run(debug=True)