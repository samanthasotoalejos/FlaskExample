from flask import Flask, render_template, request # also gets "request" from the flask module to get information from the post request
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/start')
def start():
  return render_template('start.html')
  
@app.route('/clicked', methods=['POST']) # creates a route with the path "/clicked" with the single method "POST"
def buttonClicked():
	data = request.data.decode() # gets the data from the user and puts it in the data variable
	print(data) # will print the data to the output console.
	return 'done' # this won't actually be displayed to the user

#so far can recieve data from HTML (to JS to Python)
app.run('0.0.0.0',8080)

#https://repl.it/talk/ask/Running-python-through-webserver/8107
#https://stackoverflow.com/questions/11178426/how-can-i-pass-data-from-flask-to-javascript-in-a-template (tmrw)
#look over: https://repl.it/talk/learn/Learning-Web-Development-with-Python-Part-1/12880
#https://blog.pythonanywhere.com/169/
#https://realpython.com/python-web-applications/
#google appengine