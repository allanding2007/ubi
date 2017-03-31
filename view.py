"""
    File Name: view.py
    Created On: 2017/03/21
"""
from flask import Flask, render_template, make_response, redirect, url_for, flash, abort
from flask import jsonify
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from template import template_location
from forms.form import LoginForm
from models.model import db, User, Device, SSidConfig, UsageRecord
from settings import app_config
import json


app = Flask(__name__)
bootstrap = Bootstrap()
moment = Moment()
app.config.from_object(app_config['develop'])
db.init_app(app)
bootstrap.init_app(app)
moment.init_app(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template(template_location['404']), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template(template_location['500']), 500


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login/", methods=["GET", "POST"])
def user_login():
    form = LoginForm()
    print form.data
    if form.validate_on_submit():
        user_name = form.name.data
        user = User.query.filter_by(user_name=user_name).first()
        if not user:
            abort(404)
        pwd = form.password.data
        if pwd == user.pass_word:
            return redirect(url_for('dashboard'))
        else:
            flash("Invliad username or password!")
    return render_template(template_location['login'], form=form)


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


@app.route("/assets/device/edit/<int:id>")
def edit_device(id):
    device = Device.query.filter_by(id=id).first()
    if not device:
        abort(404)
    return render_template(template_location['edit_device'], device=device)


@app.route("/ssids/ssid/")
def ssid():
    return render_template(template_location['ssid'])


@app.route("/ssids/ssid/edit/<int:id>")
def edit_ssid(id):
    ssid = SSidConfig.query.filter_by(id=id).first()
    return render_template(template_location['edit_ssid'], ssid=ssid)


@app.route("/statistics/device_statistics/")
def device_statistics():
    return render_template(template_location['device_statistics'])


@app.route("/statistics/device_detail/")
def device_statistic_detail():
    return render_template(template_location['device_statistic_detail'])


@app.route("/assets/devices/ajax/")
def devices_ajax():
    devices = Device.query.all()
    return jsonify(map(lambda device: device.to_json(), devices))


@app.route("/ssids/ajax/")
def ssids_ajax():
    ssids = SSidConfig.query.all()
    return jsonify(map(lambda ssid: ssid.to_json(), ssids))


if __name__ == "__main__":
    app.run(debug=True)
