from flask import Flask, make_response

app = Flask(__name__)

@app.route('/string/')
def return_string():
	return "Hello World!"

@app.route('/object/')
def return_object():
	response = make_response('hello world', 200)
	response.headers['Content-Type'] = 'text/plain'
	return response

@app.rout('/tuple/')
def return_tuple():
	headers = {'Content-Type': 'text/plain'}
	return ('hello world!', 200, headers)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)