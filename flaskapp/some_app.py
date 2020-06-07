from flask import Flask
from flask import request, Response, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, RecaptchaField

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')