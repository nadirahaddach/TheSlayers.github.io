from flask import Flask, render_template
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

if __name__ == "__main__":
    app.run(debug=True)