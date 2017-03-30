"""
    File Name: view.py
    Created On: 2017/03/21
"""
from flask import Flask, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from template import template_location

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/ubiwifi"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login/")
def get_name():
    return render_template(template_location['login'])


@app.route("/user/info/")
def user_info():
    return render_template(template_location['user_info'])


@app.route("/dashboard/")
def dashboard():
    return render_template(template_location['dashboard'])


@app.route("/overview/")
def overview():
    return render_template(template_location['overview'])


@app.route("/assets/devices/")
def devices():
    return render_template(template_location['devices'])


@app.route("/assets/device/edit/")
def edit_device():
    return render_template(template_location['edit_device'])


@app.route("/ssids/ssid/")
def ssid():
    return render_template(template_location['ssid'])


@app.route("/ssids/ssid/edit/")
def edit_ssid():
    return render_template(template_location['edit_ssid'])


@app.route("/statistics/device_statistics/")
def device_statistics():
    return render_template(template_location['device_statistics'])


@app.route("/statistics/device_detail/")
def device_statistic_detail():
    return render_template(template_location['device_statistic_detail'])


if __name__ == "__main__":
    app.run(debug=True)
