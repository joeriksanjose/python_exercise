from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'TestingPo'

@app.route('/')
def hello():
	return render_template('login_form.html')

@app.route('/login', methods=['POST'])
def login():
	admins = [{'username': 'erik', 'password': '123456'}, {'username': 'admin', 'password': '7890'}]
	username = request.form['username'];
	password = request.form['password'];

	for admin in admins:
		if admin['username'] == username and admin['password'] == password:
			session['username'] = username
			return redirect(username+'/42')

	return redirect(username+'/0')

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')

@app.route('/<name>/<int:answer>')
def guess(name, answer):
	print(session.get('username'))
	if not session.get('username'):
		redirect('/')

	correct = (answer == 42)
	return render_template(
		'guess.html',
		name=name,
		correct=correct
	)

if __name__ == '__main__':
	app.run(debug=True)