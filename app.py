from flask import Flask, render_template, request, flash

#initialize Flask( <app module> )
app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("Hi, " + str(request.form['name_input']) +". Nice to meet you.")
	return render_template("index.html")

@app.route("/int2308")
def int2308():
	return render_template("int2308.html")

# Fix error 500 - Set the secret_key
if __name__ == '__main__':
    app.debug = True
    app.run()
# run on anaconda - install flask
# c:\> conda activate env39