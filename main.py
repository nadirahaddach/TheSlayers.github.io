from flask import Flask, render_template, request

#from __init__ import app
#from cruddy.app_crud import app_crud
#app.register_blueprint(app_crud)

# create an instance of flask object
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/password')
def password():
    return render_template("password.html")


@app.route('/guess')
def guess():
    return render_template("guess.html")

@app.route('/findyour/', methods=['GET', 'POST'])
def findyour():
    if request.form:
        input = request.form.get("lname")
        print("works")
        if len("input") != 0:
            return render_template("findyour.html", input=input)
    return render_template("findyour.html")

if __name__ == "__main__":
    app.run(debug=True)