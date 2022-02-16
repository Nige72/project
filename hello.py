from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

# create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("DB_PASS")

#create a form class
class NamerForm(FlaskForm):
    name = StringField("What is your name:", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Index Html
@app.route('/')
def index():
    first_name = "Nige"
    stuff = "This is <strong>BOLD<strong> Text"
    favourite_pizza = ["Mexican","Cheese","Pepperoni"]
    return render_template("index.html",first_name=first_name,stuff=stuff,favourite_pizza=favourite_pizza)


# localhost:5000/user/Nige/ User.html
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)      
def page_not_found(e):
    return render_template("500.html"), 500

#create name page
@app.route('/name', methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()
    #validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name.html", name=name, form=form)




if __name__ == "__main__":
    app.run(debug=True)